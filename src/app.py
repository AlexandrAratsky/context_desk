import reflex as rx


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Context Desk", size="6"),
            rx.text("Bootstrap MVP"),
            spacing="2",
        ),
        min_height="100vh",
    )


app = rx.App()
app.add_page(index)
