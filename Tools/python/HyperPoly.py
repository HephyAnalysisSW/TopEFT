''' 
Multi-dimensional polonomial parametrization.

Given a list of values w for data-points (c1, ..., cN) in the form  
[ (w, c1, ..., cN), ... ]
a polyonomial parametrization
w(c) = w_0 + w_i c_i + w_ij c_ij + ... 
is constructed. The w_0, w_i, w_ij, ... are defined by the chi2 minimum.

Math:

Write a polyonimal parametrization as w(c) = w_0 + w_i c_i + w_ij c_ij + w_ijk c_ijk + ...
where ijkl... is summed over all combinations with repetitions.
Define the notation: < ijk > = 1/N sum_data( c_i*c_j*c_k ) etc.
Now differentiate chi2 = <(w - wEXT)**2> wrt to the w_0, w_i, ...
This gives equations of the form
< ( w - wEXT ) >  = 0    
< ( w - wEXT ) m >  = 0  
< ( w - wEXT ) mn >  = 0 
... etc.

up to 2nd order:
1. w_0      + w_i <i>   + w_ij <ij>   - < wEXT >    = 0 
2. w_0 <m>  + w_i <im>  + w_ij <ijm>  - < wEXT m >  = 0
3. w_0 <mn> + w_i <imn> + w_ij <ijmn> - < wEXT mn > = 0

up to 4nd order:
1. < ( w - wEXT ) >  = 0         w_0        + w_i <i>     + w_ij <ij>     + w_ijk <ijk>     + w_ijkl <ijkl>     = <wEXT >
2. < ( w - wEXT ) m >  = 0       w_0 <m>    + w_i <im>    + w_ij <ijm>    + w_ijk <ijkm>    + w_ijkl <ijklm>    = <wEXT m>
3. < ( w - wEXT ) mn >  = 0      w_0 <mn>   + w_i <imn>   + w_ij <ijmn>   + w_ijk <ijkmn>   + w_ijkl <ijklmn>   = <wEXT mn>
4. < ( w - wEXT ) mno >  = 0     w_0 <mnk>  + w_i <imnk>  + w_ij <ijmnk>  + w_ijk <ijkmno>  + w_ijkl <ijklmno>  = <wEXT mno>
5. < ( w - wEXT ) mnop >  = 0    w_0 <mnkl> + w_i <imnkl> + w_ij <ijmnkl> + w_ijk <ijkmnop> + w_ijkl <ijklmnop> = <wEXT mnop>

The class implements the general case of a n-th order polynomial.
'''

# Logger
import logging
logger = logging.getLogger(__name__)

# General imports
import operator
import numpy as np
import scipy.special
import itertools

# Helpers
from TopEFT.Tools.helpers import timeit as timeit

class HyperPoly:

    min_abs_float = 1e-14

    @staticmethod
    def get_ndof( nvar, order ):
        ''' Compute the number of d.o.f. of the polynomial by summing up o in the formula for combinations with repetitions of order o in nvar variables'''
        return sum( [ int(scipy.special.binom(nvar + o - 1, o)) for o in xrange(order+1) ] )

    # Initialize with data ( w, c1, ..., cN )
    def __init__( self, data, order):

        # Make sure dimensionality of data is consistent
        if not len(set( map( len, data ) )) == 1:
            raise ValueError( "Input data is not consistent. Need a list of iterables of the same size." )

        # Length of the dataset
        self.N   = len( data )
        # Values 
        self.w   = map( lambda x:operator.getitem(x,0), data )
        # Coordinates
        self.c   = map( lambda x:operator.getitem(x,slice(1,None)), data )
        # Number of variables
        self.nvar = len( data[0] ) - 1

        logger.debug( "Make parametrization of polynomial in %i variables to order %i" % (self.nvar, order ) )

        # We have Binomial( n + o - 1, o ) coefficients for n variables at order o
        #ncoeff = {o:int(scipy.special.binom(self.nvar + o - 1, o)) for o in xrange(order+1)}
        # Total number of DOF
        self.ndof = HyperPoly.get_ndof( self.nvar, order )
        # Order of combinations (with replacements) and ascending in 'order'
        self.combination  = {}
        counter = 0
        for o in xrange(order+1):
            for comb in itertools.combinations_with_replacement( xrange(self.nvar), o ):
                self.combination[counter] = comb
                counter += 1

        # Now we solve A.x = b for a system of dimension DOF
        # Fill b
        b = np.array( [ self.wEXT_expectation( self.combination[d] ) for d in range(self.ndof) ] )
        # Fill A
        A = np.empty( [self.ndof, self.ndof ] )
        for d in range(self.ndof):
            for e in range(self.ndof):
                if d > e:
                    A[d][e] = A[e][d]
                else:
                    A[d][e] = self.expectation(self.combination[d] + self.combination[e]) 

        #print A
        #print b
        # Solve
        #self.w_coeff = timeit(np.linalg.solve)(A, b)
        self.w_coeff = np.linalg.solve(A, b)

    def wEXT_expectation(self, combination ):
        ''' Compute <wEXT ijk...> = 1/Nmeas Sum_meas( wEXT_meas*i_meas*j_meas*k_meas... )
        '''
        return sum( [ self.w[n]*np.prod( [ self.c[n][elem] for elem in combination ] ) for n in xrange(self.N) ] ) / float(self.N)

    def expectation(self, combination ):
        ''' Compute <wEXT ijk...> = 1/Nmeas Sum_meas( i_meas*j_meas*k_meas... )
        '''
        return sum( [ np.prod( [ self.c[n][elem] for elem in combination ] ) for n in range(self.N) ]) / float(self.N)

    def eval( self, *args ):
        ''' Evaluate parametrization
        '''
        if not len(args) == self.nvar:
            raise ValueError( "Polynomial degree is %i. Got %i arguments." % (self.nvar, len(args) ) )
        return sum( self.w_coeff[n] * np.prod( [ args[elem] for elem in self.combination[n] ] ) for n in range(self.ndof) ) 
    
    def chi2( self ):
        return sum( [ (self.eval(*self.c[n]) - self.w[n])**2 for n in range(self.N) ] )
    
    def chi2_ndof( self ):
        return self.chi2()/float(self.ndof)
         
    def root_func_string(self):
        substrings = []
        for n in range(self.ndof):
            if abs(self.w_coeff[n])>self.min_abs_float:
                sub_substring = []
                if abs(1-self.w_coeff[n])>self.min_abs_float:
                    sub_substring.append( ('%f'%self.w_coeff[n]).rstrip('0') )
                for var in range(self.nvar):
                    power = self.combination[n].count( var )
                    if power>0:
                        sub_substring.append( "x%i" % var if power==1 else "x%i**%i" % (var, power)  )
                substrings.append( "*".join(sub_substring) ) 
        return  ( "+".join( filter( lambda s: len(s)>0, substrings) ) ).replace("+-","-")

if __name__ == "__main__":
    def f(x,y,z):
        return (x+y-z)**3 
    data = [ (f(x,y,z),x,y,z) for x in range(-3,3) for y in range(-3,3) for z in range( -3,3)]
    # 3rd order parametrization
    p = HyperPoly( data, 3)
    print "chi2/ndof", p.chi2_ndof()
    print "String:", p.root_func_string()

    #def f(x):
    #    return x 
    #data = [ (f(x),x) for x in range(0,5) ]
    #p = HyperPoly( data, 1)
