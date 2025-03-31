import math

def heron(a,b,c):
    if type(a) == int and type(b) == int and type(c) == int: #sprawdzenie poprawnosci typu danych wejsciowych
        if(a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0): # sprawdzenie czy zmienne tworza trojkat
            p = (a + b + c) / 2
            area = math.sqrt(p * (p-a) * (p-b) * (p-c)) #obliczenie pola trojkata
            area = (round(area, 2))
            return area
        else:
            raise ValueError("Trojkat o zadanych bokach nie istnieje")
    else:
        raise TypeError("Zmienne nie sa typu int")
