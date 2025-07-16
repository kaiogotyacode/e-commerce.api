class UnauthorizedException(Exception):
    def __init__(self, message: str = "Não autorizado."):
        self.message = message
        self.status_code = 401
        super().__init__(self.message)
    
    def __str__(self):
        return self.message