a = 10

def do_stuff(n):
    a = n
    return a


if __name__ == '__main__':

    # test 1
    result = do_stuff(1)
    expected = 1
    assert result == expected, f"test 1 - Resultado errado"

    # test 2
    result = do_stuff(3)
    expected = 3
    assert a == expected, f"test 2 - Resultado errado"
