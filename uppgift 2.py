"""Uppgift 2.
Denna fil börjar med två funktioner. Du ska under uppgiften använda dessa för olika saker."""

def f(x):
    return (x**3+1)/(x**2-1)

def g(x):
    if x>2:
        return 2*x
    else:
        return 4

def k_värde(funktion, x1, x2):
    return (funktion(x2)-funktion(x1))/(x2-x1)

h=0.0000001
a=-1
print(f'f({a+h})={f(a+h)}, f({a-h})={f(a-h)}')

