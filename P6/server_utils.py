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


def info(cs, argument):
    print_colored("INFO", "yellow")
    seq1 = Seq(argument)

    response = "Sequence: " + str(argument) + "\nTotal lenght: " + str(seq1.len()) + seq1.percent()
    print(response)
    cs.send(response.encode())


def comp(cs, argument):
    print_colored("COMP", "yellow")
    seq1 = Seq(argument)
    response = str(seq1.complement())
    print(response)
    cs.send(response.encode())

def rev(cs, argument):
    print_colored("REV", "yellow")
    seq1 = Seq(argument)
    response = str(seq1.reverse())
    print(response)
    cs.send(response.encode())


def gene(seq_name):
    PATH = "./Sequences/" + seq_name + '.txt'
    s1 = Seq()
    s1.read_fasta(PATH)
    context = {
        "gene_name": seq_name,
        "gene_contents": s1.str_bases
    }
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents




















