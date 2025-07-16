class BadRequestException(Exception):
    def __init__(self, message: str = "Requisição inválida."):
        self.message = message
        self.status_code = 400
        super().__init__(self.message)
    
    def __str__(self):
        return self.message