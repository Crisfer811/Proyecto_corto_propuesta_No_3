import preguntas
import puntajes

historial_resultados = []

def juego():
    puntaje_total = 0
    total = sum(puntajes.puntajes)

    print("----Bienvenido a la trivia de preguntas----\n")
    print("----A continuacion se le presentaran las pregunta----\n")

    for i, (texto, respuesta_correcta) in enumerate(preguntas.preguntas):
        valor = puntajes.puntajes[i]
        print(texto)
        respuesta_usuario = input("Responde (Si/No): ").lower()
