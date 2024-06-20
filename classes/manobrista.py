class Manobrista:
    def __init__(self, id_manobrista, nome, salario, cpf, patio):
        self.id_manobrista = id_manobrista
        self.nome = nome
        self.salario = salario
        self.cpf = cpf
        self.patio = patio

    def save_to_db(self, db):
        query = """
        INSERT INTO manobrista (id_manobrista, nome, salario, cpf, patio) 
        VALUES (%s, %s, %s, %s, %s)
        """
        params = (self.id_manobrista, self.nome, self.salario, self.cpf, self.patio)
        db.execute_query(query, params)

    @staticmethod
    def get_from_db(db, id_manobrista):
        query = "SELECT * FROM manobrista WHERE id_manobrista = %s"
        result = db.fetch_results(query, (id_manobrista,))
        if result:
            return Manobrista(*result[0])
        return None

    def update_in_db(self, db):
        query = """
        UPDATE manobrista SET nome = %s, salario = %s, cpf = %s, patio = %s
        WHERE id_manobrista = %s
        """
        params = (self.nome, self.salario, self.cpf, self.patio, self.id_manobrista)
        db.execute_query(query, params)

    def delete_from_db(self, db):
        query = "DELETE FROM manobrista WHERE id_manobrista = %s"
        db.execute_query(query, (self.id_manobrista,))