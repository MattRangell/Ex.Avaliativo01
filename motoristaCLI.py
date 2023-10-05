import motorista as motorista;
import passageiro as passageiro
import corrida as corrida

class MotoristaCLI:
    def __init__(self):
        self.passageiro = None
        self.corrida = None
        self.motorista = None

    def create(self):
        nome_passageiro = input("Digite o nome do passageiro: ")
        documento_passageiro = input("Documento do passageiro")
        self.passageiro = Passageiro(nome_passageiro,documento_passageiro)

        distancia_corrida = input("Digite a distancia da corrida: ")
        valor_corrida = input("Digite o valor da corrida: ")
        passageiro_corrida = Passageiro
        self.corrida = Corrida(distancia_corrida, valor_corrida,passageiro_corrida)

        nota_motorista = input("Digite a nota do motorista: ")
        corridas_motorista = Corrida
        self.motorista = Motorista(nota_motorista, corridas_motorista)

    def read(self):
        print("Passageiro:")
        print("Nome:", self.passageiro.nome)
        print("Corrida:")
        print("Distancia:", self.corrida.distancia_corrida)
        print("Valor:", self.corrida.valor_corrida)
        print("Motorista:")
        print("Nota:", self.motorista.nota_motorista)
        

    def update(self):
        if self.passageiro is None:
            print("Nenhum passageiro encontrado.")
            return

        new_nome_passageiro = input("Digite o novo nome do passageiro: ")
        self.passageiro.nome = new_nome_passageiro

        if self.corrida is None:
            print("Nenhuma corrida encontrada.")
            return

        if self.motorista is None:
            print("Nenhum motorista encontrado.")
            return

        new_nome_motorista = input("Digite o novo nome do motorista: ")
        new_carro_motorista = input("Digite o novo carro do motorista: ")
        self.motorista.nome = new_nome_motorista
        self.motorista.carro = new_carro_motorista

    def delete(self):
        self.passageiro = None
        self.corrida = None
        self.motorista = None

    def menu(self):
        while True:
            print("\n---- Menu ----")
            print("1. Create")
            print("2. Read")
            print("3. Update")
            print("4. Delete")
            print("5. Exit")

            choice = input("Digite a sua escolha: ")

            if choice == "1":
                self.create()
            elif choice == "2":
                self.read()
            elif choice == "3":
                self.update()
            elif choice == "4":
                self.delete()
            elif choice == "5":
                break
            else:
                print("Escolha inválida. Tente novamente.")