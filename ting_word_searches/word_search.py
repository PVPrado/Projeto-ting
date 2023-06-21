def exists_word(word, queue_instance):
    word = word.lower()
    search_results = []

    for index in range(len(queue_instance)):
        file_info = queue_instance.search(index)
        file_name = file_info["nome_do_arquivo"]
        lines = file_info["linhas_do_arquivo"]
        occurrences = []

        for j, line in enumerate(lines):
            if word in line.lower():
                occurrences.append({"linha": j + 1})

        if occurrences:
            file_result = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            }
            search_results.append(file_result)

    return search_results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
