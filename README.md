# Auto-testes-ASA

Este repositório tem apenas um ficheiro .py que produz o gráfico do T(f(n,m)) em funçao de f(n,m)

Cria um teste random em funcao de n e m
Mede o tempo que o executável demora a passar esse teste
Junta os dados todos
Produz um gráfico com a curva que melhor se aproxima

A funcao f(n,m) (i.e. nm^2) pode ser alterada na variável f_n_m (vem por default nm)
Atençao tambem ao caminho que indicam na variável "executavel" para o .py encontrar o vosso código, que deve estar compilado num exuctavel
O .py testa para n ∈ [5, 100] e m ∈ [10, 1000]
Cuidado que a primeira soluçao a que chegam provavelmente nao deverá ser testada para valores tao altos
Estes valores podem e devem ser alterados manualmente
O .py tambem cria um "test.in" para armazenar temporariamente os testes random que cria
