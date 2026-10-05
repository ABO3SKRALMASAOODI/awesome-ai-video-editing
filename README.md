# Awesome AI Video Editing [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of AI and agentic tools for editing video — plus the MCP servers, open-source
> projects, models, papers and datasets underneath them.

**Every entry below was opened and checked on 2026-08-05.** Star counts, licences and
last-commit dates are from that date and will drift; nothing is listed that could not be
confirmed to exist and to be usable. Dead products and abandoned repos are either removed or
labelled as such.

## The distinction that matters

Most "AI video" lists mix three unrelated things. Keeping them apart is the whole point of this page.

| | What it does | Your footage |
|---|---|---|
| **Agentic editors** | You state a goal in plain language; an agent plans and performs the edit | Required — it edits what you shot |
| **AI-assisted editors** | A human drives a timeline; AI does chores (silence removal, captions, reframing, grading) | Required |
| **Generative video** | A model synthesises new frames from a prompt | Not used — it makes footage instead |

A generative model cannot cut your interview. An agentic editor cannot invent a shot you never
filmed. Tools that claim both are usually strong at one.

## Contents

- [Agentic video editors](#agentic-video-editors)
- [AI-assisted editors](#ai-assisted-editors)
- [Clipping and repurposing](#clipping-and-repurposing)
- [Captions and subtitles](#captions-and-subtitles)
- [Video MCP servers](#video-mcp-servers)
- [Open-source projects and frameworks](#open-source-projects-and-frameworks)
- [Generative video](#generative-video)
- [Speech, transcription and audio](#speech-transcription-and-audio)
- [Libraries and building blocks](#libraries-and-building-blocks)
- [Research papers and benchmarks](#research-papers-and-benchmarks)
- [Datasets](#datasets)
- [Reading](#reading)
- [Contributing](#contributing)

## Agentic video editors

An agent takes a natural-language goal and performs the edit on footage you supply. This is a
young category — most entries are under two years old and every one of them has real limits,
noted here.

- [Cutback](https://cutback.video) - Assistant for Premiere Pro that pre-builds selects and rough cuts from raw and multi-cam footage. *(hosted, Premiere plugin)*
- [Diffusion Studio Agent](https://github.com/diffusionstudio/agent) - Framework where an LLM writes and runs browser-based compositing code to fulfil an editing request. *(MIT · 275★ · last commit 2025-02)*
- [Mosaic](https://mosaic.so) - Node canvas where agents run edits on autopilot and produce A/B variants from one set of rushes, with a timeline to take over. *(hosted)*
- [Underlord (Descript)](https://www.descript.com/underlord) - Agent inside Descript that acts on editing instructions across a transcript-backed timeline. *(hosted, requires Descript)*
- [Valmera](https://valmera.io) - Indexes your footage (word-level transcript, shots, frames), then edits a versioned EDL from a plain-English brief, renders and checks a preview, and turns long videos into shorts. Final MP4 renders from the original file. No SRT export or team seats. *(hosted · free account, paid editing)*
- [VideoAgent (HKUDS)](https://github.com/HKUDS/VideoAgent) - Research framework combining video understanding, editing and remaking behind one agent loop. *(MIT · 1.6k★)*
- [agentic-video-editor](https://github.com/poseljacob/agentic-video-editor) - Turns raw footage plus a creative brief into an ad using an ensemble of Gemini agents over FFmpeg. *(MIT · 467★)*

## AI-assisted editors

A human drives the timeline; AI removes the chores. Includes the plugins that add AI to a
conventional NLE.

- [Adobe Premiere](https://www.adobe.com/products/premiere.html) - Industry-standard NLE; ships Text-Based Editing, Generative Extend, Enhance Speech and Media Intelligence search. *(paid)*
- [AutoCut](https://www.autocut.com) - Premiere Pro and DaVinci Resolve plugin for silence removal, captions, B-roll, zooms and podcast multi-cam. *(paid plugin)*
- [Camtasia](https://www.techsmith.com/camtasia/) - Screen recorder and editor aimed at tutorials and software demos, with AI captions and voice. *(paid · free trial)*
- [Canva Video Editor](https://www.canva.com/video-editor/) - Browser drag-and-drop editor with templates, brand kits and AI generation built into the same canvas. *(hosted · free tier)*
- [CapCut](https://www.capcut.com) - Free social-first editor on web, desktop and mobile with auto-captions, reframing and effect templates. *(hosted and desktop · free tier)*
- [Captions](https://captions.ai) - Talking-head editor that handles cuts, captions, eye-contact correction and dubbing from a phone or browser. *(hosted)*
- [Clipchamp](https://app.clipchamp.com) - Microsoft's browser editor with auto-compose, speaker coach and text-to-speech, free with a Microsoft account. *(hosted · free tier)*
- [Clueso](https://www.clueso.io) - Turns a rough screen recording into a narrated, on-brand product video and a written step-by-step guide. *(hosted)*
- [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) - Editing, colour, VFX and audio post in one app; the Neural Engine does tracking, isolation, reframing and speech cleanup. *(desktop · free tier)*
- [Descript](https://www.descript.com) - Edits video by editing its transcript; removes filler words, clones voice and fixes gaze. *(hosted · free tier)*
- [Filmora](https://filmora.wondershare.com) - Consumer desktop and mobile editor with AI masking, smart cutout and motion tracking. *(paid · free trial)*
- [Final Cut Pro](https://www.apple.com/final-cut-pro/) - Apple's Mac and iPad NLE, with magnetic timeline, scene-removal mask and voice isolation. *(paid)*
- [FireCut](https://www.firecut.ai) - Plugin that automates silence removal, captions, zoom cuts and chapters inside Premiere Pro and Resolve. *(paid plugin · free tier)*
- [Gling](https://www.gling.ai) - Removes bad takes and silences from talking-head YouTube footage and hands back a timeline. *(hosted)*
- [Kapwing](https://www.kapwing.com) - Collaborative browser editor that can also assemble a whole project from a single prompt. *(hosted · free tier)*
- [Movavi Video Editor](https://www.movavi.com) - Lightweight consumer editor for Windows and Mac with background removal and motion tracking. *(paid · free trial)*
- [Recut](https://getrecut.com) - Desktop app that strips silence from long recordings and exports to Premiere, Resolve or Final Cut. *(paid)*
- [Riverside](https://riverside.com) - Records local-quality remote podcasts and video, then edits by transcript and cuts clips. *(hosted · free tier)*
- [Runway](https://runway.com) - Generation plus a working toolbox: inpainting, rotoscoping, motion tracking and green-screen removal. *(hosted · free tier)*
- [TimeBolt](https://www.timebolt.io) - Jump-cuts silence, filler words and bad takes out of talking videos and podcasts. *(paid)*
- [Topaz Video](https://www.topazlabs.com/topaz-video) - Model-based upscaling, denoise, deinterlacing and frame interpolation for archival and low-light footage. *(paid)*
- [VEED](https://www.veed.io) - Browser editor combining subtitles, dubbing, avatars and a template library in one workflow. *(hosted · free tier)*
- [Wisecut](https://wisecut.ai) - Auto-cuts long talking video into short clips, adds captions, ducks background music. *(hosted · free tier)*

## Clipping and repurposing

Long video in, short vertical clips out.

- [2short.ai](https://2short.ai) - Turns long YouTube uploads into shorts, aimed at channel growth rather than social scheduling. *(hosted)*
- [AI-Youtube-Shorts-Generator](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator) - Open-source clipper using LLM highlight detection, Whisper and face-aware 9:16 reframing. *(no licence file · 4.5k★)*
- [Clips AI](https://github.com/ClipsAI/clipsai) - Python library that converts long video into clips and reframes them; transcript-driven. *(MIT · 524★ · last commit 2024-01)*
- [Crayo](https://crayo.ai) - Short-form generator for gameplay-and-voiceover formats with subtitles and stock backgrounds. *(hosted)*
- [Klap](https://klap.app) - One-click clipping of podcasts and webinars with captions, reframing and a virality score. *(hosted)*
- [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) - Generates full short videos from a topic or keyword through an automated LLM plus stock pipeline. *(MIT · 102k★)*
- [OpusClip](https://www.opus.pro) - The most widely cited clipper; scores moments, reframes to vertical and adds animated captions. *(hosted · free tier)*
- [Podsqueeze](https://podsqueeze.com) - Podcast-focused: transcripts, summaries, show notes and audiogram clips from one upload. *(hosted · free tier)*
- [Reap](https://reap.video) - Clips, captions and dubs long video into 100+ languages, with an API for pipeline use. *(hosted)*
- [ShortGPT](https://github.com/RayVentura/ShortGPT) - Experimental framework for automating short-form channels end to end. *(MIT · 7.8k★ · last commit 2025-02)*
- [Spikes Studio](https://www.spikes.studio) - Clip generator built around Twitch and livestream footage as well as YouTube. *(hosted)*
- [Submagic](https://www.submagic.co) - Caption-led short-form editor with B-roll, zooms and sound effects applied automatically. *(hosted)*
- [Vizard](https://vizard.ai) - Long-to-short clipping with editable transcript, captions and a template library. *(hosted · free tier)*
- [quso.ai](https://quso.ai) - Clips long video and schedules the results straight to social accounts. *(hosted · free tier)*

## Captions and subtitles

Burn-in, translation, and the editors that handle subtitle files properly.

- [Aegisub](https://github.com/Aegisub/Aegisub) - The reference typesetting subtitle editor for ASS/SSA; still what fansub-grade karaoke and effects are built in. *(3.4k★ · last commit 2019-10; community forks are more active)*
- [Buzz](https://github.com/chidiwilliams/buzz) - Desktop app that transcribes and translates offline with Whisper, exporting SRT, VTT and more. *(MIT · 20.8k★)*
- [Happy Scribe](https://www.happyscribe.com) - Transcription and subtitling in 150+ languages with human-review upgrades. *(hosted · free tier)*
- [Maestra](https://maestra.ai) - Subtitles, transcripts and multilingual voiceover for on-demand and live media in 125+ languages. *(hosted)*
- [Notta](https://www.notta.ai) - Meeting and interview transcription with summaries and subtitle export. *(hosted · free tier)*
- [Otter](https://otter.ai) - Live meeting transcription and notes; useful as a source of timed text rather than as an editor. *(hosted · free tier)*
- [Rev](https://www.rev.com) - Human and AI transcription and captioning with a long track record on accuracy-critical work. *(hosted)*
- [Sonix](https://sonix.ai) - Transcription and subtitling in 49+ languages with an in-browser aligned editor. *(hosted)*
- [Subs AI](https://github.com/absadiki/subsai) - Web UI, CLI and Python package for generating subtitles with Whisper and its variants. *(GPL-3.0 · 1.7k★)*
- [Subtitle Edit](https://github.com/SubtitleEdit/subtitleedit) - The most complete open-source subtitle editor: sync, OCR, waveform, 300+ formats. *(MIT · 13.7k★)*
- [Vibe](https://github.com/thewh1teagle/vibe) - Cross-platform desktop transcription app that runs entirely on your machine. *(MIT · 7.0k★)*
- [Zeemo](https://zeemo.ai) - Auto-captioning with styled templates aimed at social video. *(hosted · free tier)*

## Video MCP servers

[Model Context Protocol](https://modelcontextprotocol.io) servers that give an AI assistant real
video tools. This section is the least covered elsewhere, so it is deliberately complete rather
than filtered by popularity — small repos are listed with their star counts so you can judge.

- [Claude Code Video Toolkit](https://github.com/wilwaldon/Claude-Code-Video-Toolkit) - Bundle of skills and MCP servers for Remotion, Manim, screen recording, YouTube clipping and FFmpeg. *(no licence file · 64★)*
- [DaVinci Resolve MCP](https://github.com/samuelgursky/davinci-resolve-mcp) - Drives Resolve Studio through its official scripting API: timeline, media pool, render, grade, Fusion, Fairlight. *(MIT · 2.0k★)*
- [ElevenLabs MCP](https://github.com/elevenlabs/elevenlabs-mcp) - Official server for speech synthesis, dubbing and voice cloning — the audio half of a video pipeline. *(MIT · 1.5k★)*
- [Kinocut](https://github.com/KyaniteLabs/kinocut) - Guardrailed local editing server over FFmpeg with repurposing tools, a Python client and a CLI. *(Apache-2.0 · 99★)*
- [Manim MCP Server](https://github.com/abhiemj/manim-mcp-server) - Renders Manim animations from an assistant, for explainer and motion-graphics inserts. *(MIT · 626★)*
- [MCP Server Whisper](https://github.com/arcaputo3/mcp-server-whisper) - Exposes audio transcription to an assistant, with batch processing of local files. *(MIT · 56★)*
- [Remotion MCP App](https://github.com/mcp-use/remotion-mcp-app) - The model writes React/Remotion compositions, the server compiles them and a live player renders the result. *(41★)*
- [Valmera MCP](https://github.com/ABO3SKRALMASAOODI/valmera-mcp) - Hosted editor for uploaded footage over OAuth: transcript-aware cuts, captions, reframing, shorts, b-roll, music, rendered previews and final MP4 export. Maintainer's own product, see [CONTRIBUTING](CONTRIBUTING.md). *(MIT docs · hosted service)*
- [Video Editor MCP](https://github.com/Kush36Agrawal/Video_Editor_MCP) - Compact FFmpeg server covering trim, concat, overlay and format conversion. *(no licence file · 50★)*
- [Video Jungle MCP](https://github.com/burningion/video-editing-mcp) - Client for [Video Jungle](https://www.video-jungle.com): upload, search and edit video from an assistant. *(no licence file · 284★ · last commit 2025-10)*
- [ffmpeg-mcp (AmolDerickSoans)](https://github.com/AmolDerickSoans/ffmpeg-mcp) - Broad wrapper covering decode, encode, transcode, mux, demux, stream and filter. *(MIT · 14★ · last commit 2025-03)*
- [ffmpeg-mcp (dubnium0)](https://github.com/dubnium0/ffmpeg-mcp) - 40+ tools spanning processing, analysis and streaming. *(no licence file · 19★)*
- [ffmpeg-mcp-server](https://github.com/beambuilder/ffmpeg-mcp-server) - Small, focused server for pulling highlight segments out of long recordings. *(MIT · 3★)*
- [mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) - Fetches YouTube transcripts directly into the model's context. *(MIT · 581★)*
- [mcp-video-editor](https://github.com/chandler767/mcp-video-editor) - FFmpeg plus Whisper, so cuts can be made against what was actually said. *(no licence file · 5★)*
- [mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript) - Transcript retrieval with language selection and chunking for long videos. *(MIT · 463★)*
- [vfx-mcp](https://github.com/connerohnesorge/vfx-mcp) - Effects-oriented server for compositing and filter chains. *(MIT · 8★)*
- [vibevideo-mcp](https://github.com/hyepartners-gmail/vibevideo-mcp) - FFmpeg agent server that also backs a human-facing editor front end. *(no licence file · 217★ · last commit 2025-06)*
- [video-audio-mcp](https://github.com/misbahsy/video-audio-mcp) - FFmpeg server for conversion, trimming, overlays, transitions and audio processing. *(MIT · 83★ · last commit 2025-05)*

Directories worth checking for newer servers: the [official MCP registry](https://registry.modelcontextprotocol.io),
[mcp.so](https://mcp.so), [mcpservers.org](https://mcpservers.org) and
[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) (92k★).

Note: Remotion's own hosted MCP is deprecated; its docs now point to Remotion Agent Skills instead.

## Open-source projects and frameworks

- [Diffusion Studio Core](https://github.com/diffusionstudio/core) - Browser compositing engine on WebCodecs; renders timelines client-side. *(MPL-2.0 · 1.2k★)*
- [FFCreator](https://github.com/tnfe/FFCreator) - Node.js library for building videos from images, text and transitions at speed. *(MIT · 3.2k★ · last commit 2024-12)*
- [Flowblade](https://github.com/jliljebl/flowblade) - Multitrack Linux NLE with a film-style, film-first workflow. *(GPL-3.0 · 3.1k★)*
- [HandBrake](https://github.com/HandBrake/HandBrake) - The default answer for transcoding and batch conversion before or after an edit. *(GPL-2.0 · 23.9k★)*
- [Kdenlive](https://github.com/KDE/kdenlive) - KDE's mature multitrack editor built on MLT; proxy editing, effects, keyframes. *(GPL-3.0 · 5.4k★)*
- [LosslessCut](https://github.com/mifi/lossless-cut) - Trims, cuts and merges without re-encoding — the fastest way to top and tail huge files. *(GPL-2.0 · 42.6k★)*
- [Motion Canvas](https://github.com/motion-canvas/motion-canvas) - TypeScript library and editor for procedurally animated explainer video. *(MIT · 18.9k★)*
- [Olive](https://github.com/olive-editor/olive) - Node-based free NLE with a professional feature target. *(GPL-3.0 · 9.1k★ · last commit 2024-12)*
- [OpenShot](https://github.com/OpenShot/openshot-qt) - Cross-platform desktop editor with keyframes, titles and 3D animation, aimed at beginners. *(GPL-3.0 · 6.1k★)*
- [Pitivi](https://github.com/pitivi/pitivi) - GTK non-linear editor built on GStreamer Editing Services. *(GitHub mirror · 243★)*
- [Remotion](https://github.com/remotion-dev/remotion) - Make videos programmatically in React; the standard for data-driven and templated output. *(source-available, company licence required · 55.5k★)*
- [Revideo](https://github.com/midrender/revideo) - Fork of Motion Canvas turned into a programmatic video API for parameterised rendering. *(MIT · 4.0k★)*
- [Shotcut](https://github.com/mltframework/shotcut) - Cross-platform editor on MLT with wide format support and a very active release cadence. *(GPL-3.0 · 14.8k★)*
- [auto-editor](https://github.com/WyattBlue/auto-editor) - Cuts silence and dead air from the command line, exporting to Premiere, Resolve and Final Cut. *(Unlicense · 4.7k★)*
- [autocut](https://github.com/mli/autocut) - Edit video by editing its transcript in a text editor; delete a line, lose the take. *(Apache-2.0 · 7.8k★ · last commit 2024-10)*
- [editly](https://github.com/mifi/editly) - Declarative CLI and Node API that renders an edit from a JSON spec. *(MIT · 5.5k★ · last commit 2025-02)*

## Generative video

**A different category.** These models synthesise footage; they do not edit yours. They are here
because every "AI video editor" listicle mixes them in, and because generated shots do end up on
real timelines as inserts and B-roll.

Note: OpenAI's Sora app and website were discontinued on 2026-04-26 and its API retires
2026-09-24, so it is not listed despite still appearing in most roundups.

### Hosted models and platforms

- [D-ID](https://www.d-id.com) - Talking-avatar video from a photo and a script, with an interactive-agent product on top. *(hosted)*
- [Fliki](https://fliki.ai) - Turns scripts and blog posts into narrated video with 2,000+ voices in 80+ languages. *(hosted · free tier)*
- [Gemini Omni](https://gemini.google/overview/video-generation/) - Google's conversational video model; generates from text, image or video and re-generates edits like backgrounds and lighting on uploads. *(hosted)*
- [Hailuo](https://hailuoai.video) - MiniMax's text- and image-to-video model, known for character motion. *(hosted · free tier)*
- [Hedra](https://www.hedra.com) - Character and performance video generation from image plus audio. *(hosted)*
- [HeyGen](https://www.heygen.com) - Avatar video and translation with lip-sync across languages. *(hosted)*
- [Higgsfield](https://higgsfield.ai) - Camera-motion-led generation suite with an agent for repeat creative workflows. *(hosted)*
- [Kling](https://kling.ai) - Kuaishou's video model, strong on longer shots and physical motion. *(hosted · free tier)*
- [Krea](https://www.krea.ai) - Real-time creative suite for image, video and 3D with enhancement and editing passes. *(hosted · free tier)*
- [LTX Studio](https://ltx.io/studio) - Storyboard-to-video production environment with shot-level control, built on LTX models. *(hosted)*
- [Luma Dream Machine](https://lumalabs.ai/app) - Text and image to video with keyframe interpolation between stills. *(hosted · free tier)*
- [Midjourney](https://www.midjourney.com) - Image model with video generation; the reference for stylised look development. *(hosted)*
- [Pictory](https://pictory.ai) - Script and article to video using stock footage and synthetic narration. *(hosted)*
- [Pika](https://pika.art) - Short generative clips with an effects-led, consumer-facing interface. *(hosted · free tier)*
- [Runway](https://runway.com) - Gen-series video models alongside the editing toolbox listed above. *(hosted · free tier)*
- [Renderforest](https://www.renderforest.com) - Template-driven video, logo and website generation for marketing output. *(hosted · free tier)*
- [Synthesia](https://www.synthesia.io) - Enterprise avatar video from a script, with brand templates and localisation. *(hosted)*
- [Veo](https://deepmind.google/models/veo/) - Google DeepMind's video generation model, with native audio. *(hosted)*
- [Vidu](https://www.vidu.com) - Text, image and reference-driven generation with consistent characters across shots. *(hosted · free tier)*
- [Wan](https://wan.video) - Alibaba's hosted front end for the open Wan models. *(hosted · free tier)*
- [invideo AI](https://invideo.io) - Prompt-to-video agent that scripts, sources stock and narrates a full edit. *(hosted · free tier)*

### Open models and tooling

- [Allegro](https://github.com/rhymes-ai/Allegro) - Text-to-video model producing 6-second 720p clips at 15fps. *(Apache-2.0 · 1.1k★)*
- [AnimateDiff](https://github.com/guoyww/AnimateDiff) - Motion module that animates existing Stable Diffusion checkpoints. *(Apache-2.0 · 12.2k★ · last commit 2024-07)*
- [CogVideo / CogVideoX](https://github.com/zai-org/CogVideo) - Zhipu's text- and image-to-video family with released weights and finetuning code. *(Apache-2.0 · 12.9k★)*
- [ComfyUI](https://github.com/Comfy-Org/ComfyUI) - Node-graph backend and GUI that most open video models are actually run through. *(GPL-3.0 · 124k★)*
- [Deforum](https://github.com/deforum/deforum-stable-diffusion) - Keyframed camera-motion animation from diffusion models; the origin of the look. *(2.3k★ · last commit 2024-08)*
- [EasyAnimate](https://github.com/aigc-apps/EasyAnimate) - End-to-end transformer-diffusion pipeline for long, high-resolution generation. *(Apache-2.0 · 2.3k★ · last commit 2025-03)*
- [FramePack](https://github.com/lllyasviel/FramePack) - Next-frame prediction that makes long video diffusion practical on modest GPUs. *(Apache-2.0 · 17.2k★)*
- [HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo) - Tencent's large open video generation framework with weights and inference code. *(community licence · 12.4k★)*
- [LTX-Video](https://github.com/Lightricks/LTX-Video) - Lightricks' fast DiT video model, tuned for real-time-ish local generation. *(Apache-2.0 · 10.8k★)*
- [Mochi 1](https://github.com/genmoai/mochi) - Genmo's open video generation model with an emphasis on motion fidelity. *(Apache-2.0 · 3.7k★)*
- [Open-Sora](https://github.com/hpcaitech/Open-Sora) - Full open reproduction of a Sora-style pipeline, including training code. *(Apache-2.0 · 29.2k★)*
- [Open-Sora-Plan](https://github.com/PKU-YuanGroup/Open-Sora-Plan) - Parallel community reproduction effort with released checkpoints. *(MIT · 12.2k★)*
- [Stable Video Diffusion](https://github.com/Stability-AI/generative-models) - Stability's image-to-video model and reference implementation. *(MIT · 27.2k★)*
- [VideoCrafter](https://github.com/AILab-CVC/VideoCrafter) - Research video diffusion models for text-to-video and image-to-video. *(5.1k★)*
- [Wan 2.1](https://github.com/Wan-Video/Wan2.1) - Alibaba's open video model, widely used as a finetuning base. *(Apache-2.0 · 16.7k★)*
- [Wan 2.2](https://github.com/Wan-Video/Wan2.2) - The follow-up release, with a mixture-of-experts architecture. *(Apache-2.0 · 17.0k★)*

## Speech, transcription and audio

Word-level timing is what makes transcript-driven and agentic editing possible at all.

- [AssemblyAI](https://www.assemblyai.com) - Speech-to-text API with diarization, chapters and audio intelligence models. *(hosted API · free tier)*
- [Deepgram](https://deepgram.com) - Low-latency streaming and batch speech-to-text with a strong real-time story. *(hosted API · free tier)*
- [Demucs](https://github.com/adefossez/demucs) - Hybrid source separation; splits dialogue from music and effects. *(MIT · 3.0k★)*
- [ElevenLabs](https://elevenlabs.io) - Voice synthesis, cloning and dubbing used for voiceover and localisation. *(hosted · free tier)*
- [Montreal Forced Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) - Kaldi-based forced alignment; the standard when phoneme-level timing matters. *(MIT · 1.9k★)*
- [NVIDIA NeMo](https://github.com/NVIDIA-NeMo/Speech) - Production speech toolkit with Parakeet and Canary ASR models and diarization. *(Apache-2.0 · 17.9k★)*
- [Silero VAD](https://github.com/snakers4/silero-vad) - Fast, tiny voice-activity detector — the practical way to find silences to cut. *(MIT · 9.9k★)*
- [SpeechBrain](https://github.com/speechbrain/speechbrain) - PyTorch toolkit spanning ASR, separation, enhancement and speaker tasks. *(Apache-2.0 · 11.7k★)*
- [Vosk](https://github.com/alphacep/vosk-api) - Offline speech recognition for 20+ languages on desktop, mobile and Raspberry Pi. *(Apache-2.0 · 15.0k★)*
- [Whisper](https://github.com/openai/whisper) - OpenAI's multilingual ASR model; the base almost everything below builds on. *(MIT · 107k★)*
- [WhisperX](https://github.com/m-bain/whisperX) - Whisper with forced-alignment word timestamps and speaker diarization. *(BSD-2-Clause · 23.4k★)*
- [aeneas](https://github.com/readbeyond/aeneas) - Synchronises audio to an existing text without recognising it. *(AGPL-3.0 · 2.9k★ · last commit 2020-05)*
- [ctc-forced-aligner](https://github.com/MahmoudAshraf97/ctc-forced-aligner) - Lightweight multilingual CTC forced alignment with no Kaldi dependency. *(no licence file · 542★)*
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) - CTranslate2 reimplementation, several times faster than the reference at equal accuracy. *(MIT · 24.7k★)*
- [ffmpeg-normalize](https://github.com/slhck/ffmpeg-normalize) - Batch EBU R128 and peak normalisation wrapper around FFmpeg. *(1.5k★)*
- [gentle](https://github.com/strob/gentle) - Robust forced aligner that returns word timings and flags the words it could not place. *(MIT · 1.7k★)*
- [insanely-fast-whisper](https://github.com/Vaibhavs10/insanely-fast-whisper) - Batched, optimised Whisper CLI for bulk transcription. *(Apache-2.0 · 13.0k★ · last commit 2024-05)*
- [pyannote.audio](https://github.com/pyannote/pyannote-audio) - Speaker diarization toolkit — who spoke when, which is what multi-cam cutting needs. *(MIT · 10.4k★)*
- [pyloudnorm](https://github.com/csteinmetz1/pyloudnorm) - ITU-R BS.1770-4 loudness measurement in Python, for hitting delivery LUFS targets. *(MIT · 779★)*
- [python-audio-separator](https://github.com/nomadkaraoke/python-audio-separator) - CLI and library wrapping many UVR stem-separation models. *(MIT · 1.3k★)*
- [stable-ts](https://github.com/jianfch/stable-ts) - Stabilises Whisper timestamps and adds alignment and audio indexing. *(MIT · 2.3k★)*
- [whisper-timestamped](https://github.com/linto-ai/whisper-timestamped) - Word-level timestamps and per-word confidence from Whisper directly. *(AGPL-3.0 · 2.8k★)*
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp) - C/C++ port that runs Whisper on CPU, phones and edge devices. *(MIT · 52.6k★)*

## Libraries and building blocks

- [FFmpeg](https://github.com/FFmpeg/FFmpeg) - The layer under nearly every tool on this page. *(GPL-2.0 / LGPL · 63k★)*
- [FFmpeg Filters Documentation](https://ffmpeg.org/ffmpeg-filters.html) - The filtergraph reference; the single most useful page for anyone building an editor.
- [MLT Framework](https://github.com/mltframework/mlt) - Multimedia authoring framework behind Shotcut and Kdenlive; models tracks and transitions. *(LGPL-2.1 · 1.8k★)*
- [Mediabunny](https://github.com/Vanilagy/mediabunny) - Pure TypeScript toolkit to read, write and convert media in the browser. *(MPL-2.0 · 6.9k★)*
- [MoviePy](https://github.com/Zulko/moviepy) - The usual first library for scripted cutting, concatenation and compositing in Python. *(MIT · 14.8k★)*
- [OpenCV](https://github.com/opencv/opencv) - Frame-level computer vision: tracking, face detection, cropping and reframing. *(Apache-2.0 · 90k★)*
- [PyAV](https://github.com/PyAV-Org/PyAV) - Pythonic bindings to FFmpeg's libraries for frame-accurate decode and encode. *(BSD-3-Clause · 3.3k★)*
- [PySceneDetect](https://github.com/Breakthrough/PySceneDetect) - Shot-boundary and cut detection; the standard way to segment footage before analysis. *(BSD-3-Clause · 5.1k★)*
- [TransNet V2](https://github.com/soCzech/TransNetV2) - Neural shot-transition detection, more accurate than threshold methods on hard cuts and dissolves. *(MIT · 1.0k★ · last commit 2021-07)*
- [aubio](https://github.com/aubio/aubio) - Onset, pitch and beat detection in C with Python bindings. *(3.7k★)*
- [essentia](https://github.com/MTG/essentia) - C++ audio analysis library covering rhythm, key and descriptors, with Python bindings. *(AGPL-3.0 · 3.7k★)*
- [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) - Filtergraph bindings for Python; widely used but unmaintained since 2022. *(Apache-2.0 · 11.0k★ · last commit 2022-07)*
- [ffmpeg.wasm](https://github.com/ffmpegwasm/ffmpeg.wasm) - FFmpeg compiled to WebAssembly for in-browser processing with no upload. *(MIT · 17.7k★)*
- [librosa](https://github.com/librosa/librosa) - Music and audio analysis in Python; beat tracking for cut-to-music workflows. *(ISC · 8.5k★)*
- [madmom](https://github.com/CPJKU/madmom) - Signal-processing library with strong beat and downbeat trackers. *(1.7k★ · last commit 2024-08)*
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Downloader used to fetch source material and reference footage. *(Unlicense · 182k★)*

## Research papers and benchmarks

- [Aurora: Unified Video Editing with a Tool-Using Agent](https://arxiv.org/abs/2605.18748) - Agent that plans and calls editing tools under one interface. *(2026)*
- [Audio Match Cutting](https://arxiv.org/abs/2408.10998) - Finds and creates matching audio transitions between shots. *(2024)*
- [Computational Video Editing for Dialogue-Driven Scenes](https://graphics.stanford.edu/papers/roughcut/) - Leake et al.'s idiom-based automatic cutting of multi-take dialogue; the foundational system paper. *(SIGGRAPH 2017)*
- [Edit3K: Universal Representation Learning for Video Editing Components](https://arxiv.org/abs/2403.16048) - Learns representations of the editing operations themselves. *(2024)*
- [From Shots to Stories: LLM-Assisted Video Editing](https://arxiv.org/abs/2505.12237) - Unified language representations for shots so an LLM can assemble a narrative. *(2025)*
- [LAVE: LLM-Powered Agent Assistance and Language Augmentation for Video Editing](https://arxiv.org/abs/2402.10294) - The reference user study for what an editing agent should and should not decide. *(UIST 2024)*
- [Learning to Cut by Watching Movies](https://arxiv.org/abs/2108.04294) - Learns cut plausibility from professionally edited film. *(ICCV 2021)*
- [LongVideoBench](https://arxiv.org/abs/2407.15754) - Benchmark for long-context interleaved video-language understanding. *(NeurIPS 2024)*
- [MLVU: Benchmarking Multi-task Long Video Understanding](https://arxiv.org/abs/2406.04264) - Long-video benchmark spanning retrieval, reasoning and summarisation. *(2024)*
- [Match Cutting: Finding Cuts with Smooth Visual Transitions](https://arxiv.org/abs/2210.05766) - Amazon's system for detecting match cuts at catalogue scale. *(WACV 2023)*
- [Movie Gen: A Cast of Media Foundation Models](https://arxiv.org/abs/2410.13720) - Meta's technical report on joint video and audio generation and editing. *(2024)*
- [Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356) - The Whisper paper. *(2022)*
- [Soundify: Matching Sound Effects to Video](https://arxiv.org/abs/2112.09726) - Automatic sound-effect placement against on-screen events. *(2021)*
- [TempCompass: Do Video LLMs Really Understand Videos?](https://arxiv.org/abs/2403.00476) - Probes temporal reasoning, which most video benchmarks accidentally let models skip. *(ACL 2024)*
- [Text-based Editing of Talking-head Video](https://arxiv.org/abs/1906.01524) - Editing a performance by editing its transcript; the origin of the interaction model. *(SIGGRAPH 2019)*
- [The Anatomy of Video Editing](https://arxiv.org/abs/2207.09812) - Dataset and benchmark suite built specifically for AI-assisted editing tasks. *(ECCV 2022)*
- [TransNet V2](https://arxiv.org/abs/2008.04838) - Fast, accurate shot-transition detection network. *(2020)*
- [VBench](https://arxiv.org/abs/2311.17982) - Disaggregated evaluation suite for video generative models, with [VBench-2.0](https://arxiv.org/abs/2503.21755) extending it to faithfulness. *(CVPR 2024)*
- [Video-MME](https://arxiv.org/abs/2405.21075) - Comprehensive multimodal LLM video benchmark across short, medium and long clips. *(2024)*
- [VideoAgent: A Memory-augmented Multimodal Agent for Video Understanding](https://arxiv.org/abs/2403.11481) - Long-video agent that keeps a memory rather than re-reading everything. *(ECCV 2024)*
- [pyannote.audio: neural building blocks for speaker diarization](https://arxiv.org/abs/1911.01255) - The diarization toolkit paper. *(ICASSP 2020)*

## Datasets

- [AMI Meeting Corpus](https://groups.inf.ed.ac.uk/ami/corpus/) - 100 hours of multi-modal meeting recordings; the classic diarization and multi-camera testbed.
- [ActivityNet Captions](http://activity-net.org/challenges/2017/captioning.html) - Dense temporal event descriptions over 20k untrimmed videos.
- [AudioSet](https://research.google.com/audioset/) - 2M+ labelled 10-second audio clips across 632 event classes.
- [Common Voice](https://commonvoice.mozilla.org/) - Mozilla's crowd-sourced multilingual speech corpus, CC0.
- [Condensed Movies](https://www.robots.ox.ac.uk/~vgg/data/condensed-movies/) - Key scenes from 3k+ films with captions, for story-level retrieval.
- [Ego4D](https://ego4d-data.org/) - 3,600+ hours of egocentric video with dense annotations.
- [GigaSpeech](https://github.com/SpeechColab/GigaSpeech) - 10k hours of transcribed English audio from audiobooks, podcasts and YouTube.
- [HowTo100M](https://www.di.ens.fr/willow/research/howto100m/) - 136M narrated instructional clips paired with ASR text.
- [InternVid](https://github.com/OpenGVLab/InternVideo/tree/main/Data/InternVid) - Large-scale video-text corpus for multimodal understanding and generation.
- [LibriSpeech](https://www.openslr.org/12) - 1,000 hours of read English speech; still the default ASR baseline.
- [MovieNet](https://movienet.github.io/) - 1,100 movies annotated with shots, scenes, characters, places and scripts.
- [Panda-70M](https://snap-research.github.io/Panda-70M/) - 70M high-quality video clips with captions from cross-modality teachers.
- [The Anatomy of Video Editing (AVE)](https://github.com/dawitmureja/AVE) - 196k shots labelled with editing attributes — the closest thing to a dataset of editing decisions.
- [VGGSound](https://www.robots.ox.ac.uk/~vgg/data/vggsound/) - 200k+ audio-visual clips where the sound source is visible on screen.
- [VidChapters-7M](https://antoyang.github.io/vidchapters.html) - 817k videos with user-written chapters and timestamps.
- [VoxConverse](https://www.robots.ox.ac.uk/~vgg/data/voxconverse/) - Audio-visual diarization dataset from real multi-speaker broadcast.
- [YouCook2](https://youcook2.eecs.umich.edu/) - 2,000 cooking videos with temporally localised procedure descriptions.

## Reading

- [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) - When an agent loop is the right shape and when a workflow is.
- [Build and deploy Remote MCP servers](https://blog.cloudflare.com/remote-model-context-protocol-servers-mcp/) - The practical guide to hosted MCP with OAuth, which is what puts editing tools inside a chat client.
- [Building with Remotion and AI](https://www.remotion.dev/docs/ai) - How a programmatic video framework exposes itself to models.
- [In the Blink of an Eye](https://en.wikipedia.org/wiki/In_the_Blink_of_an_Eye_(Murch_book)) - Walter Murch's rule of six for what makes a cut work; still the best statement of the problem any editing agent is solving.
- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) - The original MCP announcement.
- [It's time for agentic video editing](https://a16z.com/its-time-for-agentic-video-editing/) - a16z on why editing, not generation, is the bottleneck.
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification/draft) - The protocol itself, if you intend to ship a server.
- [The Creators of Model Context Protocol](https://www.latent.space/p/mcp) - Interview on MCP's origins, constraints and direction.
- [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) - Tool design is most of what separates a usable editing agent from a frustrating one.

## Contributing

Additions and corrections are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion
bar and the conflict-of-interest disclosure. Links are checked automatically every week.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE)

To the extent possible under law, the contributors have waived all copyright and related or
neighboring rights to this work.
