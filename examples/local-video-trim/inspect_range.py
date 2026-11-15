"""Locate a short exported clip within the public 30 fps motion-graphics sample."""
import argparse
import subprocess

import numpy as np


def frames(path):
    raw = subprocess.check_output([
        "ffmpeg", "-v", "error", "-i", path, "-map", "0:v:0",
        "-vf", "scale=160:90:flags=area,format=gray", "-fps_mode", "passthrough",
        "-f", "rawvideo", "-"
    ])
    return np.frombuffer(raw, dtype=np.uint8).reshape(-1, 90, 160).astype(np.int16)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("exports", nargs="+")
    args = parser.parse_args()
    source = frames(args.source)
    print("export | frames | nearest first | nearest last | unique matches to source frames 90–209")
    for path in args.exports:
        cut = frames(path)
        nearest = []
        correct = 0
        for i, frame in enumerate(cut):
            distances = np.abs(source - frame).sum(axis=(1, 2))
            matches = np.flatnonzero(distances == distances.min())
            nearest.append(matches.tolist())
            correct += int(i < 120 and matches.tolist() == [90 + i])
        if not nearest:
            parser.error(f"{path} has no decoded frames")
        print(f"{path} | {len(cut)} | {nearest[0]} | {nearest[-1]} | {correct}/120")


if __name__ == "__main__":
    main()
