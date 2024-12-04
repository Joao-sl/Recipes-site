from django.core.exceptions import ValidationError
import re


def time_validator(string):
    string = string.strip()

    # Expressão regular para validar as entradas especificadas no exemplo abaixo
    pattern = r'^\d+h(\s*\d+min)?$|^\d+min$'

    if not re.match(pattern, string):
        raise ValidationError(
            'Por favor siga exatamente o padrão recomendado. Exemplos: 2h, 1h 40min, 35min'
        )
