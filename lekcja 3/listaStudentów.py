import pickle


students_list = []


class Student:
    def __init__(self, name, surname, index_nmber, rating_list=[]):
        self.__name = name
        self.__surname = surname
        self.__index_number = index_nmber
        self.__rating_list = rating_list[:]

    def show(self):
        print(f"\nStudent: {self.__name} {self.__surname}")
        print(f"  Index Number: {self.__index_number}")
        print(f"  Rating list: {self.__rating_list}")

    def set_name(self, name):
        self.__name = name

    def set_surname(self, surname):
        self.__surname = surname

    def set_index_nmber(self, index_nmber):
        self.__index_number = index_nmber

    def avg_rating(self):
        return sum(self.__rating_list) / len(self.__rating_list)
    
    def indexvalue(self):
        return self.__index_number

    def change_grades(self):
        while 1:
            x = input("Dodac (D) czy usunac (U) oceny?")
            if x.lower() == "d":
                dodanie = defense_int_input("Jaka ocene dodac?", 1, 6)
                self.__rating_list.append(dodanie)
            if x.lower() == "u":
                print("Ktora ocene usunac? (podaj miejsce w dzienniku)")
                usuniecie = int(input())
                if usuniecie > len(self.__rating_list):
                    print("Nie ma takiej pozycji w dzienniku")
                else:
                    self.__rating_list.pop(usuniecie-1)
            print ("Czy chcesz kontynuować zmiany ocen? [tak/nie]")
            y = input()
            if y.lower() == "tak":
                pass
            else:
                break

def defense_int_input(text, min_val, max_val):
    value = max_val
    while True:
        value = input(text)
        try:
            if not ((int(min_val) > int(value)) or (int(value) > int(max_val))): 
                break
            print('Wartosc musi byc nie mniejsza niz', min_val, 
            'i nie wieksza niz', max_val, sep=' ', end='\n')
        except ValueError:
            print('Wartość musi być liczbą całkowitą')
    return int(value)

def display_menu():
    menu_selection = 0
    print('\nMenu:')
    print('1 - Wyświetlanie listy studentów')
    print('2 - Edycja listy studentów')
    print('3 - Wyswietlanie wybranych studentów')
    print('4 - Odczytywanie listy z pliku')
    print('5 - Zapisywanie listy do pliku')
    print('6 - Koniec programu')

    print('\n')
    menu_selection = defense_int_input("Wybierz operacje: ", 1, 6)

    return menu_selection

def display_menu2():
    menu_selection = 0
    print('\nEdycja listy studentów:')
    print('  1 - Dodaj nowego studenta')
    print('  2 - Usuń wybranego studenta')
    print('  3 - Dodaj nową ocenę')
    print('  4 - Wróć')

    print('\n')
    menu_selection = defense_int_input("Wybierz operacje: ", 1, 4)

    return menu_selection

def display_menu3():
    menu_selection = 0
    print('\nWyswietlanie wybranych studentów:')
    print('  1 - Średnia > x')
    print('  2 - Średnia < x')
    print('  3 - Wróć')

    print('\n')
    menu_selection = defense_int_input("Wybierz operacje: ", 1, 3)

    return menu_selection

def load():
    try:
        with open("bin.dat", "rb") as f:
            students_list = pickle.load(f)
            return students_list
    except FileNotFoundError:
        with open("bin.dat", "wb") as f:
            print('\nbin.dat nie został znaleziony, tworzę nowy plik...\n')

    except Exception as identifier:
        print(f'\nWarning: {identifier} podczas czytania pliku\n')
        return []


def save(students_list):
    with open("bin.dat", "wb") as f:
        pickle.dump(students_list, f)

def showStudents(s_list):
    print('\nLista studentów:\n')
    for student in s_list:
        student.show()
        print()


menu_selection = display_menu()

while(menu_selection < 6):
    if menu_selection == 1:
        showStudents(students_list)
    elif menu_selection == 2:
        m = display_menu2()
        while(m < 4):
            if m == 1:
                print('(napisz /anuluj by anulować)')
                name = input("Imię: ")
                if name == '/anuluj':
                    pass
                else:
                    surname = input('Nazwisko: ')
                    index_nmber = int(input('Numer w dzienniku: '))
                    student = Student(name, surname, index_nmber)
                    students_list.append(student)
            elif m == 2:
                showStudents(students_list)
                print('(napisz /anuluj by anulować)')
                index = int(input('Wprowadź indeks studenta którego chcesz usunąć: '))
                if index == '/anuluj':
                    pass
                else:
                    flag = False
                    for student in students_list:
                        try:
                            if student.indexvalue() == index:
                                flag = True
                                students_list.remove(student)
                                break
                            else:
                                print('Taki index nie istnieje!')
                                continue
                        except Exception:
                            print('Wystąpił problem z listą studentów')
                            print('Jeżeli to się powtórzy możliwe że będzie niezbędne ręczne usunięcie pliku bazy danych bin.dat')
                            raise
            elif m == 3:
                showStudents(students_list)
                print('(napisz /anuluj by anulować)')
                index = int(input('Wprowadź indeks studenta któremu chcesz zmienić ocenę(y): '))
                if index == '/anuluj':
                    pass
                else:
                    flag = False
                    for student in students_list:
                        try:
                            if student.indexvalue() == index:
                                student.change_grades()
                                flag = True
                                break
                        except Exception:
                            print('Wystąpił problem z listą studentów')
                            print('Jeżeli to się powtórzy możliwe że będzie niezbędne ręczne usunięcie pliku bazy danych bin.dat')
                            raise
                    if not flag:
                        input('Taki index nie istnieje!')
                        continue
            m = display_menu2()
    elif menu_selection == 3:
        m = display_menu3()
        while m < 3:
            x = input('x: ')
            try:
                x = float(x)
            except ValueError:
                print ('Wartość musi być liczbą!')
                continue    
            try:
                if m == 1:
                    for student in students_list:
                        if student.avg_rating() > x:
                            student.show()
                            print()
                if m == 2:
                    for student in students_list:
                        if student.avg_rating() < x:
                            student.show()
                            print()

            m = display_menu3()

    elif menu_selection == 4:
        students_list = load()
        
    elif menu_selection == 5:
        save(students_list)
        print('Zapisano')

    menu_selection = display_menu()