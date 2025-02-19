lst = [1,2,3,4,5,6]
print(lst)

lst[2] = 2 # alterei o valor da posição 2
print(lst)

lst.append(7) # adiciona o 7 ao final da lista
print(lst)

print(f"essa lita tem {len(lst)} elementos") # mostra quando elementos a lista possui

for v in lst:
    print(v)
