"""
Basic app structure
A very minimal Flet app has the following structure:

import flet as ft

def main(page: ft.Page):
    # add/update controls on Page
    pass

ft.app(target=main)
"""

import flet as ft


def main(page: ft.Page):
    page.title = "Пример счетчика на flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# Запуск в отдельном окне
# ft.app(target=main)

# Запуск в веб-браузере
ft.app(target=main, view=ft.AppView.WEB_BROWSER)

if __name__ == "__main__":
    # ft.app(target=main)
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
