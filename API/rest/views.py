from django.shortcuts import render
import json
import requests

from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dicttoxml import dicttoxml
import csv


# Create your views here.
@csrf_exempt
def api(request):
    body_unicode = request.body.decode('utf-8')
    if body_unicode == "":
        return HttpResponseNotFound("Request body is empty")
    body = json.loads(body_unicode)
    data = body['message']
    type = body['type']
    data_to_send = {'message': data}
    data_to_send = json.dumps(data_to_send)
    request = requests.post("http://localhost:8000/string", data_to_send)
    dict = request.text
    dict = json.loads(dict)
    lower = dict['lower']
    upper = dict['upper']
    special = dict['special']
    if type == "txt":
        message = "lower = {} upper = {} special = {}".format(lower, upper, special)
        return HttpResponse(message)

    if type == "json":
        response = {'upper': upper, 'lower': lower, 'special': special}
        return HttpResponse(json.dumps(response), content_type='application/json')

    if type == "xml":
        xml = dicttoxml(dict, custom_root='data', attr_type=False)
        return xml

    if type == "csv":
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(['upper', upper])
        writer.writerow(['lower', lower])
        writer.writerow(['special', special])
        return response
