# import time

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def get_circular_primes(start, end):
    circular_primes = []
    
    for num in range(start, end + 1):
        str_num = str(num)
        is_circular_prime = True
        
        for _ in range(len(str_num)):
            if not is_prime(num):
                is_circular_prime = False
                break
            
            str_num = str_num[1:] + str_num[0]
            num = int(str_num)
        
        if is_circular_prime:
            circular_primes.append(num)
    
    return circular_primes


# Marca o tempo inicial
# start_time = time.time()

entrada = input()
values = entrada.split()

start = int(values[0])
end = int(values[1])

primes = get_circular_primes(start, end)
sum_of_primes = sum(primes)
if (primes):
    print(*primes, sep=' ')
    print("Segredo=", sum_of_primes)
else:
    print("O segredo nao foi identificado!")


# Marca o tempo final
# end_time = time.time()

# Calcula o tempo decorrido
# elapsed_time = end_time - start_time

# print(f"Tempo decorrido: {elapsed_time} segundos")