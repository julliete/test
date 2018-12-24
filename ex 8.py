x=open('cadastro.txt','w')

nome=input('NOME: ')
while nome!='':
    sexo=input('SEXO: ')
    idade=input('IDADE: ')
    x.write(nome+','+sexo+','+idade+'\n')
    nome=input('digite nome: ')
x.close()
x=open('cadastro.txt','r')
print(x.read())
