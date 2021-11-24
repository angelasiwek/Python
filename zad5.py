class Bug:
    licznik = 0
    def __init__(self):
        Bug.licznik += 1
        self.ktory = Bug.licznik
    def __del__(self):
        Bug.licznik -= 1
        print("Usuwam obiekt. Licznik: ", Bug.licznik, " ID: " , self.ktory )
    def __str__(self):
        return "Licznik: "  + str(Bug.licznik) + " Bieżące ID: " +str(self.ktory)





licznik = 0
bugs =[]
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])