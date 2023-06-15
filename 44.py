import networkx as nx
import matplotlib.pyplot as plt

# بارگیری داده‌های گراف (فرضاً اطلاعات گراف در قالب لیست یال‌ها هستند)
G = nx.read_edgelist ('friendster_data.txt')

# محاسبه میانگین دوستان دوستان
average_friends_of_friends = {}

for node in G.nodes ():
    friends = set (G.neighbors (node))
    friends_of_friends = set ()

    for friend in friends:
        friends_of_friends.update (G.neighbors (friend))

    friends_of_friends.discard (node)

    if len (friends_of_friends) > 0:
        avg_friends_of_friends = len (friends_of_friends) / len (friends_of_friends)
        average_friends_of_friends[node] = avg_friends_of_friends

# محاسبه توزیع میانگین دوستان دوستان
avg_fof_distribution = {}

for avg_fof in average_friends_of_friends.values ():
    if avg_fof in avg_fof_distribution:
        avg_fof_distribution[avg_fof] += 1
    else:
        avg_fof_distribution[avg_fof] = 1

# نمایش توزیع میانگین دوستان دوستان
plt.bar (avg_fof_distribution.keys (), avg_fof_distribution.values ())
plt.xlabel ('میانگین دوستان دوستان')
plt.ylabel ('تعداد گره‌ها')
plt.title ('توزیع میانگین دوستان دوستان')
plt.show ()
