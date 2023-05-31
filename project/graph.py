import pyqtgraph as pg
from currency import Currency
from constants import (
    CURRENCIES_NAMES,
    BRUSHES,
)


class Graph:
    def __init__(self):
        self.plt = pg.PlotWidget

    def start(self, title: str):
        self.plt = pg.plot(title=title)
        self.plt.setBackground("w")
        self.plt.showGrid(x=True, y=True)
        self.plt.addLegend()

    def draw(self, iteration: int, currencies: list[Currency]):
        if iteration == 1:
            for index, cur in enumerate(currencies):
                item = pg.BarGraphItem(x=[iteration], y=[cur.predict()], width=0.5, height=1, brush=BRUSHES[index],
                                       name=CURRENCIES_NAMES[index])
                self.plt.addItem(item)
        else:
            for index, cur in enumerate(currencies):
                item = pg.BarGraphItem(x=[iteration], y=[cur.predict()], width=0.5, height=1, brush=BRUSHES[index])
                self.plt.addItem(item)

    @staticmethod
    def close():
        pg.exit()
