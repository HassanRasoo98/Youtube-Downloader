---
name: download-audio
description: Download the audio (MP3) of one or more YouTube videos using this repo's audio.py script. Use when the user gives YouTube URL(s) and asks to download/save the song or audio.
---

# Download Audio

Downloads the best-quality audio track from a YouTube URL and converts it to MP3 using `audio.py` (built on `yt-dlp` + ffmpeg). Output files land in the `audio/` folder, named after the video title.

## Prerequisites

Only ask about rights the first time in a session; don't re-ask on every call. Before downloading, confirm the user has the rights to download the content (e.g. it's their own upload, they hold a license, or it's Creative Commons/public domain). Do not proceed on copyrighted material without that confirmation.

Ensure dependencies are installed once per checkout:

```bash
uv sync
```

## Usage

For each YouTube URL provided, run:

```bash
uv run python audio.py "<youtube-url>"
```

Run once per URL (the script only accepts a single URL argument). After all downloads finish, list the resulting files in `audio/` for the user.

## Notes

- Requires `ffmpeg` on PATH (used by the `FFmpegExtractAudio` postprocessor).
- If a download errors, report the exact yt-dlp error message rather than retrying silently.
