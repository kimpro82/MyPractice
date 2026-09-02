from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, RichLog, Static
from textual.binding import Binding
from textual_plotext import PlotextPlot
from pathlib import Path
import random
import textwrap
import yaml                                         # PyYAML

ASSET_PATH = Path(__file__).with_suffix(".yaml")
with ASSET_PATH.open(encoding="utf-8") as asset_file:
    ASSETS = yaml.safe_load(asset_file)

class BACChart(PlotextPlot):
    """Real-time Blood Alcohol Content (BAC) and Sanity line chart."""

    def on_mount(self) -> None:
        self.plt.title(ASSETS["chart"]["title"])
        self.plt.xlabel(ASSETS["chart"]["x_label"])
        self.plt.ylabel(ASSETS["chart"]["y_label"])
        self.x_data = list(range(10))
        self.y_data = [20.0 for _ in range(10)]
        self.current_bac = 20.0
        
        self.plt.plot(self.x_data, self.y_data, marker="braille")
        self.plt.ylim(0, 110)
        
        # Background tick: updates every 1 second
        self.set_interval(1.0, self.update_bac)

    def update_bac(self) -> None:
        # Natural slight decrease over time, but never below 0
        self.current_bac = max(0.0, self.current_bac - 1.5)
        
        self.x_data.pop(0)
        self.x_data.append(self.x_data[-1] + 1)
        self.y_data.pop(0)
        self.y_data.append(self.current_bac)
        
        self.plt.clear_data()
        self.plt.plot(self.x_data, self.y_data, marker="braille")
        self.plt.ylim(0, 110)
        self.refresh()

        # Check for Over-100% BAC (Memory Blackout Over)
        if self.current_bac >= 100.0:
            self.app.exit(message=ASSETS["messages"]["blackout"])


class DrinkingStatusPanel(Static):
    """Status display widget with humorous office worker and financial quotes."""

    def on_mount(self) -> None:
        self.drinks_count = 0
        self.update_status()

    def update_status(self) -> None:
        current_quote = random.choice(ASSETS["messages"]["status_quotes"])
        
        self.update(
            ASSETS["status_panel"]["template"].format(
                drinks_count=self.drinks_count,
                current_quote=current_quote,
            )
        )

    def add_drink(self) -> None:
        self.drinks_count += 1
        chart = self.app.query_one("#bac_chart", BACChart)
        chart.current_bac = min(105.0, chart.current_bac + 35.0)
        self.app.add_event_log(ASSETS["messages"]["drink_added"], "warning")
        self.update_status()
        
        # Immediate check after adding drink
        if chart.current_bac >= 100.0:
            self.app.exit(message=ASSETS["messages"]["blackout"])

    def sober_up(self) -> None:
        chart = self.app.query_one("#bac_chart", BACChart)
        chart.current_bac = max(0.0, chart.current_bac - 25.0)
        self.app.add_event_log(ASSETS["messages"]["sober_up"], "information")
        self.update_status()


class LiquidityCrisisApp(App):
    CSS_PATH = "textual_practice.tcss"

    BINDINGS = [
        Binding("q", "quit", ASSETS["bindings"]["quit"]),
        Binding("Q", "quit", show=False),
        Binding("b", "drink_beer", ASSETS["bindings"]["drink_beer"]),
        Binding("B", "drink_beer", show=False),
        Binding("r", "hangover_cure", ASSETS["bindings"]["hangover_cure"]),
        Binding("R", "hangover_cure", show=False),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            Vertical(
                DrinkingStatusPanel(id="status_panel"),
                RichLog(id="event_log", markup=True, min_width=0, wrap=True),
                id="left_panel",
            ),
            BACChart(id="bac_chart")
        )
        yield Footer()

    def add_event_log(self, message: str, severity: str) -> None:
        log = self.query_one("#event_log", RichLog)
        style = "yellow" if severity == "warning" else "cyan"
        message_width = max(1, log.content_size.width - 2)
        formatted_message = textwrap.fill(
            message,
            width=message_width,
            initial_indent="- ",
            subsequent_indent=" ",
        )
        log.write(f"[{style}]{formatted_message}[/]", scroll_end=True)

    def action_drink_beer(self) -> None:
        panel = self.query_one("#status_panel", DrinkingStatusPanel)
        panel.add_drink()

    def action_hangover_cure(self) -> None:
        panel = self.query_one("#status_panel", DrinkingStatusPanel)
        panel.sober_up()

    def on_mount(self) -> None:
        self.schedule_random_bac_event()

    def schedule_random_bac_event(self) -> None:
        self.set_timer(random.uniform(1.0, 5.0), self.trigger_random_bac_event)

    def trigger_random_bac_event(self) -> None:
        random_event = ASSETS["random_event"]
        change = random.choices(
            random_event["changes"], weights=random_event["weights"]
        )[0]
        chart = self.query_one("#bac_chart", BACChart)

        if random.choice([True, False]):
            chart.current_bac = min(105.0, chart.current_bac + change)
            self.add_event_log(
                random.choice(random_event["increase_messages"]), "warning"
            )
        else:
            chart.current_bac = max(0.0, chart.current_bac - change)
            self.add_event_log(
                random.choice(random_event["decrease_messages"]), "information"
            )

        if chart.current_bac >= 100.0:
            self.exit(message=ASSETS["messages"]["blackout"])
            return

        self.schedule_random_bac_event()


if __name__ == "__main__":
    app = LiquidityCrisisApp()
    app.run()
