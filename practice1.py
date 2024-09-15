def co_valid_k(n,s):
  zer = s.count('0')    #count 0
  ones=n-zer            #then - the 0 countns value
  r=0
  for k in range(1,n+1):
    if k>=zer and (k-zer)%2==0:
      r+=1
    elif k>=ones and (k-ones)%2==0:
      r+=1
      return r

def main():
  import sys
  import = sys.stdin.read
  data=input().split()
  index=0
  t=int(data[index])
  index+=1
  results=[]
  for _ in range(t):
    n=int(data[index])
    index+=1
    results.append(cp_valid_(N,S))
  for r in results:
    print(n)
main()
