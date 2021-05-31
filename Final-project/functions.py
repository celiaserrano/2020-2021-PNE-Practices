
import pathlib
from jinja2 import Template
import http.client
import json



SERVER = "rest.ensembl.org"
ENDPOINT = "/info/species"
PARAMS = "?content-type=application/json"


connection = http.client.HTTPConnection(SERVER)

connection.request("GET", ENDPOINT + PARAMS)
response = connection.getresponse()
answer_decoded = response.read().decode()
print(type(answer_decoded), answer_decoded)
dict_response = json.loads(answer_decoded)
print(type(dict_response), dict_response)
dict_species = dict_response["species"]


def format_command(command):
    command2 = command.replace("\n", "").replace("\r", "")
    return command2.replace("\n", "").replace("\r", "")

def read_template_html_file(filename):
    content = Template(pathlib.Path(filename).read_text())
    return content



def limit_species(limit=None):
    dict_species = dict_response["species"]
    n_species = len(dict_species)

    context = {
            "number": n_species,
            "limits": limit,
            "names": dict_species[0:limit]
        }
    contents = read_template_html_file("./html/species.html").render(context=context)
    return contents

















