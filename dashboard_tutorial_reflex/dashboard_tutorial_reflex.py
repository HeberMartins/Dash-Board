import reflex as rx
from collections import Counter

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
    users_for_graph: list[dict] = []

    def add_user(self, form_data: dict):
        """Add a user to the table."""
        self.users.append(User(**form_data))
        self.transform_data()

    def transform_data(self):
        """Transform user gender group data into a format suitable for visualization in graphs."""
        # Count users of each gender group
        gender_counts = Counter(
            user.gender for user in self.users
        )

        self.users_for_graph = [
            {"name": gender_group, "value": count}
            for gender_group, count in gender_counts.items()
        ]



def show_user(user: User):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )

def add_costumer_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add user", size="4"),
            ),
        ),
        rx.dialog.content(
            rx.dialog.title("Add new user"),
            rx.dialog.description("Fill the form with user's info"),
            rx.form(
                rx.flex(
                    rx.input(placeholder="Name", name="name", required=True),
                    rx.input(placeholder="Email", name="email"),
                    rx.select(["Male", "Female"], placeholder="Gender", name="gender"),
                    rx.flex(
                        rx.dialog.close(
                            rx.button("Cancel", variant="soft", color_scheme="gray")
                        ),
                        rx.dialog.close(
                            rx.button("Submit", type="submit")
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=State.add_user,
                reset_on_submit=True,
            ),
            max_width="450px",
        ),
    )

def graph():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            stroke=rx.color("accent",9),
            fill=rx.color("accent",8),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=State.users_for_graph,
        width="100%",
        height=250,

    )

def index() -> rx.Component:
    return rx.vstack(
        add_costumer_button(),
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
        graph(),
    )




app = rx.App()
app.add_page(index)