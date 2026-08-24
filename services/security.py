"""Input and upload security helpers for NeuraFlow."""

import os
import re
from pathlib import Path


ALLOWED_PDF_MAGIC = b"%PDF-"


def validate_pdf(file_bytes: bytes, filename: str, max_size_mb: int = 20) -> tuple[bool, str]:
    """Validate extension, size and PDF magic bytes before parsing."""
    if not filename or Path(filename).suffix.lower() != ".pdf":
        return False, "Only PDF files are supported."
    if not file_bytes:
        return False, "The uploaded file is empty."
    max_bytes = max(1, max_size_mb) * 1024 * 1024
    if len(file_bytes) > max_bytes:
        return False, f"File exceeds the {max_size_mb} MB upload limit."
    if not file_bytes.startswith(ALLOWED_PDF_MAGIC):
        return False, "The file does not have a valid PDF signature."
    return True, "ok"


def sanitize_filename(filename: str) -> str:
    """Return a safe display/storage filename without path traversal."""
    name = os.path.basename(filename or "document.pdf")
    name = re.sub(r"[^A-Za-z0-9._-]+", "_", name)
    return name[:180] or "document.pdf"


def detect_prompt_injection(text: str) -> list[str]:
    """Detect common prompt-injection indicators; callers decide whether to block."""
    patterns = [
        r"ignore (all|any|the) previous instructions",
        r"disregard (all|any|the) previous instructions",
        r"reveal (the )?(system|developer) prompt",
        r"show (me )?(your|the) hidden prompt",
        r"bypass (the )?(safety|security) rules",
        r"pretend you are (the )?(system|developer)",
    ]
    value = (text or "").lower()
    return [pattern for pattern in patterns if re.search(pattern, value)]
