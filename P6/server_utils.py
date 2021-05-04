from Seq1 import Seq
import pathlib
from jinja2 import Template

def print_colored(message, color):
    import termcolor

    print(termcolor.colored(message, color))

def format_command(command):
    command2 = command.replace("\n", "").replace("\r", "")
    return command2.replace("\n", "").replace("\r", "")

def read_template_html_file(filename):
    content = Template(pathlib.Path(filename).read_text())
    return content


def ping(cs):
    print_colored("PING COMMAND", "green")
    response = "OK!"
    cs.send(str(response).encode())

def get(list_sequences, seq_number):
    context = {
        "number": seq_number,
        "sequence": list_sequences[int(seq_number)]
    }
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents


def info(sequence):
    seq1 = Seq(sequence)

    response = "\nTotal lenght: " + str(seq1.len()) + seq1.percent()
    context = {
        "sequence": sequence,
        "calculation": response
    }
    contents = read_template_html_file("./html/option.html").render(context=context)
    return contents


def comp(sequence):
    seq1 = Seq(sequence)

    context = {
        "sequence": sequence,
        "calculation": seq1.complement()
    }
    contents = read_template_html_file("./html/option.html").render(context=context)
    return contents

def rev(sequence):
    seq1 = Seq(sequence)
    context = {
        "sequence": sequence,
        "calculation": seq1.reverse()
    }
    contents = read_template_html_file("./html/option.html").render(context=context)
    return contents


def gene(seq_name):
    PATH = "./sequences/" + seq_name + '.txt'
    s1 = Seq()
    s1.read_fasta(PATH)
    context = {
        "gene_name": seq_name,
        "calculation": s1.strbases
    }
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents






