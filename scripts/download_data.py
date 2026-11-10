"""Download and unzip the ESA Collision Avoidance Challenge dataset into data/raw/.

Dataset: Uriot, Izzo, Martinez-Heras, Letizia, Siminski & Merz (2021),
Collision Avoidance Challenge dataset, Zenodo, https://doi.org/10.5281/zenodo.4463683
License: CC BY 4.0
"""

import hashlib
import urllib.request
import zipfile
from pathlib import Path

URL = (
    "https://zenodo.org/records/4463683/files/"
    "Collision%20Avoidance%20Challenge%20-%20Dataset.zip?download=1"
)
EXPECTED_MD5 = "d19dc8875229f2f6893253c38adddc87"

RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"
ZIP_PATH = RAW_DIR / "dataset.zip"
DATA_DIR = RAW_DIR / "Collision Avoidance Challenge - Dataset" / "kelvins_competition_data"


def md5_of(path):
    digest = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    if (DATA_DIR / "train_data.csv").exists():
        print("Dataset already downloaded:", DATA_DIR)
        return

    if not ZIP_PATH.exists():
        print("Downloading about 221 MB from Zenodo...")
        urllib.request.urlretrieve(URL, ZIP_PATH)

    if md5_of(ZIP_PATH) != EXPECTED_MD5:
        raise SystemExit("Download is corrupted. Delete data/raw/dataset.zip and try again.")

    print("Unzipping...")
    with zipfile.ZipFile(ZIP_PATH) as outer:
        outer.extractall(RAW_DIR)
    with zipfile.ZipFile(DATA_DIR / "train_data.zip") as inner:
        inner.extractall(DATA_DIR)

    print("Done:", DATA_DIR)


if __name__ == "__main__":
    main()
