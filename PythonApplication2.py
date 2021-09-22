def fill_matrix(m, n, A):
    for i in range(m):
        j = 0
        row = []
        element = 0
        while j < int(n):
            element = input()
            try:
                int(element)
            except ValueError:
                print('Wrong element type.')
            else:
                row.append(int(element))
                j += 1
        A.append(row)
def print_matrix(m, n, A):
    for i in range(m):
       for j in range(n):
          print(A[i][j], end=' ')
       print('')
def insert_integer_element(element):
    j = 0
    element = input()
    while j < 1:
        try:
            int(element)
        except ValueError:
            print('Wrong element type.')
            element = input('Insert new element ')
        else:
            j += 1
            element = int(element)
    return(element)
def sort_matrix(m,n,A):
    c = 0
    k = int(-5)  
    while (k < 0)or(k > m):
        print('Insert k')
        k = insert_integer_element(k) - 1
    for i in range(m):
      for j in range(n - 1):
          if(A[k][j] > A[k][j+1]):
              for i2 in range(m):
                  c = A[i2][j]
                  A[i2][j] = A[i2][j + 1]
                  A[i2][j + 1] = c

A = []
m = n = 0
print('Insert 2 elements - m and n')
m = insert_integer_element(m)
n = insert_integer_element(n)
print('Insert ',m*n,' elements')

fill_matrix(m, n, A)
print("Starting matrix: ")
print_matrix(m, n, A)
sort_matrix(m, n, A)
print("New matrix: ")
print_matrix(m, n, A)