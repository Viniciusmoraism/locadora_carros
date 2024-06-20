class Carro:
    def __init__(self, placa, numero_chassi, cor, disponibilidade, modelo, patio):
        self.placa = placa
        self.numero_chassi = numero_chassi
        self.cor = cor
        self.disponibilidade = disponibilidade
        self.modelo = modelo
        self.patio = patio

    def save_to_db(self, db):
        query = """
        INSERT INTO carro (placa, numero_chassi, cor, disponibilidade, modelo, patio) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (self.placa, self.numero_chassi, self.cor, self.disponibilidade, self.modelo, self.patio)
        db.execute_query(query, params)

    @staticmethod
    def get_from_db(db, placa):
        query = "SELECT * FROM carro WHERE placa = %s"
        result = db.fetch_results(query, (placa,))
        if result:
            return Carro(*result[0])
        return None

    @staticmethod
    def get_all_from_db(db):
        query = "SELECT * FROM carro"
        results = db.fetch_results(query)
        carros = []
        for result in results:
            carros.append(Carro(*result))
        return carros

    def update_in_db(self, db):
        query = """
        UPDATE carro SET numero_chassi = %s, cor = %s, disponibilidade = %s, modelo = %s, patio = %s
        WHERE placa = %s
        """
        params = (self.numero_chassi, self.cor, self.disponibilidade, self.modelo, self.patio, self.placa)
        db.execute_query(query, params)

    def delete_from_db(self, db):
        query = "DELETE FROM carro WHERE placa = %s"
        db.execute_query(query, (self.placa,))