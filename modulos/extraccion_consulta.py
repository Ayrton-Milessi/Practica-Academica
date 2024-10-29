import re

# Funcion para extraer la sintaxis de cada fila
def extraer_sintaxis(texto):
    """
    Extrae la sintaxis de cada búsqueda de los usuarios.
    Args:
        texto (str): El texto de la búsqueda.
    Returns:
        str: La sintaxis extraída.
    """
    sintaxis = re.findall(r':\s*([^,]+)', texto)
    return ', '.join(sintaxis)