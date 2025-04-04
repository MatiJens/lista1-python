import math

def heron(a,b,c):
    """
    Oblicza pole trójkąta na podstawie długości boków za pomocą wzoru Herona.

    Funkcja najpierw sprawdza, czy podane wartości są typu int oraz czy mogą utworzyć trójkąt.
    Jeśli warunki są spełnione, oblicza pole korzystajac ze wzoru Herona.

    Args:
        a (int): Długość pierwszego boku trójkąta.
        b (int): Długość drugiego boku trójkąta.
        c (int): Długość trzeciego boku trójkąta.

    Returns:
        float: Pole trójkąta

    Raises:
        TypeError: Jeżeli którekolwiek z podanych wartości nie są typu int.
        ValueError: Jeżeli boki nie spełniają warunku istnienia trójkąta.

    Examples:
        >>> heron(3, 4, 5)
        6.0
        >>> heron(10, 6, 8)
        24.0
    """
    if type(a) == int and type(b) == int and type(c) == int: #sprawdzenie poprawnosci typu danych wejsciowych
        if(a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0): # sprawdzenie czy zmienne tworza trojkat
            p = (a + b + c) / 2
            area = math.sqrt(p * (p-a) * (p-b) * (p-c)) #obliczenie pola trojkata
            return area
        else:
            raise ValueError("Trojkat o zadanych bokach nie istnieje")
    else:
        raise TypeError("Zmienne nie sa typu int")
