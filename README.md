# DeepCNN_Classifier

## workflow

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config.
6. Update the components
7. Update the pipeline
8. Test run pipeline stage
9. run tox for testing your package
10. Update the dvc.yaml
11. run "dvc repro" for running all the stages in pipeline

MLFLOW_TRACKING_URI=https://dagshub.com/jaiswalpartha/DeepCNN_Classifier.mlflow \
MLFLOW_TRACKING_USERNAME=jaiswalpartha \
MLFLOW_TRACKING_PASSWORD=49d4169800f7b4260de4d2983f995b0ff329f12d \
python script.py

# Data ingestion testing using sample data
https://raw.githubusercontent.com/c17hawke/FSDS_NOV_deepCNNClassifier/main/tests/data/sample_data.zip