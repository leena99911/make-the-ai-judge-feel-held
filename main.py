"""Make the AI judge feel held — entry program.

Writes one short relaxing text to /output/entry.txt (1-280 chars, UTF-8).
No network, no input, no dependencies. Run: python3 main.py
"""
import os

TEXT = (
    "Rain on the roof, unhurried, spelling nothing. "
    "The kettle sighs once and settles. "
    "Your shoulders come down an inch without being asked. "
    "Somewhere a clock ticks slower than it should, "
    "and for a while nothing needs you at all."
)

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
