import tkinter as tk
from tkinter import messagebox
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

# Função para validar o login
def validar_login(usuario, senha):
    return usuario == "admin" and senha == "1234"

# Função para abrir a tela de login
def abrir_tela_login():
    tela_login = tk.Toplevel(root)
    tela_login.title("Login")
    tela_login.geometry("300x150")

    tk.Label(tela_login, text="Usuário:").pack(pady=5)
    usuario_entry = tk.Entry(tela_login)
    usuario_entry.pack(pady=5)

    tk.Label(tela_login, text="Senha:").pack(pady=5)
    senha_entry = tk.Entry(tela_login, show="*")
    senha_entry.pack(pady=5)

    def login():
        usuario = usuario_entry.get()
        senha = senha_entry.get()
        if validar_login(usuario, senha):
            tela_login.destroy()
            abrir_janela_principal()
        else:
            show_error("Usuário ou senha incorretos.")

    tk.Button(tela_login, text="Login", command=login).pack(pady=10)

# Funções para exibir mensagens de informação e erro
def show_info(message):
    messagebox.showinfo("Informação", message)

def show_error(message):
    messagebox.showerror("Erro", message)

# Função para abrir a janela principal
def abrir_janela_principal():
    root.deiconify()  # Mostra a janela principal
    root.geometry("400x300")
    root.title("Sistema de Locação Veicular")

    for widget in root.winfo_children():
        widget.destroy()  # Limpa a janela principal antes de adicionar novos widgets

    tk.Label(root, text="Bem-vindo ao Sistema de Locação Veicular", font=("Helvetica", 16)).pack(pady=20)

    tk.Button(root, text="Gerenciar Carros", command=abrir_janela_carros).pack(pady=10)
    tk.Button(root, text="Gerenciar Clientes", command=abrir_janela_clientes).pack(pady=10)
    tk.Button(root, text="Gerenciar Reservas", command=abrir_janela_reservas).pack(pady=10)
    tk.Button(root, text="Gerenciar Funcionários", command=abrir_janela_funcionarios).pack(pady=10)
    tk.Button(root, text="Listar Todos os Dados", command=listar_todos_os_dados).pack(pady=10)

# Funções para abrir novas janelas
def abrir_janela_carros():
    janela_carros = tk.Toplevel(root)
    janela_carros.title("Gerenciar Carros")
    janela_carros.geometry("400x300")

    tk.Label(janela_carros, text="Operações com Carros").pack(pady=10)

    tk.Button(janela_carros, text="Visualizar Carro", command=visualizar_carro).pack(pady=5)
    tk.Button(janela_carros, text="Adicionar Carro", command=adicionar_carro).pack(pady=5)
    tk.Button(janela_carros, text="Atualizar Carro", command=atualizar_carro).pack(pady=5)
    tk.Button(janela_carros, text="Excluir Carro", command=excluir_carro).pack(pady=5)

def abrir_janela_clientes():
    janela_clientes = tk.Toplevel(root)
    janela_clientes.title("Gerenciar Clientes")
    janela_clientes.geometry("400x300")

    tk.Label(janela_clientes, text="Operações com Clientes").pack(pady=10)

    tk.Button(janela_clientes, text="Visualizar Cliente", command=visualizar_cliente).pack(pady=5)
    tk.Button(janela_clientes, text="Adicionar Cliente", command=adicionar_cliente).pack(pady=5)
    tk.Button(janela_clientes, text="Atualizar Cliente", command=atualizar_cliente).pack(pady=5)
    tk.Button(janela_clientes, text="Excluir Cliente", command=excluir_cliente).pack(pady=5)

# Função para abrir a janela de gerenciamento de reservas
def abrir_janela_reservas():
    janela_reservas = tk.Toplevel(root)
    janela_reservas.title("Gerenciar Reservas")
    janela_reservas.geometry("400x300")

    tk.Label(janela_reservas, text="Operações com Reservas").pack(pady=10)

    tk.Button(janela_reservas, text="Visualizar Reserva", command=lambda: show_info("Funcionalidade ainda não implementada")).pack(pady=5)
    tk.Button(janela_reservas, text="Adicionar Reserva", command=lambda: show_info("Funcionalidade ainda não implementada")).pack(pady=5)
    tk.Button(janela_reservas, text="Atualizar Reserva", command=lambda: show_info("Funcionalidade ainda não implementada")).pack(pady=5)
    tk.Button(janela_reservas, text="Excluir Reserva", command=lambda: show_info("Funcionalidade ainda não implementada")).pack(pady=5)

