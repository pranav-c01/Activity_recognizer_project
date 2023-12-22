import os
import csv
le,ke = [],[]
count=1
reader = csv.reader(open("bending2\dataset4.csv", "r"), delimiter=' ')
for r in reader:
    if count>5:
        # print(r)
        le.append(r[:6])
    count+=1
# for i in le:
#     ke.append(i.replace(" ",","))
# print(ke)
writer = csv.writer(open("ok.csv", "w"))
# with open("ok.csv",'w') as f:
#     print(f.writelines(le))
# for i in le:
writer.writerows(le)
# print(le)
print(le)