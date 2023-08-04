def remove_pontuation(word):
    """Aqui irá sua implementação"""
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.replace("!", "")
    word = word.replace("?", "")

    return word


def linhas_de_ocorrencias(word, lista_de_linhas):
    """Aqui irá sua implementação"""
    linhas_com_palavra = []
    for i in range(len(lista_de_linhas)):
        formatted_line = remove_pontuation(lista_de_linhas[i])
        if word in formatted_line.lower().split():
            linhas_com_palavra.append({"linha": i + 1})
    return linhas_com_palavra


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    lista_de_dicts = []

    for i in range(len(instance)):
        document_dict = instance.search(i)
        ocorrencias_formatadas = linhas_de_ocorrencias(
            word,
            document_dict["linhas_do_arquivo"]
        )

        if ocorrencias_formatadas != []:
            lista_de_dicts.append({
                "palavra": word,
                "arquivo": document_dict["nome_do_arquivo"],
                "ocorrencias": ocorrencias_formatadas
            })

    return lista_de_dicts


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
