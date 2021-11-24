def odwracanie(L: list, left: int, right: int):
    if right < left:
        return
    for i in range(int((right - left + 1)/2)):
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def odwracanie_rekurencyjnie(L: list, left: int, right: int):
    if right <= left:
        return
    L[left], L[right] = L[right], L[left]
    return odwracanie_rekurencyjnie(L, left+1, right -1)


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
odwracanie(L, 3, 8)
print("Odwracanie listy od indeksu 3 do 8. Wynikowa lista: ", L)
L2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odwracanie_rekurencyjnie(L2, 0, 9)
print("Odwracanie listy rekurencyjnie od indeksu 0 do 9: ", L2)

