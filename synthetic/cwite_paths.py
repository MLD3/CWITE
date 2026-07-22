from pathlib import Path
import os


DATA_ROOT = Path(os.environ.get("CWITE_DATA_ROOT", "../data")).expanduser()
OUTPUT_ROOT = Path(os.environ.get("CWITE_OUTPUT_ROOT", "../outputs")).expanduser()
RELEASE_ROOT = Path(__file__).resolve().parent


def data_path(*parts):
    return str(DATA_ROOT.joinpath(*parts))


def output_path(*parts):
    path = OUTPUT_ROOT.joinpath(*parts)
    path.parent.mkdir(parents=True, exist_ok=True)
    return str(path)


def output_dir(*parts):
    path = OUTPUT_ROOT.joinpath(*parts)
    path.mkdir(parents=True, exist_ok=True)
    return str(path)


def release_path(*parts):
    return str(RELEASE_ROOT.joinpath(*parts))
