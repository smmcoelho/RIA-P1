
def removerDuplicados(l: list) -> list:
    pass

if __name__ == '__main__':
    l = [1, 1, 2, 3, 2, 4, 3]
    new_l = removerDuplicados(l)

    expected_list = [1, 2, 3, 4]

    assert new_l == expected_list, "Resultado errado" 
