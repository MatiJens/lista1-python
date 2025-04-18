def komplement(DNA):
    """
    @author Mateusz Jenś
    Zwraca komplementarną nić DNA.

    Funkcja konwertuje DNA (reprezentowaną jako lista nukleotydów) na komplementarną nić DNA,
    gdzie A jest zastępowane przez T, T przez A, C przez G, a G przez C.

    Args:
        DNA (list): Lista nukleotydów (A, T, C, G) reprezentujących nić DNA.

    Returns:
        list: Komplementarna nić DNA.

    Raises:
        ValueError: Jeżeli lista zawiera niewłaściwe nukleotydy.
        TypeError: Jeżeli wejście nie jest listą.

    Examples:
        >>> komplement(['A', 'T', 'C', 'G'])
        ['T', 'A', 'G', 'C']
    """
    if type(DNA) == list:
        if all(nukleotyd in "ATCG" for nukleotyd in DNA): #sprawdzenie czy w DNA wystepuja jedynie ATCG
            nic_matrycowa = [] #utworzenie pustej tablicy z wynikami
            for i in range(len(DNA)): # sprawdzenie kazdego elementu listy wejsciowej i przypisanie do listy wyjsciowej odpowiedniej wartosci
                if DNA[i] == 'A':
                    nic_matrycowa.insert(0, 'T')
                elif DNA[i] == 'T':
                    nic_matrycowa.insert(0, 'A')
                elif DNA[i] == 'C':
                    nic_matrycowa.insert(0, 'G')
                else:
                    nic_matrycowa.insert(0, 'C')
            return nic_matrycowa
        else:
            raise ValueError("Niepoprawna wartosc danych wejsciowych")
    else:
        raise TypeError("Niepoprawny typ danych wejściowych")

def transkrybuj(nic_matrycowa):
    """
    @author Mateusz Jenś
    Przeprowadza transkrypcję DNA na RNA.

    Funkcja konwertuje nić matrycową DNA (reprezentowaną jako lista nukleotydów) na
    komplementarną nić RNA, gdzie A jest zastępowane przez U, T przez A, C przez G,
    a G przez C.

    Args:
        nic_matrycowa (list): Nić matrycowa DNA, reprezentowana jako lista nukleotydów (A, T, C, G).

    Returns:
        list: Komplementarna nić RNA (A, U, C, G).

    Raises:
        ValueError: Jeżeli lista zawiera niewłaściwe nukleotydy.
        TypeError: Jeżeli wejście nie jest listą.

    Examples:
        >>> transkrybuj(['A', 'T', 'C', 'G'])
        ['U', 'A', 'G', 'C']
    """
    if type(nic_matrycowa) == list:
        if all(nukleotyd in "ATCG" for nukleotyd in nic_matrycowa): #sprawdzenie czy w nici matrycowej wystepuja jedynie ATCG
            RNA = []
            for i in range(len(nic_matrycowa)):
                if nic_matrycowa[i] == 'A':
                    RNA.insert(0, 'U')
                elif nic_matrycowa[i] == 'T':
                    RNA.insert(0, 'A')
                elif nic_matrycowa[i] == 'C':
                    RNA.insert(0, 'G')
                else:
                    RNA.insert(0, 'C')
            return RNA
        else:
            raise ValueError("Niepoprawna wartosc danych wejsciowych")
    else:
        raise TypeError("Niepoprawny typ danych wejściowych")

def transluj(mRNA):
    """
    @author Mateusz Jenś
    Przeprowadza translację mRNA na aminokwasy.

    Funkcja tłumaczy mRNA na sekwencję aminokwasów (białko) zgodnie z kodem genetycznym.
     Proces tłumaczenia rozpoczyna sie po napotkaniu kodonu stopu a, zatrzymuje się po
     napotkaniu kodonu stopu.

    Args:
        mRNA (list): Lista nukleotydów RNA (A, U, C, G), reprezentująca łańcuch mRNA.

    Returns:
        list: Lista aminokwasów (np. "Phe", "Leu") tworząca białko.

    Raises:
        ValueError: Jeżeli lista zawiera niewłaściwe nukleotydy.
        TypeError: Jeżeli wejście nie jest listą.

    Examples:
        >>> transluj(['A', 'U', 'G', 'U', 'U', 'U','U','A','G'])
        ['Phe']
    """
    # w celu wykonania tego słownika wykorzystałem ChatGPT, prompt: "napisz mi slownik w pythonie kodon : aminokwas (wersja 3 literowa) pomin kodon start i stop"
    aminokwasy = {
        "UUU": "Phe", "UUC": "Phe",
        "UUA": "Leu", "UUG": "Leu",
        "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
        "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",
        "AUG": "Met",
        "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
        "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
        "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
        "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
        "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
        "UAU": "Tyr", "UAC": "Tyr",
        "CAU": "His", "CAC": "His",
        "CAA": "Gln", "CAG": "Gln",
        "AAU": "Asn", "AAC": "Asn",
        "AAA": "Lys", "AAG": "Lys",
        "GAU": "Asp", "GAC": "Asp",
        "GAA": "Glu", "GAG": "Glu",
        "UGU": "Cys", "UGC": "Cys",
        "UGG": "Trp",
        "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
        "AGU": "Ser", "AGC": "Ser",
        "AGA": "Arg", "AGG": "Arg",
        "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
    }
    if type(mRNA) == list: #sprwadzenie poprawnosci typu danych
        if all(nukleotyd in "AUCG" for nukleotyd in mRNA): #sprawdzenie czy w mRNA wystepuja jedynie AUCG
            bialko = [] # w tej liscie zapisywana jest struktura bialka - aminokwasy
            for i in range(len(mRNA) - 2): # dla kazdego elementu (nukleotydu) w mRNA (zmniejszone o 2 poniewaz sprawdzamy dany element listy i dwa nastepne
                kodonStart = mRNA[i] + mRNA[i + 1] + mRNA[i + 2] # zapisanie aktualnego elementu listy i dwoch nastepnym w formie zmiennej
                if kodonStart == "AUG": # jezeli ta zmienna jest rowna kodonowi startu przechodzimy do zapisywania bialka
                    for j in range((i + 3), len(mRNA) - 2, 3): # kolejna petla for, tym razem od wartosci (i + 3) pomijamy kodon startu do konca mRNA ze skokiem co 3 (z tylu kodonow sklada sie aminokwas)
                        kodon = mRNA[j] + mRNA[j + 1] + mRNA[j + 2] # zapisanie aktualnego elementu listy i dwoch nastepnym w formie zmiennej
                        if kodon in aminokwasy: # jezeli ta zmienna jest ktorymkolwiek kluczem w slowniku aminokwasy
                            bialko.append(aminokwasy[kodon]) # program dodaje wartosc dla tego klucza do listy bialka
                        if kodon == "UAA" or kodon == "UAG" or kodon == "UGA": # jesli program natrafi na kodon stop
                            return bialko # konczy dzialanie funkcji i zwraca liste bialko
                        if j == (len(mRNA) - 3): # jesli przejdzie przez cale mRNA i nie natrafi na kodon stop
                            return "brak kodonu stopu" # zwraca informacje ze nie w mRNA nie ma kodonu stop
            return "brak kodonu startu" # w przypadku gdy nie znajdzie sie kodon startu
        else:
            raise ValueError("Niepoprawna wartosc danych wejsciowych")
    else:
        raise TypeError("Niepoprawny typ danych wejsciowych")