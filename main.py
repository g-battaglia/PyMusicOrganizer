import typer

from os import walk
from mutagen.flac import FLAC
from pathlib import Path
from tqdm import tqdm


# Local
from utils import folder_count

TIDAL_DIR = ""

app = typer.Typer()


@app.command()
def main(main_path: str):
    """Main function"""

    TIDAL_DIR = main_path

    main_dir = Path(TIDAL_DIR)

    for root, dirs, files in tqdm(walk(TIDAL_DIR), total=(folder_count(TIDAL_DIR) + 1)):
        for file in files:
            if file.startswith("."):
                continue

            if file.endswith(".flac"):
                path = Path(root, file)
                audio = FLAC(path)

                index = path.parents.index(main_dir)

                # Album Name
                album_name = path.parents[index - 2].name.strip()

                audio["album"] = album_name

                if audio.get("artist"):
                    audio["albumartist"] = audio["artist"]

                # Artist Name
                artist_name = path.parents[index - 1].name.strip()

                if artist_name == "Various Artists":
                    # artist_name = audio["album"]
                    continue

                audio["artist"] = artist_name

                # print(main_dir, album_name, artist_name)
                audio.save()


if __name__ == "__main__":
    app()
