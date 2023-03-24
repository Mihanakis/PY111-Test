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


massive = ["A", "C", "T", "G"]

lst = []
for n in range(10):
    lst.append(choice(massive) + choice(massive) + choice(massive) + choice(massive))

print(lst)

count, output = [], []
for i in range(4):
    for j in range(len(lst) - 1):
        count.append(lst[j][i])
    str_ = "".join(count)
    c = Counter(str_)
    output.append(list(c.most_common())[0][0])
    count = []

print("".join(output))
