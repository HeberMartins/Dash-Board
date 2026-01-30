import reflex as rx

class User (rx.Base):
    """The User Model"""
    name: str
    email: str
    gender: str


class State(rx.State):
    users: list[User] = [
        User(
            name="Harrier Du bois",
            email="harrierdubois@rcm.com",
            gender="Male",
        ),
        User(
            name="Klaasje Amandou",
            email="msoranje@protonmail.com",
            gender="Female",
        ),
    ]

    def add_user(self, form_data: dict):
        """Add a user to the table."""
        self.users.append(User(**form_data))

def show_user(user: User):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )


def form():
    return rx.form(
        rx.vstack(
        rx.input(placeholder="User Name", name="name", required=True),
        rx.input(placeholder="User@reflex.com", name="email"),
        rx.select(["Male", "Female"], placeholder="Male", name="gender"),
        rx.button("Submit", type="submit"),
        ),
        on_submit=State.add_user,
        reset_on_submit=True,
    )

def index() -> rx.Component:
    return rx.vstack(
        form(),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Gender"),
                ),
            ),
            rx.table.body(
              rx.foreach(State.users, show_user),
            ),
            variant="surface",
            size="3",
        ),
    )




app = rx.App()
app.add_page(index)