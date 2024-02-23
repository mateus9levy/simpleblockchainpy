from blockchain import Blockchain
from block import Block
from wallet_manager import Wallet_manager
from transaction import Transaction
from datetime import datetime

# print(wallet)

# blockchain = Blockchain()
# genesis_block = blockchain.get_latest_block()
# block1 = Block(1,"23/02/2024","Transaction 1",genesis_block.compute_hash())
# blockchain.add_block(block1)
# for block in blockchain.chain:
#     print(f"{block}" + "\n")
blockchain = Blockchain()

while(True):
    menu_item  = input("Escolha as opcoes:\n1 - Blockchain\n2 - Carteiras\n3 - Sair\n")
    if(menu_item == "1"):
        while(True):
            blockchain_item = input("Escolha as opcoes:\n1 - Adicionar bloco\n2 - Ver blockchain\n3 - Voltar\n")
            if(blockchain_item == "1"):
                transaction = input("Digite a transacao: ")
                block = Block(len(blockchain.chain), "23/02/2024", transaction, blockchain.get_latest_block().compute_hash())
                blockchain.add_block(block)
            if(blockchain_item == "2"):
                for block in blockchain.chain:
                    print("\n" + f"{block}" + "\n")
            if(blockchain_item == "3"):
                break
    if(menu_item == "2"):
        while(True):
            wallet_item = input("Escolha as opcoes:\n1 - Criar carteira\n2 - Depositar\n3 - Sacar\n4 - Ver saldo\n5 - Voltar\n")
            if(wallet_item == "1"):
                wallet_manager = Wallet_manager()
                wallet_manager.create_wallet()
                wallets = wallet_manager.get_wallets()
                print(wallets[-1])
            if(wallet_item == "2"):
                public_key = input("Digite a cateira de destino: ")
                private_key = input("Digite a chave privada: ")
                amount = input("Digite o valor: ")
                transaction = Transaction(private_key, public_key, amount)
                transaction = transaction.json_Transaction()
                new_block = Block(len(blockchain.chain), datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), transaction, blockchain.get_latest_block().compute_hash())
                mined = blockchain.add_block(new_block)
                if(mined):
                    wallet_manager.deposit(public_key, amount)
                    print("Transacao realizada com sucesso")
            if(wallet_item == "4"):
                public_key = input("Digite a chave publica: ")
                balance = wallet_manager.get_balance(public_key)
                print(f"Seu saldo e: {balance}")
            if(wallet_item == "5"):
                break

    if(menu_item == "3"):
        break