import random

# seed(a=None) Initializes the given random number seed. The default is the current system time
# Case:random.seed(10)

# random() Generate a random decimal between [0.0,1.0)
# Case:random.random

# randint(a,b)  Generate a random integer between [a,b]
#

# randrange(m,n[,k]) Generate a random integer between [m, n) in steps of k

# getrandbits(k) Generates a random integer with a length of k bits

# uniform(a,b) Generate a random decimal between [a,b]

# choice(seq) Select an element randomly from the sequence
print(random.choice([1,2,3,4,5,6,7,8,9]))

# shuffle(seq) Randomly arrange the elements in the sequence and return the disorganized sequence
s=[1,2,3,4,5,6,7,8,9,10,11]
random.shuffle(s)
print(s)