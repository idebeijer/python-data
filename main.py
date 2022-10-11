import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from data_reader import get_team_data

plt.style.use('_mpl-gallery')

data = get_team_data()

profits = []
team_ids = []

for i in range(len(data)):
  if i == 0: #FIXME: this is a hack
    continue
  profits.append(math.floor(data[i]['total_profit_with_discount']))
  team_ids.append(data[i]['team_id'])


print(profits)

ypos = np.arange(len(profits))

plt.xticks(ypos, team_ids)
plt.bar(ypos, profits)
plt.subplots_adjust(left=0.3, bottom=0.1)
# fig, axes = plt.subplots(1, 1)

plt.show()
