# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 10.0 for Mac OS X x86 (64-bit) (September 10, 2014)
# Date: Thu 27 Jul 2017 17:29:36


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


UUV1 = Lorentz(name = 'UUV1',
               spins = [ -1, -1, 3 ],
               structure = 'P(3,2) + P(3,3)')

SSS1 = Lorentz(name = 'SSS1',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS2 = Lorentz(name = 'FFS2',
               spins = [ 2, 2, 1 ],
               structure = 'P(-1,3)*Gamma(-1,2,-2)*ProjM(-2,1)')

FFS3 = Lorentz(name = 'FFS3',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) + ProjP(2,1)')

FFV4 = Lorentz(name = 'FFV4',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV5 = Lorentz(name = 'FFV5',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV6 = Lorentz(name = 'FFV6',
               spins = [ 2, 2, 3 ],
               structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1)')

FFV7 = Lorentz(name = 'FFV7',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) - 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV8 = Lorentz(name = 'FFV8',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV9 = Lorentz(name = 'FFV9',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 4*Gamma(3,2,-1)*ProjP(-1,1)')

FFV10 = Lorentz(name = 'FFV10',
                spins = [ 2, 2, 3 ],
                structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)')

VVS2 = Lorentz(name = 'VVS2',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVS3 = Lorentz(name = 'VVS3',
               spins = [ 3, 3, 1 ],
               structure = 'P(1,2)*P(2,1) - P(-1,1)*P(-1,2)*Metric(1,2)')

VVV2 = Lorentz(name = 'VVV2',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVV3 = Lorentz(name = 'VVV3',
               spins = [ 3, 3, 3 ],
               structure = '-(P(1,2)*P(2,3)*P(3,1)) + P(1,3)*P(2,1)*P(3,2) + P(-1,2)*P(-1,3)*P(3,1)*Metric(1,2) - P(-1,1)*P(-1,3)*P(3,2)*Metric(1,2) - P(-1,2)*P(-1,3)*P(2,1)*Metric(1,3) + P(-1,1)*P(-1,2)*P(2,3)*Metric(1,3) + P(-1,1)*P(-1,3)*P(1,2)*Metric(2,3) - P(-1,1)*P(-1,2)*P(1,3)*Metric(2,3)')

SSSS1 = Lorentz(name = 'SSSS1',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

FFSS5 = Lorentz(name = 'FFSS5',
                spins = [ 2, 2, 1, 1 ],
                structure = 'P(-1,3)*Gamma(-1,2,-2)*ProjM(-2,1)')

FFSS6 = Lorentz(name = 'FFSS6',
                spins = [ 2, 2, 1, 1 ],
                structure = 'P(-1,4)*Gamma(-1,2,-2)*ProjM(-2,1)')

FFSS7 = Lorentz(name = 'FFSS7',
                spins = [ 2, 2, 1, 1 ],
                structure = 'P(-1,3)*Gamma(-1,2,-2)*ProjM(-2,1) - P(-1,4)*Gamma(-1,2,-2)*ProjM(-2,1)')

FFSS8 = Lorentz(name = 'FFSS8',
                spins = [ 2, 2, 1, 1 ],
                structure = 'P(-1,3)*Gamma(-1,2,-2)*ProjM(-2,1) + P(-1,4)*Gamma(-1,2,-2)*ProjM(-2,1)')

FFFF7 = Lorentz(name = 'FFFF7',
                spins = [ 2, 2, 2, 2 ],
                structure = 'Gamma(-1,2,-2)*Gamma(-1,4,-3)*ProjM(-3,1)*ProjM(-2,3)')

FFFF8 = Lorentz(name = 'FFFF8',
                spins = [ 2, 2, 2, 2 ],
                structure = 'Gamma(-1,2,-2)*Gamma(-1,4,-3)*ProjM(-3,3)*ProjM(-2,1)')

FFFF9 = Lorentz(name = 'FFFF9',
                spins = [ 2, 2, 2, 2 ],
                structure = 'ProjM(4,3)*ProjP(2,1)')

FFFF10 = Lorentz(name = 'FFFF10',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'ProjM(2,1)*ProjP(4,3)')

FFFF11 = Lorentz(name = 'FFFF11',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'Gamma(-1,2,-2)*Gamma(-1,4,-3)*ProjP(-3,1)*ProjP(-2,3)')

FFVS4 = Lorentz(name = 'FFVS4',
                spins = [ 2, 2, 3, 1 ],
                structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFVS5 = Lorentz(name = 'FFVS5',
                spins = [ 2, 2, 3, 1 ],
                structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1)')

FFVS6 = Lorentz(name = 'FFVS6',
                spins = [ 2, 2, 3, 1 ],
                structure = '-(P(-1,3)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1)) + P(-1,3)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)')

FFVV3 = Lorentz(name = 'FFVV3',
                spins = [ 2, 2, 3, 3 ],
                structure = 'Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1)')

FFVV4 = Lorentz(name = 'FFVV4',
                spins = [ 2, 2, 3, 3 ],
                structure = 'Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1)')

VVSS2 = Lorentz(name = 'VVSS2',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVSS3 = Lorentz(name = 'VVSS3',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(1,2)*P(2,1) - P(-1,1)*P(-1,2)*Metric(1,2)')

VVVS2 = Lorentz(name = 'VVVS2',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVVV4 = Lorentz(name = 'VVVV4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV5 = Lorentz(name = 'VVVV5',
                spins = [ 3, 3, 3, 3 ],
                structure = 'P(3,2)*P(4,1)*Metric(1,2) - P(3,1)*P(4,2)*Metric(1,2) + P(2,1)*P(4,2)*Metric(1,3) + P(2,4)*P(4,3)*Metric(1,3) - P(2,1)*P(3,2)*Metric(1,4) - P(2,3)*P(3,4)*Metric(1,4) - P(1,2)*P(4,1)*Metric(2,3) - P(1,4)*P(4,3)*Metric(2,3) + P(-1,1)*P(-1,2)*Metric(1,4)*Metric(2,3) + P(-1,3)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,2)*P(3,1)*Metric(2,4) + P(1,3)*P(3,4)*Metric(2,4) - P(-1,1)*P(-1,2)*Metric(1,3)*Metric(2,4) - P(-1,3)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,4)*P(2,3)*Metric(3,4) - P(1,3)*P(2,4)*Metric(3,4)')

VVVV6 = Lorentz(name = 'VVVV6',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV7 = Lorentz(name = 'VVVV7',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV8 = Lorentz(name = 'VVVV8',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV9 = Lorentz(name = 'VVVV9',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

VVVV10 = Lorentz(name = 'VVVV10',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'P(3,4)*P(4,1)*Metric(1,2) + P(3,2)*P(4,3)*Metric(1,2) - P(2,4)*P(4,1)*Metric(1,3) - P(2,3)*P(4,2)*Metric(1,3) + P(2,4)*P(3,1)*Metric(1,4) - P(2,1)*P(3,4)*Metric(1,4) + P(1,3)*P(4,2)*Metric(2,3) - P(1,2)*P(4,3)*Metric(2,3) - P(1,4)*P(3,1)*Metric(2,4) - P(1,3)*P(3,2)*Metric(2,4) + P(-1,2)*P(-1,3)*Metric(1,3)*Metric(2,4) + P(-1,1)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,4)*P(2,1)*Metric(3,4) + P(1,2)*P(2,3)*Metric(3,4) - P(-1,2)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,1)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVV11 = Lorentz(name = 'VVVV11',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'P(3,4)*P(4,2)*Metric(1,2) + P(3,1)*P(4,3)*Metric(1,2) + P(2,3)*P(4,1)*Metric(1,3) - P(2,1)*P(4,3)*Metric(1,3) - P(2,3)*P(3,1)*Metric(1,4) - P(2,4)*P(3,2)*Metric(1,4) - P(1,3)*P(4,1)*Metric(2,3) - P(1,4)*P(4,2)*Metric(2,3) + P(-1,1)*P(-1,3)*Metric(1,4)*Metric(2,3) + P(-1,2)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,4)*P(3,2)*Metric(2,4) - P(1,2)*P(3,4)*Metric(2,4) + P(1,3)*P(2,1)*Metric(3,4) + P(1,2)*P(2,4)*Metric(3,4) - P(-1,1)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,4)*Metric(1,2)*Metric(3,4)')

FFVSS2 = Lorentz(name = 'FFVSS2',
                 spins = [ 2, 2, 3, 1, 1 ],
                 structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFVVS3 = Lorentz(name = 'FFVVS3',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = 'Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1)')

FFVVS4 = Lorentz(name = 'FFVVS4',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = 'Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1)')

VVVSS2 = Lorentz(name = 'VVVSS2',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVVVS4 = Lorentz(name = 'VVVVS4',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVVS5 = Lorentz(name = 'VVVVS5',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVVS6 = Lorentz(name = 'VVVVS6',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVVV16 = Lorentz(name = 'VVVVV16',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(5,1)*Metric(1,3)*Metric(2,4) - P(3,1)*Metric(1,5)*Metric(2,4) - P(4,1)*Metric(1,3)*Metric(2,5) + P(3,1)*Metric(1,4)*Metric(2,5) - P(5,1)*Metric(1,2)*Metric(3,4) + P(2,1)*Metric(1,5)*Metric(3,4) + P(4,1)*Metric(1,2)*Metric(3,5) - P(2,1)*Metric(1,4)*Metric(3,5)')

VVVVV17 = Lorentz(name = 'VVVVV17',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(5,2)*Metric(1,4)*Metric(2,3) - P(4,2)*Metric(1,5)*Metric(2,3) + P(3,2)*Metric(1,5)*Metric(2,4) - P(3,2)*Metric(1,4)*Metric(2,5) - P(5,2)*Metric(1,2)*Metric(3,4) + P(1,2)*Metric(2,5)*Metric(3,4) + P(4,2)*Metric(1,2)*Metric(3,5) - P(1,2)*Metric(2,4)*Metric(3,5)')

VVVVV18 = Lorentz(name = 'VVVVV18',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(5,3)*Metric(1,4)*Metric(2,3) - P(4,3)*Metric(1,5)*Metric(2,3) - P(5,3)*Metric(1,3)*Metric(2,4) + P(4,3)*Metric(1,3)*Metric(2,5) + P(2,3)*Metric(1,5)*Metric(3,4) - P(1,3)*Metric(2,5)*Metric(3,4) - P(2,3)*Metric(1,4)*Metric(3,5) + P(1,3)*Metric(2,4)*Metric(3,5)')

VVVVV19 = Lorentz(name = 'VVVVV19',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(5,1)*Metric(1,4)*Metric(2,3) - P(4,1)*Metric(1,5)*Metric(2,3) + P(4,1)*Metric(1,3)*Metric(2,5) - P(3,1)*Metric(1,4)*Metric(2,5) - P(5,1)*Metric(1,2)*Metric(3,4) + P(2,1)*Metric(1,5)*Metric(3,4) + P(3,1)*Metric(1,2)*Metric(4,5) - P(2,1)*Metric(1,3)*Metric(4,5)')

VVVVV20 = Lorentz(name = 'VVVVV20',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(5,1)*Metric(1,4)*Metric(2,3) - P(4,1)*Metric(1,5)*Metric(2,3) - P(5,1)*Metric(1,3)*Metric(2,4) + P(3,1)*Metric(1,5)*Metric(2,4) + P(4,1)*Metric(1,2)*Metric(3,5) - P(2,1)*Metric(1,4)*Metric(3,5) - P(3,1)*Metric(1,2)*Metric(4,5) + P(2,1)*Metric(1,3)*Metric(4,5)')

VVVVV21 = Lorentz(name = 'VVVVV21',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(5,4)*Metric(1,3)*Metric(2,4) - P(3,4)*Metric(1,4)*Metric(2,5) - P(5,4)*Metric(1,2)*Metric(3,4) + P(1,4)*Metric(2,5)*Metric(3,4) + P(2,4)*Metric(1,4)*Metric(3,5) - P(1,4)*Metric(2,4)*Metric(3,5) + P(3,4)*Metric(1,2)*Metric(4,5) - P(2,4)*Metric(1,3)*Metric(4,5)')

VVVVV22 = Lorentz(name = 'VVVVV22',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(3,5)*Metric(1,5)*Metric(2,4) - P(4,5)*Metric(1,3)*Metric(2,5) - P(2,5)*Metric(1,5)*Metric(3,4) + P(1,5)*Metric(2,5)*Metric(3,4) + P(4,5)*Metric(1,2)*Metric(3,5) - P(1,5)*Metric(2,4)*Metric(3,5) - P(3,5)*Metric(1,2)*Metric(4,5) + P(2,5)*Metric(1,3)*Metric(4,5)')

VVVVV23 = Lorentz(name = 'VVVVV23',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(4,2)*Metric(1,5)*Metric(2,3) + P(5,2)*Metric(1,3)*Metric(2,4) - P(3,2)*Metric(1,5)*Metric(2,4) - P(4,2)*Metric(1,3)*Metric(2,5) - P(5,2)*Metric(1,2)*Metric(3,4) + P(1,2)*Metric(2,5)*Metric(3,4) + P(3,2)*Metric(1,2)*Metric(4,5) - P(1,2)*Metric(2,3)*Metric(4,5)')

VVVVV24 = Lorentz(name = 'VVVVV24',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(5,2)*Metric(1,4)*Metric(2,3) - P(5,2)*Metric(1,3)*Metric(2,4) + P(4,2)*Metric(1,3)*Metric(2,5) - P(3,2)*Metric(1,4)*Metric(2,5) - P(4,2)*Metric(1,2)*Metric(3,5) + P(1,2)*Metric(2,4)*Metric(3,5) + P(3,2)*Metric(1,2)*Metric(4,5) - P(1,2)*Metric(2,3)*Metric(4,5)')

VVVVV25 = Lorentz(name = 'VVVVV25',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(5,3)*Metric(1,4)*Metric(2,3) - P(4,3)*Metric(1,3)*Metric(2,5) - P(5,3)*Metric(1,2)*Metric(3,4) + P(1,3)*Metric(2,5)*Metric(3,4) + P(4,3)*Metric(1,2)*Metric(3,5) - P(2,3)*Metric(1,4)*Metric(3,5) + P(2,3)*Metric(1,3)*Metric(4,5) - P(1,3)*Metric(2,3)*Metric(4,5)')

VVVVV26 = Lorentz(name = 'VVVVV26',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(4,3)*Metric(1,5)*Metric(2,3) - P(5,3)*Metric(1,3)*Metric(2,4) + P(5,3)*Metric(1,2)*Metric(3,4) - P(2,3)*Metric(1,5)*Metric(3,4) - P(4,3)*Metric(1,2)*Metric(3,5) + P(1,3)*Metric(2,4)*Metric(3,5) + P(2,3)*Metric(1,3)*Metric(4,5) - P(1,3)*Metric(2,3)*Metric(4,5)')

VVVVV27 = Lorentz(name = 'VVVVV27',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(5,4)*Metric(1,4)*Metric(2,3) - P(3,4)*Metric(1,5)*Metric(2,4) - P(5,4)*Metric(1,2)*Metric(3,4) + P(2,4)*Metric(1,5)*Metric(3,4) - P(2,4)*Metric(1,4)*Metric(3,5) + P(1,4)*Metric(2,4)*Metric(3,5) + P(3,4)*Metric(1,2)*Metric(4,5) - P(1,4)*Metric(2,3)*Metric(4,5)')

VVVVV28 = Lorentz(name = 'VVVVV28',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(5,4)*Metric(1,4)*Metric(2,3) - P(5,4)*Metric(1,3)*Metric(2,4) + P(3,4)*Metric(1,5)*Metric(2,4) - P(3,4)*Metric(1,4)*Metric(2,5) - P(2,4)*Metric(1,5)*Metric(3,4) + P(1,4)*Metric(2,5)*Metric(3,4) + P(2,4)*Metric(1,3)*Metric(4,5) - P(1,4)*Metric(2,3)*Metric(4,5)')

VVVVV29 = Lorentz(name = 'VVVVV29',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(4,5)*Metric(1,5)*Metric(2,3) - P(3,5)*Metric(1,4)*Metric(2,5) - P(2,5)*Metric(1,5)*Metric(3,4) + P(1,5)*Metric(2,5)*Metric(3,4) - P(4,5)*Metric(1,2)*Metric(3,5) + P(2,5)*Metric(1,4)*Metric(3,5) + P(3,5)*Metric(1,2)*Metric(4,5) - P(1,5)*Metric(2,3)*Metric(4,5)')

VVVVV30 = Lorentz(name = 'VVVVV30',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'P(4,5)*Metric(1,5)*Metric(2,3) - P(3,5)*Metric(1,5)*Metric(2,4) - P(4,5)*Metric(1,3)*Metric(2,5) + P(3,5)*Metric(1,4)*Metric(2,5) - P(2,5)*Metric(1,4)*Metric(3,5) + P(1,5)*Metric(2,4)*Metric(3,5) + P(2,5)*Metric(1,3)*Metric(4,5) - P(1,5)*Metric(2,3)*Metric(4,5)')

VVVVSS4 = Lorentz(name = 'VVVVSS4',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVVSS5 = Lorentz(name = 'VVVVSS5',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVVSS6 = Lorentz(name = 'VVVVSS6',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVVVV16 = Lorentz(name = 'VVVVVV16',
                   spins = [ 3, 3, 3, 3, 3, 3 ],
                   structure = 'Metric(1,6)*Metric(2,4)*Metric(3,5) - Metric(1,4)*Metric(2,6)*Metric(3,5) - Metric(1,5)*Metric(2,4)*Metric(3,6) + Metric(1,4)*Metric(2,5)*Metric(3,6) - Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,3)*Metric(2,6)*Metric(4,5) + Metric(1,5)*Metric(2,3)*Metric(4,6) - Metric(1,3)*Metric(2,5)*Metric(4,6)')

VVVVVV17 = Lorentz(name = 'VVVVVV17',
                   spins = [ 3, 3, 3, 3, 3, 3 ],
                   structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) - Metric(1,5)*Metric(2,6)*Metric(3,4) + Metric(1,4)*Metric(2,6)*Metric(3,5) - Metric(1,4)*Metric(2,5)*Metric(3,6) - Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,2)*Metric(3,6)*Metric(4,5) + Metric(1,5)*Metric(2,3)*Metric(4,6) - Metric(1,2)*Metric(3,5)*Metric(4,6)')

VVVVVV18 = Lorentz(name = 'VVVVVV18',
                   spins = [ 3, 3, 3, 3, 3, 3 ],
                   structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) - Metric(1,5)*Metric(2,6)*Metric(3,4) - Metric(1,6)*Metric(2,4)*Metric(3,5) + Metric(1,5)*Metric(2,4)*Metric(3,6) + Metric(1,3)*Metric(2,6)*Metric(4,5) - Metric(1,2)*Metric(3,6)*Metric(4,5) - Metric(1,3)*Metric(2,5)*Metric(4,6) + Metric(1,2)*Metric(3,5)*Metric(4,6)')

VVVVVV19 = Lorentz(name = 'VVVVVV19',
                   spins = [ 3, 3, 3, 3, 3, 3 ],
                   structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) - Metric(1,5)*Metric(2,6)*Metric(3,4) + Metric(1,5)*Metric(2,4)*Metric(3,6) - Metric(1,4)*Metric(2,5)*Metric(3,6) - Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,3)*Metric(2,6)*Metric(4,5) + Metric(1,4)*Metric(2,3)*Metric(5,6) - Metric(1,3)*Metric(2,4)*Metric(5,6)')

VVVVVV20 = Lorentz(name = 'VVVVVV20',
                   spins = [ 3, 3, 3, 3, 3, 3 ],
                   structure = 'Metric(1,6)*Metric(2,4)*Metric(3,5) - Metric(1,4)*Metric(2,5)*Metric(3,6) - Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,2)*Metric(3,6)*Metric(4,5) + Metric(1,3)*Metric(2,5)*Metric(4,6) - Metric(1,2)*Metric(3,5)*Metric(4,6) + Metric(1,4)*Metric(2,3)*Metric(5,6) - Metric(1,3)*Metric(2,4)*Metric(5,6)')

VVVVVV21 = Lorentz(name = 'VVVVVV21',
                   spins = [ 3, 3, 3, 3, 3, 3 ],
                   structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) - Metric(1,5)*Metric(2,6)*Metric(3,4) - Metric(1,6)*Metric(2,4)*Metric(3,5) + Metric(1,4)*Metric(2,6)*Metric(3,5) + Metric(1,5)*Metric(2,3)*Metric(4,6) - Metric(1,3)*Metric(2,5)*Metric(4,6) - Metric(1,4)*Metric(2,3)*Metric(5,6) + Metric(1,3)*Metric(2,4)*Metric(5,6)')

VVVVVV22 = Lorentz(name = 'VVVVVV22',
                   spins = [ 3, 3, 3, 3, 3, 3 ],
                   structure = 'Metric(1,4)*Metric(2,6)*Metric(3,5) - Metric(1,5)*Metric(2,4)*Metric(3,6) - Metric(1,3)*Metric(2,6)*Metric(4,5) + Metric(1,2)*Metric(3,6)*Metric(4,5) + Metric(1,5)*Metric(2,3)*Metric(4,6) - Metric(1,2)*Metric(3,5)*Metric(4,6) - Metric(1,4)*Metric(2,3)*Metric(5,6) + Metric(1,3)*Metric(2,4)*Metric(5,6)')

VVVVVV23 = Lorentz(name = 'VVVVVV23',
                   spins = [ 3, 3, 3, 3, 3, 3 ],
                   structure = 'Metric(1,5)*Metric(2,6)*Metric(3,4) + Metric(1,6)*Metric(2,4)*Metric(3,5) - Metric(1,4)*Metric(2,6)*Metric(3,5) - Metric(1,5)*Metric(2,4)*Metric(3,6) - Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,2)*Metric(3,6)*Metric(4,5) + Metric(1,4)*Metric(2,3)*Metric(5,6) - Metric(1,2)*Metric(3,4)*Metric(5,6)')

VVVVVV24 = Lorentz(name = 'VVVVVV24',
                   spins = [ 3, 3, 3, 3, 3, 3 ],
                   structure = 'Metric(1,5)*Metric(2,6)*Metric(3,4) - Metric(1,4)*Metric(2,5)*Metric(3,6) - Metric(1,3)*Metric(2,6)*Metric(4,5) + Metric(1,2)*Metric(3,6)*Metric(4,5) - Metric(1,5)*Metric(2,3)*Metric(4,6) + Metric(1,3)*Metric(2,5)*Metric(4,6) + Metric(1,4)*Metric(2,3)*Metric(5,6) - Metric(1,2)*Metric(3,4)*Metric(5,6)')

VVVVVV25 = Lorentz(name = 'VVVVVV25',
                   spins = [ 3, 3, 3, 3, 3, 3 ],
                   structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) - Metric(1,6)*Metric(2,4)*Metric(3,5) + Metric(1,5)*Metric(2,4)*Metric(3,6) - Metric(1,4)*Metric(2,5)*Metric(3,6) - Metric(1,5)*Metric(2,3)*Metric(4,6) + Metric(1,2)*Metric(3,5)*Metric(4,6) + Metric(1,4)*Metric(2,3)*Metric(5,6) - Metric(1,2)*Metric(3,4)*Metric(5,6)')

VVVVVV26 = Lorentz(name = 'VVVVVV26',
                   spins = [ 3, 3, 3, 3, 3, 3 ],
                   structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) - Metric(1,4)*Metric(2,6)*Metric(3,5) - Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,3)*Metric(2,6)*Metric(4,5) - Metric(1,3)*Metric(2,5)*Metric(4,6) + Metric(1,2)*Metric(3,5)*Metric(4,6) + Metric(1,4)*Metric(2,3)*Metric(5,6) - Metric(1,2)*Metric(3,4)*Metric(5,6)')

VVVVVV27 = Lorentz(name = 'VVVVVV27',
                   spins = [ 3, 3, 3, 3, 3, 3 ],
                   structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) - Metric(1,6)*Metric(2,4)*Metric(3,5) + Metric(1,4)*Metric(2,6)*Metric(3,5) - Metric(1,4)*Metric(2,5)*Metric(3,6) - Metric(1,3)*Metric(2,6)*Metric(4,5) + Metric(1,2)*Metric(3,6)*Metric(4,5) + Metric(1,3)*Metric(2,4)*Metric(5,6) - Metric(1,2)*Metric(3,4)*Metric(5,6)')

VVVVVV28 = Lorentz(name = 'VVVVVV28',
                   spins = [ 3, 3, 3, 3, 3, 3 ],
                   structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) - Metric(1,5)*Metric(2,4)*Metric(3,6) - Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,2)*Metric(3,6)*Metric(4,5) + Metric(1,5)*Metric(2,3)*Metric(4,6) - Metric(1,3)*Metric(2,5)*Metric(4,6) + Metric(1,3)*Metric(2,4)*Metric(5,6) - Metric(1,2)*Metric(3,4)*Metric(5,6)')

VVVVVV29 = Lorentz(name = 'VVVVVV29',
                   spins = [ 3, 3, 3, 3, 3, 3 ],
                   structure = 'Metric(1,5)*Metric(2,6)*Metric(3,4) - Metric(1,6)*Metric(2,4)*Metric(3,5) + Metric(1,6)*Metric(2,3)*Metric(4,5) - Metric(1,3)*Metric(2,6)*Metric(4,5) - Metric(1,5)*Metric(2,3)*Metric(4,6) + Metric(1,2)*Metric(3,5)*Metric(4,6) + Metric(1,3)*Metric(2,4)*Metric(5,6) - Metric(1,2)*Metric(3,4)*Metric(5,6)')

VVVVVV30 = Lorentz(name = 'VVVVVV30',
                   spins = [ 3, 3, 3, 3, 3, 3 ],
                   structure = 'Metric(1,5)*Metric(2,6)*Metric(3,4) - Metric(1,4)*Metric(2,6)*Metric(3,5) - Metric(1,5)*Metric(2,4)*Metric(3,6) + Metric(1,4)*Metric(2,5)*Metric(3,6) - Metric(1,3)*Metric(2,5)*Metric(4,6) + Metric(1,2)*Metric(3,5)*Metric(4,6) + Metric(1,3)*Metric(2,4)*Metric(5,6) - Metric(1,2)*Metric(3,4)*Metric(5,6)')

