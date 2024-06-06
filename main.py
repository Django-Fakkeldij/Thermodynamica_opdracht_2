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


def vraag1e(p1=120, T2=5):
    p2 = PropsSI("P", "T", T2 + 273.15, "Q", 1, "CO2") / 1e5  # kPa to bar
    return p1 / p2


def vraag1g(T1=5, T2=130, p2=120 * 1e5):
    h1 = PropsSI("H", "T", T1 + 273.15, "Q", 1, "CO2")
    s1 = PropsSI("S", "T", T1 + 273.15, "Q", 1, "CO2")
    h2 = PropsSI("H", "T", T2 + 273.15, "P", p2, "CO2")
    s2_s = s1
    h2_s = PropsSI("H", "S", s2_s, "P", p2, "CO2")
    return ((h2_s - h1) / (h2 - h1)) * 100  # Naar %


def vraag1h(T2=130, T3=35, p2=120 * 1e5, Q_dot_out=-50 * 1e6):
    h2 = PropsSI("H", "T", T2 + 273.15, "P", p2, "CO2")

    h3 = PropsSI("H", "T", T3 + 273.15, "P", p2, "CO2")
    return -Q_dot_out / (h2 - h3)


p("1b", vraag1b())
p("1c", 330)
p("1d", "D")
p("1e", vraag1e())
p("1f", "C")
p("1g", vraag1g())
p("1h", vraag1h())
