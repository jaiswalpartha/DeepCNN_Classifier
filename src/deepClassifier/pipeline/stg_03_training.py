from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareCallback,Training
from deepClassifier import logger


STAGE_NAME = "Training stage"


def main():
    config = ConfigurationManager()
    prepare_callbacks_config = config.get_prepare_callbacks_config()
    prepare_callbacks = PrepareCallback(config =prepare_callbacks_config)
    callback_list = prepare_callbacks.get_tb_ckpt_callbacks()#output:list
   
    training_config = config.get_training_config()
    training = Training(config =training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train(
        callback_list=callback_list
    )

if __name__ == "__main__":
    try:
        logger.info(f"{20 * '*'}")
        logger.info(f">>>>>>>>>Stage {STAGE_NAME} started<<<<<<<<<<<")
        main()
        logger.info(f">>>>>>>>>Stage {STAGE_NAME} completed<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e