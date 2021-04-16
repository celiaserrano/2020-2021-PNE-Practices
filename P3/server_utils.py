from Seq1 import Seq
from pathlib import Path

def print_colored(message, color):
    import termcolor

    print(termcolor.colored(message, color))

def format_command(command):
    command2 = command.replace("\n", "").replace("\r", "")
    return command2.replace("\n", "").replace("\r", "")


def ping(cs):
    print_colored("PING COMMAND", "green")
    response = "OK!"
    cs.send(str(response).encode())

def get(cs, list_sequences, argument):
    print_colored("GET", "yellow")
    response = list_sequences[int(argument)]
    print(response)
    cs.send(response.encode())


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


def gene(cs, argument):
    print_colored("GENE", "yellow")
    response = Seq()
    response.read_fasta(argument + ".txt")
    response = str(response)

    print(response)
    cs.send(response.encode())


















