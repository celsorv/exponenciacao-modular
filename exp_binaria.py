import time

def modular_exponentiation(a, b, n):
    """
    Calcula a^b mod n usando exponenciação binária.
    
    :param a: Base
    :param b: Expoente
    :param n: Módulo
    :return: a^b mod n
    """
    result = 1
    base = a % n
    
    while b > 0:
        if b % 2 == 1:  # Se b é ímpar
            result = (result * base) % n
        base = (base * base) % n  # Quadrado da base
        b = b // 2  # Dividir b por 2 (deslocamento à direita no binário)
    
    return result

# Medição do tempo
start_time = time.time()

a = 3
b = 102458749
n = 7
result = modular_exponentiation(a, b, n)

end_time = time.time()
print(f"\n{a}^{b} mod {n} = {result}")
print(f"Tempo de execução: {end_time - start_time:.6f} segundos\n")

# Output on a Core i7-3930K CPU @ 3.20GHz
# Execution time: 0.000000 seconds
