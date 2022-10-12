
import matplotlib.pyplot as plt
import pandas as pd
from base import read_rows


# Funciones de grafico

def grafica1(stock):
    data = read_rows(stock)


    df = pd.DataFrame(data)
    df = df.set_index(0)

    plt.subplot(231)
    plt.title("Volumen")
    plt.plot(df[1], label="Volumen", color="green")
    plt.xlabel('Fecha')
    plt.ylabel('Volumen')
    plt.legend()


    plt.subplot(232)
    plt.title("Val_W")
    plt.plot(df[2], label="Val_W", color="red")
    plt.xlabel('Fecha')
    plt.ylabel('Val_W')
    plt.legend()

    plt.subplot(233)
    plt.title("Open")
    plt.plot(df[3], label="Open", color="orange")
    plt.xlabel('Fecha')
    plt.ylabel('Open')
    plt.legend()

    plt.subplot(234)
    plt.title("Close")
    plt.plot(df[4], label="Close", color="blue")
    plt.xlabel('Fecha')
    plt.ylabel('Close')
    plt.legend()

    plt.subplot(235)
    plt.title("High")
    plt.plot(df[4], label="Higt", color="orange")
    plt.xlabel('Fecha')
    plt.ylabel('High')
    plt.legend()

    plt.subplot(236)
    plt.title("Low")
    plt.plot(df[6], label="Low", color="blue")
    plt.xlabel('Fecha')
    plt.ylabel('Low')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    #grafica1()
    pass

