    
def gcd(a,b):
    
    a,b = a,b
    if b>a:
        a,b = b,a 
    
    while b!= 0:
        a,b = b, a%b
    return a

def lcm(a, b):
    
    return (a * b)// gcd(a,b)
  


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))


