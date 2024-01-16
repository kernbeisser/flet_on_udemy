import flet as ft  # type: ignore


def main(page: ft.Page):
    page.window_height = 800
    page.window_width = 500
    page.window_resizable = False

    page.title = "Huhu, Tommi!"

    huhu = ft.Text("Hi, there!", size=32, color="red", weight="bold")
    page.add(huhu)

    # page.theme_mode = ft.ThemeMode.LIGHT
    # page.update()


if __name__ == "__main__":
    ft.app(target=main)
