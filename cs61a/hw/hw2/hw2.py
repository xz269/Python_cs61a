# Name:Xieqi

def square(x):
    """Return x squared."""
    return x * x

# Q1.

def product(n, term):
    """Return the product of the first n terms in a sequence.

    term -- a function that takes one argument

    >>> product(4, square)
    576
    """
    "*** YOUR CODE HERE ***"
    total = 1
    while n > 1:
        total = total * n 
        n = n - 1 
    return square(total)

def factorial(n):
    """Return n factorial for n >= 0 by calling product.

    >>> factorial(4)
    24
    """
    "*** YOUR CODE HERE ***"
    total = 1
    while n >= 1:
        total = total * n 
        n = n - 1 
    return total 

# Q2.

def accumulate(combiner, start, n, term):
    """Return the result of combining the first n terms in a sequence."""
    "*** YOUR CODE HERE ***"
    total = start
    for i in range (start, n + 1):
        total = combiner(total, term(i))
    return total

def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate.

    >>> summation_using_accumulate(4, square)
    30
    """
    "*** YOUR CODE HERE ***"
    def summation(x, y):
            return x + y
    return accumulate(summation, 0, n, term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    """
    "*** YOUR CODE HERE ***"
    def product(x, y):
        return x * y
    return accumulate(product,1, n, term)
# Q3.

def double(f):
    """Return a function that applies f twice.

    f -- a function that takes one argument

    >>> double(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    return lambda x: f(f(x))

# Q4.

def repeated(f, n):
    """Return the function that computes the nth application of f.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    >>> repeated(square, 4)(5)
    152587890625
    """
    "*** YOUR CODE HERE ***"
    def nth_repeated(x):
        for i in range (0, n):
            x = f(x)
        return x
    return nth_repeated

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h


