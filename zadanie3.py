def podzbiory(x):
    """
    Zwraca listę wszystkich podzbiorów zbioru.

    Funkcja przyjmuje zbiór jako argument i zwraca listę wszystkich możliwych podzbiorów
    tego zbioru, w tym pusty zbiór. Wynik jest reprezentowany jako lista, a nie zbiór, ponieważ
    podzbiory są przechowywane w określonej kolejności.

    Args:
        x (set): Zbiór, dla którego mają zostać wygenerowane podzbiory.

    Returns:
        list: Lista zawierająca wszystkie podzbiory zbioru, w tym pusty zbiór.

    Raises:
        TypeError: Jeżeli argument nie jest typu `set`.

    Examples:
        >>> podzbiory({1, 2})
        [[], [1], [2], [1, 2]]

        >>> podzbiory({'a', 'b', 'c'})
        [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
    """
    if type(x) == set: # sprawdzenie poprawnosci danych wejsciowych
        lista_x = sorted(list(x)) # przeksztalcenie zbioru na liste w celu iterowania po niej (posortowano ja rowniez dla przejrzystosci wynikow, ale jest to opcjonalne)
        wynik = [[]] # lista na ktorej przechowywane sa mozliwe zbiory (zawiera pusty zbior, poniewaz kazdy zbior zawiera pusty zbior)
        for element in lista_x: # iterowanie po kazdym elemencie listy wejsciowej
            nowe_podzbiory = [] # utworzenie nowej listy, ktora bedzie zawierac nowe podzbiory
            for podzbior in wynik: # iterowanie po kazdym podzbiorze zapisanym w liscie wyjsciowej
                nowe_podzbiory.append(podzbior + [element]) # dodanie do listy nowe podzbioru, ktory jest polaczeniem aktualnego podzbioru i elementu
            wynik.extend(nowe_podzbiory) # dodanie do listy wyjsciowej nowych podzbiorow
        return wynik
    else:
        raise TypeError("Niepoprawne dane wejściowe")