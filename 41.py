import networkx as nx
import matplotlib.pyplot as plt

# بارگیری داده‌های گراف (فرضاً اطلاعات گراف در قالب لیست یال‌ها هستند)
G = nx.read_edgelist('friendster_data.txt')

# محاسبه اجزای قابل متصل بزرگتر (WCC)
wccs = list(nx.weakly_connected_components(G))
wcc_sizes = [len(wcc) for wcc in wccs]

# محاسبه توزیع اندازه WCC
wcc_size_distribution = {}

for size in wcc_sizes:
    if size in wcc_size_distribution:
        wcc_size_distribution[size] += 1
    else:
        wcc_size_distribution[size] = 1

# نمایش توزیع اندازه WCC
plt.bar(wcc_size_distribution.keys(), wcc_size_distribution.values())
plt.xlabel('اندازه WCC')
plt.ylabel('تعداد WCCs')
plt.title('توزیع اندازه WCC')
plt.show()
