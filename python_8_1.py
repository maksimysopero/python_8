#Логическое программирование/Математические выражения

from kanren import run, var, fact
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative, associative

add = 'add' #определяем математические операции, которые мы собираемся использовать
mul = 'mul'

fact(commutative, mul)
fact(commutative, add) 
fact(associative, mul)
fact(associative, add)

a, b = var('a'), var('b') # переменные
Original_pattern = (mul, (add, 5, a), b) # сравниваем с оригиналом

exp1 = (mul, 2, (add, 3, 1))
exp2 = (add, 5, (mul, 8, 1))

print(run(0, (a,b), eq(Original_pattern, exp1)))
print(run(0, (a,b), eq(Original_pattern, exp2))) # вывод
