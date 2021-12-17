import os

C_FILE = 'output.json'

def __get_filename(name: str):
    filename = name.strip()
    if filename == '':  # pragma: no cover
        filename = C_FILE
    return filename


def create_json_file(contents: str, name: str = ''):
    try:
        with open(__get_filename(name), 'w') as f:
            f.write(contents)
    except Exception as e:  # pragma: no cover
        print('create_json_file: {}'.format(e))
        return False

    return True


def read_json_file(name: str = '') -> str:
    
    filename = __get_filename(name)
    contents = ''
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                contents = str(f.read())
        except Exception as e:  # pragma: no cover
            print('read_json_file: {}'.format(e))

    return contents