import time
def adição(x,y):
    return x+y

def subtração(x,y):
    return x-y

def multiplicação(x,y):
    return x*y

def divisão(x,y):
    return x/y

E=input('Óla, gostaria de efetuar algum cálculo?(sim/não)').lower()

if E=='não' or E=='nao':
     print('Tá bom, talvez outro dia.')

elif E=='sim':
      while True:
         ç=['a','A','b','B','c','C','d','D']
         time.sleep(0.5)
         print('Adição:(a)')
         time.sleep(0.5)
         print('Subtração:(b)')
         time.sleep(0.5)
         print('Multiplicação:(c)')
         time.sleep(0.5)
         print('divisão:(d)')
         time.sleep(0.5)
         O=input('Qual operação você deseja efetuar?').lower()

         if O=='a':
            x=int(input('Digite o primeiro número: '))
            y=int(input('digite o segundo número:'))
            resutado=adição(x,y)
            time.sleep(0.8)
            print(x,'+',y,'=',resutado)

         elif O=='b':
             x=int(input('Digite o primeiro número: '))
             y=int(input('digite o segundo número:'))
             resutado=subtração(x,y)
             time.sleep(0.8)
             print(x,'-',y,'=',resutado)
            
         elif O=='c':
             x=int(input('Digite o primeiro número: '))
             y=int(input('digite o segundo número:'))
             resutado=multiplicação(x,y)
             time.sleep(0.8)
             print(x,'*',y,'=',resutado)

         elif O=='d':
             x=int(input('Digite o primeiro número: '))
             y=int(input('digite o segundo número:'))
             time.sleep(1)
             if y==0:
                 print('Erro, divisões por zero não são possiveis.')
             else:
              time.sleep(0.8)
              resutado=divisão(x,y)
              print(x,'/',y,'=',resutado)

         else:
             O not in ç
             print('Por favor, selecione uma dentre as as opções.(a,b,c,d)')
            
         N=input('Gostaria de executar outro cáculo?(sim/não)').lower()
         if N =='nao' or N=='não':
            print('Ok, até a proxima!')
            break #permite sair do loop while
         elif N=='sim':
             continue
         