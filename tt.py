import csv
f = open('main1.csv','r')
r = csv.reader(f)
l = []
p = []
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
m = []
j = []
data = list(r)
for row in data:
    l.append(row[0])
    p.append(row[1])
    a.append(row[2])
    b.append(row[3])
    c.append(row[4])
    d.append(row[5])
    e.append(row[6])
    f.append(row[7])
    g.append(row[8])
    h.append(row[9])
    m.append(row[10])
    j.append(row[11])
for i in range(len(l)):
    if(int(l[i])%10 == 0 and int(l[i])< 2010):
        print(l[i],p[i+9],a[i+9],b[i+9],c[i+9],d[i+9],e[i+9],f[i+9],h[i+9],m[i+9],j[i+9])
