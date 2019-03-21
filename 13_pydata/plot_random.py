# date: 2019/03/21 8:16 PM
# author: fanchuang
# github: https://github.com/buxuele/
# email: baogebuxuele@163.com
"""about:
1. visualizing random.random
# pip3 install seaborn matplotlib
# sudo apt-get install python3-tk
"""

import random
import matplotlib.pyplot as plt
import seaborn as sbn


data = [random.random() for x in range(1, 100000)]
sbn.distplot(data, kde=False, color='blue')
plt.show()



