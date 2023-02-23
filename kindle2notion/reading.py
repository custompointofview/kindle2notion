from pathlib import Path


def read_raw_clippings(clippings_file_path: Path) -> str:
    try:
        with open(clippings_file_path, "r") as raw_clippings_file:
            raw_clippings_text = raw_clippings_file.read()
        raw_clippings_text_decoded = raw_clippings_text.encode(
            "utf8", errors="ignore"
        ).decode()
    except UnicodeEncodeError as e:
        print(e)

    return raw_clippings_text_decoded
