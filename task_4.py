"""При чтении DNA последовательностей могут возникать единичные ошибки, выражающиеся в неверной букве в строке.
Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка, в которой на
каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно во всех чтениях. Т.е. для строк
ATTA
ACTA
AGCA
ACAA
консенсус-строка будет ACTA (в первой ячейке чаще всего встречалась A, во второй – C, в третьей – Т,
в четвертой – снова А). Для входного списка из N строк одинаковой длины построить консенсус-строку.
В случае одинаковой позиционной частоты, то выбрать ту, что меньше лексиграфически."""

from random import choice
from collections import Counter
from random import randint


massive = ["A", "C", "T", "G"]

lst = []
for n in range(randint(5, 15)):
    lst.append("".join([choice(massive) for m in range(4)]))

print(lst)

count, output = [], []
for i in range(len(lst[0])):
    for j in range(len(lst)):
        count.append(lst[j][i])
    str_ = "".join(count)
    c = Counter(str_)
    output.append(list(c.most_common())[0][0])
    count = []

print("".join(output))
