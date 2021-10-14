def kruskalMST(n, some_list):
    parent = []
    for i in range(n):
        parent.append(i)
    
    def find(parent, i):
        if parent[i] == i:
            return i
        else:
            parent[i] = find(parent, parent[i])
        return parent[i]
    
    def exsit_cycle(parent, n1, n2):
        n1 = find(parent, n1)
        n2 = find(parent, n2)
        
        if n1 == n2:
            return True
        else:
            return False
    
    def union(parent, n1, n2):
        n1 = find(parent, n1)
        n2 = find(parent, n2)
        if n1 <= n2:
            parent[n2] = n1
        else:
            parent[n1] = n2
        return parent
    
    some_list = sorted(some_list, key=lambda x: x[2])
    min_cost = 0
    for [n1, n2, w] in some_list:
        if not exsit_cycle(parent, n1, n2):
            min_cost += w
            parent = union(parent, n1, n2)
            print("{} -- {} == {}".format(n1, n2, w))
            print("parent: {}".format(parent))
            
    return min_cost

n = 4
some_list = [[0,1,10], [0,2,6], [0,3,5], [1,3,15], [2,3,4]]
min_cost = kruskalMST(n, some_list)
print("Minimum Spanning Tree: {}".format(min_cost))