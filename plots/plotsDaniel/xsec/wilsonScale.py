import math

lambdaSqInv = {}

# constants
aS      = 0.1184
aEW     = 1/127.9
ee      = math.sqrt(4*math.pi*aEW)
vev     = math.sqrt(1/(math.sqrt(2)*1.16637**2))

# masses
MW      = 80.385
MZ      = 91.1876

# weak mixing angles
cw      = MW/MZ
sw      = math.sqrt(1-cw**2)
#sw      = ee*vev/(2*MW)
#cw      = math.sqrt(1-sw**2)

# charges
g1  = ee/math.sqrt(1-sw**2)
gs  = math.sqrt(4*math.pi*aS)
gw  = ee/sw

# 1/lambda**2 [1/TeV**2]
lambdaSqInv = {
    'cuB':  g1/(2*(MW/1000)**2),
    'cuG':  gs/(MW/1000)**2,
    'cuW':  gw/(MW/1000)**2
}

