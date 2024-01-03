print("Example 1================")
i = 1
for item in ['a','b','c','d']:
    print(i, item,sep=".")
    i += 1

print("Example 2================")
for i,item in enumerate(['a','b','c','d'],1):
    print(i,item,sep=".")

