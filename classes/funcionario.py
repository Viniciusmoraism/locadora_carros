class Funcionario:
    def __init__(self, cpf, salario, nome, loja):
        self.cpf = cpf
        self.salario = salario
        self.nome = nome
        self.loja = loja

    def save_to_db(self, db):
        query = """
        INSERT INTO funcionario (cpf, salario, nome, loja) 
        VALUES (%s, %s, %s, %s)
        """
        params = (self.cpf, self.salario, self.nome, self.loja)
        db.execute_query(query, params)

    @staticmethod
    def get_from_db(db, cpf):
        query = "SELECT * FROM funcionario WHERE cpf = %s"
        result = db.fetch_results(query, (cpf,))
        if result:
            return Funcionario(*result[0])
        return None

    def update_in_db(self, db):
        query = """
        UPDATE funcionario SET salario = %s, nome = %s, loja = %s
        WHERE cpf = %s
        """
        params = (self.salario, self.nome, self.loja, self.cpf)
        db.execute_query(query, params)

    def delete_from_db(self, db):
        query = "DELETE FROM funcionario WHERE cpf = %s"
        db.execute_query(query, (self.cpf,))