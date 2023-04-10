#===========================================================================================
# WAP to print all sum of subarray in given list (Array) , code should be optimize
#===========================================================================================

def sum_of_sub_array_optimize(l):
    n = len(l)
    psum = [None] * n
    psum[0]=l[0]
    for i in range(1, n):
        psum[i]=psum[i-1]+l[i]

    print(psum) # First step to get prefix sum array

    for l in range(n):
        
        for r in range(l, n):
            total=0
            if l == 0:
                total = psum[r]
                print(total)
            else:
                total = psum[r]-psum[l-1]
                print(total)
            
    

sum_of_sub_array_optimize(l=[1,2,3,4])

print("===========================================================")

## TC => O(N**2), SC => O(n)

def sum_array_optimize(l):
    for i in range(len(l)):
        total = 0
        for j in range(i, len(l)):
            total += l[j]
            print(total)


sum_array_optimize(l=[1,2,3,4])

## TC => O(N**2), SC => O(1)

print("===========================================================")