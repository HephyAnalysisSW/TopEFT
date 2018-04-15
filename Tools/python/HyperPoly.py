''' Multi-dimensional polonomial parametrization.
Given a list of values w for data-points (c1, ..., cN) in the form  
[ (w, c1, ..., cN), ... ]
a polyonomial parametrization
w(c) = w_0 + w_i c_i + w_ij c_ij + ... 
is constructed. The w_0, w_i, w_ij, ... are defined by the chi2 minimum.
'''

# Equations

#< ijk > = 1/N sum_data( c_i*c_j*c_k ) etc.

# chi2 = <(w - wEXT)**2>

# w(c) = w_0 + w_i c_i + w_ij c_ij + w_ijk c_ijk + ...

# < ( w - wEXT ) >  = 0    ->     w_0      + w_i <i>   + w_ij <ij>   - < wEXT >    = 0 -> w_0 = <wEXT> - w_i <i> - w_ij <ij>
# < ( w - wEXT ) m >  = 0  ->     w_0 <m>  + w_i <im>  + w_ij <ijm>  - < wEXT m >  = 0
# < ( w - wEXT ) mn >  = 0 ->     w_0 <mn> + w_i <imn> + w_ij <ijmn> - < wEXT mn > = 0

#1. < ( w - wEXT ) >  = 0         w_0        + w_i <i>     + w_ij <ij>     + w_ijk <ijk>     + w_ijkl <ijkl>     = <wEXT >
#2. < ( w - wEXT ) m >  = 0       w_0 <m>    + w_i <im>    + w_ij <ijm>    + w_ijk <ijkm>    + w_ijkl <ijklm>    = <wEXT m>
#3. < ( w - wEXT ) mn >  = 0      w_0 <mn>   + w_i <imn>   + w_ij <ijmn>   + w_ijk <ijkmn>   + w_ijkl <ijklmn>   = <wEXT mn>
#4. < ( w - wEXT ) mno >  = 0     w_0 <mnk>  + w_i <imnk>  + w_ij <ijmnk>  + w_ijk <ijkmno>  + w_ijkl <ijklmno>  = <wEXT mno>
#5. < ( w - wEXT ) mnop >  = 0    w_0 <mnkl> + w_i <imnkl> + w_ij <ijmnkl> + w_ijk <ijkmnop> + w_ijkl <ijklmnop> = <wEXT mnop>

# General imports
import operator
import numpy as np
import scipy.special
import itertools

class HyperPoly:

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

        # Make parametrization
        self.makePoly( order )

    @staticmethod
    def get_ndof( nvar, order ):
        return sum( [ int(scipy.special.binom(nvar + o - 1, o)) for o in xrange(order+1) ] )

    def makePoly( self, order ):
    
        # We have Binomial( n + o - 1, o ) coefficients for n variables at order o
        ncoeff = {o:int(scipy.special.binom(self.nvar + o - 1, o)) for o in xrange(order+1)}
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
                if e > d:
                    A[d][e] = A[e][d]
                else:
                    A[d][e] = self.expectation(self.combination[d] + self.combination[e]) 

        print A
        print b
        # Solve
        self.w_coeff = np.linalg.solve(A, b)

#    def eval( self, c ):
#        if not len(c) == self.nvar:
#            raise ValueError( "Polynomial degree is %i. Got argument '%r'" % (self.nvar, c ) )
#        return sum( np.prod( [ c[elem] for elem in combination ] ) for n in range(self.ndof) ) 

         
    def wEXT_expectation(self, combination ):
        ''' Compute <wEXT ijk...> = 1/Nmeas Sum_meas( wEXT_meas*i_meas*j_meas*k_meas... )
        '''
        print self.c[0], combination, [self.c[n][elem] for elem in combination], np.prod( [self.c[n][elem] for elem in combination] ) 
        return sum( [ self.w[n]*np.prod( [ self.c[n][elem] for elem in combination ] ) for n in xrange(self.N) ] ) / float(self.N)

    def expectation(self, combination ):
        ''' Compute <wEXT ijk...> = 1/Nmeas Sum_meas( i_meas*j_meas*k_meas... )
        '''
        #print self.c[0], combination, [self.c[n][elem] for elem in combination], np.prod( [self.c[n][elem] for elem in combination] ) 
        return sum( [ np.prod( [ self.c[n][elem] for elem in combination ] ) for n in range(self.N) ]) / float(self.N)


if __name__ == "__main__":
    #def f(x,y,z):
    #    return 1+x*y+x**2+y**2 +27*x*y*z
    #data = [ (f(x,y,z),x,y,z) for x in range(-3,3) for y in range(-3,3) for z in range( -3,3)]
    #p = HyperPoly( data, 3)
    def f(x):
        return 1+x
    data = [ (f(x),x) for x in range(-3,3) ]
    p = HyperPoly( data, 1)
