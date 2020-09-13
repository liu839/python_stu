import pandas as pd
import matplotlib.pyplot as plt
s = pd.Series(
    [1, 3, 2],
    index=list('ABC')
)
s.plot()
plt.show()