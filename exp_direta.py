import time

def direct_modular_exponentiation(a, b, n):
    """
    Calcula a^b mod n usando uma abordagem direta.
    
    :param a: Base
    :param b: Expoente
    :param n: Módulo
    :return: a^b mod n
    """
    result = 1
    for _ in range(b):
        result = (result * a) % n
    return result

# Medição do tempo
start_time = time.time()

a = 3
b = 102458749
n = 7
result = direct_modular_exponentiation(a, b, n)

end_time = time.time()
print(f"\n{a}^{b} mod {n} = {result}")
print(f"Tempo de execução: {end_time - start_time:.6f} segundos\n")

# Output on a Core i7-3930K CPU @ 3.20GHz
# Execution time: 8.615234 seconds
