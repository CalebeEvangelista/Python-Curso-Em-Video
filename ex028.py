import random
import time

print("O computador vai escolher um número entre 0 e 5, você consegue adivinhar ?")

numUser = input("Tente adivinhar o numero que o PC escolheu: ")
numPc = random.randrange(6)

if numPc != numUser:
    print("PROCESSANDO ...")
    time.sleep(2)
    print("Você errou!")
    time.sleep(1)
    print("O computador escolheu o {}" .format(numPc))
    time.sleep(2)
    print("Tente novamente e boa sorte!")

else :
    print("PROCESSANDO ...")
    time.sleep(2)
    print("Parabens você acertou!")
