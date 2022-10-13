import calculator
import matplotlib.pyplot as plt

n = calculator.calcular_cont()
x = calculator.calcular_tonelaje()


def histograma_1():
    plt.title('Contenedores')
    plt.hist(x=n, bins=6, edgecolor='black',
             color='red',
             orientation='vertical',
             linewidth=2, rwidth=1)
    plt.grid(True)
    plt.show()


def histograma_2():
    plt.title('Tonelaje')
    plt.hist(x=x, bins=6, edgecolor='black',
             color='red',
             orientation='vertical',
             linewidth=2, rwidth=1)
    plt.grid(True)
    plt.show()

