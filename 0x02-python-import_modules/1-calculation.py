#!/usr/bin/python3
def main():
    import calculator_1
    a = 10
    b = 5
    print('{:d} + {:d} = {:d}'.format(a, b, calculator_1.add(a, b)))
    print('{:d} - {:d} = {:d}'.format(a, b, calculator_1.sub(a, b)))
    print('{:d} * {:d} = {:d}'.format(a, b, calculator_1.mul(a, b)))
    print('{:d} / {:d} = {:.0f}'.format(a, b, calculator_1.div(a, b)))


main()
