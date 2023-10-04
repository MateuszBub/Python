import random

opcje = ("kamien", "papier", "nozyce")
gracz = None
komputrW= random.choice(opcje)

gracz = input("wybierz swoj wybor  (kamien,papier,nozyce): ")

while gracz not in opcje:
    gracz = input("nie potrafisz w to grac czy co? podaj  (kamien,papier,nozyce) ")

if gracz == komputrW:
    print("to remis")
elif gracz == "kamien" and komputrW == "nozyce":
    print("gracz wygrywa")
elif gracz == "papier" and komputrW == "kamien":
    print("gracz wygrywa")
elif gracz == "nozyce" and komputrW == "papier":
    print("gracz wygrywa")
else:
    print("przegrales z botem ")

print(f"Gracz: {gracz}")
print(f"Komputer: {komputrW}")