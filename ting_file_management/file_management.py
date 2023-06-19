import sys

def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
        return []

    try: 
        file = open(path_file, "r")
        reading = file.read()
        lines = reading.split("\n")
        file.close()
        return lines
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return []