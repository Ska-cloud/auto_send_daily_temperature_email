from utils import load_yaml

__all__ = [
    'DO_JOB_TIME',
    'DISTRICT_ID',
    'SENDER',
    'RECEIVER',
    'USERNAME',
    'POP_TOKEN',
]

config = load_yaml.load_yml('./config.yaml')

DO_JOB_TIME = config.get('do_job_time')
DISTRICT_ID = config.get('district_id')
SENDER = config.get('sender')
RECEIVER = config.get('receiver')
USERNAME = config.get('username')
POP_TOKEN = config.get('pop_token')

