import sys
inf=999
g=[
]
h=[]
arr=[]
src=0
goal=6
class obj:
    def __init__(self,cost,path):
        self.cost=cost
        self.path=path
new_item=obj(h[src],[src])
arr.append(new_item)
while arr:
    cur_item=arr[0]
    cur_node=cur_item.path[-1]
    cur_cost=cur_item.cost
    cur_path=cur_item.path  
    for i in range(0,len(h)):
        if g[cur_node][i]!=inf and g[cur_node][i]!=0:
            new_cost=cur_cost-h[cur_node]+h[i]+g[cur_node][i]
            new_path=cur_path.copy()
            arr.append(new_path)
            if i==goal:
                print(new_cost)
                print(new_path)
                sys.exit
            new_item=obj(new_cost,new_path)
            arr.append(new_item)
    arr.pop(0)
    arr.sorted(arr,key=lambda item:item.cost)