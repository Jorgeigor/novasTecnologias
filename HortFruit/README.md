# 🛒 Hortifruit - Sistema Simples de Vendas em Python

Este é um projeto básico de terminal que simula um sistema de vendas para uma frutaria, o *Hortifruit*. Ele permite ao cliente informar seus dados, visualizar um catálogo de frutas, adicionar produtos ao carrinho, e finalizar a compra com opções de pagamento.

---

## 🧠 O que esse programa faz?

1. Dá boas-vindas ao cliente com uma breve mensagem.
2. Coleta nome e CPF do cliente.
3. Mostra um catálogo de frutas disponíveis com preços.
4. Permite ao cliente selecionar frutas e quantidades, que são adicionadas ao carrinho.
5. Mostra o carrinho com o total da compra.
6. Finaliza a compra com uma opção de pagamento:
   - à vista com desconto,
   - parcelado sem juros,
   - ou parcelado com juros.

---

## 📄 Estrutura do Código

### 1. **Boas-vindas e cadastro do cliente**
```python
class Client:
    ...
```
Cria uma classe para armazenar os dados do cliente. Logo após, ele insere nome e CPF, e é redirecionado ao catálogo.

---

### 2. **Catálogo de frutas**
```python
Frutas = {
    "1": {"nome": "Banana", "preço": 3.60},
    ...
}
```
Um dicionário com 15 frutas, cada uma com seu nome e preço por unidade. É exibido toda vez que o cliente for escolher produtos.

---

### 3. **Carrinho de compras**
```python
carrinho = []
```
O cliente escolhe os produtos pelo código e informa a quantidade. Os itens são salvos no carrinho como um dicionário com `nome`, `preço` e `quantidade`.

---

### 4. **Visualização do carrinho**
```python
mostrar_carrinho()
```
Mostra todos os produtos adicionados ao carrinho, com o valor parcial de cada um e o total da compra.

---

### 5. **Pagamento**
```python
print('''Formas de pagamento:
[ 1 ] À vista dinheiro/cheque (10% de desconto)
[ 2 ] À vista no cartão (5% de desconto)
[ 3 ] 2x no cartão (sem juros)
[ 4 ] 3x ou mais no cartão (20% de juros)''')
```
O cliente escolhe a forma de pagamento e o sistema calcula o valor final com base na opção:

- **Opção 1**: 10% de desconto;
- **Opção 2**: 5% de desconto;
- **Opção 3**: valor dividido em 2x;
- **Opção 4**: acréscimo de 20% com número de parcelas personalizado.

O programa então mostra o valor final e agradece pela compra.

---

## 💡 Por que esse código é legal?

- É simples e direto ao ponto.
- Serve como uma ótima introdução à programação com Python.
- Trabalha com conceitos como classes, dicionários, listas, laços de repetição e condicionais.
- Pode ser facilmente expandido com mais produtos, categorias, cadastro em arquivo e muito mais.

---

## 🔧 Possíveis melhorias futuras

- Salvar dados do cliente e compras em arquivo.
- Adicionar mais categorias de produtos (legumes, verduras).
- Criar um menu de navegação com mais opções.
- Interface gráfica com Tkinter ou PyQt.
- Sistema de login e senha.

---

## 🚀 Execução

Para rodar o projeto:
```bash
python hortifruit.py
```

> Requer Python 3 instalado. É só abrir no terminal ou em um editor como o VS Code.

---

## ✍️ Feito por

Esse projeto foi desenvolvido como exercício prático e pode ser usado para apresentações, estudos ou como base para algo mais completo.

