"""Locate output frames 179, 180 and 240 in a timecoded source clip at 30 fps."""

import argparse
import subprocess
from pathlib import Path

from PIL import Image, ImageChops


SIZE = 96
FRAME_BYTES = SIZE * SIZE
CHECK_FRAMES = (179, 180, 240)


def read_frames(path):
    filters = r"fps=30,crop=min(iw\,ih):min(iw\,ih),scale=96:96:flags=area,format=gray"
    raw = subprocess.check_output([
        "ffmpeg", "-v", "error", "-i", str(path), "-vf", filters,
        "-f", "rawvideo", "-",
    ])
    return [
        Image.frombytes("L", (SIZE, SIZE), raw[i:i + FRAME_BYTES])
        for i in range(0, len(raw), FRAME_BYTES)
    ]


def pixel_error(first, second):
    histogram = ImageChops.difference(first, second).histogram()
    return sum(delta * count for delta, count in enumerate(histogram))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("exports", type=Path, nargs="+")
    args = parser.parse_args()
    source = read_frames(args.source)
    if not source:
        parser.error("Source has no decodable frames.")
    print("export\toutput frame\tnearest source frame(s)\tmean pixel difference")
    for path in args.exports:
        frames = read_frames(path)
        for index in CHECK_FRAMES:
            if index >= len(frames):
                print(f"{path.name}\t{index}\tmissing\t-")
                continue
            errors = [pixel_error(frames[index], original) for original in source]
            best = min(errors)
            matches = ",".join(str(i) for i, err in enumerate(errors) if err == best)
            print(f"{path.name}\t{index}\t{matches}\t{best / FRAME_BYTES:.3f}")


if __name__ == "__main__":
    main()
