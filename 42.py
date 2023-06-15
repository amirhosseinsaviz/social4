import networkx as nx
import matplotlib.pyplot as plt

# بارگیری داده‌های گراف (فرضاً اطلاعات گراف در قالب لیست یال‌ها هستند)
G = nx.read_edgelist('friendster_data.txt')

# محاسبه ضریب خوشه‌ای برای هر گره در گراف
clustering_coefficients = nx.clustering(G)

# محاسبه توزیع ضریب خوشه‌ای
clustering_distribution = {}

for cc in clustering_coefficients.values():
    if cc in clustering_distribution:
        clustering_distribution[cc] += 1
    else:
        clustering_distribution[cc] = 1

# نمایش توزیع ضریب خوشه‌ای
plt.bar(clustering_distribution.keys(), clustering_distribution.values())
plt.xlabel('ضریب خوشه‌ای')
plt.ylabel('تعداد گره‌ها')
plt.title('توزیع ضریب خوشه‌ای')
plt.show()
