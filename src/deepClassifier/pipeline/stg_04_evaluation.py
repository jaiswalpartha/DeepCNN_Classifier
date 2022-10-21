from deepClassifier.config import ConfigurationManager
from deepClassifier.components import Evaluation
from deepClassifier import logger


STAGE_NAME = "Evaluation stage"


def main():
    config = ConfigurationManager()
    validation_config = config.get_evaluation_config()
    evaluation  = Evaluation(validation_config)
    evaluation.evaluation()
    evaluation.save_score()

if __name__ == "__main__":
    try:
        logger.info(f"{20 * '*'}")
        logger.info(f">>>>>>>>>Stage {STAGE_NAME} started<<<<<<<<<<<")
        main()
        logger.info(f">>>>>>>>>Stage {STAGE_NAME} completed<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e