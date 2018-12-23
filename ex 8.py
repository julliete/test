x=open('cadastro.txt','w')

nome=input('digite seu nome: ')
while nome!='':
    sexo=input('digite sexo: ')
    idade=input('digite idade: ')
    x.write(nome+','+sexo+','+idade+'\n')
    nome=input('digite nome: ')
x.close()
x=open('cadastro.txt','r')
print(x.read())
