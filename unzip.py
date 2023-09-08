import zipfile
import os

zip_file = "train_dataset_DCS.zip"

with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall()
#os.remove(zip_file)