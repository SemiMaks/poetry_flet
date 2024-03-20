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


ft.app(target=main)


def hello_world():
    # Code to run when the script is executed directly
    print("Hello, world!")


if __name__ == "__main__":
    hello_world()
    ft.app(target=main)
