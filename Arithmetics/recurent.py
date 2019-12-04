import math
from typing import Tuple

print("program calculates the value of function given in Variant 25")
print("the work of Rozzalovets Maxym, K-10")


def domain(x: float) -> bool:
    """ checks if x value is true, or false"""
    return x >= -3 and x != 4 and x != 10


def f(x: float) -> float:
    """calculates the value of function given in variant25"""
    a1 = (1 / (math.tan(19 / 63)))
    a2 = (((20 * math.e) / (60 * math.pi)) * (9 / ((x - 10) * (x + 11))))
    a3 = (5 * (math.atan(x + 8)))
    a4 = ((12 - (math.sqrt(x + 3))) / (x - 4))
    return a1 + a2 - a3 - a4


def f_total(x: float) -> Tuple[bool, float]:
    """combine function domain and function f"""
    if domain(x):
        return True, f(x)
    else:
        return False, None


if __name__ == '__main__':
    try:
        x = float(input('Enter x value: '))
        print('***** do calculations ... ', end='')
        pointer, result = f_total(x)
        print('done')
        print(f'for x = {x:.6f}')  # prints x with six numbers after point
        if pointer:
            print(f'result = {result:.6f}')
            # prints result of program with six numbers after point
        else:
            print('result = undefined')
    except:
        print('wrong input')
