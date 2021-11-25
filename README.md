## StringAPI

Counts the occurrences of lower, upper and special character in given string

# Resource URL
http://127.0.0.1:8000/api

# Resource info

Response format : JSON, plain text, CSV, XML
Requires authentication: No

# Request parameters
message(required) : string provided for calculation
type(required): type of return message

# Example of request_1
{'message': 'teSt_message',
'type': 'json'}

# Example response_1
{'upper': '1' 'lower':, '10', 'special': '1}

# Example of request_2
{'message': 'teSt_message',
'type': 'txt'}

# Example of response_2

lower = 10 upper = 1 special = 1
