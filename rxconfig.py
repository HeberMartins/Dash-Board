import reflex as rx

config = rx.Config(
    app_name="dashboard_tutorial_reflex",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)