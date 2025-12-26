import random
import time

# Funkcja do sortowania bąbelkowego (Bubble Sort)
def babelkowe(tablica):
    for j in range(0, len(tablica) - 1):
        for i in range(0, len(tablica) - 1):
            if tablica[i] > tablica[i + 1]:
                tablica[i], tablica[i + 1] = tablica[i + 1], tablica[i]


# Funkcja do sortowania przez wstawianie (Insertion Sort)
def wstawianie(tablica):
    for i in range(1, len(tablica)):

        # wstawienie elementu w odpowiednie miejsce
        pom = tablica[i]

        # ten element zostanie wstawiony w odpowiednie miejsce
        j = i - 1

        # przesuwanie elementów większych od pom
        while j >= 0 and tablica[j] > pom:
            # przesuwanie elementów
            tablica[j + 1] = tablica[j]
            j -= 1

        tablica[j + 1] = pom  # wstawienie wartości zmiennej pom w odpowiednie miejsce

# Funkcja do sortowania przez wybieranie (Selection Sort)
def wybieranie(tablica):
    for i in range(len(tablica) - 1):
        pmin = i

        for j in range(i + 1, len(tablica)):
            if tablica[j] < tablica[pmin]:
                pmin = j

        tablica[i], tablica[pmin] = tablica[pmin], tablica[i]

# Funkcja do sortowania szybkiego (Quick Sort)
def szybkie(tablica):
    def sortuj(lewy, prawy):
        if lewy >= prawy:
            return

        i = lewy
        j = prawy
        pivot = tablica[(lewy + prawy) // 2]

        while i <= j:
            while tablica[i] < pivot:
                i += 1
            while tablica[j] > pivot:
                j -= 1
            if i <= j:
                tablica[i], tablica[j] = tablica[j], tablica[i]
                i += 1
                j -= 1

        if lewy < j:
            sortuj(lewy, j)
        if i < prawy:
            sortuj(i, prawy)

    sortuj(0, len(tablica) - 1)

# Funkcja do sortowania kubełkowego (Bucket Sort)
def kubelkowe(tablica):
    mini = min(tablica)
    maks = max(tablica)

    liczniki = [0] * (maks - mini + 1)

    for i in range(len(tablica)):
        liczniki[tablica[i] - mini] += 1

    j = 0

    for i in range(len(liczniki)):
        while liczniki[i] > 0:
            tablica[j] = i + mini
            liczniki[i] -= 1
            j += 1


# Funkcja do wstawiania wykonanego sortowania do pliku
def wstaw_do_pliku(tablica, czas, zloznosc, nazwa_pliku):
    with open(nazwa_pliku, "w") as plik:

        tekst = f"Czas wykonania: {str(czas)} sekund. \nZłożność obliczeniowa algorytmu: {zloznosc} \nPosortowane liczby: \n"
        plik.write(tekst)
        plik.write("\n")

        for element in tablica:
            plik.write(str(element))
            plik.write("\n")

def generuj_dane():
    with open("dane.txt", "w") as plik:
        for i in range(9999):
            plik.write(str(random.randint(-100000, 100000)))
            plik.write("\n")


# Główna funkcjonalność programu

czas = 0

print("Program do testowania różnych algorytmów sortowania.")
print()

print("Czy wygenerować nowe dane? (T/N)")

while True:
    wybor = input().strip().lower()
    if wybor in ("t", "y"):
        generuj_dane()
        break
    if wybor == "n":
        break
    print("Wpisz T lub N")

print()
print("Wybierz algorytm sortowania:")
print("1. Sortowanie bąbelkowe (Bubble Sort)")
print("2. Sortowanie przez wstawianie (Insertion Sort)")
print("3. Sortowanie przez wybieranie (Selection Sort)")
print("4. Sortowanie szybkie (Quick Sort)")
print("5. Sortowanie kubełkowe (Bucket Sort)")
print()

try:
    with open("dane.txt", "r") as plik:
        tablica = []
        for linia in plik:
            s = linia.strip()
            if s:
                tablica.append(int(s))
    if not tablica:
        print("Brak danych w dane.txt")
        exit()
except FileNotFoundError:
    print("Brak pliku dane.txt")
    exit()
except ValueError:
    print("W dane.txt jest linia, która nie jest liczbą")
    exit()

while True:
    wybor = input().strip()
    if wybor in ("1", "2", "3", "4", "5"):
        break
    print("Wpisz liczbę 1-5")

if wybor == "1":
    zloznosc = str("O(n^2)")

    start = time.time()
    babelkowe(tablica)
    czas = round(time.time() - start, 4)
    wstaw_do_pliku(tablica, czas, zloznosc, "wynik.txt")

elif wybor == "2":
    zloznosc = str("O(n^2)")

    start = time.time()
    wstawianie(tablica)
    czas = round(time.time() - start, 4)
    wstaw_do_pliku(tablica, czas, zloznosc, "wynik.txt")

elif wybor == "3":
    zloznosc = str("O(n^2)")

    start = time.time()
    wybieranie(tablica)
    czas = round(time.time() - start, 4)
    wstaw_do_pliku(tablica, czas, zloznosc, "wynik.txt")

elif wybor == "4":
    zloznosc = str("Optymalna: O(n log n), Pesymistyczna: O(n^2)")

    start = time.time()
    szybkie(tablica)
    czas = round(time.time() - start, 4)
    wstaw_do_pliku(tablica, czas, zloznosc, "wynik.txt")

elif wybor == "5":
    zloznosc = str("O(n^2)")

    start = time.time()
    kubelkowe(tablica)
    czas = round(time.time() - start, 4)
    wstaw_do_pliku(tablica, czas, zloznosc, "wynik.txt")
else:
    print("Wybrano zły typ sortowania.")

print("Posortowane.")