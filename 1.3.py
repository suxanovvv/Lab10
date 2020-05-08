#3. Сформувати функцію для обчислення індексу максимального елемента масиву
#n*n, де 1<=n<=5.

import numpy as np
import random

while True:
    #Задання розміру масиву та його ініціалізація.
    n=int(input('Введіть розмірність масиву від 1 до 5!: '))
    
    if n>5 or n<0:
        print('Виберіть розмірність від 1 до 5!')
        break
    else:
           A=np.zeros((n,n), dtype=int)
           
    for i in range(len(A)):
        for j in range(len(A)):
            A[i,j]=random.randint(-5,10)
    print(A)

    #Ітераційний розв'язок задачі.
    def max_el(f):
        max_elem = f[0][0]
        for i in range(len(f)):
            for j in range(len(f[i])):
                 if f[i][j] > max_elem:
                       max_elem=f[i][j]

        #Знаходження індексу максимального рядка (його стовпчик та рядок).
        list_index_max =[(i,j) for i in range(len(f))  for j in range(len(f[i])) if f[i][j]  == max_elem]
        line, column = list_index_max[0]

        return line, column
    
    print('Максимальний елемент під індексом: ', max_el(A))


    #Рекурсивний розв'язок задачі.
    def max_el_rec(array, count=0, temp=0, i=0, j=0):
        if temp==len(array[count]):
            count+=1
            temp=0
        if count==len(array):
            return i, j
        if array[count][temp]>array[i][j]:
            i=count
            j=temp
        temp+=1
        return max_el_rec(array, count, temp, i, j)

    print('Максимальний елемент під індексом: ', max_el_rec(A))
    
    #Чи бажаєте запустити програму заново?
    result=input('Input "1" to continue, and other to exit: ')
    if result=='1':
        continue
    break

#У цій задачі краще використовувати рекурсивний метод розв'язку.
#Він займає менше часу та вимагає менше перевірок і порівнянь.

