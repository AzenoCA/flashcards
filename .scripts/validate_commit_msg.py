import re
import sys
from pathlib import Path

ALLOWED_TYPES = (
    "feat",
    "fix",
    "docs",
    "style",
    "refactor",
    "perf",
    "test",
    "build",
    "ci",
    "chore",
)

TYPE_PATTERN = "|".join(ALLOWED_TYPES)
CONVENTIONAL_SUBJECT_RE = re.compile(rf"^(?:{TYPE_PATTERN})(?:\([a-z0-9][a-z0-9._/\-]*\))?: .+")
ALLOWED_PREFIXES = ("Merge ", 'Revert "', "fixup! ", "squash! ")


def _write_stderr(message: str = "") -> None:
    sys.stderr.write(f"{message}\n")


def _read_subject_line(commit_msg_file: Path) -> str:
    lines = commit_msg_file.read_text(encoding="utf-8").splitlines()

    for line in lines:
        subject = line.strip()
        if subject and not subject.startswith("#"):
            return subject
    return ""


def main() -> int:
    """Validate git commit subject against Conventional Commits."""
    if len(sys.argv) != 2:
        _write_stderr("Expected a commit message file path as the only argument.")
        return 2

    commit_msg_file = Path(sys.argv[1])
    if not commit_msg_file.exists():
        _write_stderr(f"Commit message file does not exists: {commit_msg_file}.")
        return 2

    subject = _read_subject_line(commit_msg_file)
    if not subject:
        _write_stderr("Commit message subject is empty.")
        return 1

    if subject.startswith(ALLOWED_PREFIXES) or CONVENTIONAL_SUBJECT_RE.match(subject):
        return 0

    _write_stderr("Commit message must follow Conventional Commits:")
    _write_stderr("  <type>(<scope>): <description>")
    _write_stderr()
    _write_stderr(f"Allowed <type>: {', '.join(ALLOWED_TYPES)}")
    _write_stderr("Examples:")
    _write_stderr("  feat(auth): add OAuth login")
    _write_stderr("  fix!: remove deprecated API")
    _write_stderr()
    _write_stderr(f"Received subject: {subject!r}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
