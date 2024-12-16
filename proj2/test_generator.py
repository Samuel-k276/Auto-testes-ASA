import math
import subprocess


def generate_tests(n, m, l, b, path):
    with open(path, 'w') as outfile:
        subprocess.run(
            ['./gera', str(n), str(m), str(l), str(b)],  # Arguments for the executable
            stdout=outfile,  # Redirect the output to the file
            stderr=subprocess.PIPE,  # Capture errors (if necessary)
            text=True  # Treat the data as text
        )


for n in range(0, 50):
    print(n)
    generate_tests(50000+(n+1)*5000, 100000+(n+1)*10000, int(100+20*math.log(n+1)), 1, f"tests/test_{n:02d}.in")




