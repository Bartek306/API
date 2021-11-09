import json

import requests


def test():
    message = "teSt_message"
    data = {'message': message,
            'type': 'txt'}
    data = json.dumps(data)
    request = requests.post("http://localhost:7000/api", data)
    print(request.text)

test()