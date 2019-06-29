from sympy.solvers import solve
from sympy import Symbol
from sympy import Eq

x = Symbol('x')
y = Symbol('y')
result = solve(Eq(7*x-5*y, 3), x, y)
print(result)

print(5*(3/5))