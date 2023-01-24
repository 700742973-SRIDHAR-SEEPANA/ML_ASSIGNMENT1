#Question4
it_companies={'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A={19, 22, 24, 20, 25, 26}
B={19, 22, 20, 25, 26, 24, 28, 27}
age=[22, 19, 24, 25, 26, 24, 25, 24]
print("Length of IT Companies: ",len(it_companies))
#adding  new company Twitter
it_companies.add('Twitter')
multi=['TCS','Infy','Reuters']
#Updating Companies
it_companies.update(multi)
print("Updated list of Companies: ",it_companies)
#removing company
it_companies.remove('Amazon')
print("List after removal:", it_companies)
#joining tuples
print("Join A and B: ",A.union(B))
#intersection of tuples
print("A intersection B: ",A.intersection(B))
#subset check
print("Is A subset of B: ",A.issubset(B))
#Disjoint check
print("Are A and B disjoint sets: ",A.isdisjoint(B))
print("JOining A with B: ",A.union(B))
print("JOining B with A: ",B.union(A))
#Symmetric diff
print("Symmetric diff between A and B: ",A.symmetric_difference(B))
#deleting
del A
del B
#list compare
ages=set(age)
print("Set Length: ",len(ages))
print("List Length: ", len(age))