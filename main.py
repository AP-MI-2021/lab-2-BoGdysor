import math
from typing import List


def is_prime(n):
    d = 0
    for i in range(1, n + 1):
        if n % i == 0:
            d = d + 1
    if d == 2:
        return 1
    return 0


def get_largest_prime_below(n):
    """
      1.Returneaza ultimul numar prim mai mic decat un numar dat.
      :param n: numar natural
      :return: ultimul numar prim mai mic decat un numar dat,iar daca acesta nu exista retuneaza returneaza None
    """
    for i in range(n - 1, 1, -1):
        if is_prime(i):
            return i
    return None


def test_get_largest_prime_bellow():
    """Testeaza valori pentru functia get_largest_prime_bellow"""
    assert get_largest_prime_below(5) == 3
    assert get_largest_prime_below(7) == 5
    assert get_largest_prime_below(49) == 47
    assert get_largest_prime_below(0) is None
    assert get_largest_prime_below(1) is None
    assert get_largest_prime_below(2) is None
    assert get_largest_prime_below(200) == 199
    assert get_largest_prime_below(3) == 2


def get_perfect_squares(start: int, end: int) -> List[int]:
    """
    12.Afiseaza toate patratele perfecte dintr-un interval inchis dat.
    :param start: inceputul intervalului
    :param end: sfarsitul intervalului
    :return: lista cu toate patratele perfecte din interval
    """
    list_of_perfect_squares = []
    for i in range(start, end + 1):
        if math.sqrt(i) == int(math.sqrt(i)) and i != 0:
            list_of_perfect_squares.append(int(i))
    return list_of_perfect_squares


def test_get_perfect_squares():
    """ Testaza valori pentru functia get_perfect_squares"""
    assert get_perfect_squares(4, 16) == [4, 9, 16]
    assert get_perfect_squares(5, 25) == [9, 16, 25]
    assert get_perfect_squares(1, 2) == [1]
    assert get_perfect_squares(0, 3) == [1]
    assert get_perfect_squares(0, 0) == []
    assert get_perfect_squares(5, 5) == []
    assert get_perfect_squares(4, 4) == [4]


test_get_perfect_squares()
test_get_largest_prime_bellow()


def main():
    while True:
        print("1.Ultimul numar prim mai mic decat un numar dat.")
        print("2.Afiseaza toate patratele perfecte dintr-un interval inchis dat.")
        print("3.Iesire")
        optiune = int(input("selectati optiunea: "))
        if optiune == 1:
            n = int(input("\nIntroduceti numarul n: "))
            if get_largest_prime_below(n) is None:
                print("Nu exista numar prim mai mic decat numarul dat")
            else:
                print(get_largest_prime_below(n))
        elif optiune == 2:
            x = int(input("Introduceti de unde sa inceapa intervalul: "))
            y = int(input("Introduceti unde sa se termine intervalul: "))
            print(get_perfect_squares(x, y))
        elif optiune == 3:
            break
        else:
            print("Optiune invalida")


if __name__ == '__main__':
    main()
