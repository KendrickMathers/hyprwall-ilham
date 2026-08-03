import hashlib
import subprocess
from pathlib import Path

CACHE_DIR = Path("thumbnails")
CACHE_DIR.mkdir(exist_ok=True)

def thumbnail_path(video):
    h = hashlib.md5(video.encode()).hexdigest()
    return CACHE_DIR / f"{h}.jpg"

def create_thumbnail(video):
    thumb = thumbnail_path(video)

    if thumb.exists():
        return str(thumb)

    subprocess.run([
        "ffmpeg",
        "-loglevel", "quiet",
        "-y",
        "-ss", "00:00:02",
        "-i", video,
        "-frames:v", "1",
        "-vf", "scale=320:-1",
        str(thumb)
    ])

    return str(thumb)
