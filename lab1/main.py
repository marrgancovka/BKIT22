import sys
import math


def check_input():
    while True:
        coef = input()
        try:
            coef=float(coef)
            return coef
        except ValueError:
            print("Введены некорректные данные. Введите заново.")

def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
        coef = float(coef_str)
    except IndexError:
        print(prompt)
        coef = check_input()
    except ValueError:
        print("Значения командной строки некорректны.")
        print(prompt)
        coef = check_input()

    return coef

def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c

    if D == 0.0:
        root0 = -b / (2.0 * a)
        if root0==0 :
            result.append(root0)
        elif root0>0:
            root1=math.sqrt(root0)
            root2= -1* math.sqrt(root0)
            result.append(root1)
            result.append(root2)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root01 = (-b + sqD) / (2.0 * a)
        root02 = (-b - sqD) / (2.0 * a)
        if root01==0 :
            result.append(root01)
        if root02==0:
            result.append(root02)
        if root01>0:
            root1 = math.sqrt(root01)
            root11 = -1*math.sqrt(root01)
            result.append(root1)
            result.append(root11)
        if root02>0 :
            root2 = math.sqrt(root02)
            root22 = -1 * math.sqrt(root02)
            result.append(root2)
            result.append(root22)
    return result

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    while a==0:
        print("При таком а уравнение не является биквадратным")
        a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a, b, c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))

if __name__ == "__main__":
    main()