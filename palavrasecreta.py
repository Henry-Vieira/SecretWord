import os 

palavrasecreta = 'python'

letra_acertada = ''

numero_tentativas = 0

start = True

while start:
  letra_digitada = input("Digite uma letra: ")
  numero_tentativas += 1

  if len(letra_digitada) > 1:
    print("Digite uma só letra")
    continue
  
  if letra_digitada in palavrasecreta:
    letra_acertada += letra_digitada

  palavraformada = ''
  for letra_secreta in palavrasecreta:
    if letra_secreta in letra_acertada:
      palavraformada += letra_secreta
    
    else:
      palavraformada += '*'
  
  print("Palavra formada:",palavraformada)
  
  if palavraformada == palavrasecreta:
    os.system('cls')
    print("VOCÊ É O VENCEDOR!!!")
    print("Número de tentativas:", numero_tentativas)
 