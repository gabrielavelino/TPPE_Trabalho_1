# -*- coding: utf-8 -*-

import pytest

class DescricaoEmBrancoException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'

class ValorRendimentoInvalidoException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'

class ValorDeducaoInvalidoException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class NomeEmBrancoException(Exception):
    
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)
    
        def __str__(self):
            return f'{self.message}'