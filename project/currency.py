from constants import STEP
from random import random
from math import (
    log,
    cos,
    pi,
    sqrt,
)


class Currency:
    def __init__(self, value: float, drift: float, volatility: float):
        self.value: float = value
        self.drift: float = drift
        self.volatility: float = volatility

    def predict(self) -> float:
        self.value = self.value + self.value * (self.drift * STEP + self.volatility * sqrt(STEP) * self.get_normal_rv())
        return self.value

    def get_normal_rv(self) -> float:
        return sqrt(-2 * log(self.generator())) * cos(2 * pi * self.generator())

    @staticmethod
    def generator() -> float:
        return random()
