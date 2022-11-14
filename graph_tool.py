import matplotlib.pyplot as plt
import get_list


thisList = get_list.get_ordered_list(1,True)

print(thisList)
plt.plot(thisList[0], thisList[1])
plt.show()