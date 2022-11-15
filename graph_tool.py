import matplotlib.pyplot as plt
import get_list

def graph_default(): # default call for a graph, demonstrative purposoes
    thisList = get_list.get_ordered_list(True, 20, 4, 1)

    print(thisList)
    plt.plot(thisList[0], thisList[1], 'o--')
    plt.show()