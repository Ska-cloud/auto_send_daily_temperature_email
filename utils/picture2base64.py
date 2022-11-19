import base64


def convert_base64(file_path: str) -> str:
    with open(file_path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
    return base64_data.decode('utf8')


if __name__ == '__main__':
    print(convert_base64("../static/bg2.jpg"))
