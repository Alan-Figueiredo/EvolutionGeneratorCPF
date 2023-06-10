import random;

cpf = ""
for _ in range(9):
    number = random.randint(0,9);
    cpf += str(number);
cpf = cpf.replace(".","") if "." in cpf else cpf
for x in range(2):
    
    calculo = sum([i * int(valor) for i, valor in enumerate(cpf[::-1],2)]);
    calculo *= 10;
    calculo %= 11;
    calculo = calculo if calculo < 9 else 0;
    cpf += str(calculo);

print(cpf)