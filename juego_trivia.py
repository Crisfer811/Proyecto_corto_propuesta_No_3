import preguntas
import puntajes


def mostrar_bienvenida():
    print("----Bienvenido a la trivia de preguntas----\n")
    print("----A continuacion se le presentaran las preguntas----\n")


def preguntas_mostrar(texto, respuesta_correcta, valor):
    print(texto)
    respuesta = input("----Responde Si/No en cada pregunta: ").lower()
    if respuesta == respuesta_correcta:
        print(f"Correcto! (+{valor} puntos)\n")
        return valor
    else:
        print("----Respuesta incorrecta----\n")
        print("----Pasando a la siguiente pregunta----\n")
        return 0


def jugar_trivia():
    puntaje_total = 0
    total = sum(puntajes.puntajes)

    mostrar_bienvenida()

    for i, (texto, respuesta_correcta) in enumerate(preguntas.preguntas):
        valor = puntajes.puntajes[i]
        puntaje_total += preguntas_mostrar(texto, respuesta_correcta, valor)

    return puntaje_total, total
