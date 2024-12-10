# README

## Projetos de ASA - Testes Públicos e Medição de Desempenho

Este repositório contém os **testes públicos** e os **scripts Python** utilizados para medir a eficiência e a velocidade de projetos desenvolvidos na disciplina **Análise e Síntese de Algoritmos (ASA)** do Instituto Superior Técnico (IST).

### Estrutura do Repositório

- `proj1/`
  - `speed_test.py`
    - Cria testes aleatórios para um determinado intervalo de parametros e executa-os automaticamente.
    - Mede o desempenho (tempo de execução) das implementações submetidas.
    - Produz um gráfico do Tempo(s) em função de uma F(n,m) especificada.

- `proj2/`
  - `tests/`
    - Contém os **testes públicos** fornecidos para validar as soluções dos projetos.
    - Cada teste inclui um ficheiro de entrada (`.in`) e um ficheiro de saída esperado (`.out`). 
  - `speed_test.py`
    - Executa testes automaticamente.
    - Mede o desempenho (tempo de execução) das implementações submetidas.
    - Produz um gráfico do Tempo(s) em função de uma F(n,m,l) especificada.

- `proj3/`
  - Ainda vazio.

### Como Utilizar

#### 1. Executar Testes Públicos

Para validar o seu código utilizando os testes públicos:

1. Certifique-se de que o código compilado tem o nome "projX" e que se encontra ao mesmo nível da pasta "tests/".
2. Execute os testes:

   ```bash
   cd tests
   make
   ```

3. O script irá:
   - Comparar a saída gerada pelo seu programa com a saída esperada.
   - Indicar quais testes passaram ou falharam.

#### 2. Medir Desempenho

Para avaliar a eficiência da sua solução:

1. Certifique-se de que o código compilado tem o nome "projX" e que se encontra ao mesmo nível do script "speed_test.py".
2. Execute o script de medição de desempenho:

   ```bash
   python3 speed_test.py
   ```

3. O script irá:
   - Executar a sua solução com os testes fornecidos.
   - Medir e registar o tempo de execução de cada teste.

### Requisitos

- Python 3.8 ou superior.
- Bibliotecas adicionais estão listadas no ficheiro `requirements.txt`. Para instalá-las, execute:

  ```bash
  pip install -r requirements.txt
  ```
  
### Ficheiro `requirements.txt`

O ficheiro `requirements.txt` inclui as seguintes dependências:

```
matplotlib
numpy
```
