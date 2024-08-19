import re

def extract_emails(text):
    """
    Extrae todos los correos electrónicos presentes en el texto dado.
    
    :param text: Cadena de texto en la que buscar los correos electrónicos.
    :return: Lista de correos electrónicos encontrados.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails

def extract_comments(code):
    """
    Extrae todos los comentarios de un código fuente dado. 
    Soporta comentarios de una línea y multilínea.
    
    :param code: Cadena de texto que representa el código fuente.
    :return: Lista de comentarios encontrados.
    """
    # Comentarios de una línea
    single_line_comment_pattern = r'//.*'
    # Comentarios multilínea
    multi_line_comment_pattern = r'/\*[\s\S]*?\*/'
    
    # Buscar comentarios de una línea y multilínea
    single_line_comments = re.findall(single_line_comment_pattern, code)
    multi_line_comments = re.findall(multi_line_comment_pattern, code)
    
    return single_line_comments + multi_line_comments

def validate_date(date):
    """
    Valida si una fecha dada está en el formato mm/dd/yyyy y es una fecha válida.
    
    :param date: Fecha en formato de cadena 'mm/dd/yyyy'.
    :return: True si la fecha es válida, False en caso contrario.
    """
    date_pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$'
    match = re.match(date_pattern, date)
    
    if match:
        # Verificar que el día sea válido para el mes dado
        month, day, year = map(int, date.split('/'))
        if month == 2 and day > 29:
            return False  # Febrero no puede tener más de 29 días
        if month in {4, 6, 9, 11} and day > 30:
            return False  # Abril, junio, septiembre y noviembre tienen 30 días
        return True
    return False

# Ejemplos de uso:
if __name__ == "__main__":
    text = "Aquí hay algunos correos: example1@gmail.com, contacto@empresa.com, y otro-correo@dominio.org."
    code = """
    // Este es un comentario de una línea
    int a = 0; /* Este es un comentario
    multilínea */
    """
    date = "12/31/2024"

    try:
        emails = extract_emails(text)
        comments = extract_comments(code)
        is_valid_date = validate_date(date)

        print("Correos electrónicos encontrados:", emails)
        print("Comentarios encontrados:", comments)
        print("¿Fecha válida?:", is_valid_date)

    except Exception as e:
        print(f"Se produjo un error: {e}")
