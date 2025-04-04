def Fibonacci_iteracyjnie(n):
    """
    Oblicza n-ty wyraz ciągu Fibonacciego iteracyjnie.

    Funkcja oblicza n-ty wyraz ciągu Fibonacciego za pomocą podejścia iteracyjnego.
    Dla n = 0 zwraca 0, dla n = 1 zwraca 1. Dla pozostałych wartości n oblicza wyraz
    ciągu na podstawie dwóch pierwszych wyrazów ciągu, wykorzystując pętlę.

    Args:
        n (int): Indeks wyrazu ciągu Fibonacciego.

    Returns:
        int: n-ty wyraz ciągu Fibonacciego.

    Raises:
        ValueError: Jeżeli n jest mniejsze niż 0.
        TypeError: Jeżeli n nie jest liczbą całkowitą.

    Examples:
        >>> Fibonacci_iteracyjnie(5)
        5

        >>> Fibonacci_iteracyjnie(10)
        55
    """
    if type(n) == int: # sprawdzenie poprawnosci danych wejsciowych
        if n >= 0:
            if n == 0:  # pierwsze dwie wartosci zbioru wynosza 0, 1 i sa z gory narzucone
                return 0
            elif n == 1:
                return 1
            else: # dla kazdego nastepnego n wynik nalezy obliczyc
                a, b, wynik = 0, 1, 0 # inicjalizacja zmiennych
                for i in range(2, n + 1): # iterujemy od 2 (pierwsze dwie wartosci sa z gory narzucone) do n + 1 (range w pythonie konczy sie 1 przed wartoscia zadana)
                    wynik = a + b # wzor fibonaciego
                    a = b
                    b = wynik
            return wynik
        else:
            raise ValueError("Niepoprawne wartosci danych wejsciwoych")
    else:
        raise TypeError("Niepoprawne typ danych wejściowych")

def Fibonacci_rekurencyjnie(n):
    """
    Oblicza n-ty wyraz ciągu Fibonacciego rekurencyjnie.

     Funkcja oblicza n-ty wyraz ciągu Fibonacciego za pomocą podejścia rekurencyjnego.
     Dla n = 0 zwraca 0, dla n = 1 zwraca 1. Dla pozostałych wartości n funkcja wywołuje
     sama siebie z mniejszymi argumentami, aż osiągnie warunki końcowe.

     Args:
         n (int): Indeks wyrazu ciągu Fibonacciego.

     Returns:
         int: n-ty wyraz ciągu Fibonacciego.

     Raises:
         ValueError: Jeżeli n jest mniejsze niż 0.
         TypeError: Jeżeli n nie jest liczbą całkowitą.

     Examples:
         >>> Fibonacci_rekurencyjnie(5)
         5

         >>> Fibonacci_rekurencyjnie(10)
         55
     """
    if type(n) == int: # sprawdzenie poprawnosci danych wejsciowych
        if n >= 0:
            if n == 0:  # warunki koncowe rekurencji
                return 0
            elif n == 1:
                return 1
            else: # funkcja wywoluje sama siebie z coraz to mniejszymi argumentami wejsciowymi, az do osiagniecia wartosci n = 1 lub n = 0. Wartosci te sa sumowane
                return Fibonacci_rekurencyjnie(n - 1) + Fibonacci_rekurencyjnie(n - 2)
        else:
            raise ValueError("Niepoprawne wartosci danych wejsciwoych")
    else:
        raise TypeError("Niepoprawne typ danych wejściowych")