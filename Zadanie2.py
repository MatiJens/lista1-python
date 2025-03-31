def wspolne(a,b):
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