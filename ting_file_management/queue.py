from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._lista = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._lista)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._lista.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if len(self._lista) == 0:
            raise IndexError("Índice Inválido ou Inexistente")
        return self._lista.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index >= len(self._lista):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._lista[index]
