# Did the next shot move when the middle shot got shorter?

The first edit keeps source seconds 3–7, 12–16 and 19–23. The revision shortens the middle selection to 12–14. In the revised cut, the closing shot should start at output second 6 and show source second 19. Valmera ran this check on November 16, 2026 using its own 25-second silent clock clip.

## Get the files

1. [Download and extract the source and four hosted/local MCP exports](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/ed1374e07ba63652f8461280cf69ca19c67f2ee8/docs/examples/video-edit-revision/revision-test.zip). The archive contains the initial and revised files from Valmera and MakeMyClip.
2. Save [Auto-Editor’s first cut](cli-first.mp4), [its revised cut](cli-revised.mp4) and the [frame check](inspect_join.py) in the extracted folder.
3. With Python 3, Pillow and FFmpeg installed, run the following command there.

```sh
python3 inspect_join.py original-source.mp4 first-preview.mp4 revised-final.mp4 first-cut.mp4 shorter-cut.mp4 cli-first.mp4 cli-revised.mp4
```

The check compares each selected output frame with every frame of the source, returns the closest match and reports ties. It uses a centered 96 × 96 grayscale crop to compare different canvas shapes. Mean absolute pixel difference is on a 0–255 scale. The synthetic clock makes these three moments visually distinct. For footage with static holds, repeated frames can produce equally good matches. To inspect the result by eye, step across output frames 179 and 180 and read the clock in the picture.

| File pair | Frame 179, before the join | Frame 180, at the join | Frame 240, two seconds later |
| --- | --- | --- | --- |
| Valmera first / revised | 419 / 419 | 420 / 570 | 570 / 630 |
| MakeMyClip first / revised | 419 / 419 | 420 / 570 | 570 / 630 |
| Auto-Editor first / revised | 419 / 419 | 420 / 570 | 570 / 630 |

Each cell gives the source-frame number for the first cut and the revised cut. All 18 matches were unique within this source. This exercise checks shot timing. The input has no speech and the editor receives the selection boundaries.

## Render the command-line cuts yourself

Install [Auto-Editor 31.9.0](https://github.com/WyattBlue/auto-editor/releases/tag/31.9.0). From the folder with the source clip, run these commands. The revision moves the start of one removed interval from 16 s to 14 s. Both commands use the original file as input.

```sh
auto-editor original-source.mp4 --edit none --cut 0sec,3sec --cut 7sec,12sec --cut 16sec,19sec --cut 23sec,end --no-open -o cli-first.mp4
auto-editor original-source.mp4 --edit none --cut 0sec,3sec --cut 7sec,12sec --cut 14sec,19sec --cut 23sec,end --no-open -o cli-revised.mp4
```

Auto-Editor kept the original 1280 × 720 landscape frame. The MCP tools used different canvases. The [local timeline calls and hosted editing record](https://github.com/ABO3SKRALMASAOODI/valmera-mcp/blob/ed1374e07ba63652f8461280cf69ca19c67f2ee8/docs/examples/video-edit-revision/makemyclip/README.md) explain how those files were made.
