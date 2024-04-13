

from math import*

def diag(a:str,b:str,c:str)->str:
  a,b,c = int(a),int(b),int(c)
  global d
  d = (a**2+b**2+c**2)**.5 
  return str(d)

def volume(a:str,b:str,c:str)->str:
  a,b,c = int(a),int(b),int(c)
  return str(a*b*c)

def surface_area(a:str,b:str,c:str)->str:
  a,b,c = int(a),int(b),int(c)
  return str(2*(a*b+a*c+b*c))

def alpha(a:str,d:str)->str:
  a, d = int(a),float(d)
  return str(degrees(acos(a/d)))

def beta(b:str,d:str)->str:
  b, d = int(b),float(d)
  return str(degrees(acos(b/d)))

def gamma(c:str,d:str)->str:
  c, d = int(c),float(d)
  return str(degrees(acos(c/d)))

def radius_described_sphere(d:str)->str:
  d = float(d)
  return str(d/2)

def volume_described_sphere(d:str)->str:
  d = float(d)
  return str((4/3)*pi*(d/2)**3)
