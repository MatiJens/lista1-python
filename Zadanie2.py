def wspolne(a,b):
    """
    @author Mateusz Jenś
    Zwraca listę wspólnych elementów dwóch list, unikając duplikatów.

    Funkcja porównuje dwie listy, a i b, i zwraca listę zawierającą elementy,
    które występują w obu listach. Każdy element pojawia się w wynikowej liście tylko raz,
    niezależnie od liczby jego wystąpień w obu listach. Funkcja pomija elementy, które zostały już sprawdzone.

    Args:
        a (list): Pierwsza lista, w której będziemy szukać wspólnych elementów.
        b (list): Druga lista, w której będziemy szukać wspólnych elementów.

    Returns:
        list: Lista zawierająca wspólne elementy z obu list, bez duplikatów.

    Raises:
        TypeError: Jeżeli którykolwiek z argumentów nie jest typu list.

    Examples:
        >>> wspolne([1, 2, 3], [2, 3, 4])
        [2, 3]
        >>> wspolne([5, 6, 7], [8, 9, 7])
        [7]
    """
    if type(a) == list and type(a) == type(b): # sprawdzenie poprawności danych wejściowych
        common = [] # tu zapisywane sa wspolne elementy
        skip = [] # tu zapisywane sa indeksy elementow ktore zostaly juz sprawdzone
        for i in range (0, (len(a))):
            for j in range (0, (len(b))):
                if a[i] == b[j]: # jesli wystepuje wspolny element
                    if j in skip: # jesli dany indeks zostal juz sprawdzony program go pomija
                        continue
                    else:
                        common.append(a[i]) # dodanie wspolnego elementu do tabeli
                        skip.append(j) # dodanie indeksu do tabeli
                        break
        return common
    else:
        raise TypeError("Niepoprawny typ danych wejściowych")