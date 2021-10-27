def show_menu():
    print('''1. Citire date.
2. Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sunt palindroame.
3. Determinare cea mai lungă subsecvență cu proprietatea ca numărul de cifre este în ordine descrescătoare.
4. Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sunt neprime.
X. Iesire din meniu
''')

def cifre_ordine_descrescatoare(n):

    '''
    determina daca un numar are cifrele in ordine descrescatoare
    :param n:
    :return:
    '''

    x= n % 10
    n //= 10
    while n > 0:
        if x >= n % 10:
            return False
        x = n % 10
        n //= 10
    return True

def palindrom (n):

    '''
    determina daca un numar este palindrom
    :param n:
    :return:
    '''

    cn = n
    s = 0
    while(n):
        s = s * 10 + n % 10
        n//=10
    if(s == cn):
        return True
    return False

def numar_cifre_ord_desc(lst):

    '''
    determina subsecventa de lungime maximala care are numerele cu cifrele ordonate descrescator
    :param lst:
    :return:
    '''

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

    '''
    determina secventa maximala care are cea mai mare subsecventa de numere palindroame
    :param lst:
    :return:
    '''

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

    '''
    functie care citeste datele de la tastatura
    :return:
    '''

    n = int(input("Numarul de elemente citite este: "))
    lst = []
    print("Elementele citite sunt: ")
    for i in range(n):
        i = str(i)
        ele = int(input("a["+i+"]= " ))
        i = int(i)
        lst.append(ele)
    return lst

def prime(n):

    '''
    determina daca un numar este neprim sau nu
    :param n:
    :return:
    '''

    for d in range(2,n // 2):
        if(n % d == 0):
            return True
    return False

def get_longest_all_not_prime(lst):

    '''
    determina secventa de lungime maximala care are toate numere neprime
    :param lst:
    :return:
    '''

    temp = []
    rez = []
    for i in lst:
        if(prime(i) == True):
            temp.append(i)
        else:
            if(len(temp) > len(rez)):
                rez = temp.copy()
            temp.clear()
        if (len(temp) > len(rez)):
            rez = temp.copy()
    return rez

def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([12, 15, 13, 16, 17]) == [12, 15]
    assert get_longest_all_not_prime([]) == []


test_get_longest_all_palindromes()
test_numar_cifre_ord_desc()
test_get_longest_all_not_prime()

def main():
    lst = []
    while True:
        show_menu()
        P = input("Selecteaza numarul problemei: ")
        if(P == '1'):
            lst = citire_date()
        elif(P == '2'):
            print("Secventa maximala de numere palindroame este:",
                  get_longest_all_palindromes(lst))
        elif(P == '3'):
            print("Secventa maximala care are numere cu cifre ordonate descrescator este:",
                  numar_cifre_ord_desc(lst))
        elif(P == '4'):
            print("Secventa maximala care are numere neprime este:",
                  get_longest_all_not_prime(lst))
        elif(P == 'X'):
            print("Ati iesit din meniu.")
            break
        else:
            print("Comanda invalida. Reincearca")
main()
