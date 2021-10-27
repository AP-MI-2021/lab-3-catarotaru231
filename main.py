def show_menu():
    print('''1. Citire date.
2. Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sunt palindroame.
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

def palindrom (n):
    cn = n
    s = 0
    while(n):
        s = s * 10 + n % 10
        n//=10
    if(s == cn):
        return True
    return False

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
    assert numar_cifre_ord_desc([11, 21, 31]) == [21, 31]
    assert numar_cifre_ord_desc([331, 321, 54231]) == [321]
    assert numar_cifre_ord_desc([10, 541, 2050, 101]) == [10, 541]

def get_longest_all_palindromes(lst):
    temp = []
    rez = []
    for i in lst:
        if(palindrom(i)):
            temp.append(i)
        else:
            if(len(temp)>len(rez)):
                rez = temp.copy()
            temp.clear()
        if(len(temp) > len(rez)):
            rez = temp.copy()
    return rez



def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([]) == []
    assert get_longest_all_palindromes([11, 22, 33, 121]) == [11, 22, 33, 121]
    assert get_longest_all_palindromes([10, 102, 204, 506]) == []
    assert get_longest_all_palindromes([11, 505, 304, 123450, 16]) == [11, 505]

def citire_date():
    n = int(input("Numarul de elemente citite este: "))
    lst = []
    print("Elementele citite sunt: ")
    for i in range(n):
        i = str(i)
        ele = int(input("a["+i+"]= " ))
        i = int(i)
        lst.append(ele)
    return lst
test_get_longest_all_palindromes()
test_numar_cifre_ord_desc()
def main():
    lst = []
    while True:
        show_menu()
        P = input("Selecteaza numarul problemei: ")
        if(P == '1'):
            lst = citire_date()
        elif(P == '2'):
            print("Secventa maximala de numere palindroame este: ",
                  get_longest_all_palindromes(lst))
        elif(P == '3'):
            print("Secventa maximala care are numere cu cifre ordonate descrescator este",
                  numar_cifre_ord_desc(lst))
        elif(P == '4'):
            print("Ati iesit din meniu.")
            break
        else:
            print("Comanda invalida. Reincearca")
main()
