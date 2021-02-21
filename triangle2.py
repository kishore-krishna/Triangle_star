def K(n):
    for i in range(n):
        print((n-i-1)*' ', end='')
        print((i+1)*'*')
K(5)