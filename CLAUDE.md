# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Dependencies are managed with `uv` (see `pyproject.toml` / `uv.lock`); `requirements.txt` (`yt-dlp`) is kept for the plain `pip install -r requirements.txt` path described in the README.

```bash
uv sync                              # install/sync dependencies into .venv
uv run python main.py <youtube-url>  # download a video
uv run python audio.py <youtube-url> # download audio as mp3
```

Both scripts take exactly one YouTube URL as `sys.argv[1]`. There is no test suite, linter, or build step in this repo.

## Architecture

Two standalone, single-purpose CLI scripts, each wrapping `yt_dlp.YoutubeDL` with its own options — there is no shared module between them:

- `main.py` — downloads video (`format: bestvideo+bestaudio/best`) into `videos/`.
- `audio.py` — downloads audio only, extracts/transcodes to mp3 via the `FFmpegExtractAudio` postprocessor (requires `ffmpeg` on PATH), into `audio/`. Creates the `audio/` directory if missing.

Output filenames use yt-dlp's `outtmpl` with `%(title)s.%(ext)s`, so downloaded files are named after the video title. Both `videos/` and `audio/` are created on demand (not committed); `.gitignore` excludes `*.part`, `*.mp3`, `*.mp4`, `*.ytdl`.

Each script prints `Error: {e}` and exits gracefully on failure rather than raising — errors surface as printed text, not stack traces or non-zero exit codes.

## Copyright

Only download content the user has rights to (their own upload, a license, or Creative Commons/public domain). See `.claude/skills/download-audio/SKILL.md` for the audio-download workflow, which confirms this before running.
