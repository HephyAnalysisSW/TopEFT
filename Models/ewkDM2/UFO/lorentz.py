# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.0.0 for Mac OS X x86 (64-bit) (July 28, 2016)
# Date: Fri 15 Sep 2017 10:14:26


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


UUV3 = Lorentz(name = 'UUV3',
               spins = [ -1, -1, 3 ],
               structure = 'P(3,2) + P(3,3)')

SSS3 = Lorentz(name = 'SSS3',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS3 = Lorentz(name = 'FFS3',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) + ProjP(2,1)')

FFV15 = Lorentz(name = 'FFV15',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,1)')

FFV16 = Lorentz(name = 'FFV16',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma5(-1,1)*Gamma(3,2,-1)')

FFV17 = Lorentz(name = 'FFV17',
                spins = [ 2, 2, 3 ],
                structure = '-(P(-1,1)*Gamma(-1,2,-2)*Gamma(3,-2,1)) - P(-1,2)*Gamma(-1,2,-2)*Gamma(3,-2,1) + P(-1,1)*Gamma(-1,-2,1)*Gamma(3,2,-2) + P(-1,2)*Gamma(-1,-2,1)*Gamma(3,2,-2)')

FFV18 = Lorentz(name = 'FFV18',
                spins = [ 2, 2, 3 ],
                structure = '-(P(-1,1)*Gamma5(-2,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2)) - P(-1,2)*Gamma5(-2,1)*Gamma(-1,2,-3)*Gamma(3,-3,-2) + P(-1,1)*Gamma5(-2,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3) + P(-1,2)*Gamma5(-2,1)*Gamma(-1,-3,-2)*Gamma(3,2,-3)')

FFV19 = Lorentz(name = 'FFV19',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV20 = Lorentz(name = 'FFV20',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjP(-1,1)')

FFV21 = Lorentz(name = 'FFV21',
                spins = [ 2, 2, 3 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 4*Gamma(3,2,-1)*ProjP(-1,1)')

VVS3 = Lorentz(name = 'VVS3',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVV3 = Lorentz(name = 'VVV3',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

SSSS3 = Lorentz(name = 'SSSS3',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

VVSS3 = Lorentz(name = 'VVSS3',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVVV11 = Lorentz(name = 'VVVV11',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV12 = Lorentz(name = 'VVVV12',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV13 = Lorentz(name = 'VVVV13',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV14 = Lorentz(name = 'VVVV14',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV15 = Lorentz(name = 'VVVV15',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

