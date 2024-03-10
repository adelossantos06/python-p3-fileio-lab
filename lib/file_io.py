def write_file(file_name, file_content):
    file_path = f'{file_name}.txt'
    with open(file_path, mode='w') as text_file:
        text_file.write(file_content)


def append_file(file_name, append_content):
    file_path = f'{file_name}.txt'
    with open(file_path, mode='a') as text_file:
        text_file.write(append_content)

def read_file(file_name):
    file_path = f'{file_name}.txt'
    with open(file_path) as text_file:
        file_content = text_file.read()
    return file_content



