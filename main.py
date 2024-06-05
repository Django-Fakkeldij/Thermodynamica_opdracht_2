import matplotlib.pyplot as plt
import numpy as np
from CoolProp.CoolProp import PropsSI


def p(vraag, *args):
    print(f"vraag {vraag}:", *args)


def vraag1a(T_h=90 + 273.15, T_c=10 + 273.15):
    return T_h / (T_h - T_c)


p("1a", vraag1a())


def vraag1b(Q_dot_out=50.0):
    COP = vraag1a()
    W_out = Q_dot_out / COP  # MW
    return W_out


def vraag1e(p1=120, T4=5):
    p4 = PropsSI("P", "T", T4 + 273.15, "Q", 1, "CO2") / 100_000  # kPa to bar
    return p1 / p4


def vraag1g(T1=130, T4=5):
    h4 = PropsSI("H", "T", T4 + 273.15, "Q", 1, "CO2")
    print(h4)
    h1 = PropsSI("H", "T", T1 + 273.15, "Q", 1, "CO2")
    print(h1)
    return


p("1b", vraag1b())
p("1c", 330)
p("1d", "D")
p("1e", vraag1e())
p("1f", "C")
p("1g", vraag1g())
