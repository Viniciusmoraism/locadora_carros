class Pagamento:
    def __init__(self, id_pagamento, data_pagamento, id_reserva):
        self.id_pagamento = id_pagamento
        self.data_pagamento = data_pagamento
        self.id_reserva = id_reserva

    def save_to_db(self, db):
        query = """
        INSERT INTO pagamento (id_pagamento, data_pagamento, id_reserva) 
        VALUES (%s, %s, %s)
        """
        params = (self.id_pagamento, self.data_pagamento, self.id_reserva)
        db.execute_query(query, params)

    @staticmethod
    def get_from_db(db, id_pagamento):
        query = "SELECT * FROM pagamento WHERE id_pagamento = %s"
        result = db.fetch_results(query, (id_pagamento,))
        if result:
            return Pagamento(*result[0])
        return None

    def update_in_db(self, db):
        query = """
        UPDATE pagamento SET data_pagamento = %s, id_reserva = %s
        WHERE id_pagamento = %s
        """
        params = (self.data_pagamento, self.id_reserva, self.id_pagamento)
        db.execute_query(query, params)

    def delete_from_db(self, db):
        query = "DELETE FROM pagamento WHERE id_pagamento = %s"
        db.execute_query(query, (self.id_pagamento,))