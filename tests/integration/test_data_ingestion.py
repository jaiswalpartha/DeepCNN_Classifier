import pytest
from deepClassifier.entity import DataIngestionConfig
from deepClassifier.components import DataIngestion
from pathlib import Path
import os

class Test_DataIngestion:
    data_ingestion_config = DataIngestionConfig(
        root_dir=Path("tests/data"),
        source_url="https://raw.githubusercontent.com/c17hawke/FSDS_NOV_deepCNNClassifier/main/tests/data/sample_data.zip",
        local_data_file=Path("tests/data/data_integration.zip"),
        unzip_dir=Path("tests/data")
    )
    def test_download(self):
        data_ingestion = DataIngestion(config=self.data_ingestion_config)
        #data_ingestion.download_file()
        data_ingestion.download_file()
        assert os.path.exists(self.data_ingestion_config.local_data_file)

    def test_unzip(self):
            data_ingestion = DataIngestion(config=self.data_ingestion_config)
            data_ingestion.unzip_and_clean()
            assert os.path.isdir(Path("tests/data/PetImages"))
            assert os.path.isdir(Path("tests/data/PetImages/Cat"))
            assert os.path.isdir(Path("tests/data/PetImages/Dog"))

   