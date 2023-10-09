from consolemenu import *
from consolemenu.items import *
from consolemenu.prompt_utils import PromptUtils
from colors import color
import random

# Valores iniciales del jugador
vida = 100
experiencia = 0
pociones = 1


def mostrar_estado():
    """Muestra el estado actual del jugador."""
    print(color(f"Vida: {vida}", fg="red"))
    print(color(f"Experiencia: {experiencia}", fg="blue"))
    print(color(f"Pociones: {pociones}", fg="green"))
    PromptUtils(Screen()).enter_to_continue()


def enfrentar_monstruo():
    """El jugador se enfrenta a un monstruo."""
    global vida, experiencia, pociones
    decision = input(
        "Te encuentras con un monstruo feroz. ¿Deseas luchar (l) o huir (h)? "
    ).lower()

    dano = 10

    if decision == "l":
        print(
            f"Has ganado experiencia pero el monstruo te ha causado {dano} puntos de daño."
        )

        # Posibilidad del 33% de encontrar una poción
        if random.uniform(0, 1) <= 0.33:
            pociones += 1
            print(
                color(
                    "¡Después de derrotar al monstruo, encuentras una poción de vida!",
                    fg="green",
                )
            )

    elif decision == "h":
        vida -= dano // 2
        print(
            f"Has huido, pero el monstruo te ha herido causándote {dano // 2} puntos de daño mientras escapabas."
        )

    else:
        vida -= dano
        print(
            f"No has tomado una decisión a tiempo y el monstruo te ha atacado causándote {dano} puntos de daño."
        )

    PromptUtils(Screen()).enter_to_continue()


def main():
    menu = ConsoleMenu(
        "Elige tu Aventura",
        prologue_text="¡Bienvenido a tu aventura!",
        exit_option_text="Salir del juego",
        exit_menu_char="3",
    )

    # Añadir opciones al menú
    menu.append_item(FunctionItem("Mostrar estado", mostrar_estado, menu_char="e"))
    menu.append_item(
        FunctionItem(
            color("Enfrentar un monstruo", fg="red"), enfrentar_monstruo, menu_char="m"
        )
    )

    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
