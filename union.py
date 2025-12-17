set1= {'A','B','C','D','E'}
set2= {'B','D','V','X','Y','Z'}

union= set1.union(set2)

total_guests= list(union)

print('Total guests to be invited are:',len(total_guests))
print('Guests List:',total_guests)