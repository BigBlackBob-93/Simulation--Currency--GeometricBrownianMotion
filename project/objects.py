from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QDoubleSpinBox,
    QPushButton,
)
from base_object import Object
from constants import (
    CURRENCIES_NAMES,
    LEFT,
)
from currency import Currency

obj: Object = Object()

window: QMainWindow = obj.set_obj(
    object=QMainWindow(),
    title="Simulation: Currency",
)
obj.set_obj(
    object=QLabel(window),
    title='Initial',
)
obj.increase_indent()

for cur in CURRENCIES_NAMES:
    obj.set_obj(
        object=QLabel(window),
        title=cur,
        above=obj.indent,
        left=LEFT * 4,
    )
    obj.add_obj(
        obj.set_obj(
            object=QDoubleSpinBox(window),
            span=[0, 1000],
            step=0.01,
            value=50,
            left=LEFT * 6,
            above=obj.indent + 5,
        ),
        key='spinbox'
    )
    obj.increase_indent()
    obj.add_obj(
        obj.set_obj(
            object=QDoubleSpinBox(window),
            step=0.01,
            value=0,
            above=obj.indent + 5,
        ),
        key='spinbox'
    )
    obj.set_obj(
        object=QLabel(window),
        title=' - drift',
        above=obj.indent,
        case=0,
        left=LEFT * 4,
    )
    obj.increase_indent()
    obj.add_obj(
        obj.set_obj(
            object=QDoubleSpinBox(window),
            step=0.001,
            value=0.01,
            above=obj.indent + 5,
        ),
        key='spinbox'
    )
    obj.set_obj(
        object=QLabel(window),
        title=' - volatility',
        above=obj.indent,
        case=0,
        left=LEFT * 4,
    )
    obj.increase_indent(2)

obj.add_obj(
    obj.set_obj(
        object=QPushButton(window),
        title="Start/Stop",
        above=obj.indent,
    ),
    key='button'
)
obj.add_obj(
    obj.set_obj(
        object=QPushButton(window),
        title="Close",
        left=LEFT * 6,
        above=obj.indent,
    ),
    key='button'
)

window.show()


def get_data() -> list[Currency]:
    count = 0
    data: list[Currency] = []
    for i in range(len(CURRENCIES_NAMES)):
        data.append(
            Currency(
                value=obj.objects.get('spinbox')[i + count].value(),
                drift=obj.objects.get('spinbox')[i + count + 1].value(),
                volatility=obj.objects.get('spinbox')[i + count + 2].value()
            )
        )
        count += 2
    return data
