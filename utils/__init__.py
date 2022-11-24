from utils import load_yaml

config = load_yaml.load_yml('./config.yaml')

BIRTHDAY_DAY = config.get('birthday_day')
FALL_IN_LOVE_DAY = config.get('fall_in_love_day')
