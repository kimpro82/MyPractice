from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Header, Footer, Static
from textual.binding import Binding
from textual_plotext import PlotextPlot
import random

class BACChart(PlotextPlot):
    """Real-time Blood Alcohol Content (BAC) and Sanity line chart."""

    def on_mount(self) -> None:
        self.plt.title("Liquidity Crisis: Real-time BAC & Sanity Tracker")
        self.plt.xlabel("Time (s)")
        self.plt.ylabel("Level (%)")
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
            self.app.exit(message="🚨 Liquidity Crisis! Memory Blackout triggered. Sent home & forced exit.")


class DrinkingStatusPanel(Static):
    """Status display widget with humorous office worker and financial quotes."""

    def on_mount(self) -> None:
        self.drinks_count = 0
        self.update_status()

    def update_status(self) -> None:
        quotes = [
            "HODLing my sobriety with diamond hands...",
            "High liquidity detected in the blood stream.",
            "Sudden urge to execute `git push -f origin main`.",
            "Not sure if I wrote the code or the alcohol wrote me.",
            "If you don't remember writing it, it doesn't exist."
        ]
        current_quote = random.choice(quotes)
        
        self.update(
            f"\n[bold cyan]🍻 Liquidity Crisis Monitoring[/]\n\n"
            f"• Drinks Consumed: {self.drinks_count} glasses\n"
            f"• Current Status: {current_quote}\n\n"
            f"[dim]----------------------------------------[/]\n"
            f"[bold green]Key Bindings:[/]\n"
            f" [B] Add Beer (Sharp BAC spike)\n"
            f" [R] Hangover Cure (Lower BAC)\n"
            f" [Q] Quit App"
        )

    def add_drink(self) -> None:
        self.drinks_count += 1
        chart = self.app.query_one("#bac_chart", BACChart)
        chart.current_bac = min(105.0, chart.current_bac + 35.0)
        self.app.notify("🍺 Liquid injection! BAC is spiking.", severity="warning")
        self.update_status()
        
        # Immediate check after adding drink
        if chart.current_bac >= 100.0:
            self.app.exit(message="🚨 Liquidity Crisis! Memory Blackout triggered. Sent home & forced exit.")

    def sober_up(self) -> None:
        chart = self.app.query_one("#bac_chart", BACChart)
        chart.current_bac = max(0.0, chart.current_bac - 25.0)
        self.app.notify("🍲 Hangover soup consumed! Capital preservation active.", severity="information")
        self.update_status()


class LiquidityCrisisApp(App):
    CSS = """
    Screen {
        background: #1e1e2e;
    }
    Horizontal {
        height: 1fr;
    }
    DrinkingStatusPanel {
        width: 1fr;
        height: 1fr;
        border: solid yellow;
        margin: 1;
        padding: 2;
    }
    BACChart {
        width: 1fr;
        height: 1fr;
        border: solid cyan;
        margin: 1;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("b", "drink_beer", "Beer"),
        Binding("r", "hangover_cure", "Relief"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            DrinkingStatusPanel(id="status_panel"),
            BACChart(id="bac_chart")
        )
        yield Footer()

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
        increase_messages = [
            "An expense report was approved. Confidence is carbonated.",
            "The office coffee was replaced with mystery punch.",
            "A teammate said 'quick deploy' with a straight face.",
            "Someone opened a meeting with 'one tiny update.'",
            "The build turned green, so celebration became a service.",
            "A spreadsheet achieved sentience and ordered a round.",
            "The snack budget was reclassified as liquid assets.",
            "A calendar invite arrived labeled 'casual emergency.'",
            "The printer finally worked. This felt historically important.",
            "A bug was fixed by restarting it. Cheers to science.",
        ]
        decrease_messages = [
            "Water appeared, pretending to be a responsible adult.",
            "The finance team discovered the receipt trail.",
            "A production alert provided instant emotional clarity.",
            "Someone asked for the password manager master key.",
            "The CEO entered the room. Gravity returned.",
            "A lint error gently escorted the party outside.",
            "The coffee machine served a sobering error code.",
            "A code review comment contained the word 'actually.'",
            "The expense policy materialized in full legal font.",
            "The meeting recorder announced it was already running.",
        ]
        change = random.choices([1.0, 2.0, 3.0, 4.0, 5.0], weights=[35, 30, 20, 10, 5])[0]
        chart = self.query_one("#bac_chart", BACChart)

        if random.choice([True, False]):
            chart.current_bac = min(105.0, chart.current_bac + change)
            self.notify(random.choice(increase_messages), severity="warning")
        else:
            chart.current_bac = max(0.0, chart.current_bac - change)
            self.notify(random.choice(decrease_messages), severity="information")

        if chart.current_bac >= 100.0:
            self.exit(message="Liquidity Crisis! Memory Blackout triggered. Sent home & forced exit.")
            return

        self.schedule_random_bac_event()


if __name__ == "__main__":
    app = LiquidityCrisisApp()
    app.run()
