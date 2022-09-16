from os import walk
from mutagen.flac import FLAC
from pathlib import Path
from tqdm import tqdm

TIDAL_DIR = "/volumes/SD1T/MUSIC/TIDAL"


def folder_count(path):
    count1 = 0
    for root, dirs, files in walk(path):
        count1 += len(dirs)

    return count1


def main():
    for root, dirs, files in tqdm(walk(TIDAL_DIR), total=folder_count(TIDAL_DIR)):
        for file in files:
            if file.startswith("."):
                continue

            if file.endswith(".flac"):
                path = Path(root, file)

                album_name = path.parent.name.strip()
                if album_name == "Various Artists":
                    continue

                artist_name = path.parent.parent.name.strip()
                audio = FLAC(path)

                if audio.get("artist"):
                    audio["albumartist"] = audio["artist"]

                audio["artist"] = album_name
                audio["album"] = artist_name
                audio.save()


if __name__ == "__main__":
    main()
