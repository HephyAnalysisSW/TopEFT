''' Class to hold a float and it's Gaussian uncertainty.
'''
from math import sqrt
import numbers

class u_float():

    def __init__(self,val,sigma=0):
        if type(val)==type(()):
            if not len(val)==2: 
                raise ValueError( "Not possible to construct u_float from tuple %r"%val )
            if not (isinstance(val[0], numbers.Number) and isinstance(val[1], numbers.Number)): 
                raise ValueError("Not a number among %r, %r"%val)
            self.val    = float(val[0])
            self.sigma  = float(val[1])
        elif type(val)==type({}):
            self.val = val['val']
            self.sigma = val['sigma']
        else:
            if not (isinstance(val, numbers.Number) and isinstance(sigma, numbers.Number)):
                raise ValueError( "Not a number among %r, %r"%(val, sigma) )
            self.val    = float(val)
            self.sigma  = float(sigma)

    @classmethod
    def fromString(cls, uString):
        s = uString.split('+-')
        if len(s) == 2:
            u = u_float(float(s[0]), float(s[1]))
        else:
            u = u_float(float(s[0]))
        return u

    def __add__(self,other):
        if not type(other)==type(self):
            if other == 0 or other == None: return self
            elif self == 0 or self == None: return other
            else: raise ValueError( "Can't add, two objects should be u_float but is %r."%(type(other)) )
        val = self.val+other.val
        sigma = sqrt(self.sigma**2+other.sigma**2)
        return u_float(val,sigma)

    def __iadd__(self,other):
        self = self + other
        return self

    def __radd__(self,other):
        return self + other

    def __sub__(self,other):
        if not type(other)==type(self):
            raise ValueError( "Can't add, two objects should be u_float but is %r."%(type(other)) )

        val = self.val-other.val
        sigma = sqrt(self.sigma**2+other.sigma**2)
        return u_float(val,sigma)

    def __mul__(self,other):
        if not ( isinstance(other, numbers.Number) or type(other)==type(self)):
            raise ValueError( "Can't multiply, %r is not a float, int or u_float"%type(other) )
        if type(other)==type(self):
            val = self.val*other.val
            sigma = sqrt((self.sigma*other.val)**2+(self.val*other.sigma)**2)
        elif isinstance(other, numbers.Number):
            val = self.val*other
            sigma = self.sigma*other
        else:
            raise NotImplementedError("This should never happen.")
        return u_float(val,sigma)

    def __rmul__(self,other):
        return self.__mul__(other)

    def __div__(self,other):
        if not ( isinstance(other, numbers.Number) or type(other)==type(self)):
            raise ValueError( "Can't divide, %r is not a float, int or u_float"%type(other) )
        if type(other)==type(self):
            val = self.val/other.val
            sigma = (1./other.val)*sqrt(self.sigma**2+((self.val*other.sigma)/other.val)**2)
        elif isinstance(other, numbers.Number):
            val = self.val/other
            sigma = self.sigma/other
        else:
            raise NotImplementedError("This should never happen.")
        return u_float(val,sigma)

    def __lt__(self,other):
        if type(other)==type(self):             return self.val < other.val
        elif isinstance(other, numbers.Number): return self.val < other
        else:                                   raise ValueError("Can only compare with u_float, float or int, got %r" % type(other))

    def __gt__(self,other):
        if type(other)==type(self):             return self.val > other.val
        elif isinstance(other, numbers.Number): return self.val > other
        else:                                   raise ValueError("Can only compare with u_float, float or int, got %r" % type(other))

    def __eq__(self,other): return not self < other and not self > other
    def __ge__(self,other): return not self < other
    def __le__(self,other): return not self > other
    def __ne__(self,other): return self < other or self > other

    def __abs__(self): return u_float(abs(self.val), self.sigma)

    def __str__(self):
        return str(self.val)+'+-'+str(self.sigma)

    def __repr__(self):
        return self.__str__()
