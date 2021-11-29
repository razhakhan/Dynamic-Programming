inf=100000
res=[]

def findsol(v,den,n):
    if(v==0):
        print(*res)
        return
    for i in range(n):
        if( (v-den[i]>=0) and dp[n][v-den[i]]+1==dp[n][v] ):
            res.append(den[i])
            findsol(v-den[i], den, n)
            break

t=int(input())
for z in range(t):
    v,n=map(int, input().split())
    den=[int(x) for x in input().split()]
    
    dp=[[0 for x in range(v+1)] for y in range(n+1)] 
    
    for i in range(0,n+1):
        for j in range(0, v+1):
            
            if(j==0):
                dp[i][j]=0
                
            elif(i==0):
                dp[i][j]=inf
                
            elif(den[i-1]>j):
                dp[i][j]=dp[i-1][j]
                
            else:
                dp[i][j]=min( 1+dp[i][j-den[i-1]], dp[i-1][j] )
                
    if(dp[n][v]>=inf):
        print("-1")
    else:
        findsol(v,den,n)
        print(dp[n][v])

'''
input 
1
7 2
2 1
output
2 2 2 1
4
'''

'''
Algorithm :
Initialize an auxiliary array dp[], where dp[i] will store the minimum number of coins needed to make sum equals to i.
Find the minimum number of coins needed to make their sum equals to v using the approach discussed in this article.
After finding the minimum number of coins use the Backtracking Technique to track down the coins used, to make the sum equals to v.
In backtracking, traverse the array and choose a coin which is smaller than the current sum such that dp[v] equals to dp[v – chosen_coin]+1. Store the chosen coin in an array.
After completing the above step, backtrack again by passing the v as (v – chosen coin value).
After finding the solution, print the array of chosen coins.
'''
