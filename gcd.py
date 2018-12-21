def gcd(a,b):
  while ( a!=0):
    r=b%a
    b=a
    a=r
  return b
print(gcd(62,96))
print(gcd(12,14))
