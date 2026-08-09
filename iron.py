from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from textual.containers import Horizontal, Container
from textual import events

textContent = "Welcome to the gym app"

class MyApp(App):
    # stylesheet for widgets
    CSS_PATH = "iron.tcss"
    # bindings for app
    BINDINGS = [
        ("ENTER", "logFunc", "Log Session"),
        ("b", "bodyFunc", "Body"),
        ("p", "progressFunc", "Progress"),
        ("h", "homeFunc", "Home"),
        ("q", "quitFunc", "Quit")
    ]

    # adding widgets for landing screen
    def compose(self) -> ComposeResult:
        yield Header()
        # main window with sidebar always there
        with Horizontal(id="mainWindow"):
            yield Container(id="sidebar")
            yield Container(id="main")
        yield Footer()

    # event keys
    def on_key(self, event: events.Key) -> None:
        if event.key == "a":
            self.screen.styles.background = "red"


if __name__ == "__main__":
    app = MyApp()
    app.run()
