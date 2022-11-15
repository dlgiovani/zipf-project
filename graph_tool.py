import matplotlib.pyplot as plt
import get_list
from fractions import Fraction

def graph_default(): # default call for a graph, demonstrative purposoes
    thisList = get_list.get_ordered_list(True, 20, 0, 1)

    plt.plot(thisList[0], thisList[1], 'o--')
    for i in range(len(thisList[0])):
        plt.text(thisList[0][i], thisList[1][i]+20, str(thisList[1][i]))
        plt.text(thisList[0][i], thisList[1][i]+100, Fraction(thisList[1][i], thisList[1][0]))
    plt.show()