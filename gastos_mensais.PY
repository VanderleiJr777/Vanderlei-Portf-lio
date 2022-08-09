luz = int(input('qual o valor da luz? '))
despesas_fixas = int(input('o que tem pra pagar ainda? '))
salario_mensal = int(input('quanto voce recebe por mes? '))

if (luz + despesas_fixas < salario_mensal):
    print ('restou' + " " + str(salario_mensal - despesas_fixas - luz))
else:
    print ('salario insuficiente' + " " + str (salario_mensal - despesas_fixas - luz))