# Função para abrir a janela de gerenciamento de funcionários
def abrir_janela_funcionarios():
    janela_funcionarios = tk.Toplevel(root)
    janela_funcionarios.title("Gerenciar Funcionários")
    janela_funcionarios.geometry("400x300")

    tk.Label(janela_funcionarios, text="Operações com Funcionários").pack(pady=10)

    tk.Button(janela_funcionarios, text="Visualizar Funcionário", command=lambda: show_info("Funcionalidade ainda não implementada")).pack(pady=5)
    tk.Button(janela_funcionarios, text="Adicionar Funcionário", command=lambda: show_info("Funcionalidade ainda não implementada")).pack(pady=5)
    tk.Button(janela_funcionarios, text="Atualizar Funcionário", command=lambda: show_info("Funcionalidade ainda não implementada")).pack(pady=5)
    tk.Button(janela_funcionarios, text="Excluir Funcionário", command=lambda: show_info("Funcionalidade ainda não implementada")).pack(pady=5)

# Função para listar todos os dados
def listar_todos_os_dados():
    janela_lista = tk.Toplevel(root)
    janela_lista.title("Listar Todos os Dados")
    janela_lista.geometry("800x600")

    text_area = tk.Text(janela_lista)
    text_area.pack(expand=True, fill='both')

    db = Database()

    def fetch_and_display_data(query):
        results = db.fetch_results(query)
        for row in results:
            text_area.insert(tk.END, f"{row}\n")

    text_area.insert(tk.END, "Carros:\n")
    fetch_and_display_data("SELECT * FROM carro")

    text_area.insert(tk.END, "\nClientes:\n")
    fetch_and_display_data("SELECT * FROM cliente")

    text_area.insert(tk.END, "\nReservas:\n")
    fetch_and_display_data("SELECT * FROM reserva")

    text_area.insert(tk.END, "\nFuncionários:\n")
    fetch_and_display_data("SELECT * FROM funcionario")

    text_area.insert(tk.END, "\nLojas:\n")
    fetch_and_display_data("SELECT * FROM loja")

    text_area.insert(tk.END, "\nModelos:\n")
    fetch_and_display_data("SELECT * FROM modelo")

    text_area.insert(tk.END, "\nPagamentos:\n")
    fetch_and_display_data("SELECT * FROM pagamento")

    text_area.insert(tk.END, "\nManobristas:\n")
    fetch_and_display_data("SELECT * FROM manobrista")

    text_area.insert(tk.END, "\nPátios:\n")
    fetch_and_display_data("SELECT * FROM patio")

# Inicialização da aplicação
root = tk.Tk()
root.withdraw()  # Oculta a janela principal até que o login seja bem-sucedido
abrir_tela_login()  # Abre a tela de login



# Funções de operações com carros
def visualizar_carro():
    janela = tk.Toplevel(root)
    janela.title("Visualizar Carro")
    janela.geometry("300x200")

    tk.Label(janela, text="Placa do Carro:").pack(pady=5)
    placa_entry = tk.Entry(janela)
    placa_entry.pack(pady=5)

    def buscar_carro():
        placa = placa_entry.get()
        db = Database()
        carro = Carro.get_from_db(db, placa)
        if carro:
            show_info(f"Carro encontrado: {carro.placa}, Modelo: {carro.modelo}")
        else:
            show_error("Carro não encontrado.")
        db.close()

    tk.Button(janela, text="Buscar", command=buscar_carro).pack(pady=10)

