from deepClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from deepClassifier.utils import read_yaml, create_directories
from deepClassifier.entity import DataIngestionConfig, PrepareBaseModelConfig
from pathlib import Path




class ConfigurationManager:
    def __init__(
        self, config_filepath=CONFIG_FILE_PATH, parms_filepath=PARAMS_FILE_PATH
    ):

        self.config = read_yaml(config_filepath)
        self.parms = read_yaml(parms_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )
        return data_ingestion_config

    def get_prepare_base_model_config(self)->PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        create_directories([config.root_dir])
        prepare_base_model_config = PrepareBaseModelConfig(
                root_dir=Path(config.root_dir),
                base_model_path= Path(config.base_model_path),
                updated_base_model_path= Path(config.updated_base_model_path),
                params_image_size=self.parms.IMAGE_SIZE,
                params_include_top= self.parms.INCLUDE_TOP,
                params_learning_rate= self.parms.LEARNING_RATE,
                params_classes= self.parms.CLASSES,
                params_weights= self.parms.WEIGHTS,
                )
        return prepare_base_model_config   