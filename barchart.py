
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('new', 'year', 'today', 'engagements', 'students', 'held', 'life', 'two', 'power', 'case')
y_pos = np.arange(len(objects))
performance = [160,111,97,85,73,68,65,64,62,57]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Count')
plt.title('')
 
plt.show()