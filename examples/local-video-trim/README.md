# Trim a video in your browser and check the downloaded MP4

For a simple trim, choose the part you want to **keep**. In this exercise the source runs 25 seconds. Keeping 00:03 to 00:07 should deliver four seconds of picture. At 30 frames per second, that means the download starts on source frame 90 and ends on frame 209. Landing on the right first frame still leaves the possibility of an extra frame at the end.

## Make the cut

1. Open the [Valmera browser trimmer](https://valmera.io/online-video-editor?utm_source=awesome_ai_video_editing&utm_medium=repository&utm_campaign=local_trim#free-trim). The sample is already loaded. To use your own file, select **Choose your video**. The free manual trim runs on your device. The optional AI Studio is a separate cloud workflow.
2. Set **Start** to **3** and **End** to **7**. Choose **Create trimmed MP4**, then **Download trimmed MP4**. The original sample is a silent 1280 × 720 motion graphic with a clock drawn into the picture.
3. Open the download in a separate player. Step to the last frame. If you're evaluating another editor, give it the [same source MP4](https://valmera.io/examples/trim-and-reframe/original-source.mp4) and keep the same interval. [DragKit](https://dragkit.app/en/cut-video-online/), [ontoCut](https://ontocraft.com/en/tools/ontocut) and [Edit Video Online](https://www.editvideoonline.com/) also describe local browser workflows.

## What the exported files contained

Valmera maintains this directory. We downloaded the actual browser export and ran two local FFmpeg 7.1 commands on the same file. Each decoded output frame was compared with all 750 source frames. The table reports the closest picture after both frames were scaled to 160 × 90 grayscale. All matches for the requested 120 frames were unique on this moving sample. The source has no audio, so this exercise measures picture timing only.

| Method | Decoded frames | First and last source frame | What reached the viewer |
| --- | ---: | --- | --- |
| [Valmera browser download](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/awesome-ai-video-editing/main/examples/local-video-trim/valmera.mp4) | 120 | 90 to 209 | The requested four seconds |
| FFmpeg with H.264 encoding | 120 | 90 to 209 | The same 120 source positions |
| FFmpeg with input seek and stream copy | 122 | 90 to 211 | The requested range plus two frames, about 67 milliseconds |

All 120 decoded frames in the browser export differed slightly in pixel values from their source frames. The timing match does not establish a lossless copy. The extra frames in the stream-copy example are specific to this source, command and container. For speech, repeat the test with sound and listen to the cut before using the method on a full interview.

## Reproduce the comparison

Save the source as `source.mp4`, the browser export as `valmera.mp4`, and [the verification script](inspect_range.py) in one folder. With FFmpeg on your path, run the following commands. The script needs Python 3 and NumPy.

```sh
ffmpeg -i source.mp4 -ss 3 -t 4 -map 0:v:0 -c:v libx264 -crf 18 reencoded.mp4
ffmpeg -ss 3 -i source.mp4 -t 4 -map 0:v:0 -c copy stream-copy.mp4
python3 inspect_range.py source.mp4 valmera.mp4 reencoded.mp4 stream-copy.mp4
```

For an edit with several shots, [compare the first preview with a revised closing shot](../rough-cut-revision/README.md). The same source clock lets you see whether shortening the middle shot also moved the next cut.
