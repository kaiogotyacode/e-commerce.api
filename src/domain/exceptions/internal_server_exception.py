class InternalServerException(Exception):
    def __init__(self, message: str = "Erro interno do servidor."):
        self.message = message
        self.status_code = 500
        super().__init__(self.message)
    
    def __str__(self):
        return self.message