

import matplotlib.pyplot as plt
import json

l1 = json.load(open('cent_hist.json', 'r'))
dictionary = dict(l1)
xAxis = [key for key, value in dictionary.items()]
yAxis = [value for key, value in dictionary.items()]
plt.grid(True)

## LINE GRAPH ##
plt.plot(xAxis,yAxis, color='maroon', marker='o')
plt.xlabel('variable')
plt.ylabel('value')


plt.show()
