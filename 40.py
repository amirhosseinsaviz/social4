import networkx as nx
import matplotlib.pyplot as plt

# بارگیری داده‌های گراف (فرضاً اطلاعات گراف در قالب لیست یال‌ها هستند)
G = nx.read_edgelist('friendster_data.txt')

# محاسبه توزیع طول مسیرها
path_lengths = dict(nx.all_pairs_shortest_path_length(G))
length_distribution = {}

for source, paths in path_lengths.items():
    for target, length in paths.items():
        if length in length_distribution:
            length_distribution[length] += 1
        else:
            length_distribution[length] = 1

# نمایش توزیع طول مسیرها
plt.bar(length_distribution.keys(), length_distribution.values())
plt.xlabel('طول مسیر')
plt.ylabel('تعداد مسیرها')
plt.title('توزیع طول مسیرها')
plt.show()
