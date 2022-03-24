import pandas as pd
from collections import Counter
import math
tennis=pd.read_csv('')
print("\nGiven dataset \n",tennis)
def entropy(alist):
    c=Counter(x for x in alist)
    instances=len(alist)
    prob=[x/10 for x in c.values]
    return sum(-p*math.log(p,2) for p in prob)
def information_gain(d,split,target):
    splitting=d.groupby(split)
    n=len(d.index)
    agent=splitting.agg({target:[entropy,lambda x:len(x)/n]})[target]
    agent.columns=['Entropy','Obsevations']
    new_entropy=sum(agent['Entropy']*agent['Obsevations'])
    old_entropy=entropy(d[target])
    return old_entropy-new_entropy
def id3(sub,target,a):
    count=Counter(x for x in sub[target])
    if len(count)==1:
        return next(iter(count))
    else:
        gain=[information_gain(sub,attr,target) for attr in a]
        print("Gain=",gain)
        maximum=gain.index(max(gain))
        best=a[maximum]
        tree={tree:{}}
        remaining=[i for i in a if i!=best]
        for val,subset in sub.groupby(best):
            subtree=id3(subset,target,remaining)
            tree[best][val]=subtree
        return tree
names=list(tennis.columns)
print("The attributes",names)
names.remove('playtennis')
print("The predicting attributes",names)
tree=id3(tennis,'plattennis',names)
print("the decision tree")
print(tree)