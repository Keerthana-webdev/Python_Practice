def km_to_m(km): return km * 1000
def m_to_km(m): return m / 1000
def c_to_f(c): return (c * 9/5) + 32

while True:
    print("\n1.KM->M 2.M->KM 3.C->F 4.Exit")
    ch = input("Choice: ")

    if ch == "4":
        break

    val = float(input("Enter value: "))

    if ch == "1":
        print(km_to_m(val))
    elif ch == "2":
        print(m_to_km(val))
    elif ch == "3":
        print(c_to_f(val))
    else:
        print("Invalid")