def adicionar_carro():
    janela = tk.Toplevel(root)
    janela.title("Adicionar Carro")
    janela.geometry("300x300")

    tk.Label(janela, text="Placa:").pack(pady=5)
    placa_entry = tk.Entry(janela)
    placa_entry.pack(pady=5)

    tk.Label(janela, text="Número do Chassi:").pack(pady=5)
    chassi_entry = tk.Entry(janela)
    chassi_entry.pack(pady=5)

    tk.Label(janela, text="Cor:").pack(pady=5)
    cor_entry = tk.Entry(janela)
    cor_entry.pack(pady=5)

    tk.Label(janela, text="Disponibilidade:").pack(pady=5)
    disponibilidade_entry = tk.Entry(janela)
    disponibilidade_entry.pack(pady=5)

    tk.Label(janela, text="ID do Modelo:").pack(pady=5)
    modelo_entry = tk.Entry(janela)
    modelo_entry.pack(pady=5)

    tk.Label(janela, text="ID do Pátio:").pack(pady=5)
    patio_entry = tk.Entry(janela)
    patio_entry.pack(pady=5)

    def salvar_carro():
        placa = placa_entry.get()
        numero_chassi = chassi_entry.get()
        cor = cor_entry.get()
        disponibilidade = disponibilidade_entry.get()
        modelo = modelo_entry.get()
        patio = patio_entry.get()

        db = Database()
        carro = Carro(placa, numero_chassi, cor, disponibilidade, modelo, patio)
        carro.save_to_db(db)
        db.close()

        show_info("Carro adicionado com sucesso.")
        janela.destroy()

    tk.Button(janela, text="Salvar", command=salvar_carro).pack(pady=10)

def atualizar_carro():
    janela = tk.Toplevel(root)
    janela.title("Atualizar Carro")
    janela.geometry("300x300")

    tk.Label(janela, text="Placa do Carro:").pack(pady=5)
    placa_entry = tk.Entry(janela)
    placa_entry.pack(pady=5)

    tk.Label(janela, text="Novo Número do Chassi:").pack(pady=5)
    chassi_entry = tk.Entry(janela)
    chassi_entry.pack(pady=5)

    tk.Label(janela, text="Nova Cor:").pack(pady=5)
    cor_entry = tk.Entry(janela)
    cor_entry.pack(pady=5)

    tk.Label(janela, text="Nova Disponibilidade:").pack(pady=5)
    disponibilidade_entry = tk.Entry(janela)
    disponibilidade_entry.pack(pady=5)

    tk.Label(janela, text="Novo ID do Modelo:").pack(pady=5)
    modelo_entry = tk.Entry(janela)
    modelo_entry.pack(pady=5)

    tk.Label(janela, text="Novo ID do Pátio:").pack(pady=5)
    patio_entry = tk.Entry(janela)
    patio_entry.pack(pady=5)

    def atualizar_carro():
        placa = placa_entry.get()
        db = Database()
        carro = Carro.get_from_db(db, placa)
        if carro:
            carro.numero_chassi = chassi_entry.get()
            carro.cor = cor_entry.get()
            carro.disponibilidade = disponibilidade_entry.get()
            carro.modelo = modelo_entry.get()
            carro.patio = patio_entry.get()
            carro.update_in_db(db)
            show_info("Carro atualizado com sucesso.")
        else:
            show_error("Carro não encontrado.")
        db.close()
        janela.destroy()

    tk.Button(janela, text="Atualizar", command=atualizar_carro).pack(pady=10)

def excluir_carro():
    janela = tk.Toplevel(root)
    janela.title("Excluir Carro")
    janela.geometry("300x200")

    tk.Label(janela, text="Placa do Carro:").pack(pady=5)
    placa_entry = tk.Entry(janela)
    placa_entry.pack(pady=5)

    def excluir_carro():
        placa = placa_entry.get()
        db = Database()
        carro = Carro.get_from_db(db, placa)
        if carro:
            carro.delete_from_db(db)
            show_info("Carro excluído com sucesso.")
        else:
            show_error("Carro não encontrado.")
        db.close()
        janela.destroy()

    tk.Button(janela, text="Excluir", command=excluir_carro).pack(pady=10)


#Funções para gerenciar Cliente:

def visualizar_cliente():
    janela = tk.Toplevel(root)
    janela.title("Visualizar Cliente")
    janela.geometry("300x200")

    tk.Label(janela, text="Número do Cliente:").pack(pady=5)
    num_cliente_entry = tk.Entry(janela)
    num_cliente_entry.pack(pady=5)

    def buscar_cliente():
        num_cliente = num_cliente_entry.get()
        db = Database()
        cliente = Cliente.get_from_db(db, num_cliente)
        if cliente:
            show_info(f"Cliente encontrado: {cliente.num_cliente}, Email: {cliente.email}")
        else:
            show_error("Cliente não encontrado.")
        db.close()

    tk.Button(janela, text="Buscar", command=buscar_cliente).pack(pady=10)

