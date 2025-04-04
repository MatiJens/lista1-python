def collatz(c):
    """
    Zwraca ciąg liczb według hipotezy Collatza dla danej liczby całkowitej.

    Funkcja generuje ciąg liczb, który zaczyna się od wartości c. Jeśli c jest liczbą parzystą, dzielimy ją przez 2,
    w przeciwnym razie mnożymy ją przez 3 i dodajemy 1. Proces powtarzamy, aż osiągniemy 1.
    Ciąg jest zwracany w postaci listy, zawierającej kolejne liczby.

    Args:
        c (int): Liczba całkowita, dla której ma zostać wygenerowany ciąg Collatza.

    Returns:
        list: Lista liczb tworzących ciąg Collatza, który kończy się na 1.

    Raises:
        ValueError: Jeżeli c jest mniejsze lub równe 0.
        TypeError: Jeżeli c nie jest liczbą całkowitą.

    Examples:
        >>> collatz(6)
        [3, 10, 5, 16, 8, 4, 2, 1]

        >>> collatz(11)
        [34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    if type(c) == int: # sprawdzenie poprawnosci danych wejsciowych
        if c > 0:
            wynik = []
            while c != 1:
                if (c % 2) == 0:
                    c = c // 2
                else:
                    c = 3 * c + 1
                wynik.append(c)
            return wynik
        else:
            raise ValueError("niepoprawna wartosc danych wejsciowych")
    else:
        raise TypeError("Niepoprawny typ danych wejściowych")