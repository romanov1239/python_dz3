# ; Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# ; Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# ;  В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input("Введите размер массива: "))  
arr = []  
for i in range(n):
    num = int(input(f"Введите {i+1}-е число: "))
    arr.append(num)
x = int(input("Введите искомое число: "))  
print("Массив: ", arr)
bliz = arr[0] 
diff = abs(bliz-x) 
for i in range(1, n): 
    if abs(arr[i] - x) < diff: 
        bliz = arr[i] 
diff = abs(arr[i] - x)
print("Самое близкое число: ",bliz) 