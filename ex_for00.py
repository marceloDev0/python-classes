#programa de contagem regressiva para o estouro de fogos, indo de 10 ate 0, com pausa de 1 segundo entres eles
from time import sleep
import emoji
for c in range(10, -1, -1):
    
    print(c)
    sleep(1)
print(emoji.emojize(":collision: :firecracker:"))