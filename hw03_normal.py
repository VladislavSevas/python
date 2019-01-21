print('Прудников В.В.')


print('Задание-1')
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n = 1, m = 1):
    n = int(input('введи число'))
    m = int(input('введи число'))
    
    fib = [0,1]
    i=1
    while i != m:
        x = int(fib[i-1]) + int(fib[i])
        fib.append(x)
        i += 1
        
    
    return fib[n:m]
    
print(fibonacci())


print('Задача-2')
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
def sorting(arr):
    print(arr)
    for i in range (len(arr)):
        swap = 0
        for j in range (len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap = 1
                #print(arr)
        if swap == 0:
            return arr
            
   
    
print(sorting([3,1,2,7,6,-1,9,0,1,-3]))

'''
arr = [30-i for i in range(30)]
print(arr)
sorte = False
while not sorte:
    sorte = True
    for i in range(0,len(arr)-1):
        j = len(arr) - i -1
        if arr[i] > arr[i+1]:
            sorte = False
            arr[i], arr[i + 1] = arr[i+1], arr[i]
        if arr[j-1] > arr[j]:
            sorte = False
            arr[j-1], arr[j] = arr[j], arr[j-1]
print(arr)
'''

print('Задача-3')
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filt(arr):
    arr1 = []
    j = 0
    for i in arr:
        if i < 5:
            #print(i) 
            j += 1
        else:
            i >= 5
            arr1.append(i)
            #print(i)
            j += 1
    return(arr1)
print(filt([1,2,3,4,5,6,7,8,-1,-3,8]))

print('Задача-4')
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

A = [1,0]
B = [1,1]
C = [0,1]
D = [0,0]

len1 = [A[0] - D[0], A[1] - D[1]]  #print(len1)
len2 = [B[0] - C[0], B[1] - C[1]]  #print(len2)
len3 = [B[0] - A[0], B[1] - A[1]]  #print(len3)
len4 = [C[0] - D[0], C[1] - D[1]]  #print(len4)

if len1 == len2:
    print('AD || BC')
    if len3 == len4:
        print('AB || CD')
        print('Это параллелограмм')



