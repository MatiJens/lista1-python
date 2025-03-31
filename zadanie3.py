def podzbiory(x):
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