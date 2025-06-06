import time
def area(altura, largura):
    return altura*largura

while True:
 
 print('Triângulo:(1)')
 print('Quadrado:(2)')
 time.sleep(0.5)
 F=input('Qual a forma geometrica você deseja saber a area?')

 if F=='1':
    time.sleep(0.5)
    M=input('Em que unidade de medida você que medir seu triângulo(cm/m)')

    if M=='cm' or M=='centimetros':  
     time.sleep(0.5)
     altura=int(input('Digite a Altura do Triângulo(em cm):'))
     time.sleep(0.5)
     largura=int(input('Digite a largura do Triângulo(em cm):'))
     time.sleep(1)
     resultado=((altura*largura)/2)
     print(int(resultado),'cm² Ou', int(resultado)/100,'m²')
    
    elif M=='m' or M=='metros':      
           time.sleep(0.5)
           altura=int(input('Digite a Altura do Triângulo(em m):'))
           time.sleep(0.5)
           largura=int(input('Digite a largura do Triângulo(em m):'))
           time.sleep(1)
           resultado=((altura*largura)/2)
           print(int(resultado),'m²')

 if F=='2':
    time.sleep(0.5)
    M=input('Em que unidade de medida você que medir seu Quadrado(cm/m)')

    if M=='cm' or M=='centimetros': 
      time.sleep(0.5)
      altura=int(input('Digite a Altura do Quadrado(em cm):'))
      time.sleep(0.5)
      largura=int(input('Digite a largura do Quadrado(em cm):'))
      time.sleep(1)
      resultado=((altura*largura))
      print(int(resultado),'cm² Ou',int(resultado)/100,'m²')
    
    elif M=='m' or M=='metros':  
           time.sleep(0.5) 
           altura=int(input('Digite a Altura do Triângulo(em m):'))
           time.sleep(0.5)
           largura=int(input('Digite a largura do Triângulo(em m):'))
           time.sleep(1)
           resultado=((altura*largura))
           print(int(resultado),'m²')
