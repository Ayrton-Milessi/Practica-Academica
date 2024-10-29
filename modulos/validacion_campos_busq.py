# Lista de campos que necesitan un número
campos_necesitan_numero = ['an', 'bc', 'callnum']

# Función para verificar si el campo necesita un número y el usuario ingresó un string
def verificar_error_campo(row):
    if len(row['sintaxis']) == 0 or row['sintaxis'] == ' ' or row['sintaxis'] == None:
        return 'usuario no ingreso nada'
    elif row['campo_utilizado'] in campos_necesitan_numero and not row['sintaxis'].isdigit():
        return 'campo incorrecto'
    return ''