# Write your code here
total = 0
    print(len(a))
    m = (pow(10,9)+7)
    for i,j in enumerate(a):
        lst = sorted(a[:i+1])
        r_list = range(1,i+2)
        total += sum(list(map(mul,lst,r_list)))
        # for x,y in zip(lst,r_list):
            # total += x*y
    print(total)
    return total % m
