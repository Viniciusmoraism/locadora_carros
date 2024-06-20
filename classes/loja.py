class Loja:
    def __init__(self, id_loja, cep, numero):
        self.id_loja = id_loja
        self.cep = cep
        self.numero = numero

    def save_to_db(self, db):
        query = """
        INSERT INTO loja (id_loja, cep, numero) 
        VALUES (%s, %s, %s)
        """
        params = (self.id_loja, self.cep, self.numero)
        db.execute_query(query, params)

    @staticmethod
    def get_from_db(db, id_loja):
        query = "SELECT * FROM loja WHERE id_loja = %s"
        result = db.fetch_results(query, (id_loja,))
        if result:
            return Loja(*result[0])
        return None

    def update_in_db(self, db):
        query = """
        UPDATE loja SET cep = %s, numero = %s
        WHERE id_loja = %s
        """
        params = (self.cep, self.numero, self.id_loja)
        db.execute_query(query, params)

    def delete_from_db(self, db):
        query = "DELETE FROM loja WHERE id_loja = %s"
        db.execute_query(query, (self.id_loja,))