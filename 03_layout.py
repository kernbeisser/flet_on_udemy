import flet as ft  # type: ignore


def main(page: ft.Page):
    page.window_height = 800
    page.window_width = 500
    page.window_resizable = False

    page.title = "Tagesplaner"


if __name__ == "__main__":
    ft.app(target=main)
