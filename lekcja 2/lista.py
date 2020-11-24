import random
from statistics import median

loop=True
liczby = []
minimalna = 0
maksymalna = 100

def menu():
    print("1 - wprowadzenie liczb")
    print("2 - wyświetlanie")
    print("3 - sortowanie")
    print("4 - informacje o liście")
    print("5 - usunięcie liczb z listy")
    print("0 - zamknij program")

def wprowadzanie(lista):
    Elementy = int(input("Ile liczb chcesz wprowadzic?\n"))
    los = input("Czy chcesz wprowadzic liczby losowo? [t/n]\n")
    if los.lower() == "t":
        for i in range(Elementy):
            lista.append(random.randint(minimalna, maksymalna))
    elif los.lower() == "n":
        for i in range(Elementy):
            lista.append(int(input(f"Podaj {i+1} liczbe: ")))
    else:
        print("Niepoprawny wybor")

def usun(lista):
    usuniecie = input("Usunac element czy przedział? [e/p]\n")
    if usuniecie.lower() == "e":
        usune = int(input("Ktory element listy chcesz usunac?\n"))
        lista.pop(usune-1)
    elif usuniecie.lower() == "p":
        print("Ktore elementy listy chcesz usunac?")
        usunP1 = int(input("Od: "))
        if usunP1 > len(lista):
            print("out of range")      
        else:
            usunP2 = int(input("Do: "))
            del liczby[usunP1-1:usunP2]

while loop:
    menu()
    wybor = input("Co chcesz zrobić?\n")
    if wybor=='1':
        wprowadzanie(liczby)
    elif wybor=='2':
        print(f"Lista: {liczby}")
    elif wybor=='3':
        liczby = sorted(liczby)
        print(f"Posortowana lista: {liczby}")
    elif wybor=='4':
        print(f"Ilosc liczb z listy to {len(liczby)}")
        print(f"Mediana liczb z listy to {median(liczby)}")
        print(f"Suma liczb z listy to {sum(liczby)}")
        print(f"Srednia liczb z listy to {sum(liczby)/len(liczby)}")
        print(f"Najmniejsza liczba z listy to {min(liczby)}")
        print(f"Najwieksza liczba z listy to {max(liczby)}")
    elif wybor=='5':
        usun(liczby)
    elif wybor.lower() == '0':
        loop=False
    else:
        print("Coś nie tak")