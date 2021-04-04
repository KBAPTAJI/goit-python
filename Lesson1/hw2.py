first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))
if first < second:
    number = first
else:
    number = second
nod = 100
a = number / nod
while not a % 2:
    nod -= 1
    continue
    print(nod)
    if nod > 10:
        break
print(nod)
