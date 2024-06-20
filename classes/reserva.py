class Reserva:
    def __init__(self, id_reserva, num_diarias, data_inicio, cliente, carro):
        self.id_reserva = id_reserva
        self.num_diarias = num_diarias
        self.data_inicio = data_inicio
        self.cliente = cliente
        self.carro = carro

    def save_to_db(self, db):
        query = """
        INSERT INTO reserva (num_diarias, data_inicio, cliente, carro) 
        VALUES (%s, %s, %s, %s)
        """
        params = (self.num_diarias, self.data_inicio, self.cliente, self.carro)
        db.execute_query(query, params)

    @staticmethod
    def get_from_db(db, id_reserva):
        query = "SELECT * FROM reserva WHERE id_reserva = %s"
        result = db.fetch_results(query, (id_reserva,))
        if result:
            return Reserva(*result[0])
        return None

    def update_in_db(self, db):
        query = """
        UPDATE reserva SET num_diarias = %s, data_inicio = %s, cliente = %s, carro = %s
        WHERE id_reserva = %s
        """
        params = (self.num_diarias, self.data_inicio, self.cliente, self.carro, self.id_reserva)
        db.execute_query(query, params)

    def delete_from_db(self, db):
        query = "DELETE FROM reserva WHERE id_reserva = %s"
        db.execute_query(query, (self.id_reserva,))