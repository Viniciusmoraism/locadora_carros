# main.py
from classes.carro import Carro
from classes.cliente import Cliente
from classes.reserva import Reserva
from classes.funcionario import Funcionario
from classes.loja import Loja
from classes.modelo import Modelo
from classes.pagamento import Pagamento
from classes.manobrista import Manobrista
from classes.patio import Patio
from classes.database import Database

def main():
    # Conectando ao banco de dados
    db = Database()

    try:
        # Operações com a classe Carro
        print("\nOperações com a classe Carro:")
        carro1 = Carro.get_from_db(db, 'HIJ1817')
        if carro1:
            print(f"Carro encontrado: {carro1.placa}, Modelo: {carro1.modelo}")
        else:
            print("Carro não encontrado.")

        # Exemplo de buscar todos os carros
        print("\nTodos os Carros:")
        carros = Carro.get_all_from_db(db)
        for carro in carros:
            print(f"Carro encontrado: {carro.placa}, Modelo: {carro.modelo}")

    
        # Operações com a classe Cliente
        print("\nOperações com a classe Cliente:")
        cliente1 = Cliente.get_from_db(db, 1)
        if cliente1:
            print(f"Cliente encontrado: {cliente1.num_cliente}, Email: {cliente1.email}")
        else:
            print("Cliente não encontrado.")

        # Operações com a classe Reserva
        print("\nOperações com a classe Reserva:")
        reserva1 = Reserva.get_from_db(db, 1)
        if reserva1:
            print(f"Reserva encontrada: {reserva1.id_reserva}, Data Início: {reserva1.data_inicio}")
        else:
            print("Reserva não encontrada.")

        # Operações com a classe Funcionário
        print("\nOperações com a classe Funcionário:")
        funcionario1 = Funcionario.get_from_db(db, 12345678901)
        if funcionario1:
            print(f"Funcionário encontrado: {funcionario1.cpf}, Nome: {funcionario1.nome}")
        else:
            print("Funcionário não encontrado.")

    except Exception as e:
        print(f"Erro durante operações: {e}")

    finally:
        # Fechando a conexão com o banco de dados
        db.close()

if __name__ == "__main__":
    main()