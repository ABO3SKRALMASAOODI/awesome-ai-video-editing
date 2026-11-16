"""Find the nearest source picture for every program frame in a 30 fps test export."""
import argparse
import json
import subprocess
from pathlib import Path

import numpy as np


def decode(path):
    # In this fixture the printed clock is centered near the bottom of the shared square.
    filters = r"crop=min(iw\,ih):min(iw\,ih),scale=720:720:flags=area,crop=168:32:276:642,format=gray"
    raw = subprocess.check_output([
        "ffmpeg", "-v", "error", "-i", str(path), "-map", "0:v:0", "-vf", filters,
        "-fps_mode", "passthrough", "-f", "rawvideo", "-",
    ])
    return np.frombuffer(raw, dtype=np.uint8).reshape(-1, 168 * 32).astype(np.int16)


def normalize(frames):
    centered = frames.astype(np.float64) - frames.mean(axis=1, keepdims=True)
    lengths = np.linalg.norm(centered, axis=1, keepdims=True)
    return np.divide(centered, lengths, out=np.zeros_like(centered), where=lengths > 0)


def inspect(source, export, middle_stop):
    expected = np.concatenate([np.arange(start * 30, stop * 30) for start, stop
                               in [(3, 7), (12, middle_stop), (19, 23)]])
    if len(export) < len(expected):
        raise ValueError("Export ends before the program does.")
    if len(source) <= expected.max():
        raise ValueError("Source ends before the requested shot does.")
    correlations = normalize(export[:len(expected)]) @ normalize(source).T
    counts = {"unique_match": 0, "tied_for_best": 0, "other_frame_closer": 0}
    exceptions = []
    contrast_adjusted_unique = 0
    contrast_exceptions = []
    for index, frame in enumerate(expected):
        scores = correlations[index]
        adjusted = np.flatnonzero(np.isclose(scores, scores.max(), atol=1e-8, rtol=0))
        if adjusted.tolist() == [frame]:
            contrast_adjusted_unique += 1
        else:
            contrast_exceptions.append({"output": index, "expected": int(frame), "nearest": adjusted.tolist()})
        errors = np.abs(source - export[index]).sum(axis=1, dtype=np.int32)
        nearest = np.flatnonzero(errors == errors.min())
        if frame not in nearest:
            result = "other_frame_closer"
        elif len(nearest) > 1:
            result = "tied_for_best"
        else:
            result = "unique_match"
        counts[result] += 1
        if result != "unique_match":
            exceptions.append({"output": index, "expected": int(frame), "nearest": nearest.tolist()})
    return {"program_frames": len(expected), "decoded_frames": len(export),
            "counts": counts, "exceptions": exceptions,
            "contrast_adjusted_unique": contrast_adjusted_unique,
            "contrast_adjusted_exceptions": contrast_exceptions}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("first", type=Path)
    parser.add_argument("revision", type=Path)
    args = parser.parse_args()
    source = decode(args.source)
    for path, middle_stop in [(args.first, 16), (args.revision, 14)]:
        print(json.dumps({"file": path.name, **inspect(source, decode(path), middle_stop)}))
