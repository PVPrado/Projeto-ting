from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None

    data = txt_importer(path_file)
    data_instance = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(data),
        'linhas_do_arquivo': data,
    }

    instance.enqueue(data_instance)
    print(data_instance)
    return data_instance


def remove(instance):
    if not instance or len(instance) == 0:
        return print("Não há elementos")

    data_deleted = instance.dequeue()
    name = data_deleted["nome_do_arquivo"]
    print(f"Arquivo {name} removido com sucesso")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file)
    except IndexError:
        sys.stderr.write("Posição inválida")
