with open('input.txt', 'r+') as f:
    groups = [line.replace('\n','') for line in f.read().split("\n\n")]
    sum_of_counts = 0
    for g in groups:
        count = len(set(g))
        sum_of_counts = sum_of_counts + count
print(sum_of_counts)
    
