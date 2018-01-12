# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.0.0 for Mac OS X x86 (64-bit) (July 28, 2016)
# Date: Fri 3 Nov 2017 11:08:39


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-6*complex(0,1)*lam',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = 'DC1A*ee*complex(0,1)*projThirdGen3x3',
                 order = {'NP':1,'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = 'DC1V*ee*complex(0,1)*projThirdGen3x3',
                 order = {'NP':1,'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '-(DAG*ee*projThirdGen3x3)/(2.*MT)',
                 order = {'QED':1,'NP':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(DVG*ee*complex(0,1)*projThirdGen3x3)/(2.*MT)',
                 order = {'QED':1,'NP':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(DC2A*ee*projThirdGen3x3)/(2.*MZ)',
                 order = {'NP':1,'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '(DC2V*ee*complex(0,1)*projThirdGen3x3)/(2.*MZ)',
                 order = {'NP':1,'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '-6*complex(0,1)*lam*vev',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                 order = {'QED':1})

