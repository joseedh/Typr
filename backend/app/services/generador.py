from google import genai 
from app.config import settings

client = genai.Client(
    api_key = settings.gemini_api_key

)

respuesta = client.interactions.create(
    model=settings.gemini_model,
    input=
    """
    Genera 30 frases para un juego de mecanografía

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

print(respuesta.output_text)