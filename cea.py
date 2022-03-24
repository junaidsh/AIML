import csv
csvfile=open('','r')
reader=csv.reader(csvfile)
a=[]
for row in reader:
    a.append(row)
    print(row)
num_attr=len(a[0])-1
print("initial hypo")
s=['o']*num_attr
g=['?']*num_attr
print("specific hypo",s)
print("generic hypo",g)
temp=[]
for i in range(0,len(a)):
    if a[i][num_attr]=='yes':
        for j in range(0,num_attr):
            if s[j]!=a[i][j]:
                s[j]='?'
        for j in range(0,num_attr):
            for k in range(1,len(temp)):
                if temp[k][j]!='?' and temp[k][j]!=s[j]:
                    del temp[k]
        print("for instance {0} the hypo s{0}".format(i+1),s)
        if len(temp)==0:
            print("for instance {0} the hypo g{0}".format(i+1),g)
        else:
            print("for instance {0} the hypo g{0}".format(i+1),temp)    
    if a[i][num_attr]=='no':
        for j in range(0,num_attr):
            if a[i][j]!=s[j] and s[j]!='?':
                g[j]=s[j]
                temp.append(g)
                g=['?']*num_attr
        print("for instance {0} the hypo s{0}".format(i+1),s)
        print("for instance {0} the hypo s{0}".format(i+1),temp)
