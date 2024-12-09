import time
import subprocess
import matplotlib.pyplot as plt
import numpy as np

# Caminho para o executável a ser testado
executavel = "./proj2"


# Dicionários para guardar tempos de execução
tempos = []

big_o = []

# Testes de velocidade na pasta tests
for i in range(200):
   with open(f"tests/test_{i:02d}.in", "r") as f:
      linha = f.readline()
      linha = linha.split()
      n = int(linha[0])
      m = int(linha[1])
      l = int(linha[2])
      big_o.append((n+m)*l)

      f.close()

   # Mede o tempo antes da execução
   inicio = time.time()
    
   # Executa o programa com o input do ficheiro
   with open(f"tests/test_{i:02d}.in", "r") as entrada:
      subprocess.run([executavel], stdin=entrada, stdout=subprocess.DEVNULL)
    
   # Mede o tempo após a execução
   fim = time.time()

   # Calcula o tempo total
   tempo_execucao = fim - inicio
   tempos.append(tempo_execucao)

   print(f"Teste {i:02d} concluído. Tempo de execução: {tempo_execucao:.4f} segundos")
   

# Plota os pontos de dados originais
plt.scatter(big_o, tempos, label="Dados experimentais", alpha=0.5, color="blue")

# Ajusta uma curva polinomial de tendência para todos os dados combinados
degree = 2  # Ajusta o grau conforme necessário
coef = np.polyfit(big_o, tempos, degree)
poly_fn = np.poly1d(coef)

# Plota a curva de ajuste
sorted_nm_values = sorted(big_o)  # Ordena para uma curva suave
plt.plot(sorted_nm_values, poly_fn(sorted_nm_values), '--', label="Tendência global", color="red")

plt.xlabel("f(n,m,l) = (n + m)*l")
plt.ylabel("Tempo de execução (segundos)")
plt.title("Curva de tendência para tempo de execução em função de f(n,m,l)")
plt.legend()
plt.show()