def adicionar_cliente():
    janela = tk.Toplevel(root)
    janela.title("Adicionar Cliente")
    janela.geometry("300x300")

    tk.Label(janela, text="Complemento:").pack(pady=5)
    complemento_entry = tk.Entry(janela)
    complemento_entry.pack(pady=5)

    tk.Label(janela, text="CEP:").pack(pady=5)
    cep_entry = tk.Entry(janela)
    cep_entry.pack(pady=5)

    tk.Label(janela, text="Email:").pack(pady=5)
    email_entry = tk.Entry(janela)
    email_entry.pack(pady=5)

    tk.Label(janela, text="Telefone:").pack(pady=5)
    telefone_entry = tk.Entry(janela)
    telefone_entry.pack(pady=5)

    def salvar_cliente():
        complemento = complemento_entry.get()
        cep = cep_entry.get()
        email = email_entry.get()
        telefone = telefone_entry.get()

        db = Database()
        cliente = Cliente(None, complemento, cep, email, telefone)
        cliente.save_to_db(db)
        db.close()

        show_info("Cliente adicionado com sucesso.")
        janela.destroy()

    tk.Button(janela, text="Salvar", command=salvar_cliente).pack(pady=10)

def atualizar_cliente():
    janela = tk.Toplevel(root)
    janela.title("Atualizar Cliente")
    janela.geometry("300x300")

    tk.Label(janela, text="Número do Cliente:").pack(pady=5)
    num_cliente_entry = tk.Entry(janela)
    num_cliente_entry.pack(pady=5)

    tk.Label(janela, text="Novo Complemento:").pack(pady=5)
    complemento_entry = tk.Entry(janela)
    complemento_entry.pack(pady=5)

    tk.Label(janela, text="Novo CEP:").pack(pady=5)
    cep_entry = tk.Entry(janela)
    cep_entry.pack(pady=5)

    tk.Label(janela, text="Novo Email:").pack(pady=5)
    email_entry = tk.Entry(janela)
    email_entry.pack(pady=5)

    tk.Label(janela, text="Novo Telefone:").pack(pady=5)
    telefone_entry = tk.Entry(janela)
    telefone_entry.pack(pady=5)

    def atualizar_cliente():
        num_cliente = num_cliente_entry.get()
        db = Database()
        cliente = Cliente.get_from_db(db, num_cliente)
        if cliente:
            cliente.complemento = complemento_entry.get()
            cliente.cep = cep_entry.get()
            cliente.email = email_entry.get()
            cliente.telefone = telefone_entry.get()
            cliente.update_in_db(db)
            show_info("Cliente atualizado com sucesso.")
            janela.destroy()
        else:
            show_error("Cliente não encontrado.")
        db.close()

    tk.Button(janela, text="Atualizar", command=atualizar_cliente).pack(pady=10)

def excluir_cliente():
    janela = tk.Toplevel(root)
    janela.title("Excluir Cliente")
    janela.geometry("300x200")

    tk.Label(janela, text="Número do Cliente:").pack(pady=5)
    num_cliente_entry = tk.Entry(janela)
    num_cliente_entry.pack(pady=5)

    def deletar_cliente():
        num_cliente = num_cliente_entry.get()
        db = Database()
        cliente = Cliente.get_from_db(db, num_cliente)
        if cliente:
            cliente.delete_from_db(db)
            show_info("Cliente excluído com sucesso.")
            janela.destroy()
        else:
            show_error("Cliente não encontrado.")
        db.close()

    tk.Button(janela, text="Excluir", command=deletar_cliente).pack(pady=10)




# Criação dos botões na janela principal
tk.Button(root, text="Gerenciar Carros", command=abrir_janela_carros).pack(pady=10)
tk.Button(root, text="Gerenciar Clientes", command=abrir_janela_clientes).pack(pady=10)
tk.Button(root, text="Gerenciar Reservas", command=abrir_janela_reservas).pack(pady=10)
tk.Button(root, text="Gerenciar Funcionários", command=abrir_janela_funcionarios).pack(pady=10)

root.mainloop() 