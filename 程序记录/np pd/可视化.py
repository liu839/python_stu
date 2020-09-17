import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
""" s = pd.Series(
    [1, 3, 2],
    index=['A', 'B', 'C']
) """
s = pd.Series(np.random.randn(1000))
#s.plot.kde()
#s.plot.density()
df = pd.DataFrame(np.random.randn(1000, 2), columns=['X', 'Y'])
df.plot.scatter(x="X", y="Y")
#df.plot.hexbin(x="X", y="Y", gridsize=8)# 六角箱图
plt.show()