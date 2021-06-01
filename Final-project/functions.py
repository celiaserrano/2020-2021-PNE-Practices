import pathlib
from jinja2 import Template
import http.client
import json



SERVER = "rest.ensembl.org"



def read_template_html_file(filename):
    content = Template(pathlib.Path(filename).read_text())
    return content



def limit_species(limit=None):
    try:
        ENDPOINT = "/info/species"
        PARAMS = "?content-type=application/json"

        connection = http.client.HTTPConnection(SERVER)

        connection.request("GET", ENDPOINT + PARAMS)
        response = connection.getresponse()
        if response.status == 200:
            answer_decoded = response.read().decode()

            dict_response = json.loads(answer_decoded)

            dict_species = dict_response["species"]
            n_species = len(dict_species)

            context = {
                "number": n_species,
                "limits": limit,
                "names": dict_species[0:limit]
            }

            contents = read_template_html_file("./html/species.html").render(context=context)
            return contents

        else:
            print("ERROR!!! Cannot connect to the server")

    except ConnectionRefusedError:
        print("ERROR!!! Cannot connect to the server")
        exit()



def print_karyotype(specie):
    try:
        ENDPOINT = "/info/assembly/"
        PARAMS = "?content-type=application/json"
        PARAMS_DEF = specie + PARAMS

        connection = http.client.HTTPConnection(SERVER)

        connection.request("GET", ENDPOINT + PARAMS_DEF)
        response = connection.getresponse()
        if response.status == 200:
            answer_decoded = response.read().decode()
            dict_response = json.loads(answer_decoded)

            dict_karyotype = dict_response["karyotype"]

            context = {
                "karyotype": dict_karyotype
            }
            contents = read_template_html_file("./html/karyotype.html").render(context=context)
            return contents

        else:
            contents = read_template_html_file("./html/error.html").render()
            return contents

    except ConnectionRefusedError:
        print("ERROR!!! Cannot connect to the server")
        exit()





def print_lenght(specie, chromo):
    try:
        ENDPOINT = "info/assembly/"
        PARAMS = "?content-type=application/json"
        PARAMS_DEF = specie + PARAMS

        connection = http.client.HTTPConnection(SERVER)

        connection.request("GET", ENDPOINT + PARAMS_DEF)
        response = connection.getresponse()
        if response.status == 200:
            answer_decoded = response.read().decode()
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


                else:
                    contents = read_template_html_file("./html/error.html").render()
                    return contents

        else:
            contents = read_template_html_file("./html/error.html").render()
            return contents


    except ConnectionRefusedError:
        print("ERROR!!! Cannot connect to the server")
        exit()

