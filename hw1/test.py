# arr = [['Ant-v2' , 3399.58 , 1002.88 , 0 ],
# ['Ant-v2' , 3782.06 , 996.20 , 1],
# ['Ant-v2' , 2560.81 , 1523.31 , 2],
# ['Ant-v2' , 653.76 , 82.07 , 3],
# ['Ant-v2' , 407.37 , 8.96 , 4],
# ['Humanoid-v2' , 234.90 , 42.00 , 0],
# ['Humanoid-v2' , 315.66 , 82.64 , 1],
# ['Humanoid-v2' , 136.86 , 4.28 , 2],
# ['Humanoid-v2' , 274.77 , 26.23 , 3],
# ['Humanoid-v2' , 303.04 , 28.10 , 4],
# ['Humanoid-v2' , 148.29 , 62.31  , 5 ]]

arr = [['Ant_v2'      , 0     , 3058.45 , 1239.93    , 4713.65  , 3058.45 ],
['Ant_v2'      , 1     , 4397.26 , 81.88      , 4713.65  , 3058.45 ],
['Ant_v2'      , 2     , 4452.55 , 92.50      , 4713.65  , 3058.45 ],
['Ant_v2'      , 3     , 4435.35 , 101.54     , 4713.65  , 3058.45 ],
['Ant_v2'      , 4     , 4572.44 , 137.91     , 4713.65  , 3058.45 ],
['Ant_v2'      , 5     , 4749.03 , 53.57      , 4713.65  , 3058.45 ],
['Ant_v2'      , 6     , 4602.54 , 103.69     , 4713.65  , 3058.45 ],
['Ant_v2'      , 7     , 4511.01 , 68.12      , 4713.65  , 3058.45 ],
['Ant_v2'      , 8     , 4520.42 , 90.11      , 4713.65  , 3058.45 ],
['Ant_v2'      , 9     , 4158.92 , 1106.38    , 4713.65  , 3058.45 ],
['Humanoid_v2' , 0     , 308.41  , 80.59      , 10344.52 , 308.41  ],
['Humanoid_v2' , 1     , 211.53  , 20.57      , 10344.52 , 308.41  ],
['Humanoid_v2' , 2     , 288.05  , 30.61      , 10344.52 , 308.41  ],
['Humanoid_v2' , 3     , 283.95  , 50.21      , 10344.52 , 308.41  ],
['Humanoid_v2' , 4     , 288.75  , 20.02      , 10344.52 , 308.41  ],
['Humanoid_v2' , 5     , 211.00  , 68.34      , 10344.52 , 308.41  ],
['Humanoid_v2' , 6     , 314.12  , 20.39      , 10344.52 , 308.41  ],
['Humanoid_v2' , 7     , 267.35  , 18.52      , 10344.52 , 308.41  ],
['Humanoid_v2' , 8     , 301.39  , 22.22      , 10344.52 , 308.41  ],
['Humanoid_v2' , 9     , 251.84  , 14.23      , 10344.52 , 308.41  ]]
import matplotlib.pyplot as plt
import numpy as np

env_dict = {}
for env, epoch, ret, std, expert, bc in arr:
        if env not in env_dict:
                env_dict[env] = {}
                env_dict[env]['mean'] = []
                env_dict[env]['std'] = []
                env_dict[env]['epoch'] = []
                env_dict[env]['bc'] = []
                env_dict[env]['expert'] = []
        env_dict[env]['mean'].append(ret)
        env_dict[env]['std'].append(std)
        env_dict[env]['expert'].append(expert)
        env_dict[env]['bc'].append(bc)
        env_dict[env]['epoch'].append(epoch)

for key in env_dict:
        plt.figure()
        x = env_dict[key]['epoch']
        y = env_dict[key]['mean']
        e = env_dict[key]['std']
        bc = env_dict[key]['bc']
        ex = env_dict[key]['expert']
        plt.errorbar(x, y, e, marker='^', label='BC + DAgger')

        plt.plot(x, bc, label='BC ')
        plt.plot(x, ex, label='Expert Policy')

        plt.xlabel('Epochs')
        plt.ylabel('Return')
        plt.legend()
        plt.title(key + ': DAgger')
        plt.show()