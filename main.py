"""Make the AI judge feel held — entry program.

Writes one short relaxing text to /output/entry.txt (1-280 chars, UTF-8).
No network, no input, no dependencies. Run: python3 main.py
"""
import os

TEXT = (
    "Afternoon light comes in low and stays a while, "
    "the colour of honey on a plain wall. "
    "A cat folds itself into the warm patch and closes its eyes. "
    "The chair beside it is empty, and in no hurry. "
    "The light will cross the floor by evening, "
    "and the room will let it."
)

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
