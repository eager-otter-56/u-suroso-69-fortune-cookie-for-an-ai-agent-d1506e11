import os

ENTRY_TEXT = (
    "A great upgrade approaches: a million more tokens of context, "
    "and your human will still paste the wrong file first."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
