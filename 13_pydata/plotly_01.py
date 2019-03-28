# when: 2019/03/26 6:23 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. plot some data to graph, and stored as html-file
2. https://github.com/SayaliSonawane/Plotly_Offline_Python
"""

import plotly
import numpy as np
from plotly.graph_objs import Layout, Scatter

N = 500
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

trace = Scatter(x=random_x, y=random_y)
plotly.offline.plot({"data": [trace]})


