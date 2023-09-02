# Se coloca un capital C, a un interés I (que oscila entre 0 y 100),
# durante M años y se desea saber en cuanto se habrá convertido ese
# capital en “M” años, sabiendo que es acumulativo


def capital(capital, interes, anios):
    for i in range(0, anios):
        capital = capital * (1 + (interes / 100))
    return capital


print(capital(100, 50, 1))
