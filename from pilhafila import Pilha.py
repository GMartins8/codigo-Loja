from pilhafila import Pilha 
from pilhafila import Fila
from pilhafila import TrocarJogo

pilha = Pilha()
fila = Fila()
troca = TrocarJogo(pilha, fila)

while True:
    print("Menu:")
    print("(1) Cadastrar jogo")
    print("(2) Exibir pilha e fila")
    print("(3) Trocar jogo")
    print("(4) Sair")
    print(" ")
  
    opcao = input("Escolha uma opção: ")

    if opcao == "1": 
        nome = input("Digite o nome do jogo : ")
        tipo = input("digite P = pilha ou F = fila: ").upper()
        if tipo not in ['P', 'F']: 
            print("tipo invalido. Use 'P' para Pilha ou 'F' para Fila.") 
            continue
        if tipo == 'P':
            pilha.cadastrar_jogo(nome) 
        else:
            fila.cadastrar_jogo(nome)
          
    elif opcao == "2":
      pilha.visualizar()
      fila.visualizar()

    elif opcao == "3":
        troca.trocar()

          
    elif opcao == "4":
      print ("Encerrando o programa...")
      break

    else:
      print ("Opção inválida!")