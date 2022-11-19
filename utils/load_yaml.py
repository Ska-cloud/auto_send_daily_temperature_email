import yaml


def load_yml(file_path: str):
    with open(file_path, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config


if __name__ == '__main__':
    load_yml('../config.yaml')
