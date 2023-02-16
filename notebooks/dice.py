import random
#list to store results
results=[0,0,0,0,0,0]
total_rolls=1000
for i in range(total_rolls):
    #generate a random number
    roll=random.random()
    if roll<1/6:
        results[0]+=1
    elif roll<2/6:
        results[1]+=1
    elif roll<3/6:
        results[2]+=1
    elif roll<4/6:
        results[3]+=1
    elif roll<5/6:
        results[4]+=1
    else:
        results[5]+=1
#print the results
print("Face       Percentage")
print("----       ----------")
for i,j in enumerate(results):
    print(f"Face {i+1}: {j} ({j/total_rolls*100:.2f}%)")
