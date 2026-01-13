
# input: [1, 2, 3, 4] -> result: 4
def encontrarMaior(l: list):
    return 0

# input: [1, 2, 3, 4] -> result: 3
def encontrarSegundoMaior(l: tuple):
    return 0

# divisivel por 1 e por si proprio
def verificarSePrimo(n: int) -> bool:
    return True


if __name__ == '__main__':

    # test 1
    l = [1, 10, 20, 15, 3]
    result = encontrarMaior(l)
    expected = 20
    assert result == expected, f"test 1 - Resultado errado {result} != {expected}"

    # test 2
    l = [-1, -10, -20, -15, -3]
    result = encontrarMaior(l)
    expected = -1
    assert result == expected, f"test 2 - Resultado errado {result} != {expected}"

    # test 3
    l = [-1, -10, -20, -15, 0]
    result = encontrarMaior(l)
    expected = 0
    assert result == expected, f"test 3 - Resultado errado {result} != {expected}"

    # test 4
    l = (1, 10, 20, 15, 3)
    result = encontrarSegundoMaior(l)
    expected = 15
    assert result == expected, f"test 4 - Resultado errado {result} != {expected}"

    # test 5
    l = (1, 10, 20, 15, 20)
    result = encontrarSegundoMaior(l)
    expected = 15
    assert result == expected, f"test 5 - Resultado errado {result} != {expected}"

    # test 6
    assert verificarSePrimo(17), f"test 6 - Resultado errado"

    # test 7
    assert not verificarSePrimo(4), f"test 7 - Resultado errado"

    # test 8
    assert not verificarSePrimo(1), f"test 8 - Resultado errado"
