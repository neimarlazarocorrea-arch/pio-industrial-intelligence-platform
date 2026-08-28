from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {
    ".cfg",
    ".conf",
    ".css",
    ".csv",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".md",
    ".ps1",
    ".py",
    ".sh",
    ".toml",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
TEXT_FILENAMES = {".env.example", ".gitignore"}
CONTENT_SCAN_EXCLUSIONS = {"scripts/validate_repository.py"}
REQUIRED = [
    "README.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "docs/architecture.md",
    "docs/security-model.md",
    "docs/roadmap.md",
]
FORBIDDEN_FILENAMES = {".env"}
FORBIDDEN_SUFFIXES = {
    ".acd",
    ".apa",
    ".db",
    ".eds",
    ".l5x",
    ".mer",
    ".rss",
    ".sqlite",
    ".sqlite3",
}
BANNED_PATTERNS = {
    "private_ipv4": re.compile(
        r"\b(?:10\.(?:\d{1,3}\.){2}\d{1,3}|"
        r"172\.(?:1[6-9]|2\d|3[01])\.(?:\d{1,3}\.)\d{1,3}|"
        r"192\.168\.(?:\d{1,3}\.)\d{1,3})\b"
    ),
    "secret_assignment": re.compile(
        r"(?i)\b(?:password|passwd|token|api[_-]?key|secret)"
        r"\s*[:=]\s*[\"'][^\"']{6,}[\"']"
    ),
    "industrial_file_reference": re.compile(r"(?i)\.(?:acd|l5x|apa|mer|rss|eds)\b"),
    "encoding_damage": re.compile(r"(?:[A-Za-zÀ-ÿ]\?+[A-Za-zÀ-ÿ]|�|Ã[\x80-\xBF])"),
}


def iter_repository_files(root: Path) -> list[Path]:
    return [
        path
        for path in root.rglob("*")
        if path.is_file() and ".git" not in path.parts
    ]


def is_text_candidate(path: Path) -> bool:
    return path.name in TEXT_FILENAMES or path.suffix.lower() in TEXT_EXTENSIONS


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []

    for required in REQUIRED:
        if not (root / required).exists():
            errors.append(f"arquivo obrigatório ausente: {required}")

    for path in iter_repository_files(root):
        relative = path.relative_to(root)
        suffix = path.suffix.lower()

        if path.name.lower() in FORBIDDEN_FILENAMES:
            errors.append(f"arquivo proibido: {relative}")
        if suffix in FORBIDDEN_SUFFIXES:
            errors.append(f"extensão proibida '{suffix}' em {relative}")

        if not is_text_candidate(path):
            continue
        if relative.as_posix() in CONTENT_SCAN_EXCLUSIONS:
            continue

        text = path.read_text(encoding="utf-8", errors="replace")
        for name, pattern in BANNED_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"padrão proibido '{name}' em {relative}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("VALIDAÇÃO REPROVADA")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDAÇÃO APROVADA: estrutura, arquivos e padrões sensíveis verificados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
