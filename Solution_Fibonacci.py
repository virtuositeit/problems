'''
    Fibonacci Sequence

    Write a function to generate the Fibonacci sequence to a specific place without using a loop.

    Example Input:
    5

    Example Output:
    0, 1, 1, 2, 3

'''

from __future__ import print_function
import sys


def generate_fibonacci_sequence(n):
    # return [] when n=0, [0] when n=1, [0, 1] when n=2,
    if n <= 2:
        return range(n)
    # append the next fabonacci number to the returned sequence
    fib = generate_fibonacci_sequence(n - 1)
    fib.append(sum(fib[-2:]))
    return fib


def main():

    while True:
        try:
            n = input('How many Fibonacci numbers would you like to generate? ')
        except:
            print('Please provide a number between 0 and 999 as the amount of Fibonacci numbers to generate!')
            continue
        else:
            break

    fibonacci_nums = generate_fibonacci_sequence(n)
    for num in fibonacci_nums:
        print(num, end=' ')
    print('')


if __name__ == '__main__':
    main()

    '''
    # tests
    # generate fibonacci sequence for the following lengths
    tests = [0, 1, 2, 5, 10, 50, 999]
    print('----- Below are test output -----')
    for n in tests:
        print('n = {}, {}'.format(n, generate_fibonacci_sequence(n)))
    '''
