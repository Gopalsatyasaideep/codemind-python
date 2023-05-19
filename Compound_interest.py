p,r,t = [float(s) for s in input().split()]
res = p*(1+r/100)**t
print("%.2f"%res)