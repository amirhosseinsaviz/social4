import networkx as nx
import matplotlib.pyplot as plt
# بارگیری داده‌های گراف (فرضاً اطلاعات گراف در قالب لیست یال‌ها هستند)
G = nx.read_edgelist ('friendster_data.txt')

# محاسبه میانگین درجه همسایگان برای هر گره در گراف
average_neighbour_degrees = {}

for node in G.nodes ():
    neighbours = G.neighbors (node)
    neighbour_degrees = [G.degree (neighbour) for neighbour in neighbours]

    if len (neighbour_degrees) > 0:
        avg_neighbour_degree = sum (neighbour_degrees) / len (neighbour_degrees)
        average_neighbour_degrees[node] = avg_neighbour_degree

# محاسبه توزیع میانگین درجه همسایگان
avg_neighbour_degree_distribution = {}

for avg_neighbour_degree in average_neighbour_degrees.values ():
    if avg_neighbour_degree in avg_neighbour_degree_distribution:
        avg_neighbour_degree_distribution[avg_neighbour_degree] += 1
    else:
        avg_neighbour_degree_distribution[avg_neighbour_degree] = 1

# نمایش توزیع میانگین درجه همسایگان
plt.bar (avg_neighbour_degree_distribution.keys (), avg_neighbour_degree_distribution.values ())
plt.xlabel ('میانگین درجه همسایگان')
plt.ylabel ('تعداد گره‌ها')
plt.title ('توزیع میانگین درجه همسایگان')
plt.show ()
