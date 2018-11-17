from math import sqrt


def quadratic(a=0, b=0, c=0):

    discriminant = (b**2) - (4 * a * c)

    if discriminant < 0:
        raise ValueError('Discriminant is less than 0')

    pos_root = (-b + sqrt(discriminant))/(2 * a)
    neg_root = -(-b + sqrt(discriminant))/(2 * a)

    roots = (pos_root, neg_root)

    return roots


try:
    a = float(input('Enter "a" value: '))
    b = float(input('Enter "b" value: '))
    c = float(input('Enter "c" value: '))
    print(quadratic(a, b, c))

except TypeError as err:
    print(err)
    print(quadratic(a, b, c))
except ValueError as err:
    print(err)
    print(quadratic(a, b, c))
except:
    print('Wtf did you do?')