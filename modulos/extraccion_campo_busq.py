import re

# Creamos una lista de los campos de búsqueda
campos_busqueda = ['kw', 'au', 'mc-itype', 'ti', 'an', 'itype', 'su', 'BC', 'bc', 'callnum', 
    'I-format', 'AU', 'an', 'se', 'In', 'bx', 'se', 'su-to', 'mc-itype,phr', 'l-format', 'Provider']

# Creamos una expresión regular para encontrar los campos
patrones = r'\b(?:' + '|'.join(campos_busqueda) + r')\b'

# Funcion para extraer el campo de cada fila
def extraer_campo(texto):
    """
    Extrae un campo específico de un texto dado utilizando una expresión regular.
    Args:
        texto (str): El texto del cual se desea extraer el campo.
    Returns:
        str or None: El campo extraído si se encuentra una coincidencia, de lo contrario, None.
    """
    match = re.search(patrones, texto)
    return match.group(0) if match else None