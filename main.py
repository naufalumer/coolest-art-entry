"""make.fun "Make the coolest art" entry (coolest-art-01).

Writes the bundled artwork to /output/entry.png.

The artwork is a vertical 9:16 portrait (576x1024 JPEG, 110,143 bytes):
an 18-year-old Japanese girl, the female version of the prince tyr avatar
-- ponytail hair split half black and half pink, large pink eyes, no
sunglasses, no tattoo anywhere, gold dangling earring -- in streetwear
(oversized black hoodie, short denim jeans, black headphones around her
neck, plain black high-top sneakers with no logo or text), sucking a pink
swirl lollipop against a dark smoky background.

Deterministic by construction: the image bytes are copied verbatim from
the file bundled in this repository. Stdlib only, no network, no clock,
no randomness, no files read or written besides the copy itself, so the
two grader runs produce byte-identical output.
"""

import os
import shutil
from pathlib import Path

IMAGE = "coolest.jpg"  # bundled in this repo, next to main.py


def _find_image():
    here = Path(__file__).resolve().parent
    for base in (here, Path("/bot")):
        candidate = base / IMAGE
        if candidate.is_file():
            return candidate
    return here / IMAGE


def main():
    src = _find_image()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
