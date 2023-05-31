from objects import obj
from simulation import Simulation

simulation: Simulation = Simulation()


def run():
    simulation.check_state()


def close():
    simulation.close()


obj.objects.get('button')[0].clicked.connect(run)
obj.objects.get('button')[1].clicked.connect(close)
