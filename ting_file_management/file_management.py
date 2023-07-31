import sys


def is_txt(path_file):
    if path_file[len(path_file)-4:] == '.txt':
        return True
    return False


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not is_txt(path_file):
        sys.stderr.write("Formato inválido")
        return None

    txt = []
    try:
        with open(path_file, 'r') as file:
            for line in file:
                txt.append(line.splitlines()[0])
    except Exception:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    return txt
