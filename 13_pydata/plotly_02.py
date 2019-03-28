# when: 2019/03/26 6:30 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. 

"""

import numpy as np
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode,\
    plot, iplot
import plotly.graph_objs as go


print(__version__)
plot([go.Scatter(x=[1, 2, 3], y=[3, 1, 6])])

init_notebook_mode(connected=True)
# ...




