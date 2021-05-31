import pathlib
from jinja2 import Template
import http.client
import json



SERVER = "rest.ensembl.org"
ENDPOINT = "/info/assembly/"



def format_command(command):
    command2 = command.replace("\n", "").replace("\r", "")
    return command2.replace("\n", "").replace("\r", "")

def read_template_html_file(filename):
    content = Template(pathlib.Path(filename).read_text())
    return content

def print_karyotype(specie):
    PARAMS = "?content-type=application/json"
    PARAMS_DEF = specie + PARAMS

    connection = http.client.HTTPConnection(SERVER)

    connection.request("GET", ENDPOINT + PARAMS_DEF)
    response = connection.getresponse()
    answer_decoded = response.read().decode()
    print(type(answer_decoded), answer_decoded)
    dict_response = json.loads(answer_decoded)
    print(type(dict_response), dict_response)

    dict_karyotype = dict_response["karyotype"]


    context = {
            "karyotype": dict_karyotype
            }
    contents = read_template_html_file("./html/karyotype.html").render(context=context)
    return contents


