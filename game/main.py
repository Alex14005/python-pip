import random


round=1
computer_wins=0
user_wins=0
while True:

  
  print("*"*12)
  print("ROUND ", round)
  print("*"*12)
  options = ("piedra", "papel", "tijera")
  
  user_option = input("elige piedra, papel o tijera =>")
  user_option = user_option.lower()
  computer_option = random.choice(options)
  if not user_option in options:
    print("Hechale ganas, escoge bien...")
    continue
  print("Tu elegiste =>" + user_option)
  print("Computadora eligió =>" + computer_option)
  
  
  if user_option == computer_option:
    print("Empate!")
  
  elif user_option == "piedra":
    if computer_option == "papel":
      print("papel gana a piedra...")
      print("computadora ganó!")
      computer_wins +=1
    elif computer_option == "tijera":
      print("piedra gana a tijera...")
      print("usuario ganó!")
      user_wins +=1
  
  elif user_option == "papel":
    if computer_option == "piedra":
      print("papel gana a piedra...")
      print("usuario ganó!")
      user_wins +=1
    elif computer_option == "tijera":
      print("tijera gana a papel...")
      print("computadora ganó!")
      computer_wins +=1
  
  elif user_option == "tijera":
    if computer_option == "papel":
      print("tijera gana a papel...")
      print("usuario ganó!")
      user_wins +=1
    elif computer_option == "piedra":
      print("piedra gana a tijera...")
      print("computadora ganó!")
      computer_wins +=1

  print("COMPUTADORA: ", computer_wins)
  print("USUARIO: ", user_wins)
  if computer_wins >= 2:
    print("COMPUTADORA GANÓ LA PARTIDA!")
    print("SIGUE INTENTANDO")
    break

  if user_wins >= 2:
    print("USUARIO GANO LA PARTIDA!!!")
    print("EXCELENTE HAS GANADO")
    break
  round += 1
  if user_wins >= 2 or computer_wins >= 2:
    resp = input("¿Quieres reiniciar el juego?")
    if resp == 'si':
      print('Reinicio de juego')
    else:
      print('Hasta luego')
    