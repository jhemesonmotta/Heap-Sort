def trocar(lista, i, j):                    
    lista[i], lista[j] = lista[j], lista[i]
    return lista

def heapficar(lista, tamanho, i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < tamanho and lista[i] < lista[l]:   
        max = l   
    if r < tamanho and lista[max] < lista[r]:   
        max = r   
    if max != i:   
        lista = trocar(lista, i, max)   
        heapficar(lista, tamanho, max)   

def heap_sort(lista):     
    tamanho = len(lista)   
    inicio = tamanho // 2 - 1 # use // para divisão de inteiros
    for i in range(inicio, -1, -1):   
        heapficar(lista, tamanho, i)   
    for i in range(tamanho-1, 0, -1):   
        trocar(lista, i, 0)   
        heapficar(lista, i, 0)

arrei = [2, 7, 1, -2, 56, 5, 3]
heap_sort(arrei)
print(arrei)
