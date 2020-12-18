import json


def write_json_content(filename, content):
    with open("resources/" + filename + ".json", "w") as file_object:
        file_object.write(json.dumps(content))
        file_object.close()


def get_json_content(filename, specific_element='', field=''):
    file_object = open("resources/" + filename + ".json", )
    file_data = json.load(file_object)
    file_object.close()
    if specific_element != '' and field != '':
        for i in file_data:
            if str(i[field]) == specific_element:
                return i
        raise IOError("Specified element not in file")
    return file_data
