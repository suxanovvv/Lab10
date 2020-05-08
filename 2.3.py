#3. Сформувати функцію для переведення натурального числа з десяткової системи
#числення у шістнадцятирічну.

x=int(input('Введіть число, яке бажаєте перевести у 16-річну СЧ: '))

#Ітераційний розв'зок задачі.
def dec_to_base_it(N, chyslennya):
    if not hasattr(dec_to_base_it, 'table'):        
        dec_to_base_it.table = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'       
    n = N    
    r = []
    while n:
        x, y = divmod(n, chyslennya) 
        r.append(dec_to_base_it.table[y])
        n = x
    return ''.join(reversed(r))

print(dec_to_base_it(x, 16))


y=int(input('Введіть число, яке бажаєте перевести у 16-річну СЧ: '))

#Рекурсивний розв'язок задачі.
def dec_to_base_rec(N, chyslennya):
    if not hasattr(dec_to_base_rec, 'table'):        
        dec_to_base_rec.table = '0123456789ABCDEF'       
    x, y = divmod(N, chyslennya)        
    return dec_to_base_rec(x, chyslennya) + dec_to_base_rec.table[y] if x else dec_to_base_rec.table[y]
 
print(dec_to_base_rec(y, 16))


#Ітераційний розв'зок у даній задачі кращий, так як у ньому використовується
#менша кількість порівнянь.
