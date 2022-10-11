import spark_ml_app
from config.reader import ConfReader
from sys import argv

if __name__ == "__main__":
    script_path, conf_file_path = argv

    config = ConfReader.get_config_obj(conf_file_path)

    spark_ml_app.run(config)