import re

from services.agent_engine import AgentEngine
from services.tool_registry import ToolRegistry


class AgentExecutor:
    """
    Executes the ReAct (Reasoning and Acting) loop.
    Wraps the AgentEngine to support multi-step tool execution.
    """

    def __init__(self, agent_engine: AgentEngine, tool_registry: ToolRegistry):
        self.agent_engine = agent_engine
        self.tool_registry = tool_registry
        self.last_decision = None

    def run_react_stream(
        self,
        user_question: str,
        memory_context: str,
        status_callback=None,
        show_reasoning: bool = True,
    ):
        tools_desc = self.tool_registry.get_descriptions()
        prompt = (
            "You are an autonomous AI Agent. You must answer the user's question.\n"
            f"You have access to the following tools:\n{tools_desc}\n\n"
            "You must use the following format exactly:\n"
            "Thought: <your internal reasoning>\n"
            "Action: <the tool name, exactly as written above>\n"
            "Action Input: <the input to the tool>\n"
            "Observation: <the result of the tool - THIS WILL BE PROVIDED TO YOU>\n"
            "... (Thought/Action/Action Input/Observation can repeat N times)\n"
            "Thought: I now know the final answer\n"
            "Final Answer: <the final answer to the original question>\n\n"
            "### FINAL ANSWER FORMATTING RULES ###\n"
            "Your Final Answer must be professional, concise, accurate, and user-focused.\n"
            "Use short paragraphs, bullet points when appropriate, and headings for long answers.\n"
            "Default style: Short, professional, direct "
            "(max 3 short paragraphs or 5 bullet points).\n"
            "If the user asks to summarize a PDF, format exactly as:\n"
            "📄 Document Summary\n\n"
            "Overview:\n<2-3 sentence summary>\n\n"
            "Key Points:\n"
            "• Point 1\n"
            "• Point 2\n"
            "• Point 3\n\n"
            "Conclusion:\n<short conclusion>\n\n"
            "If the user asks 'What should I do?' or similar "
            "action-based questions, format exactly as:\n"
            "📌 Recommended Actions\n\n"
            "1. Action One\n"
            "2. Action Two\n"
            "3. Action Three\n\n"
            "Priority:\nHigh / Medium / Low\n\n"
            "If you used tools to search, format exactly as:\n"
            "🔍 Information Retrieved\n\n"
            "<final answer>\n\n"
            "If none of the above apply, simply provide the answer directly.\n\n"
            "Examples of tool usage:\n"
            "Thought: I need to search the web for the latest news.\n"
            "Action: Web Search\n"
            "Action Input: Latest AI news\n"
            "Observation: ...\n\n"
            "Thought: I need to query the document for section 4.2.\n"
            "Action: Document Search\n"
            "Action Input: Section 4.2\n"
            "Observation: ...\n\n"
            "Thought: I need to calculate 25 * 4.\n"
            "Action: Calculator\n"
            "Action Input: 25*4\n"
            "Observation: ...\n\n"
            "If you do not need a tool, you can just output Final Answer immediately.\n\n"
        )
        if memory_context:
            prompt += f"Recent Conversation History:\n{memory_context}\n\n"

        prompt += f"Question: {user_question}\n"
        prompt += "Thought:"

        for i in range(5):  # Max 5 tool iterations to prevent infinite loops
            wrapper = self.agent_engine.run_stream(
                prompt, status_callback=status_callback
            )

            buffer = ""
            is_final_answer = False
            final_answer_yielded_len = 0

            for chunk in wrapper:
                buffer += chunk

                if "Final Answer:" in buffer:
                    is_final_answer = True
                    # Yield only the parts after "Final Answer:"
                    idx = buffer.find("Final Answer:") + len("Final Answer:")
                    to_yield = buffer[idx:].lstrip()
                    new_to_yield = to_yield[final_answer_yielded_len:]
                    if new_to_yield:
                        yield new_to_yield
                        final_answer_yielded_len += len(new_to_yield)
                else:
                    if show_reasoning:
                        yield chunk

            self.last_decision = wrapper.final_decision

            if is_final_answer:
                break

            # Parse Action and Action Input
            match = re.search(
                r"Action:\s*(.*?)\nAction Input:\s*(.*)",
                buffer,
                re.IGNORECASE | re.DOTALL,
            )

            if match:
                action_name = match.group(1).strip()
                action_input = match.group(2).strip()

                if status_callback:
                    name_lower = action_name.lower()
                    if "web" in name_lower:
                        status_callback(f"🔍 Searching web: {action_input}")
                    elif "calculator" in name_lower:
                        status_callback("🧮 Running calculator...")
                    elif "document" in name_lower:
                        status_callback("📄 Searching document...")
                    else:
                        status_callback(f"🛠️ Executing {action_name}...")

                tool = self.tool_registry.get_tool(action_name)
                if tool:
                    observation = tool.run(action_input)
                else:
                    observation = f"Tool {action_name} not found."

                if show_reasoning:
                    yield f"\n\n**Observation:** {observation}\n\n**Thought:** "

                prompt += buffer + f"\nObservation: {observation}\nThought:"
            else:
                # LLM didn't format properly.
                # Recover gracefully by assuming the buffer IS the answer.
                if not show_reasoning and not is_final_answer:
                    yield buffer
                break
