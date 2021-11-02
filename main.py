def czyPierwsza(n):
    if n < 2:
        return False
    for i in (range(2, n)):
        if n % i == 0:
            return False
    return True


print("Program sprawdzający, czy liczba jest liczbą pierwszą.")
print("Podaj liczbę: ")
n = int(input())
print(czyPierwsza(n))