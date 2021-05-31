import pathlib
from jinja2 import Template
import http.client
import json

def format_command(command):
    command2 = command.replace("\n", "").replace("\r", "")
    return command2.replace("\n", "").replace("\r", "")

def read_template_html_file(filename):
    content = Template(pathlib.Path(filename).read_text())
    return content


SERVER = "rest.ensembl.org"
ENDPOINT = "info/assembly/"




def print_lenght(specie, chromo):
    PARAMS = "?content-type=application/json"
    PARAMS_DEF = specie + PARAMS

    connection = http.client.HTTPConnection(SERVER)

    connection.request("GET", ENDPOINT + PARAMS_DEF)
    response = connection.getresponse()
    answer_decoded = response.read().decode()
    print(type(answer_decoded), answer_decoded)
    dict_response = json.loads(answer_decoded)

    new_list = dict_response["top_level_region"]
    for elem in new_list:
        if elem["name"] == chromo:
            chromo_lenght = elem["length"]

    context = {
            "lenght": chromo_lenght
            }
    contents = read_template_html_file("./html/lenght.html").render(context=context)
    return contents
