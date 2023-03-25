def find_pair(list_a):
    
    count = 0
    
    for i in range(len(list_a)):
        if list_a[i] == 'a':
            for j in range(i+1, len(list_a)):
                if list_a[j] == 'g':
                    count += 1
    return count
     
print(find_pair(['h','g','a','g','a','g','b','g']))


def find_pair_optimize(list_a):
    count_g = 0
    count_pair = 0
    n = len(list_a)
    for i in range (-1, -(n +1), -1):
        if list_a[i] == 'g':
            count_g += 1
        elif list_a[i] == 'a':
            count_pair += count_g
    return count_pair

print(find_pair_optimize(['h','g','a','g','a','g','b','g']))


