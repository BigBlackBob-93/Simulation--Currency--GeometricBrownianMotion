from timer import Timer
from currency import Currency
from objects import get_data
from graph import Graph


class Simulation:
    def __init__(self):
        self.timer: Timer = Timer()
        self.iteration: int = 0
        self.sensor: bool = False
        self.currencies: list[Currency] = []
        self.graph: Graph = Graph()

    def start(self):
        self.sensor = True
        self.currencies = get_data()
        self.graph.start(title="Simulation: Currency")
        self.timer.start(self.shot)

    def shot(self):
        self.iteration += 1
        self.draw()

    def draw(self):
        self.graph.draw(self.iteration, self.currencies)

    def check_state(self):
        if self.sensor:
            self.stop()
        else:
            self.start()

    def stop(self):
        self.timer.stop()
        self.iteration = 0
        self.sensor = False

    def close(self):
        self.graph.close()
