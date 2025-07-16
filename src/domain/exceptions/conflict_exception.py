class ConflictException(Exception):
    def __init__(self, message: str = "Conflito de dados."):
        self.message = message
        self.status_code = 409
        super().__init__(self.message)
    
    def __str__(self):
        return self.message