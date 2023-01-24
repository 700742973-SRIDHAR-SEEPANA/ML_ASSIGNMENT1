#Question3
#Tuple creation
sisters=('tina','emily','dolly')
brothers=('john','travour','hitesh')
#tuples joining
siblings=sisters+brothers
print("Siblings: ",siblings)
#siblings length
print("Total Siblings: ",len(siblings))
fam=list(siblings)
fam.append('Natalie')
fam.append('Shane')
family_members=tuple(fam)
print("Family members: ",family_members)