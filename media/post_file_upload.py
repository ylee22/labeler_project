import requests
import os


def upload_file(filename):
    url = 'http://localhost:8000/images/'
    local_path = os.getcwd()

    with open(filename, 'rb') as file:
        file_data = {'file': (filename, file), 'file_name': filename}
        resp = requests.post(url, files = file_data)
        print(resp)


upload_file('HUNT0133.jpg')