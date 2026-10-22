from google import genai 
from app.config import settings

client = genai.Client(
    api_key = settings.gemini_api_key

)

def generar_frases(idioma):
    if idioma == "es":
        frases_es = client.interactions.create(
            model=settings.gemini_model,
            input=
            """
            Genera 60 frases para un juego de mecanografía

            Grupo 1 - Complejidad baja:
                - Longitud de 40 a 80 caracteres.
                - Vocabulario simple y cotidiano del español.
                - Máximo 2 signos de puntuación por frase, además del punto final.
                - Pueden contener tildes.
                - Sin números ni símbolos especiales.

            Grupo 2 - Complejidad media:
                - Longitud de 81 a 100 caracteres.
                - Vocabulario variado y algo más complejo.
                - Entre 3 y 5 signos de puntuación por frase, además del punto final.
                - Pueden contener tildes, mayúsculas, comas, dos puntos, signos de interrogación y signos de exclamación.
                - Sin números ni símbolos especiales.

            Grupo 3 - Complejidad alta:
                - Longitud de 101 a 150 caracteres.
                - Vocabulario avanzado y expresiones idiomáticas.
                - Entre 6 y 10 signos de puntuación por frase, además del punto final.
                - Pueden contener tildes, mayúsculas, números, comas, dos puntos, punto y coma, paréntesis, signos de interrogación y signos de exclamación.
                - Sin símbolos especiales.

            Varía también su complejidad de escritura. Algunas deben ser simples y otras pueden contener tildes, mayúsculas, números, comas, dos puntos, punto y coma, paréntesis, signos de interrogación y signos de exclamación.

            Requisitos:
            - Cada frase debe ser única y no repetirse.
            - Cada frase debe tener sentido.
            - Cada frase debe tener una gramatica perfecta.
            - Cada frase debe sonar natural en el español.
            - Las frases deben tener temas variados.
            - Utilizar únicamente caracteres habituales de escritura en español.
            - No utilizar Markdown ni LaTeX.
            - No utilizar $, barra invertida, _, ^, {, }, [, ], <, >, |, ~ ni `.
            - Devolver exactamente una frase por línea.
            - No utilizar numeración, títulos ni explicaciones.
            """
        )
        return frases_es.output_text
    
    elif idioma == "en":
        frases_en = client.interactions.create(
            model=settings.gemini_model,
            input=
            """
            Generate 60 sentences for a typing game.

            Group 1 - Low complexity:
                - Length between 40 and 80 characters.
                - Simple and everyday English vocabulary.
                - Maximum of 2 punctuation marks per sentence, in addition to the final period.
                - May contain apostrophes in common contractions.
                - No numbers or special symbols.

            Group 2 - Medium complexity:
                - Length between 81 and 100 characters.
                - More varied and slightly more complex vocabulary.
                - Between 3 and 5 punctuation marks per sentence, in addition to the final period.
                - May contain uppercase letters, commas, colons, apostrophes, question marks and exclamation marks.
                - No numbers or special symbols.

            Group 3 - High complexity:
                - Length between 101 and 150 characters.
                - Advanced vocabulary and natural English expressions or idioms.
                - Between 6 and 10 punctuation marks per sentence, in addition to the final period.
                - May contain uppercase letters, numbers, commas, colons, semicolons, parentheses, apostrophes, quotation marks, question marks and exclamation marks.
                - Do not use unusual special symbols.

            Also vary the typing complexity. Some sentences should be simple, while others may contain uppercase letters, numbers, commas, colons, semicolons, parentheses, apostrophes, quotation marks, question marks and exclamation marks.

            Requirements:
                - Every sentence must be unique and must not be repeated.
                - Every sentence must make sense.
                - Every sentence must use correct English grammar.
                - Every sentence must sound natural to a native English speaker.
                - Use varied topics.
                - Use only characters commonly found on a standard English keyboard.
                - Do not use Markdown or LaTeX.
                - Do not use $, backslash, _, ^, {, }, [, ], <, >, |, ~ or `.
                - Return exactly one sentence per line.
                - Do not include numbering, headings, explanations or introductory text.
            """  
        )
        return frases_en.output_text


print("Generando frases en español:")
texto_es = generar_frases("es")
frases_es = [
    frase.strip()
    for frase in texto_es.splitlines()
    if frase.strip()
]
frases_es_easy = frases_es[:20]
frases_es_medium = frases_es[20:40]
frases_es_hard = frases_es[40:60]

print("Bajas:", len(frases_es_easy))
print("Medias:", len(frases_es_medium))
print("Altas:", len(frases_es_hard))

print("Generando frases en inglés:")
texto_en = generar_frases("en")
frases_en = [
    frase.strip()
    for frase in texto_en.splitlines()
    if frase.strip()
]
frases_en_easy = frases_en[:20]
frases_en_medium = frases_en[20:40] 
frases_en_hard = frases_en[40:60]

print("Bajas:", len(frases_en_easy))
print("Medias:", len(frases_en_medium))
print("Altas:", len(frases_en_hard))
