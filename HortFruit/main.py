import time

print("Bem vindo ao nosso Hortifruit, iremos prosseguir com seu atendimento em instantes!")
time.sleep(1)

class Client:
    def __init__(self):
        self.name = ""
        self.cpf = ""

    def get_Info(self):
        print(f"Nome: {self.name}, CPF: {self.cpf}")

p = Client()
p.name = input("Insira seu Nome: ")
p.cpf = int(input("Insira seu CPF: "))
p.get_Info()
print(f"Olá {p.name}, iremos redirecionalo para o catálogo.")
time.sleep(1)
Frutas = {
    "1": {"nome": "Banana", "preço": 3.60},
    "2": {"nome": "Maçã", "preço": 2.50},
    "3": {"nome": "Pera", "preço": 3.00},
    "4": {"nome": "Melancia", "preço": 4.00},
    "5": {"nome": "Uva", "preço": 5.50},
    "6": {"nome": "Laranja", "preço": 2.20},
    "7": {"nome": "Limão", "preço": 1.80},
    "8": {"nome": "Abacaxi", "preço": 6.00},
    "9": {"nome": "Manga", "preço": 3.90},
    "10": {"nome": "Kiwi", "preço": 4.50},
    "11": {"nome": "Mamão", "preço": 3.70},
    "12": {"nome": "Morango", "preço": 7.50},
    "13": {"nome": "Coco", "preço": 5.00},
    "14": {"nome": "Goiaba", "preço": 2.80},
    "15": {"nome": "Caqui", "preço": 3.40}
}

def frutas_estoque():
    print("\nFRUTAS")
    for cod, produto in Frutas.items():
        print(f"{cod}. {produto['nome']} - R${produto['preço']:.2f}")
        
carrinho = []
def mostrar_carrinho():
    if not carrinho:
        print("\nSeu carrinho está vazio.")
        return
    print("\n----- CARRINHO -----")
    total = 0
    for item in carrinho:
        subtotal = item['preço'] * item['quantidade']
        total += subtotal
        print(f"{item['nome']} x{item['quantidade']} - R${subtotal:.2f}")
    print(f"Total: R${total:.2f}")

while True:
    frutas_estoque()
    cod = input("Digite o código da fruta que deseja comprar (ou 0 para finalizar): ")

    if cod == "0":
        break

    if cod in Frutas:
        try:
            quantidade = int(input(f"Quantas unidades de {Frutas[cod]['nome']}? "))
            if quantidade <= 0:
                print("Quantidade inválida.")
                continue
            item = {
                "nome": Frutas[cod]['nome'],
                "preço": Frutas[cod]['preço'],
                "quantidade": quantidade
            }
            carrinho.append(item)
            print(f"{quantidade} x {item['nome']} adicionado ao carrinho!")
        except ValueError:
            print("Por favor, insira uma quantidade válida.")
    else:
        print("Código inválido. Tente novamente.")
print("\nCompra finalizada!")
mostrar_carrinho()
print("Prossiga para finalizar sua compra.")
time.sleep(2)
total_compra = sum(item['preço'] * item['quantidade'] for item in carrinho)
print("\n=== PAGAMENTO ===")
print('''Formas de pagamento:
[ 1 ] À vista dinheiro/cheque (10% de desconto)
[ 2 ] À vista no cartão (5% de desconto)
[ 3 ] 2x no cartão (sem juros)
[ 4 ] 3x ou mais no cartão (20% de juros)''')

while True:
    pagamento = int(input("Informe a forma de pagamento: "))
    if pagamento == 1:
        total = total_compra - (total_compra * 10 / 100)
        break
    elif pagamento == 2:
        total = total_compra - (total_compra * 5 / 100)
        break
    elif pagamento == 3:
        total = total_compra
        parcela = total / 2
        print(f"Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.")
        break
    elif pagamento == 4:
        total = total_compra + (total_compra * 20 / 100)
        totalparc = int(input("Quantas parcelas? "))
        parcela = total / totalparc
        print(f"Sua compra será parcelada em {totalparc}x de R${parcela:.2f} COM JUROS.")
        break
    else:
        total = total_compra
        print("OPÇÃO DE PAGAMENTO INVÁLIDA. Insira a opção corretamente.")
        continue
    
time.sleep(2)
print(f"Sua compra de R${total_compra:.2f} vai custar R${total:.2f} no final.")
print("Obrigado por comprar conosco! Volte sempre 🌱🍎")