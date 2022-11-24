from utils import load_yaml

config = load_yaml.load_yml('./config.yaml')

AK_TOKEN = config.get('ak_token')
TOKEN = config.get('tianxing_token')
