from dataclasses import dataclass


@dataclass(frozen=True)
class Spark:
    app_name: str
    master: str


@dataclass(frozen=True)
class SparkML:
    training_data_path: str
    ready_models_path: str


@dataclass(frozen=True)
class MlFlow:
    tracking_uri: str
    experiment_name: str
    model_name: str
    artifact_tmp_path: str


@dataclass(frozen=True)
class ConfigFile:
    spark: Spark
    spark_ml: SparkML
    ml_flow: MlFlow
