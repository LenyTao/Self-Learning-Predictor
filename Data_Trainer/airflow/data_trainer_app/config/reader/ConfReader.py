import yaml

from config.reader import ConfigClass


def get_config_info(path):
    with open(f'{path}/config.yaml', encoding="utf-8") as config_file:
        data_from_config: dict = dict(yaml.load(config_file, Loader=yaml.FullLoader))
        return data_from_config


def get_config_obj(path: str):
    conf_dict = get_config_info(path)

    config = ConfigClass.ConfigFile(
        ConfigClass.Spark(
            conf_dict["spark"]["app_name"],
            conf_dict["spark"]["master"]
        ),
        ConfigClass.SparkML(
            conf_dict["spark_ml"]["training_data_path"],
            conf_dict["spark_ml"]["ready_models_path"]
        ),
        ConfigClass.MlFlow(
            conf_dict["ml_flow"]["tracking_uri"],
            conf_dict["ml_flow"]["experiment_name"],
            conf_dict["ml_flow"]["model_name"],
            conf_dict["ml_flow"]["artifact_tmp_path"]
        )
    )
    return config
