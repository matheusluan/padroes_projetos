from datetime import datetime
class BancoDeDados:

    # instancia unica da classe BancoDeDados
    _instance = None  
    def __init__(self):
        self.data = datetime.now()
        self.driver = 'mysql'
    
    def __new__(cls, *args, **kwargs):
        # cls = classe BancoDeDados
        # _instance = singleton
        if cls._instance is None:
            # super() chama o __new__ da classe ancestral
            cls._instance = super().__new__(cls)
        return cls._instance
    
    
if __name__ == '__main__':

    # aqui faz o get do _instance
    conn1 = BancoDeDados()
    conn2 = BancoDeDados()

    # deve ser igual (se nao for o singleton falhou)
    print(id(conn1))
    print(id(conn2))

    print(conn1.driver)
    print(conn1.data)

    print(conn2.driver)
    print(conn2.data)