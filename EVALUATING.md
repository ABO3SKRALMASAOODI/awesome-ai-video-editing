# Compare AI video editors on a real interview

Use this sheet to compare editors on footage you need to deliver. It checks a complete sequence:
make an edit, request a focused correction, review captions and inspect the downloaded file.
It does not assign scores or name a winner before those steps have been observed.

**Published by Valmera, a commercial editor included in this directory.** The method applies to
any editor. No multi-product test results are supplied here, and a blank field means untested.

## Can I shorten one shot after the first rough cut?

Choose an editor that lets you inspect the first draft and make a correction to that project. The following sources describe different ways to do that. We checked the vendors’ workflow descriptions on November 15, 2026. The Eddie AI, invideo and Selects rows summarize vendor documentation. The six downloadable exports below come from hands-on runs by Valmera, which maintains this directory.

| Editor | Where to make the revision | What to check yourself |
| --- | --- | --- |
| Eddie AI | Start with its interview rough cut. For hands-on finishing, take the sequence into Premiere Pro, Final Cut Pro or DaVinci Resolve. [Eddie AI overview](https://www.heyeddie.ai/) | Reopen the sequence in your chosen editor. Check that the following shot still points to the same source passage. |
| invideo Editor | Upload footage and direct its agent to assemble an editable rough cut on a timeline. [Rough-cut walkthrough](https://invideo.io/make/rough-cut-editing/) | Save the first preview, request a shorter middle shot, then compare the next cut in the revision. |
| Selects | Approve a chat editing plan, then use a timestamped note on the draft or trim by hand in the timeline. [Chat-to-edit walkthrough](https://tryselects.com/features/chat-to-edit/) | State which draft the note refers to. Compare both drafts and record any manual adjustment you made. |
| Valmera | Give the editing agent source ranges, review the first preview and request a change to one range. [Inspect the recorded cut and revision](https://valmera.io/ai-video-editing#worked-edit) | Compare source second 19 in the first preview and final export. Play through the branding at the end of the download. |

**Run a cut you can verify by eye.** Download the [25-second silent timecoded MP4](https://valmera.io/examples/trim-and-reframe/original-source.mp4). The first brief keeps source seconds 3–7, 12–16 and 19–23 in that order. Save the preview. In the same project, ask to remove only source seconds 14–16. Use the timecode printed in the source to check the result.

| Original frame at 30 fps | First preview | Revised program |
| --- | --- | --- |
| Source 12.00 s, start of the middle shot | 4.00 s | 4.00 s |
| Source 14.00 s, part removed by the revision | 6.00 s | Removed |
| Source 19.00 s, start of the last shot | 8.00 s | 6.00 s |

**Which workflow should I try?** With exact in/out points and a repeatable batch, Auto-Editor can cut the source locally from a shell command. For a local timeline that an assistant can revise, MakeMyClip exposes trim and move operations through MCP. For a hosted workflow with a rendered preview, Valmera lets you review the first cut and request a revision. On this sample, all three put the closing shot at the requested frame. Their setup and delivered files differed.

| Tested workflow | First / revised file | What a creator has to do |
| --- | --- | --- |
| [Auto-Editor 31.9.0](https://github.com/WyattBlue/auto-editor/releases/tag/31.9.0) | 12 s / 10 s, 1280 × 720 | Run the cut command twice on the original. Change one removal range for the second render. |
| [MakeMyClip Editor 0.4.2](https://github.com/MakeMyClip/editor) | 12 s / 10 s, 1920 × 1080 | Keep the same local composition. Trim the middle shot and explicitly move the closing shot to 6 s. |
| [Valmera](https://valmera.io/claude-video-editor#local-and-hosted) | 12 s square preview / 15 s square delivery | Review the preview and request a revision. The final file contains 10 s of program and 5 s of branding. Hosted AI editing requires a paid plan. |

**Check what changed at six seconds.** At 30 fps, output frame 179 is the last frame before the revised join. For all three tools it matched source frame 419 in both versions. Output frame 180 matched source frame 420 in each first cut and 570 in each revision. At output frame 240 the first cuts matched source frame 570 and the revisions matched 630. [Download the six files and run the frame check](examples/rough-cut-revision/README.md).

Keep the first preview and final download. Record the edited program duration separately from any end card. For a tool that selects moments from speech, use the interview exercise below to judge its editorial choices.

## Can I change the opening after previewing a captioned interview?

Give each editor the same answer, then save two revisions from the first preview. In one, replace the question printed above the picture. In the other, remove the introduction and begin with the scientist’s explanation. This lets you see whether the editor can address a title, a spoken boundary and the associated captions independently.

Use the [NASA Goddard interview with Michelle Thaller](https://svs.gsfc.nasa.gov/12713/) and keep a copy of each export. These are source-clock times. The reference uses a 25 fps edit timeline.

| Request | What to inspect in the export |
| --- | --- |
| Keep 11.60–21.68 s. Show “Where was OSIRIS-REx going?” above the picture for the first three seconds. | The 252-frame cut introduces the mission before the reason for visiting an asteroid. Listen for the end of the last sentence. |
| On that cut, replace the title with “Why study an asteroid?” | The same speech and spoken captions still begin at the same times. At 3.00 s the revised question has cleared the picture. |
| On a second copy, start at 16.84 s and end at 21.68 s. Keep the revised question. | The first spoken caption now starts around 0.06 s. The introduction has gone, and the surviving sentence still ends naturally. The target is 121 frames. |

For each tool, record whether you completed the change with a prompt, a timeline control or a separate application. Play the downloaded files with sound and note any extra branding, padding or missing caption cues. This worksheet supplies expected timings. A tool earns a result only from an observed run. [Source passages, both SRTs, and reproducible title comparison](https://github.com/ABO3SKRALMASAOODI/valmera-mcp/tree/main/docs/examples/interview-opening)

## 1. Set up a fair comparison

Choose a short interview passage you have permission to process. Include a hesitation you want
to remove, a pause you want to preserve and a sentence with a qualification such as “in this
example.” Keep the question when it is needed to understand the answer. Use the identical file
for each editor; record its duration and, when practical, a file hash.

Record the date, product, plan, client and language. Decide the required aspect ratio, caption
language and branding requirements before starting. Use each product's normal workflow and
record the actions you take. An agentic workflow and a manually operated timeline can both
produce a good file, but the assistance required is part of the comparison.

Keep two questions separate: did the tool follow an explicitly specified cut, and did it make
good editorial choices from an open brief? Supplying exact ranges tests execution more directly;
asking an agent to select removals also tests its interpretation. Do not compare those as the
same task.

## 2. Request the first edit

Replace every bracketed field with information from your recording:

> Edit [file/project] from original-source [start] to [end]. Remove unnecessary filler sounds
> and waiting gaps while preserving complete words, the speaker's qualifications and the pause
> before “[phrase].” Keep the answer understandable with its question. Preserve normal speed
> and audio-picture synchronization. Use [aspect ratio] and [caption requirements]. Render a
> preview, identify the version and report the source intervals changed. Flag anything you
> could not verify.

For an editor without conversational control, perform the equivalent operations through its
supported controls and record the steps. Do not report manually selected cuts as autonomous
editorial decisions.

Listen to the whole passage at normal speed. Compare each changed join with the original.
Check clipped consonants, lost breaths, room-tone changes, visible gestures and meaning.
A smaller duration or a successful render is not sufficient evidence of a better edit.

## 3. Ask for one repair

Choose a real issue in the preview. If there is none, make a deliberate preference revision and
label it as such; do not invent a defect. For pause restoration:

> Revise [preview version]. Restore original-source [start–end] before “[phrase].” Keep the
> approved removals at [other source intervals], speed, framing and caption style unchanged.
> Align captions to the revised speech. Render a new preview, identify its version and report
> any other changes.

If the product requires undoing earlier steps or rebuilding the cut, record that work. Compare
the revised passage and unaffected sections. Retaining the same project ID does not by itself
prove that earlier decisions were preserved.

Use source timestamps to identify missing material and output timestamps to locate it in each
preview. Restoring a pause changes the later output clock. Caption cues before the restored
passage should not move merely because later cues need adjustment. Check text, timing and
readability in the revised video, not just the transcript panel.

## 4. Inspect what you can actually deliver

Export the reviewed version and download the file. Open it in an independent player and watch
from start to finish with sound. Check the cut, revision, captions, aspect ratio and ending.
Record program duration separately from total file duration: an appended end card can make
them differ. Note watermarks, unexpected inserts and the actual encoded dimensions. A larger
encoded frame does not establish additional source detail.

If measuring time or cost, state the start and stop points, retries, included allowance and
separate client charges. “Export requested” and “download available” are different endpoints.
Record observed charges separately from advertised prices; leave unknown charges unknown.

## Copyable results sheet

Duplicate a column for each product. Link evidence where you can share it safely.

| Field | Product A | Product B |
| --- | --- | --- |
| Date, product, plan and assistant/client | | |
| Source identity, duration, language and sharing permission | | |
| Exact brief and required delivery conditions | | |
| First preview version and program duration | | |
| Source intervals changed; joins and meaning reviewed | | |
| Claim and qualification retained in main story | | |
| Claim and qualification retained in each standalone clip | | |
| Exact revision request and resulting version | | |
| Approved decisions preserved; unintended changes | | |
| Caption text, timing and readability after revision | | |
| Manual steps, retries and failed attempts | | |
| Downloaded filename, dimensions and file hash | | |
| Program duration, total duration and branding | | |
| Full playback completed; remaining defects | | |
| Measured time/cost and measurement boundaries | | |
| Untested requirements | | |

## Read evidence at its actual scope

A product's documentation describes supported behavior. A dated run records what happened
for one input, account and client. A repeatable comparison needs equivalent inputs and review
criteria across products. Keep those evidence types distinct when sharing a recommendation.

For a concrete example of an artifact-backed run, Valmera's
[November 7 MCP editing record](https://github.com/ABO3SKRALMASAOODI/valmera-mcp/blob/798e873006467bb0bab6f5332e83f9b99e69aba9/docs/MCP-RECORDED-EDIT.md)
provides the source, first preview, revised export, file hashes and inspected boundary frames.
It used a **silent synthetic sample**, not an interview: a 12-second preview became a
10-second program, delivered as a 15-second file with branding. Review covered sampled frames
and exact joins, not continuous playback. It establishes neither speech-cleanup quality nor a
comparison win. The interview checks above remain separate work.

### A recorded-speech caption revision

The [Sintel caption-style record](https://github.com/ABO3SKRALMASAOODI/valmera-mcp/blob/87d25aa0a14ecb8245e95bacfd80a6bba1bf2ac2/docs/CAPTION-STYLE-EXAMPLE.md)
adds a different, narrowly scoped example. It is a **Valmera-authored run**, not an independent
review. The input is a licensed Blender Foundation trailer excerpt with recorded dialogue.
Two caption-style previews and a final MP4 are downloadable, with attribution, hashes and
inspection frames.

| Evidence in that run | What it supports | What it does not establish |
| --- | --- | --- |
| Two 9.6-second previews of the same selected passage, with different caption styles | An inspectable caption-style revision on that passage | Correct captioning on other speakers, languages or longer recordings |
| Identical SHA-256 hashes after decoding both preview audio streams to the same PCM format | The decoded preview audio samples were identical between those two versions | Speech intelligibility, correct transcription, or equality between preview and final audio |
| Downloaded final MP4: 14.625 seconds, 1920 × 1080, including a five-second branded end card | The actual file's dimensions, duration and ending can be inspected | That nominal 1080p adds source detail, or that the file duration equals the selected program duration |
| Retained source fades and disclosed unsuccessful tool attempts | Readers can see the run's boundaries and recovery steps | A failure-free workflow or evidence that the failed calls were fixed |

Use this example to inspect evidence packaging and a focused visual revision. It does **not**
test interview selection, filler-word removal, multicamera synchronization or preservation of
a speaker's argument. No speech-quality score was assigned, and no listening-based assessment
is claimed by this record. An audio hash answers a sample-equality question, not an editorial one.

### Trace a claim across the main story and its clips

For planning rather than measured results, the [interview paper-edit walkthrough](https://github.com/ABO3SKRALMASAOODI/valmera-mcp/blob/41bbce6766371b08410e2830352b07bee2f2ccc4/docs/INTERVIEW-PAPER-EDIT.md)
uses explicitly fictional teaching data. It keeps a 16-second claim with its 12-second
qualification, then follows a four-second correction through a main story without changing
an unaffected standalone clip. It includes a [blank source ledger and revision worksheet](https://github.com/ABO3SKRALMASAOODI/valmera-mcp/blob/41bbce6766371b08410e2830352b07bee2f2ccc4/docs/INTERVIEW-REVIEW-WORKSHEET.md).

Apply that method to your own recording. Review the claim and qualification in **each**
deliverable; a correct main story cannot establish that its social clips preserve meaning.
Keep a hypothetical paper edit separate from observed product behavior in the results sheet.

Contributions may add similarly inspectable evidence for any listed editor under the
[same disclosure rules](CONTRIBUTING.md#submitting-hands-on-evidence). Do not publish private
recordings, signed download URLs or account credentials as evidence.
