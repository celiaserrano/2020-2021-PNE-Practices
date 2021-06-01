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
        if response.status == 200:
            answer_decoded = response.read().decode()

            dict_response = json.loads(answer_decoded)
            sequence = Seq1.Seq(dict_response["seq"])

            context = {
                "gene_name": gene,
                "gene_content": sequence
            }
            contents = read_template_html_file("./html/sequence.html").render(context=context)
            return contents

        else:
            print("ERROR!!! Cannot connect to the server")

    except KeyError:
        contents = read_template_html_file("./html/error_gene.html").render()
        return contents




def info_seq(gene):
    try:
        ID = DICT_GENES[gene]

        PARAMS = "?content-type=application/json"
        connection = http.client.HTTPConnection(SERVER)
        connection.request("GET", ENDPOINT + ID + PARAMS)

        response = connection.getresponse()
        if response.status == 200:
            answer_decoded = response.read().decode()

            dict_response = json.loads(answer_decoded)
            sequence = Seq1.Seq(dict_response["seq"])

            new_dict = dict_response["desc"]
            new_dict2 = new_dict.split(":")
            new_list = list(new_dict2)

            name = new_list[2]
            sequence_start = new_list[3]
            sequence_end = new_list[4]
            sequence_lenght = sequence.len()
            context = {
                "gene": gene,
                "gene_name": name,
                "starting": sequence_start,
                "ending": sequence_end,
                "lenght": sequence_lenght,
                "gene_id": ID
            }
            contents = read_template_html_file("./html/information.html").render(context=context)
            return contents

        else:
            print("ERROR!!! Cannot connect to the server")


    except KeyError:
        contents = read_template_html_file("./html/error_gene.html").render()
        return contents




def calc_seq(gene):
    try:
        ID = DICT_GENES[gene]

        PARAMS = "?content-type=application/json"
        connection = http.client.HTTPConnection(SERVER)
        connection.request("GET", ENDPOINT + ID + PARAMS)

        response = connection.getresponse()
        if response.status == 200:
            answer_decoded = response.read().decode()

            dict_response = json.loads(answer_decoded)
            sequence = Seq1.Seq(dict_response["seq"])

            n_bases = sequence.count()
            percentage = sequence.percent()
            sequence_lenght = sequence.len()
            most_base = sequence.most_freq_base()

            context = {
                "gene_name": gene,
                "number_bases": n_bases,
                "percent": percentage,
                "lenght": sequence_lenght,
                "freq_base": most_base
            }
            contents = read_template_html_file("./html/calcs.html").render(context=context)
            return contents

        else:
            print("ERROR!!! Cannot connect to the server")


    except KeyError:
        contents = read_template_html_file("./html/error_gene.html").render()
        return contents


