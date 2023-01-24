#Question1
from statistics import median
import math
ages=[19,22,19,24,20,25,26,24,25,24]
ages.sort()
print("Sorted: ",ages)
mini=min(ages)
ages.append(mini)
maxi=max(ages)
ages.append(maxi)
print("Appended: ",ages)
#Median
print("Median age:",median(ages))
#Average
print("Average age:",sum(ages)/len(ages))
#Range
print("Range :",max(ages)-min(ages))