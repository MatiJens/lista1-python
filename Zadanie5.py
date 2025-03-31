def collatz(c):
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