class Modelo:
    def __init__(self, id_modelo, fabricante, tipo):
        self.id_modelo = id_modelo
        self.fabricante = fabricante
        self.tipo = tipo

    def save_to_db(self, db):
        query = """
        INSERT INTO modelo (id_modelo, fabricante, tipo) 
        VALUES (%s, %s, %s)
        """
        params = (self.id_modelo, self.fabricante, self.tipo)
        db.execute_query(query, params)

    @staticmethod
    def get_from_db(db, id_modelo):
        query = "SELECT * FROM modelo WHERE id_modelo = %s"
        result = db.fetch_results(query, (id_modelo,))
        if result:
            return Modelo(*result[0])
        return None

    def update_in_db(self, db):
        query = """
        UPDATE modelo SET fabricante = %s, tipo = %s
        WHERE id_modelo = %s
        """
        params = (self.fabricante, self.tipo, self.id_modelo)
        db.execute_query(query, params)

    def delete_from_db(self, db):
        query = "DELETE FROM modelo WHERE id_modelo = %s"
        db.execute_query(query, (self.id_modelo,))