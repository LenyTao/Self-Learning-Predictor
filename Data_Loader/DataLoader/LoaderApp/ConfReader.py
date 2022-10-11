import yaml


def get_config_info(path):
    with open(f'{path}/config.yaml') as config_file:
        data_from_config: dict = dict(yaml.load(config_file, Loader=yaml.FullLoader))
        return data_from_config
