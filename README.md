# Algoritmos de Exponenciação Modular

Este repositório contém implementações em Python para dois algoritmos de exponenciação modular:

1. **Exponenciação Binária (ou Rápida)**
2. **Abordagem Direta**

Ambos os algoritmos são usados para calcular ``a^b mod n``, mas diferem em eficiência.

## Algoritmos

### 1. Exponenciação Binária

A exponenciação binária é um método eficiente para calcular ``a^b mod n``. Este método usa a representação binária do expoente para reduzir o número de multiplicações necessárias. Em vez de realizar _b_ multiplicações, a exponenciação binária reduz o número de operações para aproximadamente _log_2(b)_, o que é muito mais eficiente para expoentes grandes.

#### Complexidade

- **Tempo**: ``O(log b)``
- **Espaço**: ``O(1)`` (além das variáveis utilizadas)

#### Vantagens

- Reduz significativamente o número de multiplicações comparado com métodos diretos.
- É amplamente utilizado em criptografia e outras aplicações matemáticas que envolvem expoentes grandes.

### 2. Abordagem Direta

A abordagem direta para a exponenciação modular é a forma mais simples de calcular ``a^b mod n``. Ela envolve realizar _b_ multiplicações e operações de módulo. Embora seja direta e fácil de implementar, é menos eficiente para expoentes grandes devido à sua complexidade linear.

#### Complexidade

- **Tempo**: ``O(b)``
- **Espaço**: ``O(1)`` (além das variáveis utilizadas)

#### Desvantagens

- Para valores grandes de _b_, o tempo de execução pode ser muito alto.
- Não é prático para aplicações que requerem cálculos rápidos com expoentes grandes.

## Comparação de Desempenho

A comparação entre os dois algoritmos demonstra que a exponenciação binária é muito mais eficiente para expoentes grandes. A abordagem direta pode ser útil para expoentes pequenos ou em contextos onde a simplicidade é mais importante que a eficiência.

### Medição de Tempo

Os códigos fornecidos medem o tempo necessário para calcular ``a^b mod n`` usando ambos os métodos. Para expoentes grandes, a diferença no tempo de execução entre a exponenciação binária e a abordagem direta pode ser bastante significativa.

## Como Usar

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/celsorv/exponenciacao-modular.git
   ```

2. **Navegue até o Diretório do Repositório:**
    ```bash
    cd exponenciacao-modular
    ```

3. **Execute os Scripts Python:**
    - Para a exponenciação binária:
        ```bash
        python exp_binaria.py
        ```
    - Para a abordagem direta:
        ```bash
        python exp_direta.py
        ```


