class Cliente:
    def __init__(self, num_cliente, complemento, cep, email, telefone):
        self.num_cliente = num_cliente
        self.complemento = complemento
        self.cep = cep
        self.email = email
        self.telefone = telefone

    def save_to_db(self, db):
        query = """
        INSERT INTO cliente (complemento, cep, email, telefone) 
        VALUES (%s, %s, %s, %s)
        """
        params = (self.complemento, self.cep, self.email, self.telefone)
        db.execute_query(query, params)

    @staticmethod
    def get_from_db(db, num_cliente):
        query = "SELECT * FROM cliente WHERE Num_cliente = %s"
        result = db.fetch_results(query, (num_cliente,))
        if result:
            return Cliente(*result[0])
        return None

    def update_in_db(self, db):
        query = """
        UPDATE cliente SET complemento = %s, cep = %s, email = %s, telefone = %s
        WHERE Num_cliente = %s
        """
        params = (self.complemento, self.cep, self.email, self.telefone, self.num_cliente)
        db.execute_query(query, params)

    def delete_from_db(self, db):
        query = "DELETE FROM cliente WHERE Num_cliente = %s"
        db.execute_query(query, (self.num_cliente,))