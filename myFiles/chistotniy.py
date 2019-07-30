s1 = '''oh you touch my tralala mmm my ding ding dong'''
lst = [word for line in s1.split('\n') for word in line.split()]
print(sorted(set(lst), key=lambda x: (-lst.count(x), x)))
s2 = '''hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme'''
lst = [word for line in s2.split('\n') for word in line.split()]
print(sorted(set(lst), key=lambda x: (-lst.count(x), x)))
s3 = '''one two one tho three'''
lst = [word for line in s3.split('\n') for word in line.split()]
print(sorted(set(lst), key=lambda x: (-lst.count(x), x)))

