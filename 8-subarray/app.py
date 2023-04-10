# WAP to print all subarray in given list (Array)


def print_sub_array(l):
    n = len(l)

    for start in range(n):
        for end in range(start, n):
            for k in range(start ,end+1):
                print(l[k], end=" ")
            print()

l = [1,2,3,4]

print_sub_array(l)

# TC => O(N**3), SC => O(1)

print("###################################")
#===========================================================================================
# WAP to print all sum of subarray in given list (Array)
#===========================================================================================
def print_sum_of_sub_array(l):
    n = len(l)

    for start in range(n):
        for end in range(start, n):
            total = 0
            for k in range(start ,end+1):
                total += l[k]
            print(total)

l = [1,2,3,4]
print_sum_of_sub_array(l)

# TC => O(N**3), SC => O(1)

