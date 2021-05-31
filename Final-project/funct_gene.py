import pathlib
from jinja2 import Template
import http.client
import json
import Seq1


DICT_GENES = {
       "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
     "RNU6-269P": "ENSG00000212379",
     "MIR633": "ENSG00000207552",
     "TTTY4": "ENSG00000226906",
     "RBMY2YP": "ENSG00000227633",
     "FGFR3": "ENSG00000068078",
     "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"


def hola():
        context = {
            "name": gene,
            "sequence": sequence
        }
        contents = read_template_html_file("./html/.html").render(context=context)
        return contents
def format_command(command):
    command2 = command.replace("\n", "").replace("\r", "")
    return command2.replace("\n", "").replace("\r", "")

def read_template_html_file(filename):
    content = Template(pathlib.Path(filename).read_text())
    return content




def open_seq(gene):
    try:
        ID = DICT_GENES[gene]

        PARAMS = "?content-type=application/json"
        connection = http.client.HTTPConnection(SERVER)
        connection.request("GET", ENDPOINT + ID + PARAMS)

        response = connection.getresponse()
        answer_decoded = response.read().decode()

        dict_response = json.loads(answer_decoded)
        sequence = Seq1.Seq(dict_response["seq"])
        print(sequence)
        context = {
            "gene_name": gene,
            "gene_content": sequence
        }
        contents = read_template_html_file("./html/sequence.html").render(context=context)
        return contents



    except KeyError:
        print("The gene is not inside our dictionary,. Choose one of the following:", list(DICT_GENES.keys()))
