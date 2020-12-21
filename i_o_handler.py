import json


def write_json_content(filename, content):
    with open("resources/" + filename + ".json", "w") as file_object:
        file_object.write(json.dumps(content))


def get_json_content(filename, specific_element='', field=''):
    with open("resources/" + filename + ".json", ) as file_object:
        file_data = json.load(file_object)
        if specific_element != '' and field != '':
            for fd in file_data:
                if str(fd[field]) == specific_element:
                    return fd
            raise IOError("Specified element not in file")
        return file_data
