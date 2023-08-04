import sys
import ting_file_management.file_management as file_management


def exists_in_queue(instance, dicionario):
    """Aqui irá sua implementação"""
    for i in range(len(instance)):
        if instance.search(i) == dicionario:
            return True
    return False


def process(path_file, instance):
    """Aqui irá sua implementação"""
    linhas_do_txt = file_management.txt_importer(path_file)

    novo_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(linhas_do_txt),
        "linhas_do_arquivo": linhas_do_txt
    }

    if not exists_in_queue(instance, novo_dict):
        instance.enqueue(novo_dict)

    sys.stdout.write(str(novo_dict))


def remove(instance):
    try:
        file_dict = instance.dequeue()
        sys.stdout.write(
            f"Arquivo {file_dict['nome_do_arquivo']} removido com sucesso\n"
        )
        return file_dict
    except IndexError:
        sys.stdout.write("Não há elementos\n")
        return False


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        file_dict = instance.search(position)
        sys.stdout.write(str(file_dict))
        return True
    except IndexError:
        sys.stderr.write("Posição inválida\n")
        return False
