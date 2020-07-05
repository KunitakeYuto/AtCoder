N=int(input())
List=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
for i in range(10):
    if List[i]-N >= 0:
        print(List[i]-N)
        quit()