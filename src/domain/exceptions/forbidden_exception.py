class ForbiddenException(Exception):
    def __init__(self, message: str = "Acesso negado."):
        self.message = message
        self.status_code = 403
        super().__init__(self.message)
    
    def __str__(self):
        return self.message