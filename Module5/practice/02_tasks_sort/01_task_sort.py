import random

def quick_sort(data, lindex, rindex):
    count = 0
    i = lindex
    j = rindex
    p = (lindex + rindex) // 2
    while True:
        while data[i] < data[p]:
            i += 1
        while data[j] > data[p]:
            j -= 1
        if i <= j:
            if i < j:
                if p == i:
                    p = j
                elif p == j:
                    p = i
                l[i], l[j] = l[j], l[i]
                count += 1
            i += 1
            j -= 1
        if i > j:
            break
    if j > lindex:
        count += quick_sort(data, lindex, j)
    if i < rindex:
        count += quick_sort(data, i, rindex)
    return count

def binary_search(l, value, lindex=-1, rindex=-1):
    if lindex == -1:
        lindex = 0
    if rindex == -1:
        rindex = len(l) - 1
    while lindex < rindex:
        index = (lindex + rindex) // 2
        if l[index] < value:
            lindex = index + 1
        elif l[index] > value:
            rindex = index - 1
        else:
            return index
    return -1

# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    return [random.randint(at, to) for _ in range(size)]

l = gen_list(1000, -1000, 1000)
# print(l)
# print("count:", quick_sort(l, 0, len(l) - 1))
# print(l)
quick_sort(l, 0, len(l) - 1)
# index = binary_search(l, 10)
# print(l)
# print(index, ":", l[index])
a = 100
index = len(l) - 1
sum = 0
while index >= 0:
    sum += l[index]
    index -= 1
    if l[index] < a:
        break

print(sum)
