def show_menu():
    print('''
1. Citire date.
2. Determinare cea mai lungă subsecvență cu proprietatea ca numerele sunt ordonate crescător.
3. Determinare cea mai lungă subsecvență cu proprietatea ca numărul de cifre este în ordine descrescătoare.
4. Ieșire.
''')

def cifre_ordine_descrescatoare(n):
    x= n % 10
    n //= 10
    while n > 0:
        if x >= n % 10:
            return False
        x = n % 10
        n //= 10
    return True

def numar_cifre_ord_desc(lst):
    temp = []
    rez = []
    for i in range (len(lst)):
        if(cifre_ordine_descrescatoare(lst[i]) == True):
            temp.append(lst[i])
        else:
            if(len(temp)>len(rez)):
                rez = temp.copy()
            temp.clear()
    if (len(temp) > len(rez)):
        rez = temp.copy()
    return rez

def test_numar_cifre_ord_desc():
    assert numar_cifre_ord_desc([]) == []
    assert numar_cifre_ord_desc([11,21,31]) == [21,31]
    assert (numar_cifre_ord_desc([331,321,54231])) == [321]

def numere_ordonate_crescator(lst):
    rez = []
    temp = []
    for x in range(len(lst)-1):
        if(lst[x]<lst[x+1]):
            temp.append(lst[x])
        else:
            temp.append(lst[x])
            if(len(temp) > len(rez)):
                rez = temp.copy()
            temp.clear()
    if (len(temp) > len(rez)):
        rez = temp.copy()
    return rez
def test_numere_ordonate_crescator():
    assert numere_ordonate_crescator([]) == []
    assert numere_ordonate_crescator([1,2,3,1]) == [1,2,3]

def citire_date():
    n = int(input("Numarul de elemente citite este: "))
    lst = []
    print("Elementele citite sunt: ")
    for i in range(n):
        ele = int(input())
        lst.append(ele)
    return lst
test_numar_cifre_ord_desc()
test_numere_ordonate_crescator()
def main():
    lst = []
    while True:
        show_menu()
        P = input("Selecteaza numarul problemei: ")
        if(P == '1'):
            lst = citire_date()
        elif(P == '2'):
            print("Secventa maximala de numere ordonate crescator este: ",
                  numere_ordonate_crescator(lst))
        elif(P == '3'):
            print("Secventa maximala care are numere cu cifre ordonate crescator este",
                  numar_cifre_ord_desc(lst))
        elif(P == '4'):
            print("Ati iesit din meniu.")
            break
        else:
            print("Comanda invalida. Reincearca")
main()
