class DomainError(Exception):
    """Error base del dominio"""

    pass


class EmptyTitleError(DomainError):

    def __init__(self, message="El título del gasto no puede estar vacío"):
        self.message = message
        super().__init__(self.message)
    pass


class InvalidAmountError(DomainError):
    def __init__(self, message="El gasto debe ser un número positivo"):
        self.message = message
        super().__init__(self.message)
    pass


class InvalidExpenseDateError(DomainError):
    def __init__(self, message="La fecha del gasto no puede ser posterior a hoy"):
        self.message = message
        super().__init__(self.message)
    pass
