import networkx as nx
import matplotlib.pyplot as plt

# بارگیری داده‌های گراف (فرضاً اطلاعات گراف در قالب لیست یال‌ها هستند)
G = nx.read_edgelist('friendster_data.txt')

# محاسبه اندازه گره‌های مرکزی k-core
k_core_sizes = nx.core_number(G).values()
k_core_size_distribution = {}

for size in k_core_sizes:
    if size in k_core_size_distribution:
        k_core_size_distribution[size] += 1
    else:
        k_core_size_distribution[size] = 1

# نمایش توزیع اندازه گره‌های مرکزی k-core
plt.bar(k_core_size_distribution.keys(), k_core_size_distribution.values())
plt.xlabel('اندازه گره‌های مرکزی k-core')
plt.ylabel('تعداد گره‌ها')
plt.title('توزیع اندازه گره‌های مرکزی k-core')
plt.show()
