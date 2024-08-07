"""
Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
    --> Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
    --> En morse se soporta raya "—", 
        punto ".", 
        un espacio " " entre letras o símbolos 
        y dos espacios entre palabras "  ".
    --> El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
"""


# Diccionarios Para la Conversion entre Texto y Codigo morse
TEXTO_A_MORSE = {
    'A': '•-',    'B': '-•••', 'C': '-•-•', 'D': '-••',
    'E': '•',     'F': '••-•', 'G': '--•',  'H': '••••',
    'I': '••',    'J': '•---', 'K': '-•-',  'L': '•-••',
    'M': '--',    'N': '-•',   'O': '---',  'P': '•--•',
    'Q': '--•-',  'R': '•-•',  'S': '•••',  'T': '-',
    'U': '••-',   'V': '•••-', 'W': '•--',  'X': '-••-',
    'Y': '-•--',  'Z': '--••', 
    '0': '-----', '1': '•----', '2': '••---', '3': '•••--',
    '4': '••••-', '5': '•••••', '6': '-••••', '7': '--•••',
    '8': '---••', '9': '----•',
    '.': '•-•-•-', ',': '--••--', '?': '••--••', "'": '•----•',
    '!': '-•-•--', '/': '-••-•', '(': '-•--•', ')': '-•--•-',
    '&': '•-•••', ':': '---•••', ';': '-•-•-•', '=': '-•••-',
    '+': '•-•-•', '-': '-••••-', '_': '••--•-', '"': '•-••-•',
    '$': '•••-••-', '@': '•--•-•', '¿': '••-•-•', '¡': '--••-•'
}

MORSE_A_TEXTO = {}

for clave, valor in TEXTO_A_MORSE.items():
    MORSE_A_TEXTO[valor] = clave


def texto_a_morse (texto:str):
    """Convierte una cadena de texto a código Morse.

    Args:
        texto (str): La cadena de texto a convertir.

    Returns:
        str: La cadena de texto convertida a código Morse.
    """

    texto = texto.upper() # Convertimos a mayúsculas para una búsqueda más sencilla
    morse = []
    
    for caracter in texto:
        if caracter in TEXTO_A_MORSE: # Si el caracter esta en el diccionario
            morse.append(TEXTO_A_MORSE[caracter]) # Se agrega el valor correspondiente a su clave
        elif caracter == " ": # Si el caracter es un espacio
            morse.append(" ") # Se agrega el espacio a la lista

    texto_convertido = " ".join(morse) # Se unen los elementos de la lista a una unica cadena de caracteres

    return texto_convertido


def morse_a_texto (morse:str):
    """Convierte una cadena de código Morse a texto.

    Args:
        morse (str): La cadena de código Morse a convertir.

    Returns:
        str: La cadena de texto decodificada.
    """

    palabras = morse.split("  ") # Se separan las palabras (se identifican al tener doble espacio)
    mensage = []

    for palabra in palabras: 
        letras = palabra.split(" ") # Se separan las letras de cada palabra (se identifican al tener un solo espacio)
        palabra_decodificada = [] 

        for letra in letras:
            if letra in MORSE_A_TEXTO: # Si la letra en morse esta en el diccionario
                palabra_decodificada.append(MORSE_A_TEXTO[letra]) # Se agrega la su correspondiente valor a la lista 
            else: # Si no se encuentra
                palabra_decodificada.append("") # Se agrega una cadena vacia
        
        mensage.append("".join(palabra_decodificada)) # Se juntan los elementos para formar cada palabra

    mensage_decodificado = " ".join(mensage) # Se juntan los elementos que contienen las palabras del mensaje

    return mensage_decodificado


def detectar_tipo (entrada_cadena:str):
    """Detecta si la cadena de entrada es texto o código Morse.

    Args:
        entrada_cadena (str): La cadena a analizar.

    Returns:
        str: El resultado de la conversión (texto o Morse).
    """

    es_morse = False
    
    for caracter in entrada_cadena:
        if caracter in [".", "-"]:
            es_morse = True
            break

    if es_morse:
        return morse_a_texto(entrada_cadena)
    else:
        return texto_a_morse(entrada_cadena)
    

resultado1 = detectar_tipo("Hola Mundo")
resultado2 = detectar_tipo("•••• --- •-•• •-   -- ••- -• -•• ---")

print(resultado1)
print(resultado2)
