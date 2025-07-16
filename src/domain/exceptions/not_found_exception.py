class NotFoundException(Exception):
    def __init__(self, message: str = "Não encontrado."):
        self.message = message
        self.status_code = 404
        super().__init__(self.message)
    
    def __str__(self):
        return self.message