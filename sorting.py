"""
Algoritmos de ordenação implementados como *generators*.

Cada função recebe uma lista e, a cada `yield`, devolve uma tupla:
    (lista_atual, indices_em_destaque)

O `yield` acontece a cada comparação/troca relevante, permitindo que o
laço principal do pygame avance um passo por frame e desenhe o estado
atual das barras. Quando o algoritmo termina, a função simplesmente
retorna (StopIteration), e o chamador sabe que aquele algoritmo
"cruzou a linha de chegada".
"""

import random


def bogo_sort(data):
    lst = data
    while True:
        if is_sorted(lst):
            return
        random.shuffle(lst)
        yield lst, list(range(len(lst)))


def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


def bubble_sort(data):
    lst = data
    n = len(lst)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            yield lst, [j, j + 1]
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
                yield lst, [j, j + 1]
        if not swapped:
            break


def merge_sort(data):
    lst = data

    def _merge_sort(array, offset):
        if len(array) <= 1:
            return
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        yield from _merge_sort(left_half, offset)
        yield from _merge_sort(right_half, offset + mid)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
            lst[offset:offset + len(array)] = array
            yield lst, [offset + k - 1]
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
            lst[offset:offset + len(array)] = array
            yield lst, [offset + k - 1]
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
            lst[offset:offset + len(array)] = array
            yield lst, [offset + k - 1]

    yield from _merge_sort(lst, 0)


def cocktail_shaker_sort(data):
    lst = data
    n = len(lst)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False
        for i in range(start, end):
            yield lst, [i, i + 1]
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
                yield lst, [i, i + 1]

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            yield lst, [i, i + 1]
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
                yield lst, [i, i + 1]

        start += 1


def insertion_sort(data):
    lst = data
    for i in range(1, len(lst)):
        current = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > current:
            lst[j + 1] = lst[j]
            j -= 1
            yield lst, [j + 1, j + 2]
        lst[j + 1] = current
        yield lst, [j + 1]


def bucket_sort(data):
    """Bucket sort assume valores em [0, 1). O chamador normaliza antes."""
    lst = data
    n = len(lst)
    slot_num = 10
    buckets = [[] for _ in range(slot_num)]

    for j in lst:
        index_b = min(int(slot_num * j), slot_num - 1)
        buckets[index_b].append(j)
        yield lst, []

    k = 0
    for i in range(slot_num):
        sorted_bucket = list(buckets[i])
        for step, _ in insertion_sort(sorted_bucket):
            pass  # ordena o bucket internamente sem animar cada micro-passo
        buckets[i] = sorted_bucket
        for value in buckets[i]:
            lst[k] = value
            k += 1
            yield lst, [k - 1]


ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Cocktail Shaker": cocktail_shaker_sort,
    "Bucket Sort": bucket_sort,
    # Bogo sort é opcional: com listas > ~7 elementos pode nunca terminar
    # em tempo hábil. Deixe fora da corrida "séria", mas disponível.
    "Bogo Sort": bogo_sort,
}