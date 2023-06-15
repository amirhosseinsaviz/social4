import networkx as nx
import matplotlib.pyplot as plt
# بارگیری داده‌های گراف (فرضاً اطلاعات گراف در قالب لیست یال‌ها هستند)
G = nx.read_edgelist('friendster_data.txt')

# محاسبه درجه هر گره در گراف
degrees = [d for n, d in G.degree()]

# محاسبه توزیع درجه
degree_distribution = nx.degree_histogram(G)

# نمایش توزیع درجه
plt.bar(range(len(degree_distribution)), degree_distribution)
plt.xlabel('درجه')
plt.ylabel('تعداد گره‌ها')
plt.title('توزیع درجه')
plt.show()
