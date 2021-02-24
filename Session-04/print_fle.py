from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "../P0/sequences/RNU6_269P.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
print(file_contents)


FILENAME = "../P0/sequences/RNU6_269P.txt"

try:
    file_contents = Path(FILENAME).read_text()
    print(file_contents)

except FileNotFoundError:
    print("Something wrong has happened")

f = open(FILENAME, 'r')
data = f.read()
print(data)

with open(FILENAME) as reader:
    print(reader.read())
