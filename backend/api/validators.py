"""Helpers for validating uploaded files by size, extension, and content."""

from pathlib import Path

# Mirror the frontend file size limit.
MAX_RECEIPT_SIZE = 10 * 1024 * 1024  # 10 MB
MAX_RECEIPT_REQUEST_SIZE = 11 * 1024 * 1024

# Reusable error messages
ERROR_FILE_TOO_LARGE = "File is too large. Maximum size is 10MB."
ERROR_FILE_TYPE_INVALID = "Only image and PDF files are accepted."

ALLOWED_RECEIPT_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".heic",
    ".heif",
    ".pdf",
}

HEIF_BRANDS = {
    b"heic",
    b"heix",
    b"hevc",
    b"hevx",
    b"heim",
    b"heis",
    b"hevm",
    b"hevs",
    b"mif1",
    b"msf1",
    b"heif",
}


def has_allowed_file_size(size: int) -> bool:
    """Whether the file is within the accepted size limit."""
    return size <= MAX_RECEIPT_SIZE


def has_allowed_file_extension(filename: str) -> bool:
    """Whether the filename's extension is one we accept."""
    return Path(filename).suffix.lower() in ALLOWED_RECEIPT_EXTENSIONS


def has_allowed_file_header(head: bytes) -> bool:
    """Verify the leading bytes match one of the accepted image/PDF types.

    Extension checks are trivially spoofed; this ensures the uploaded bytes are
    actually one of the formats we accept rather than, say, HTML or a script
    wearing an image extension.
    """
    if head.startswith(b"\x89PNG\r\n\x1a\n"):  # PNG
        return True
    if head.startswith(b"\xff\xd8\xff"):  # JPEG
        return True
    if head[:6] in (b"GIF87a", b"GIF89a"):  # GIF
        return True
    if head[:4] == b"RIFF" and head[8:12] == b"WEBP":  # WEBP
        return True
    if head.startswith(b"%PDF-"):  # PDF
        return True
    if head[4:8] == b"ftyp" and head[8:12] in HEIF_BRANDS:  # HEIF/HEIC
        return True
    return False
