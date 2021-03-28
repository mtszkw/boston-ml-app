from pathlib import Path
import urllib.request
import zipfile


def prepare_data_folder(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)


def download_data(url: str, save_dir: str):
    download_zip_path = save_dir + "dataset.zip"
    
    with urllib.request.urlopen(url) as dl_file:
        with open(download_zip_path, 'wb') as out_file:
            out_file.write(dl_file.read())

    with zipfile.ZipFile(download_zip_path, 'r') as zip_ref:
        zip_ref.extractall(save_dir)


DATA_DIR = "data/"
DATA_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip"

prepare_data_folder(path=DATA_DIR)
download_data(url=DATA_URL, save_dir=DATA_DIR)

