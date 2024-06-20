class Patio:
    def __init__(self, id_patio, endereco, capacidade):
        self.id_patio = id_patio
        self.endereco = endereco
        self.capacidade = capacidade

    def save_to_db(self, db):
        query = """
        INSERT INTO patio (id_patio, endereco, capacidade) 
        VALUES (%s, %s, %s)
        """
        params = (self.id_patio, self.endereco, self.capacidade)
        db.execute_query(query, params)

    @staticmethod
    def get_from_db(db, id_patio):
        query = "SELECT * FROM patio WHERE id_patio = %s"
        result = db.fetch_results(query, (id_patio,))
        if result:
            return Patio(*result[0])
        return None

    def update_in_db(self, db):
        query = """
        UPDATE patio SET endereco = %s, capacidade = %s
        WHERE id_patio = %s
        """
        params = (self.endereco, self.capacidade, self.id_patio)
        db.execute_query(query, params)

    def delete_from_db(self, db):
        query = "DELETE FROM patio WHERE id_patio = %s"
        db.execute_query(query, (self.id_patio,))