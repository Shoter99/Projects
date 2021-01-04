rows = int(input("Podaj liczbę wierszy: "))
columns = int(input("Podaj liczbę kolmun: "))


def draw_row(row, column):
    while row >= 0:
        print(" --- --- --- ")
        print(column*"|   "+"|")
        row -= 1
    print(" --- --- --- ")


draw_row(rows, columns)
