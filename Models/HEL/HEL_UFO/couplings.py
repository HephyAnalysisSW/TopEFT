# This file was automatically created by FeynRules 2.0.29
# Mathematica version: 10.2.0 for Mac OS X x86 (64-bit) (July 29, 2015)
# Date: Fri 13 Jan 2017 01:20:34


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(AH*complex(0,1))',
                order = {'QED':2})

GC_2 = Coupling(name = 'GC_2',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_6 = Coupling(name = 'GC_6',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '-ee**2/(2.*cw)',
                order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = '(ee**2*complex(0,1))/(2.*cw)',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = 'ee**2/(2.*cw)',
                 order = {'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '-G',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_13 = Coupling(name = 'GC_13',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(complex(0,1)*GH)',
                 order = {'QCD':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(G*GH)',
                 order = {'QCD':3})

GC_16 = Coupling(name = 'GC_16',
                 value = 'complex(0,1)*G**2*GH',
                 order = {'QCD':4})

GC_17 = Coupling(name = 'GC_17',
                 value = 'I2a33',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '(cd*I2a33)/2.',
                 order = {'NP':1,'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '-I3a33',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '-(cu*I3a33)/2.',
                 order = {'NP':1,'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = 'I5a33',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(cu*I5a33)/2.',
                 order = {'NP':1,'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '-I6a33',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-(cd*I6a33)/2.',
                 order = {'NP':1,'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(cHB*ee)/MW**2 - (cHW*ee)/MW**2',
                 order = {'NP':1,'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-((cHB*ee*complex(0,1))/MW**2) - (cHW*ee*complex(0,1))/MW**2',
                 order = {'NP':1,'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(cB*ee)/(2.*MW**2) - (cWW*ee)/(2.*MW**2)',
                 order = {'NP':1,'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '-(cB*ee*complex(0,1))/(2.*MW**2) - (cWW*ee*complex(0,1))/(2.*MW**2)',
                 order = {'NP':1,'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '(cHB*ee**2*complex(0,1))/MW**2 + (cHW*ee**2*complex(0,1))/MW**2',
                 order = {'NP':1,'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '-((cB*ee**2*complex(0,1))/MW**2) - (cWW*ee**2*complex(0,1))/MW**2',
                 order = {'NP':1,'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(2*cdB*ee*I2a33)/MW**2 + (2*cdW*ee*I2a33)/MW**2',
                 order = {'NP':1,'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '(-2*cuB*ee*I3a33)/MW**2 + (2*cuW*ee*I3a33)/MW**2',
                 order = {'NP':1,'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(2*cuB*ee*I5a33)/MW**2 - (2*cuW*ee*I5a33)/MW**2',
                 order = {'NP':1,'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '(-2*cdB*ee*I6a33)/MW**2 - (2*cdW*ee*I6a33)/MW**2',
                 order = {'NP':1,'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '(2*c2W*ee*complex(0,1))/MW**2',
                 order = {'NP':1,'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(-8*c2W*ee**2*complex(0,1))/MW**2',
                 order = {'NP':1,'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '(4*cA*ee**2*complex(0,1))/MW**2',
                 order = {'NP':1,'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '-(cB*ee**2)/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '-(cB*ee**2*complex(0,1))/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '(cB*ee**2)/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '-(cHB*ee**2)/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '(cHB*ee**2*complex(0,1))/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '(cHB*ee**2)/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '-(cHW*ee**2)/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '(cHW*ee**2*complex(0,1))/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '(cHW*ee**2)/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(cWW*ee**2)/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '-(cWW*ee**2*complex(0,1))/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '(cWW*ee**2)/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(-12*c2W*ee**3*complex(0,1))/MW**2',
                 order = {'NP':1,'QED':3})

GC_51 = Coupling(name = 'GC_51',
                 value = '-(cHB*ee**3*complex(0,1))/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':3})

GC_52 = Coupling(name = 'GC_52',
                 value = '(cHB*ee**3*complex(0,1))/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':3})

GC_53 = Coupling(name = 'GC_53',
                 value = '(cHB*ee**3)/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':3})

GC_54 = Coupling(name = 'GC_54',
                 value = '-(cHW*ee**3)/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':3})

GC_55 = Coupling(name = 'GC_55',
                 value = '-(cHW*ee**3*complex(0,1))/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':3})

GC_56 = Coupling(name = 'GC_56',
                 value = '(cHW*ee**3*complex(0,1))/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':3})

GC_57 = Coupling(name = 'GC_57',
                 value = '-(cWW*ee**3)/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':3})

GC_58 = Coupling(name = 'GC_58',
                 value = '-(cWW*ee**3*complex(0,1))/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':3})

GC_59 = Coupling(name = 'GC_59',
                 value = '(cWW*ee**3*complex(0,1))/(2.*cw*MW**2)',
                 order = {'NP':1,'QED':3})

GC_60 = Coupling(name = 'GC_60',
                 value = '(-4*c2W*ee**4*complex(0,1))/MW**2',
                 order = {'NP':1,'QED':4})

GC_61 = Coupling(name = 'GC_61',
                 value = '(-2*c2G*G)/MW**2',
                 order = {'NP':1,'QCD':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '(-2*c2G*complex(0,1)*G**2)/MW**2',
                 order = {'NP':1,'QCD':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '(-8*c2G*complex(0,1)*G**2)/MW**2',
                 order = {'NP':1,'QCD':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '(4*cG*dum**2*complex(0,1)*G**2)/MW**2',
                 order = {'NP':1,'QCD':2,'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '(-4*c2G*G**3)/MW**2',
                 order = {'NP':1,'QCD':3})

GC_66 = Coupling(name = 'GC_66',
                 value = '(-2*c2G*G**3)/MW**2',
                 order = {'NP':1,'QCD':3})

GC_67 = Coupling(name = 'GC_67',
                 value = '(4*c2G*G**3)/MW**2',
                 order = {'NP':1,'QCD':3})

GC_68 = Coupling(name = 'GC_68',
                 value = '(6*c3G*G**3)/MW**2',
                 order = {'NP':1,'QCD':3})

GC_69 = Coupling(name = 'GC_69',
                 value = '(4*cG*dum**2*G**3)/MW**2',
                 order = {'NP':1,'QCD':3,'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '(-2*c2G*complex(0,1)*G**4)/MW**2',
                 order = {'NP':1,'QCD':4})

GC_71 = Coupling(name = 'GC_71',
                 value = '(2*c2G*complex(0,1)*G**4)/MW**2',
                 order = {'NP':1,'QCD':4})

GC_72 = Coupling(name = 'GC_72',
                 value = '(-6*c3G*complex(0,1)*G**4)/MW**2',
                 order = {'NP':1,'QCD':4})

GC_73 = Coupling(name = 'GC_73',
                 value = '(-4*cG*dum**2*complex(0,1)*G**4)/MW**2',
                 order = {'NP':1,'QCD':4,'QED':2})

GC_74 = Coupling(name = 'GC_74',
                 value = '(-3*c3G*G**5)/MW**2',
                 order = {'NP':1,'QCD':5})

GC_75 = Coupling(name = 'GC_75',
                 value = '(3*c3G*G**5)/MW**2',
                 order = {'NP':1,'QCD':5})

GC_76 = Coupling(name = 'GC_76',
                 value = '-((c3G*complex(0,1)*G**6)/MW**2)',
                 order = {'NP':1,'QCD':6})

GC_77 = Coupling(name = 'GC_77',
                 value = '(c3G*complex(0,1)*G**6)/MW**2',
                 order = {'NP':1,'QCD':6})

GC_78 = Coupling(name = 'GC_78',
                 value = '(4*cdG*G*I2a33)/MW**2',
                 order = {'NP':1,'QCD':1,'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '(-4*cdG*complex(0,1)*G**2*I2a33)/MW**2',
                 order = {'NP':1,'QCD':2,'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '(-4*cuG*G*I3a33)/MW**2',
                 order = {'NP':1,'QCD':1,'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(4*cuG*complex(0,1)*G**2*I3a33)/MW**2',
                 order = {'NP':1,'QCD':2,'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(4*cuG*G*I5a33)/MW**2',
                 order = {'NP':1,'QCD':1,'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '(-4*cuG*complex(0,1)*G**2*I5a33)/MW**2',
                 order = {'NP':1,'QCD':2,'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '(-4*cdG*G*I6a33)/MW**2',
                 order = {'NP':1,'QCD':1,'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '(4*cdG*complex(0,1)*G**2*I6a33)/MW**2',
                 order = {'NP':1,'QCD':2,'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '(cHW*ee**4*complex(0,1))/(MW**2*sw**4) + (2*cWW*ee**4*complex(0,1))/(MW**2*sw**4)',
                 order = {'NP':1,'QED':4})

GC_87 = Coupling(name = 'GC_87',
                 value = '-(cHW*ee**3)/(2.*MW**2*sw**3) - (cWW*ee**3)/(2.*MW**2*sw**3)',
                 order = {'NP':1,'QED':3})

GC_88 = Coupling(name = 'GC_88',
                 value = '-(cHW*ee**3*complex(0,1))/(2.*MW**2*sw**3) - (cWW*ee**3*complex(0,1))/(2.*MW**2*sw**3)',
                 order = {'NP':1,'QED':3})

GC_89 = Coupling(name = 'GC_89',
                 value = '-((cHW*ee**3*complex(0,1))/(MW**2*sw**3)) - (cWW*ee**3*complex(0,1))/(MW**2*sw**3)',
                 order = {'NP':1,'QED':3})

GC_90 = Coupling(name = 'GC_90',
                 value = '(cHW*ee**3)/(MW**2*sw**3) + (cWW*ee**3)/(MW**2*sw**3)',
                 order = {'NP':1,'QED':3})

GC_91 = Coupling(name = 'GC_91',
                 value = '-((cHW*cw*ee**3)/(MW**2*sw**3)) - (cw*cWW*ee**3)/(MW**2*sw**3)',
                 order = {'NP':1,'QED':3})

GC_92 = Coupling(name = 'GC_92',
                 value = '-(cHW*cw*ee**3*complex(0,1))/(2.*MW**2*sw**3) - (3*cw*cWW*ee**3*complex(0,1))/(2.*MW**2*sw**3)',
                 order = {'NP':1,'QED':3})

GC_93 = Coupling(name = 'GC_93',
                 value = '-(cHW*cw**2*ee**3*complex(0,1))/(2.*MW**2*sw**3) - (cw**2*cWW*ee**3*complex(0,1))/(2.*MW**2*sw**3)',
                 order = {'NP':1,'QED':3})

GC_94 = Coupling(name = 'GC_94',
                 value = '(cHW*cw**2*ee**3*complex(0,1))/(2.*MW**2*sw**3) + (cw**2*cWW*ee**3*complex(0,1))/(2.*MW**2*sw**3)',
                 order = {'NP':1,'QED':3})

GC_95 = Coupling(name = 'GC_95',
                 value = '(cHW*cw**2*ee**3)/(2.*MW**2*sw**3) + (cw**2*cWW*ee**3)/(2.*MW**2*sw**3)',
                 order = {'NP':1,'QED':3})

GC_96 = Coupling(name = 'GC_96',
                 value = '-(cHW*ee**4*complex(0,1))/(2.*MW**2*sw**3) - (cWW*ee**4*complex(0,1))/(2.*MW**2*sw**3)',
                 order = {'NP':1,'QED':4})

GC_97 = Coupling(name = 'GC_97',
                 value = '(cHW*ee**4*complex(0,1))/(MW**2*sw**3) + (cWW*ee**4*complex(0,1))/(MW**2*sw**3)',
                 order = {'NP':1,'QED':4})

GC_98 = Coupling(name = 'GC_98',
                 value = '(cHW*ee**4)/(2.*MW**2*sw**3) + (cWW*ee**4)/(2.*MW**2*sw**3)',
                 order = {'NP':1,'QED':4})

GC_99 = Coupling(name = 'GC_99',
                 value = '(cHW*ee**4)/(MW**2*sw**3) + (cWW*ee**4)/(MW**2*sw**3)',
                 order = {'NP':1,'QED':4})

GC_100 = Coupling(name = 'GC_100',
                  value = '(cHW*ee**3)/(2.*MW**2*sw**2) + (cWW*ee**3)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_101 = Coupling(name = 'GC_101',
                  value = '-((cHW*cw**2*ee**4*complex(0,1))/(MW**2*sw**4)) - (2*cw**2*cWW*ee**4*complex(0,1))/(MW**2*sw**4) - (cHW*ee**4*complex(0,1))/(MW**2*sw**2) - (cWW*ee**4*complex(0,1))/(MW**2*sw**2)',
                  order = {'NP':1,'QED':4})

GC_102 = Coupling(name = 'GC_102',
                  value = '-((cHW*cw**2*ee**4*complex(0,1))/(MW**2*sw**4)) - (2*cw**2*cWW*ee**4*complex(0,1))/(MW**2*sw**4) + (cHW*ee**4*complex(0,1))/(MW**2*sw**2) + (cWW*ee**4*complex(0,1))/(MW**2*sw**2)',
                  order = {'NP':1,'QED':4})

GC_103 = Coupling(name = 'GC_103',
                  value = '(-2*cHW*ee**4*complex(0,1))/(MW**2*sw**2) - (3*cWW*ee**4*complex(0,1))/(MW**2*sw**2)',
                  order = {'NP':1,'QED':4})

GC_104 = Coupling(name = 'GC_104',
                  value = '(cHW*ee**4*complex(0,1))/(2.*cw*MW**2*sw**2) + (cWW*ee**4*complex(0,1))/(2.*cw*MW**2*sw**2)',
                  order = {'NP':1,'QED':4})

GC_105 = Coupling(name = 'GC_105',
                  value = '-((cHW*ee**4*complex(0,1))/(cw*MW**2*sw**2)) - (cWW*ee**4*complex(0,1))/(cw*MW**2*sw**2)',
                  order = {'NP':1,'QED':4})

GC_106 = Coupling(name = 'GC_106',
                  value = '(cHW*ee**4)/(2.*cw*MW**2*sw**2) + (cWW*ee**4)/(2.*cw*MW**2*sw**2)',
                  order = {'NP':1,'QED':4})

GC_107 = Coupling(name = 'GC_107',
                  value = '(cHW*ee**4)/(cw*MW**2*sw**2) + (cWW*ee**4)/(cw*MW**2*sw**2)',
                  order = {'NP':1,'QED':4})

GC_108 = Coupling(name = 'GC_108',
                  value = '-(cHW*ee**4)/(2.*cw*MW**2) - (cWW*ee**4)/(2.*cw*MW**2) - (cHW*cw*ee**4)/(2.*MW**2*sw**2) - (cw*cWW*ee**4)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':4})

GC_109 = Coupling(name = 'GC_109',
                  value = '-(cHW*ee**4*complex(0,1))/(2.*cw*MW**2) - (cWW*ee**4*complex(0,1))/(2.*cw*MW**2) - (cHW*cw*ee**4*complex(0,1))/(2.*MW**2*sw**2) - (cw*cWW*ee**4*complex(0,1))/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':4})

GC_110 = Coupling(name = 'GC_110',
                  value = '(cHW*ee**4)/(2.*cw*MW**2) + (cWW*ee**4)/(2.*cw*MW**2) + (cHW*cw*ee**4)/(2.*MW**2*sw**2) + (cw*cWW*ee**4)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':4})

GC_111 = Coupling(name = 'GC_111',
                  value = '-(cHW*cw**2*ee**4)/(2.*MW**2*sw**3) - (cw**2*cWW*ee**4)/(2.*MW**2*sw**3) - (cHW*ee**4)/(2.*MW**2*sw) - (cWW*ee**4)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':4})

GC_112 = Coupling(name = 'GC_112',
                  value = '(cHW*cw**2*ee**4*complex(0,1))/(2.*MW**2*sw**3) + (cw**2*cWW*ee**4*complex(0,1))/(2.*MW**2*sw**3) + (cHW*ee**4*complex(0,1))/(2.*MW**2*sw) + (cWW*ee**4*complex(0,1))/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':4})

GC_113 = Coupling(name = 'GC_113',
                  value = '(cHW*cw**2*ee**4)/(2.*MW**2*sw**3) + (cw**2*cWW*ee**4)/(2.*MW**2*sw**3) + (cHW*ee**4)/(2.*MW**2*sw) + (cWW*ee**4)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':4})

GC_114 = Coupling(name = 'GC_114',
                  value = '(3*cHW*cw*ee**4*complex(0,1))/(MW**2*sw**3) + (5*cw*cWW*ee**4*complex(0,1))/(MW**2*sw**3) - (cHW*ee**4*complex(0,1))/(cw*MW**2*sw) - (cWW*ee**4*complex(0,1))/(cw*MW**2*sw)',
                  order = {'NP':1,'QED':4})

GC_115 = Coupling(name = 'GC_115',
                  value = '(cHW*cw*ee**4*complex(0,1))/(MW**2*sw**3) + (3*cw*cWW*ee**4*complex(0,1))/(MW**2*sw**3) + (cHW*ee**4*complex(0,1))/(cw*MW**2*sw) + (cWW*ee**4*complex(0,1))/(cw*MW**2*sw)',
                  order = {'NP':1,'QED':4})

GC_116 = Coupling(name = 'GC_116',
                  value = '(-24*c3W*cw**2*ee**6*complex(0,1))/(MW**2*sw**6)',
                  order = {'NP':1,'QED':6})

GC_117 = Coupling(name = 'GC_117',
                  value = '(6*c3W*cw*ee**5*complex(0,1))/(MW**2*sw**5)',
                  order = {'NP':1,'QED':5})

GC_118 = Coupling(name = 'GC_118',
                  value = '(6*c3W*cw**3*ee**5*complex(0,1))/(MW**2*sw**5)',
                  order = {'NP':1,'QED':5})

GC_119 = Coupling(name = 'GC_119',
                  value = '(-24*c3W*cw*ee**6*complex(0,1))/(MW**2*sw**5)',
                  order = {'NP':1,'QED':6})

GC_120 = Coupling(name = 'GC_120',
                  value = '(12*c2W*ee**4*complex(0,1))/(MW**2*sw**4)',
                  order = {'NP':1,'QED':4})

GC_121 = Coupling(name = 'GC_121',
                  value = '(6*c3W*ee**4*complex(0,1))/(MW**2*sw**4)',
                  order = {'NP':1,'QED':4})

GC_122 = Coupling(name = 'GC_122',
                  value = '(12*c2W*cw**2*ee**4*complex(0,1))/(MW**2*sw**4)',
                  order = {'NP':1,'QED':4})

GC_123 = Coupling(name = 'GC_123',
                  value = '(-6*c3W*cw**2*ee**4*complex(0,1))/(MW**2*sw**4)',
                  order = {'NP':1,'QED':4})

GC_124 = Coupling(name = 'GC_124',
                  value = '(-4*c2W*cw**4*ee**4*complex(0,1))/(MW**2*sw**4)',
                  order = {'NP':1,'QED':4})

GC_125 = Coupling(name = 'GC_125',
                  value = '(6*c3W*ee**5*complex(0,1))/(MW**2*sw**4)',
                  order = {'NP':1,'QED':5})

GC_126 = Coupling(name = 'GC_126',
                  value = '(6*c3W*cw**2*ee**5*complex(0,1))/(MW**2*sw**4)',
                  order = {'NP':1,'QED':5})

GC_127 = Coupling(name = 'GC_127',
                  value = '(-24*c3W*ee**6*complex(0,1))/(MW**2*sw**4)',
                  order = {'NP':1,'QED':6})

GC_128 = Coupling(name = 'GC_128',
                  value = '(-8*c2W*cw*ee**3*complex(0,1))/(MW**2*sw**3)',
                  order = {'NP':1,'QED':3})

GC_129 = Coupling(name = 'GC_129',
                  value = '(-6*c3W*cw*ee**3*complex(0,1))/(MW**2*sw**3)',
                  order = {'NP':1,'QED':3})

GC_130 = Coupling(name = 'GC_130',
                  value = '-(cHW*cw*ee**3*complex(0,1))/(2.*MW**2*sw**3)',
                  order = {'NP':1,'QED':3})

GC_131 = Coupling(name = 'GC_131',
                  value = '(2*c2W*cw**3*ee**3*complex(0,1))/(MW**2*sw**3)',
                  order = {'NP':1,'QED':3})

GC_132 = Coupling(name = 'GC_132',
                  value = '(-3*cw*cWW*ee**3*complex(0,1))/(2.*MW**2*sw**3)',
                  order = {'NP':1,'QED':3})

GC_133 = Coupling(name = 'GC_133',
                  value = '(32*c2W*cw*ee**4*complex(0,1))/(MW**2*sw**3)',
                  order = {'NP':1,'QED':4})

GC_134 = Coupling(name = 'GC_134',
                  value = '(6*c3W*cw*ee**4*complex(0,1))/(MW**2*sw**3)',
                  order = {'NP':1,'QED':4})

GC_135 = Coupling(name = 'GC_135',
                  value = '(-4*c2W*cw**3*ee**4*complex(0,1))/(MW**2*sw**3)',
                  order = {'NP':1,'QED':4})

GC_136 = Coupling(name = 'GC_136',
                  value = '(6*c3W*cw*ee**5*complex(0,1))/(MW**2*sw**3)',
                  order = {'NP':1,'QED':5})

GC_137 = Coupling(name = 'GC_137',
                  value = '(ee**2*complex(0,1))/(2.*sw**2)',
                  order = {'QED':2})

GC_138 = Coupling(name = 'GC_138',
                  value = '-((ee**2*complex(0,1))/sw**2)',
                  order = {'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '-(cH*ee**2*complex(0,1))/(2.*sw**2)',
                  order = {'NP':1,'QED':2})

GC_140 = Coupling(name = 'GC_140',
                  value = '-((cT*ee**2*complex(0,1))/sw**2)',
                  order = {'NP':1,'QED':2})

GC_141 = Coupling(name = 'GC_141',
                  value = '(2*cT*ee**2*complex(0,1))/sw**2',
                  order = {'NP':1,'QED':2})

GC_142 = Coupling(name = 'GC_142',
                  value = '(cw**2*ee**2*complex(0,1))/sw**2',
                  order = {'QED':2})

GC_143 = Coupling(name = 'GC_143',
                  value = '(8*c2W*ee**2*complex(0,1))/(MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_144 = Coupling(name = 'GC_144',
                  value = '-(cHW*ee**2)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_145 = Coupling(name = 'GC_145',
                  value = '(cHW*ee**2*complex(0,1))/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_146 = Coupling(name = 'GC_146',
                  value = '(cHW*ee**2*complex(0,1))/(MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_147 = Coupling(name = 'GC_147',
                  value = '-(cHW*cw*ee**2)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_148 = Coupling(name = 'GC_148',
                  value = '-(cHW*cw*ee**2*complex(0,1))/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_149 = Coupling(name = 'GC_149',
                  value = '(cHW*cw*ee**2)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_150 = Coupling(name = 'GC_150',
                  value = '(-8*c2W*cw**2*ee**2*complex(0,1))/(MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_151 = Coupling(name = 'GC_151',
                  value = '-((cWW*ee**2)/(MW**2*sw**2))',
                  order = {'NP':1,'QED':2})

GC_152 = Coupling(name = 'GC_152',
                  value = '-(cWW*ee**2*complex(0,1))/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_153 = Coupling(name = 'GC_153',
                  value = '-((cw*cWW*ee**2)/(MW**2*sw**2))',
                  order = {'NP':1,'QED':2})

GC_154 = Coupling(name = 'GC_154',
                  value = '-((cw*cWW*ee**2*complex(0,1))/(MW**2*sw**2))',
                  order = {'NP':1,'QED':2})

GC_155 = Coupling(name = 'GC_155',
                  value = '(cw*cWW*ee**2)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_156 = Coupling(name = 'GC_156',
                  value = '(4*c2W*ee**3*complex(0,1))/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_157 = Coupling(name = 'GC_157',
                  value = '(-6*c3W*ee**3*complex(0,1))/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_158 = Coupling(name = 'GC_158',
                  value = '-(cHB*ee**3*complex(0,1))/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_159 = Coupling(name = 'GC_159',
                  value = '(cHB*ee**3*complex(0,1))/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_160 = Coupling(name = 'GC_160',
                  value = '-(cHW*ee**3*complex(0,1))/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_161 = Coupling(name = 'GC_161',
                  value = '-(cHB*cw*ee**3*complex(0,1))/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_162 = Coupling(name = 'GC_162',
                  value = '(cHB*cw*ee**3*complex(0,1))/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_163 = Coupling(name = 'GC_163',
                  value = '(cHB*cw*ee**3)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_164 = Coupling(name = 'GC_164',
                  value = '-(cHW*cw*ee**3*complex(0,1))/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_165 = Coupling(name = 'GC_165',
                  value = '(cHW*cw*ee**3*complex(0,1))/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_166 = Coupling(name = 'GC_166',
                  value = '(cHW*cw*ee**3)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_167 = Coupling(name = 'GC_167',
                  value = '(-8*c2W*cw**2*ee**3*complex(0,1))/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_168 = Coupling(name = 'GC_168',
                  value = '(-3*cWW*ee**3*complex(0,1))/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_169 = Coupling(name = 'GC_169',
                  value = '-((cw*cWW*ee**3*complex(0,1))/(MW**2*sw**2))',
                  order = {'NP':1,'QED':3})

GC_170 = Coupling(name = 'GC_170',
                  value = '(cw*cWW*ee**3*complex(0,1))/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_171 = Coupling(name = 'GC_171',
                  value = '(cw*cWW*ee**3)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_172 = Coupling(name = 'GC_172',
                  value = '(12*c2W*ee**4*complex(0,1))/(MW**2*sw**2)',
                  order = {'NP':1,'QED':4})

GC_173 = Coupling(name = 'GC_173',
                  value = '(-6*c3W*ee**4*complex(0,1))/(MW**2*sw**2)',
                  order = {'NP':1,'QED':4})

GC_174 = Coupling(name = 'GC_174',
                  value = '(16*c2W*cw**2*ee**4*complex(0,1))/(MW**2*sw**2)',
                  order = {'NP':1,'QED':4})

GC_175 = Coupling(name = 'GC_175',
                  value = '-((cWW*ee**4*complex(0,1))/(MW**2*sw**2))',
                  order = {'NP':1,'QED':4})

GC_176 = Coupling(name = 'GC_176',
                  value = '(12*c3W*ee**5*complex(0,1))/(MW**2*sw**2)',
                  order = {'NP':1,'QED':5})

GC_177 = Coupling(name = 'GC_177',
                  value = '(-2*cdW*ee**2*I2a33)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_178 = Coupling(name = 'GC_178',
                  value = '(2*cdW*cw*ee**2*complex(0,1)*I2a33)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_179 = Coupling(name = 'GC_179',
                  value = '(2*cdW*cw*ee**2*I2a33)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_180 = Coupling(name = 'GC_180',
                  value = '(-2*cuW*ee**2*I3a33)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_181 = Coupling(name = 'GC_181',
                  value = '(2*cuW*cw*ee**2*complex(0,1)*I3a33)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_182 = Coupling(name = 'GC_182',
                  value = '(2*cuW*cw*ee**2*I3a33)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_183 = Coupling(name = 'GC_183',
                  value = '(2*cuW*ee**2*I5a33)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_184 = Coupling(name = 'GC_184',
                  value = '(-2*cuW*cw*ee**2*complex(0,1)*I5a33)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_185 = Coupling(name = 'GC_185',
                  value = '(2*cuW*cw*ee**2*I5a33)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_186 = Coupling(name = 'GC_186',
                  value = '(2*cdW*ee**2*I6a33)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_187 = Coupling(name = 'GC_187',
                  value = '(-2*cdW*cw*ee**2*complex(0,1)*I6a33)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_188 = Coupling(name = 'GC_188',
                  value = '(2*cdW*cw*ee**2*I6a33)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_189 = Coupling(name = 'GC_189',
                  value = '-ee/(2.*sw)',
                  order = {'QED':1})

GC_190 = Coupling(name = 'GC_190',
                  value = '-(ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '(ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '(cH*ee)/(4.*sw)',
                  order = {'NP':1,'QED':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '-((cT*ee*complex(0,1))/sw)',
                  order = {'NP':1,'QED':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '(cT*ee*complex(0,1))/sw',
                  order = {'NP':1,'QED':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '-(cw*ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '(cw*ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_198 = Coupling(name = 'GC_198',
                  value = '-((cw*ee*complex(0,1))/sw)',
                  order = {'QED':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '(cHud*DEL1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = '(cpHL*DEL1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '(cHud*DEL1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '(cpHL*DEL1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '(cHud*DEL1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '(cpHL*DEL1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '(cHud*DEL2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '(cpHL*DEL2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '(cHud*DEL2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_209 = Coupling(name = 'GC_209',
                  value = '(cpHL*DEL2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_210 = Coupling(name = 'GC_210',
                  value = '(cHud*DEL2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '(cpHL*DEL2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_212 = Coupling(name = 'GC_212',
                  value = '(cHud*DEL3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '(cpHL*DEL3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '(cHud*DEL3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '(cpHL*DEL3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '(cHud*DEL3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_217 = Coupling(name = 'GC_217',
                  value = '(cpHL*DEL3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '-ee**2/(2.*sw)',
                  order = {'QED':2})

GC_219 = Coupling(name = 'GC_219',
                  value = '-(ee**2*complex(0,1))/(2.*sw)',
                  order = {'QED':2})

GC_220 = Coupling(name = 'GC_220',
                  value = 'ee**2/(2.*sw)',
                  order = {'QED':2})

GC_221 = Coupling(name = 'GC_221',
                  value = '(-2*cw*ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_222 = Coupling(name = 'GC_222',
                  value = '(cpHQ*ee*complex(0,1)*I4a11)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '(cpHQ*ee*complex(0,1)*I4a12)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_224 = Coupling(name = 'GC_224',
                  value = '(cpHQ*ee*complex(0,1)*I4a13)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '(cpHQ*ee*complex(0,1)*I4a21)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '(cpHQ*ee*complex(0,1)*I4a22)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '(cpHQ*ee*complex(0,1)*I4a23)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '(cpHQ*ee*complex(0,1)*I4a31)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '(cpHQ*ee*complex(0,1)*I4a32)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '(cpHQ*ee*complex(0,1)*I4a33)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '(cpHQ*ee*complex(0,1)*I7a11)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_232 = Coupling(name = 'GC_232',
                  value = '(cpHQ*ee*complex(0,1)*I7a12)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '(cpHQ*ee*complex(0,1)*I7a13)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '(cpHQ*ee*complex(0,1)*I7a21)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_235 = Coupling(name = 'GC_235',
                  value = '(cpHQ*ee*complex(0,1)*I7a22)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_236 = Coupling(name = 'GC_236',
                  value = '(cpHQ*ee*complex(0,1)*I7a23)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '(cpHQ*ee*complex(0,1)*I7a31)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_238 = Coupling(name = 'GC_238',
                  value = '(cpHQ*ee*complex(0,1)*I7a32)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '(cpHQ*ee*complex(0,1)*I7a33)/(sw*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '-((cHW*ee)/(MW**2*sw))',
                  order = {'NP':1,'QED':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '-((cHW*ee*complex(0,1))/(MW**2*sw))',
                  order = {'NP':1,'QED':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '(cHW*ee*complex(0,1))/(MW**2*sw)',
                  order = {'NP':1,'QED':1})

GC_243 = Coupling(name = 'GC_243',
                  value = '(2*c2W*cw*ee*complex(0,1))/(MW**2*sw)',
                  order = {'NP':1,'QED':1})

GC_244 = Coupling(name = 'GC_244',
                  value = '-(cWW*ee)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':1})

GC_245 = Coupling(name = 'GC_245',
                  value = '-(cWW*ee*complex(0,1))/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':1})

GC_246 = Coupling(name = 'GC_246',
                  value = '(cWW*ee*complex(0,1))/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':1})

GC_247 = Coupling(name = 'GC_247',
                  value = '-(cB*ee**2)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_248 = Coupling(name = 'GC_248',
                  value = '(cB*ee**2*complex(0,1))/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_249 = Coupling(name = 'GC_249',
                  value = '(cB*ee**2)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_250 = Coupling(name = 'GC_250',
                  value = '-(cHB*ee**2)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_251 = Coupling(name = 'GC_251',
                  value = '-(cHB*ee**2*complex(0,1))/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_252 = Coupling(name = 'GC_252',
                  value = '(cHB*ee**2)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_253 = Coupling(name = 'GC_253',
                  value = '-(cHW*ee**2)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_254 = Coupling(name = 'GC_254',
                  value = '(cHW*ee**2*complex(0,1))/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_255 = Coupling(name = 'GC_255',
                  value = '(cHW*ee**2)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_256 = Coupling(name = 'GC_256',
                  value = '(8*c2W*cw*ee**2*complex(0,1))/(MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_257 = Coupling(name = 'GC_257',
                  value = '-(cWW*ee**2)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_258 = Coupling(name = 'GC_258',
                  value = '(cWW*ee**2*complex(0,1))/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_259 = Coupling(name = 'GC_259',
                  value = '(cWW*ee**2)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_260 = Coupling(name = 'GC_260',
                  value = '-(cHB*ee**3)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_261 = Coupling(name = 'GC_261',
                  value = '-(cHB*ee**3*complex(0,1))/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_262 = Coupling(name = 'GC_262',
                  value = '(cHB*ee**3*complex(0,1))/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_263 = Coupling(name = 'GC_263',
                  value = '-(cHW*ee**3)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_264 = Coupling(name = 'GC_264',
                  value = '-(cHW*ee**3*complex(0,1))/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_265 = Coupling(name = 'GC_265',
                  value = '(cHW*ee**3*complex(0,1))/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_266 = Coupling(name = 'GC_266',
                  value = '-(cHB*ee**3*complex(0,1))/(2.*cw*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_267 = Coupling(name = 'GC_267',
                  value = '(cHB*ee**3*complex(0,1))/(2.*cw*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_268 = Coupling(name = 'GC_268',
                  value = '-(cHW*ee**3*complex(0,1))/(2.*cw*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_269 = Coupling(name = 'GC_269',
                  value = '(cHW*ee**3*complex(0,1))/(2.*cw*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_270 = Coupling(name = 'GC_270',
                  value = '(-2*c2W*cw*ee**3*complex(0,1))/(MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_271 = Coupling(name = 'GC_271',
                  value = '-((cWW*ee**3)/(MW**2*sw))',
                  order = {'NP':1,'QED':3})

GC_272 = Coupling(name = 'GC_272',
                  value = '-(cWW*ee**3)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_273 = Coupling(name = 'GC_273',
                  value = '-(cWW*ee**3*complex(0,1))/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_274 = Coupling(name = 'GC_274',
                  value = '(cWW*ee**3*complex(0,1))/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_275 = Coupling(name = 'GC_275',
                  value = '-((cWW*ee**3*complex(0,1))/(MW**2*sw))',
                  order = {'NP':1,'QED':3})

GC_276 = Coupling(name = 'GC_276',
                  value = '(cWW*ee**3*complex(0,1))/(MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_277 = Coupling(name = 'GC_277',
                  value = '-(cWW*ee**3*complex(0,1))/(2.*cw*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_278 = Coupling(name = 'GC_278',
                  value = '(cWW*ee**3*complex(0,1))/(2.*cw*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_279 = Coupling(name = 'GC_279',
                  value = '(-4*c2W*cw*ee**4*complex(0,1))/(MW**2*sw)',
                  order = {'NP':1,'QED':4})

GC_280 = Coupling(name = 'GC_280',
                  value = '(-2*cdW*ee*I2a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_281 = Coupling(name = 'GC_281',
                  value = '(-2*cdW*ee*complex(0,1)*I2a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_282 = Coupling(name = 'GC_282',
                  value = '(-2*cdW*ee**2*I2a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_283 = Coupling(name = 'GC_283',
                  value = '(-2*cdW*ee**2*complex(0,1)*I2a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_284 = Coupling(name = 'GC_284',
                  value = '(-2*cuW*ee*I3a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_285 = Coupling(name = 'GC_285',
                  value = '(-2*cuW*ee*complex(0,1)*I3a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_286 = Coupling(name = 'GC_286',
                  value = '(-2*cuW*ee**2*I3a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_287 = Coupling(name = 'GC_287',
                  value = '(-2*cuW*ee**2*complex(0,1)*I3a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_288 = Coupling(name = 'GC_288',
                  value = '(-2*cuW*ee*complex(0,1)*I5a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_289 = Coupling(name = 'GC_289',
                  value = '(2*cuW*ee*I5a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_290 = Coupling(name = 'GC_290',
                  value = '(-2*cuW*ee**2*I5a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_291 = Coupling(name = 'GC_291',
                  value = '(2*cuW*ee**2*complex(0,1)*I5a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_292 = Coupling(name = 'GC_292',
                  value = '(-2*cdW*ee*complex(0,1)*I6a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_293 = Coupling(name = 'GC_293',
                  value = '(2*cdW*ee*I6a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_294 = Coupling(name = 'GC_294',
                  value = '(-2*cdW*ee**2*I6a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_295 = Coupling(name = 'GC_295',
                  value = '(2*cdW*ee**2*complex(0,1)*I6a33)/(MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_296 = Coupling(name = 'GC_296',
                  value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'QED':1})

GC_297 = Coupling(name = 'GC_297',
                  value = '(ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_298 = Coupling(name = 'GC_298',
                  value = '(-4*cA*ee**2*complex(0,1)*sw)/(cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_299 = Coupling(name = 'GC_299',
                  value = '(4*cA*ee**2*complex(0,1)*sw**2)/(cw**2*MW**2)',
                  order = {'NP':1,'QED':2})

GC_300 = Coupling(name = 'GC_300',
                  value = '-(cw*ee)/(2.*sw) - (ee*sw)/(2.*cw)',
                  order = {'QED':1})

GC_301 = Coupling(name = 'GC_301',
                  value = '-(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_302 = Coupling(name = 'GC_302',
                  value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_303 = Coupling(name = 'GC_303',
                  value = '(3*cT*cw*ee)/(2.*sw) + (3*cT*ee*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_304 = Coupling(name = 'GC_304',
                  value = '-(cHe*cw*DEL1x1*ee*complex(0,1))/(4.*sw) - (cHe*DEL1x1*ee*complex(0,1)*sw)/(4.*cw)',
                  order = {'NP':1,'QED':1})

GC_305 = Coupling(name = 'GC_305',
                  value = '-(cHe*cw*DEL1x2*ee*complex(0,1))/(4.*sw) - (cHe*DEL1x2*ee*complex(0,1)*sw)/(4.*cw)',
                  order = {'NP':1,'QED':1})

GC_306 = Coupling(name = 'GC_306',
                  value = '-(cHL*cw*DEL1x2*ee*complex(0,1))/(2.*sw) - (cpHL*cw*DEL1x2*ee*complex(0,1))/(2.*sw) - (cHL*DEL1x2*ee*complex(0,1)*sw)/(2.*cw) - (cpHL*DEL1x2*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_307 = Coupling(name = 'GC_307',
                  value = '-(cHL*cw*DEL1x2*ee*complex(0,1))/(2.*sw) + (cpHL*cw*DEL1x2*ee*complex(0,1))/(2.*sw) - (cHL*DEL1x2*ee*complex(0,1)*sw)/(2.*cw) + (cpHL*DEL1x2*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_308 = Coupling(name = 'GC_308',
                  value = '-(cHQ*cw*DEL1x2*ee*complex(0,1))/(2.*sw) + (cpHQ*cw*DEL1x2*ee*complex(0,1))/(2.*sw) - (cHQ*DEL1x2*ee*complex(0,1)*sw)/(2.*cw) + (cpHQ*DEL1x2*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_309 = Coupling(name = 'GC_309',
                  value = '-(cHe*cw*DEL1x3*ee*complex(0,1))/(4.*sw) - (cHe*DEL1x3*ee*complex(0,1)*sw)/(4.*cw)',
                  order = {'NP':1,'QED':1})

GC_310 = Coupling(name = 'GC_310',
                  value = '-(cHL*cw*DEL1x3*ee*complex(0,1))/(2.*sw) - (cpHL*cw*DEL1x3*ee*complex(0,1))/(2.*sw) - (cHL*DEL1x3*ee*complex(0,1)*sw)/(2.*cw) - (cpHL*DEL1x3*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_311 = Coupling(name = 'GC_311',
                  value = '-(cHL*cw*DEL1x3*ee*complex(0,1))/(2.*sw) + (cpHL*cw*DEL1x3*ee*complex(0,1))/(2.*sw) - (cHL*DEL1x3*ee*complex(0,1)*sw)/(2.*cw) + (cpHL*DEL1x3*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_312 = Coupling(name = 'GC_312',
                  value = '-(cHQ*cw*DEL1x3*ee*complex(0,1))/(2.*sw) + (cpHQ*cw*DEL1x3*ee*complex(0,1))/(2.*sw) - (cHQ*DEL1x3*ee*complex(0,1)*sw)/(2.*cw) + (cpHQ*DEL1x3*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_313 = Coupling(name = 'GC_313',
                  value = '-(cHe*cw*DEL2x1*ee*complex(0,1))/(4.*sw) - (cHe*DEL2x1*ee*complex(0,1)*sw)/(4.*cw)',
                  order = {'NP':1,'QED':1})

GC_314 = Coupling(name = 'GC_314',
                  value = '-(cHL*cw*DEL2x1*ee*complex(0,1))/(2.*sw) - (cpHL*cw*DEL2x1*ee*complex(0,1))/(2.*sw) - (cHL*DEL2x1*ee*complex(0,1)*sw)/(2.*cw) - (cpHL*DEL2x1*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_315 = Coupling(name = 'GC_315',
                  value = '-(cHL*cw*DEL2x1*ee*complex(0,1))/(2.*sw) + (cpHL*cw*DEL2x1*ee*complex(0,1))/(2.*sw) - (cHL*DEL2x1*ee*complex(0,1)*sw)/(2.*cw) + (cpHL*DEL2x1*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_316 = Coupling(name = 'GC_316',
                  value = '-(cHQ*cw*DEL2x1*ee*complex(0,1))/(2.*sw) + (cpHQ*cw*DEL2x1*ee*complex(0,1))/(2.*sw) - (cHQ*DEL2x1*ee*complex(0,1)*sw)/(2.*cw) + (cpHQ*DEL2x1*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_317 = Coupling(name = 'GC_317',
                  value = '-(cHe*cw*DEL2x2*ee*complex(0,1))/(4.*sw) - (cHe*DEL2x2*ee*complex(0,1)*sw)/(4.*cw)',
                  order = {'NP':1,'QED':1})

GC_318 = Coupling(name = 'GC_318',
                  value = '-(cHe*cw*DEL2x3*ee*complex(0,1))/(4.*sw) - (cHe*DEL2x3*ee*complex(0,1)*sw)/(4.*cw)',
                  order = {'NP':1,'QED':1})

GC_319 = Coupling(name = 'GC_319',
                  value = '-(cHL*cw*DEL2x3*ee*complex(0,1))/(2.*sw) - (cpHL*cw*DEL2x3*ee*complex(0,1))/(2.*sw) - (cHL*DEL2x3*ee*complex(0,1)*sw)/(2.*cw) - (cpHL*DEL2x3*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_320 = Coupling(name = 'GC_320',
                  value = '-(cHL*cw*DEL2x3*ee*complex(0,1))/(2.*sw) + (cpHL*cw*DEL2x3*ee*complex(0,1))/(2.*sw) - (cHL*DEL2x3*ee*complex(0,1)*sw)/(2.*cw) + (cpHL*DEL2x3*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_321 = Coupling(name = 'GC_321',
                  value = '-(cHQ*cw*DEL2x3*ee*complex(0,1))/(2.*sw) + (cpHQ*cw*DEL2x3*ee*complex(0,1))/(2.*sw) - (cHQ*DEL2x3*ee*complex(0,1)*sw)/(2.*cw) + (cpHQ*DEL2x3*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_322 = Coupling(name = 'GC_322',
                  value = '-(cHe*cw*DEL3x1*ee*complex(0,1))/(4.*sw) - (cHe*DEL3x1*ee*complex(0,1)*sw)/(4.*cw)',
                  order = {'NP':1,'QED':1})

GC_323 = Coupling(name = 'GC_323',
                  value = '-(cHL*cw*DEL3x1*ee*complex(0,1))/(2.*sw) - (cpHL*cw*DEL3x1*ee*complex(0,1))/(2.*sw) - (cHL*DEL3x1*ee*complex(0,1)*sw)/(2.*cw) - (cpHL*DEL3x1*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_324 = Coupling(name = 'GC_324',
                  value = '-(cHL*cw*DEL3x1*ee*complex(0,1))/(2.*sw) + (cpHL*cw*DEL3x1*ee*complex(0,1))/(2.*sw) - (cHL*DEL3x1*ee*complex(0,1)*sw)/(2.*cw) + (cpHL*DEL3x1*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_325 = Coupling(name = 'GC_325',
                  value = '-(cHQ*cw*DEL3x1*ee*complex(0,1))/(2.*sw) + (cpHQ*cw*DEL3x1*ee*complex(0,1))/(2.*sw) - (cHQ*DEL3x1*ee*complex(0,1)*sw)/(2.*cw) + (cpHQ*DEL3x1*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_326 = Coupling(name = 'GC_326',
                  value = '-(cHe*cw*DEL3x2*ee*complex(0,1))/(4.*sw) - (cHe*DEL3x2*ee*complex(0,1)*sw)/(4.*cw)',
                  order = {'NP':1,'QED':1})

GC_327 = Coupling(name = 'GC_327',
                  value = '-(cHL*cw*DEL3x2*ee*complex(0,1))/(2.*sw) - (cpHL*cw*DEL3x2*ee*complex(0,1))/(2.*sw) - (cHL*DEL3x2*ee*complex(0,1)*sw)/(2.*cw) - (cpHL*DEL3x2*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_328 = Coupling(name = 'GC_328',
                  value = '-(cHL*cw*DEL3x2*ee*complex(0,1))/(2.*sw) + (cpHL*cw*DEL3x2*ee*complex(0,1))/(2.*sw) - (cHL*DEL3x2*ee*complex(0,1)*sw)/(2.*cw) + (cpHL*DEL3x2*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_329 = Coupling(name = 'GC_329',
                  value = '-(cHQ*cw*DEL3x2*ee*complex(0,1))/(2.*sw) + (cpHQ*cw*DEL3x2*ee*complex(0,1))/(2.*sw) - (cHQ*DEL3x2*ee*complex(0,1)*sw)/(2.*cw) + (cpHQ*DEL3x2*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_330 = Coupling(name = 'GC_330',
                  value = '-(cHe*cw*DEL3x3*ee*complex(0,1))/(4.*sw) - (cHe*DEL3x3*ee*complex(0,1)*sw)/(4.*cw)',
                  order = {'NP':1,'QED':1})

GC_331 = Coupling(name = 'GC_331',
                  value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                  order = {'QED':2})

GC_332 = Coupling(name = 'GC_332',
                  value = '-(cHQ*cw*ee*complex(0,1)*I1a12)/(2.*sw) - (cpHQ*cw*ee*complex(0,1)*I1a12)/(2.*sw) - (cHQ*ee*complex(0,1)*I1a12*sw)/(2.*cw) - (cpHQ*ee*complex(0,1)*I1a12*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_333 = Coupling(name = 'GC_333',
                  value = '-(cHQ*cw*ee*complex(0,1)*I1a13)/(2.*sw) - (cpHQ*cw*ee*complex(0,1)*I1a13)/(2.*sw) - (cHQ*ee*complex(0,1)*I1a13*sw)/(2.*cw) - (cpHQ*ee*complex(0,1)*I1a13*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_334 = Coupling(name = 'GC_334',
                  value = '-(cHQ*cw*ee*complex(0,1)*I1a21)/(2.*sw) - (cpHQ*cw*ee*complex(0,1)*I1a21)/(2.*sw) - (cHQ*ee*complex(0,1)*I1a21*sw)/(2.*cw) - (cpHQ*ee*complex(0,1)*I1a21*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_335 = Coupling(name = 'GC_335',
                  value = '-(cHQ*cw*ee*complex(0,1)*I1a23)/(2.*sw) - (cpHQ*cw*ee*complex(0,1)*I1a23)/(2.*sw) - (cHQ*ee*complex(0,1)*I1a23*sw)/(2.*cw) - (cpHQ*ee*complex(0,1)*I1a23*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_336 = Coupling(name = 'GC_336',
                  value = '-(cHQ*cw*ee*complex(0,1)*I1a31)/(2.*sw) - (cpHQ*cw*ee*complex(0,1)*I1a31)/(2.*sw) - (cHQ*ee*complex(0,1)*I1a31*sw)/(2.*cw) - (cpHQ*ee*complex(0,1)*I1a31*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_337 = Coupling(name = 'GC_337',
                  value = '-(cHQ*cw*ee*complex(0,1)*I1a32)/(2.*sw) - (cpHQ*cw*ee*complex(0,1)*I1a32)/(2.*sw) - (cHQ*ee*complex(0,1)*I1a32*sw)/(2.*cw) - (cpHQ*ee*complex(0,1)*I1a32*sw)/(2.*cw)',
                  order = {'NP':1,'QED':1})

GC_338 = Coupling(name = 'GC_338',
                  value = '-(cw*cWW*ee)/(2.*MW**2*sw) - (cB*ee*sw)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':1})

GC_339 = Coupling(name = 'GC_339',
                  value = '-(cw*cWW*ee*complex(0,1))/(2.*MW**2*sw) + (cB*ee*complex(0,1)*sw)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':1})

GC_340 = Coupling(name = 'GC_340',
                  value = '-((cHW*cw*ee)/(MW**2*sw)) - (cHB*ee*sw)/(cw*MW**2)',
                  order = {'NP':1,'QED':1})

GC_341 = Coupling(name = 'GC_341',
                  value = '-((cHW*cw*ee*complex(0,1))/(MW**2*sw)) + (cHB*ee*complex(0,1)*sw)/(cw*MW**2)',
                  order = {'NP':1,'QED':1})

GC_342 = Coupling(name = 'GC_342',
                  value = '-(cw*cWW*ee**2*complex(0,1))/(2.*MW**2*sw) + (cB*ee**2*complex(0,1)*sw)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_343 = Coupling(name = 'GC_343',
                  value = '(cHW*cw*ee**2*complex(0,1))/(2.*MW**2*sw) - (cHB*ee**2*complex(0,1)*sw)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_344 = Coupling(name = 'GC_344',
                  value = '(cHB*cw*ee**2*complex(0,1))/(2.*MW**2*sw) - (cHW*ee**2*complex(0,1)*sw)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_345 = Coupling(name = 'GC_345',
                  value = '-(cHB*cw*ee**2*complex(0,1))/(2.*MW**2*sw) + (cHW*cw*ee**2*complex(0,1))/(2.*MW**2*sw) - (cHB*ee**2*complex(0,1)*sw)/(2.*cw*MW**2) + (cHW*ee**2*complex(0,1)*sw)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_346 = Coupling(name = 'GC_346',
                  value = '(cB*cw*ee**2*complex(0,1))/(2.*MW**2*sw) - (cw*cWW*ee**2*complex(0,1))/(2.*MW**2*sw) + (cB*ee**2*complex(0,1)*sw)/(2.*cw*MW**2) - (cWW*ee**2*complex(0,1)*sw)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_347 = Coupling(name = 'GC_347',
                  value = '-(cB*cw*ee**2*complex(0,1))/(2.*MW**2*sw) + (cWW*ee**2*complex(0,1)*sw)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_348 = Coupling(name = 'GC_348',
                  value = '(2*cdW*cw*ee*I2a33)/(MW**2*sw) - (2*cdB*ee*I2a33*sw)/(cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_349 = Coupling(name = 'GC_349',
                  value = '(2*cuW*cw*ee*I3a33)/(MW**2*sw) + (2*cuB*ee*I3a33*sw)/(cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_350 = Coupling(name = 'GC_350',
                  value = '(-2*cuW*cw*ee*I5a33)/(MW**2*sw) - (2*cuB*ee*I5a33*sw)/(cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_351 = Coupling(name = 'GC_351',
                  value = '(-2*cdW*cw*ee*I6a33)/(MW**2*sw) + (2*cdB*ee*I6a33*sw)/(cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_352 = Coupling(name = 'GC_352',
                  value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_353 = Coupling(name = 'GC_353',
                  value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_354 = Coupling(name = 'GC_354',
                  value = '-(cB*ee**2*complex(0,1))/(2.*MW**2) - (cWW*ee**2*complex(0,1))/(2.*MW**2) - (cw**2*cWW*ee**2*complex(0,1))/(2.*MW**2*sw**2) - (cB*ee**2*complex(0,1)*sw**2)/(2.*cw**2*MW**2)',
                  order = {'NP':1,'QED':2})

GC_355 = Coupling(name = 'GC_355',
                  value = '(cB*ee**2*complex(0,1))/(2.*MW**2) + (cWW*ee**2*complex(0,1))/(2.*MW**2) - (cw**2*cWW*ee**2*complex(0,1))/(2.*MW**2*sw**2) - (cB*ee**2*complex(0,1)*sw**2)/(2.*cw**2*MW**2)',
                  order = {'NP':1,'QED':2})

GC_356 = Coupling(name = 'GC_356',
                  value = '-(cHB*ee**2*complex(0,1))/(2.*MW**2) - (cHW*ee**2*complex(0,1))/(2.*MW**2) + (cHW*cw**2*ee**2*complex(0,1))/(2.*MW**2*sw**2) + (cHB*ee**2*complex(0,1)*sw**2)/(2.*cw**2*MW**2)',
                  order = {'NP':1,'QED':2})

GC_357 = Coupling(name = 'GC_357',
                  value = '(cHB*ee**2*complex(0,1))/(2.*MW**2) + (cHW*ee**2*complex(0,1))/(2.*MW**2) + (cHW*cw**2*ee**2*complex(0,1))/(2.*MW**2*sw**2) + (cHB*ee**2*complex(0,1)*sw**2)/(2.*cw**2*MW**2)',
                  order = {'NP':1,'QED':2})

GC_358 = Coupling(name = 'GC_358',
                  value = '-(G**3*tc3G)/(2.*MW**2)',
                  order = {'NP':1,'QCD':3})

GC_359 = Coupling(name = 'GC_359',
                  value = '(complex(0,1)*G**4*tc3G)/(2.*MW**2)',
                  order = {'NP':1,'QCD':4})

GC_360 = Coupling(name = 'GC_360',
                  value = '(complex(0,1)*G**4*tc3G)/MW**2',
                  order = {'NP':1,'QCD':4})

GC_361 = Coupling(name = 'GC_361',
                  value = '(-2*G**5*tc3G)/MW**2',
                  order = {'NP':1,'QCD':5})

GC_362 = Coupling(name = 'GC_362',
                  value = '(2*G**5*tc3G)/MW**2',
                  order = {'NP':1,'QCD':5})

GC_363 = Coupling(name = 'GC_363',
                  value = '-((complex(0,1)*G**6*tc3G)/MW**2)',
                  order = {'NP':1,'QCD':6})

GC_364 = Coupling(name = 'GC_364',
                  value = '(complex(0,1)*G**6*tc3G)/MW**2',
                  order = {'NP':1,'QCD':6})

GC_365 = Coupling(name = 'GC_365',
                  value = '(4*cw*ee**5*complex(0,1)*tc3W)/(MW**2*sw**5)',
                  order = {'NP':1,'QED':5})

GC_366 = Coupling(name = 'GC_366',
                  value = '(4*cw**3*ee**5*complex(0,1)*tc3W)/(MW**2*sw**5)',
                  order = {'NP':1,'QED':5})

GC_367 = Coupling(name = 'GC_367',
                  value = '(-2*ee**4*complex(0,1)*tc3W)/(MW**2*sw**4)',
                  order = {'NP':1,'QED':4})

GC_368 = Coupling(name = 'GC_368',
                  value = '(2*cw**2*ee**4*complex(0,1)*tc3W)/(MW**2*sw**4)',
                  order = {'NP':1,'QED':4})

GC_369 = Coupling(name = 'GC_369',
                  value = '(-4*ee**5*complex(0,1)*tc3W)/(MW**2*sw**4)',
                  order = {'NP':1,'QED':5})

GC_370 = Coupling(name = 'GC_370',
                  value = '(4*cw**2*ee**5*complex(0,1)*tc3W)/(MW**2*sw**4)',
                  order = {'NP':1,'QED':5})

GC_371 = Coupling(name = 'GC_371',
                  value = '(-2*cw*ee**3*complex(0,1)*tc3W)/(MW**2*sw**3)',
                  order = {'NP':1,'QED':3})

GC_372 = Coupling(name = 'GC_372',
                  value = '(-2*cw*ee**4*complex(0,1)*tc3W)/(MW**2*sw**3)',
                  order = {'NP':1,'QED':4})

GC_373 = Coupling(name = 'GC_373',
                  value = '(4*cw*ee**5*complex(0,1)*tc3W)/(MW**2*sw**3)',
                  order = {'NP':1,'QED':5})

GC_374 = Coupling(name = 'GC_374',
                  value = '(-2*ee**3*complex(0,1)*tc3W)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_375 = Coupling(name = 'GC_375',
                  value = '(2*ee**4*complex(0,1)*tc3W)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':4})

GC_376 = Coupling(name = 'GC_376',
                  value = '(4*ee**5*complex(0,1)*tc3W)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':5})

GC_377 = Coupling(name = 'GC_377',
                  value = '(-2*ee**2*complex(0,1)*tcA)/MW**2',
                  order = {'NP':1,'QED':2})

GC_378 = Coupling(name = 'GC_378',
                  value = '(-4*ee**2*complex(0,1)*sw*tcA)/(cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_379 = Coupling(name = 'GC_379',
                  value = '(-2*ee**2*complex(0,1)*sw**2*tcA)/(cw**2*MW**2)',
                  order = {'NP':1,'QED':2})

GC_380 = Coupling(name = 'GC_380',
                  value = '(-2*dum**2*complex(0,1)*G**2*tcG)/MW**2',
                  order = {'NP':1,'QCD':2,'QED':2})

GC_381 = Coupling(name = 'GC_381',
                  value = '(-4*dum**2*G**3*tcG)/MW**2',
                  order = {'NP':1,'QCD':3,'QED':2})

GC_382 = Coupling(name = 'GC_382',
                  value = '-(ee**2*tcHB)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_383 = Coupling(name = 'GC_383',
                  value = '(ee**2*complex(0,1)*tcHB)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_384 = Coupling(name = 'GC_384',
                  value = '(ee**2*tcHB)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_385 = Coupling(name = 'GC_385',
                  value = '-(ee**3*tcHB)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':3})

GC_386 = Coupling(name = 'GC_386',
                  value = '-(ee**3*complex(0,1)*tcHB)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':3})

GC_387 = Coupling(name = 'GC_387',
                  value = '(ee**3*complex(0,1)*tcHB)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':3})

GC_388 = Coupling(name = 'GC_388',
                  value = '-(ee**3*complex(0,1)*tcHB)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_389 = Coupling(name = 'GC_389',
                  value = '(ee**3*complex(0,1)*tcHB)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_390 = Coupling(name = 'GC_390',
                  value = '-(cw*ee**3*tcHB)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_391 = Coupling(name = 'GC_391',
                  value = '-(cw*ee**3*complex(0,1)*tcHB)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_392 = Coupling(name = 'GC_392',
                  value = '(cw*ee**3*complex(0,1)*tcHB)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_393 = Coupling(name = 'GC_393',
                  value = '-(ee**2*tcHB)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_394 = Coupling(name = 'GC_394',
                  value = '(ee**2*complex(0,1)*tcHB)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_395 = Coupling(name = 'GC_395',
                  value = '(ee**2*tcHB)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_396 = Coupling(name = 'GC_396',
                  value = '-(ee**3*complex(0,1)*tcHB)/(2.*cw*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_397 = Coupling(name = 'GC_397',
                  value = '(ee**3*complex(0,1)*tcHB)/(2.*cw*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_398 = Coupling(name = 'GC_398',
                  value = '-(ee**2*tcHW)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_399 = Coupling(name = 'GC_399',
                  value = '-(ee**2*complex(0,1)*tcHW)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_400 = Coupling(name = 'GC_400',
                  value = '(ee**2*tcHW)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_401 = Coupling(name = 'GC_401',
                  value = '-(ee**3*complex(0,1)*tcHW)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':3})

GC_402 = Coupling(name = 'GC_402',
                  value = '(ee**3*complex(0,1)*tcHW)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':3})

GC_403 = Coupling(name = 'GC_403',
                  value = '(ee**3*tcHW)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':3})

GC_404 = Coupling(name = 'GC_404',
                  value = '(cw*ee**3*complex(0,1)*tcHW)/(2.*MW**2*sw**3)',
                  order = {'NP':1,'QED':3})

GC_405 = Coupling(name = 'GC_405',
                  value = '-(ee**2*complex(0,1)*tcHW)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_406 = Coupling(name = 'GC_406',
                  value = '(ee**2*complex(0,1)*tcHW)/(MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_407 = Coupling(name = 'GC_407',
                  value = '(ee**2*tcHW)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_408 = Coupling(name = 'GC_408',
                  value = '-(cw*ee**2*tcHW)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_409 = Coupling(name = 'GC_409',
                  value = '(cw*ee**2*complex(0,1)*tcHW)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_410 = Coupling(name = 'GC_410',
                  value = '(cw*ee**2*tcHW)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_411 = Coupling(name = 'GC_411',
                  value = '(ee**3*complex(0,1)*tcHW)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_412 = Coupling(name = 'GC_412',
                  value = '-(cw*ee**3*complex(0,1)*tcHW)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_413 = Coupling(name = 'GC_413',
                  value = '(cw*ee**3*complex(0,1)*tcHW)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_414 = Coupling(name = 'GC_414',
                  value = '(cw*ee**3*tcHW)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':3})

GC_415 = Coupling(name = 'GC_415',
                  value = '-((ee*tcHW)/(MW**2*sw))',
                  order = {'NP':1,'QED':1})

GC_416 = Coupling(name = 'GC_416',
                  value = '-(ee**2*tcHW)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_417 = Coupling(name = 'GC_417',
                  value = '-(ee**2*complex(0,1)*tcHW)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_418 = Coupling(name = 'GC_418',
                  value = '(ee**2*tcHW)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_419 = Coupling(name = 'GC_419',
                  value = '-(ee**3*complex(0,1)*tcHW)/(2.*cw*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_420 = Coupling(name = 'GC_420',
                  value = '(ee**3*complex(0,1)*tcHW)/(2.*cw*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_421 = Coupling(name = 'GC_421',
                  value = '(ee*tcHB)/MW**2 - (ee*tcHW)/MW**2',
                  order = {'NP':1,'QED':1})

GC_422 = Coupling(name = 'GC_422',
                  value = '-((ee*complex(0,1)*tcHB)/MW**2) - (ee*complex(0,1)*tcHW)/MW**2',
                  order = {'NP':1,'QED':1})

GC_423 = Coupling(name = 'GC_423',
                  value = '-((ee**2*complex(0,1)*tcHB)/MW**2) - (ee**2*complex(0,1)*tcHW)/MW**2',
                  order = {'NP':1,'QED':2})

GC_424 = Coupling(name = 'GC_424',
                  value = '-(ee**2*complex(0,1)*tcHB)/(2.*MW**2) - (ee**2*complex(0,1)*sw**2*tcHB)/(2.*cw**2*MW**2) - (ee**2*complex(0,1)*tcHW)/(2.*MW**2) - (cw**2*ee**2*complex(0,1)*tcHW)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_425 = Coupling(name = 'GC_425',
                  value = '(ee**2*complex(0,1)*tcHB)/(2.*MW**2) - (ee**2*complex(0,1)*sw**2*tcHB)/(2.*cw**2*MW**2) + (ee**2*complex(0,1)*tcHW)/(2.*MW**2) - (cw**2*ee**2*complex(0,1)*tcHW)/(2.*MW**2*sw**2)',
                  order = {'NP':1,'QED':2})

GC_426 = Coupling(name = 'GC_426',
                  value = '(ee*complex(0,1)*sw*tcHB)/(cw*MW**2) - (cw*ee*complex(0,1)*tcHW)/(MW**2*sw)',
                  order = {'NP':1,'QED':1})

GC_427 = Coupling(name = 'GC_427',
                  value = '-((ee**2*complex(0,1)*sw*tcHB)/(cw*MW**2)) + (cw*ee**2*complex(0,1)*tcHW)/(MW**2*sw)',
                  order = {'NP':1,'QED':2})

GC_428 = Coupling(name = 'GC_428',
                  value = '-(ee**3*tcHB)/(2.*MW**2*sw) - (ee**3*tcHW)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_429 = Coupling(name = 'GC_429',
                  value = '-(ee**3*complex(0,1)*tcHB)/(2.*MW**2*sw) - (ee**3*complex(0,1)*tcHW)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_430 = Coupling(name = 'GC_430',
                  value = '(ee**3*complex(0,1)*tcHB)/(2.*MW**2*sw) + (ee**3*complex(0,1)*tcHW)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_431 = Coupling(name = 'GC_431',
                  value = '(ee**3*tcHB)/(2.*MW**2*sw) + (ee**3*tcHW)/(2.*MW**2*sw)',
                  order = {'NP':1,'QED':3})

GC_432 = Coupling(name = 'GC_432',
                  value = '(cw*ee**2*complex(0,1)*tcHB)/(2.*MW**2*sw) + (ee**2*complex(0,1)*sw*tcHB)/(2.*cw*MW**2) - (cw*ee**2*complex(0,1)*tcHW)/(2.*MW**2*sw) - (ee**2*complex(0,1)*sw*tcHW)/(2.*cw*MW**2)',
                  order = {'NP':1,'QED':2})

GC_433 = Coupling(name = 'GC_433',
                  value = '(-1755*c6**2*cH**5*complex(0,1)*MH**2)/(128.*vev**4) + (495*c6*cH**6*complex(0,1)*MH**2)/(64.*vev**4)',
                  order = {'NP':7,'QED':4})

GC_434 = Coupling(name = 'GC_434',
                  value = '(585*c6**2*cH**6*complex(0,1)*MH**2)/(512.*vev**4) - (45*c6*cH**7*complex(0,1)*MH**2)/(64.*vev**4)',
                  order = {'NP':8,'QED':4})

GC_435 = Coupling(name = 'GC_435',
                  value = '(-585*c6**2*cH**5*complex(0,1)*MH**2)/(256.*vev**3) + (45*c6*cH**6*complex(0,1)*MH**2)/(32.*vev**3)',
                  order = {'NP':7,'QED':3})

GC_436 = Coupling(name = 'GC_436',
                  value = '(cHL*DEL1x1)/vev**2 - (cpHL*DEL1x1)/vev**2',
                  order = {'NP':1,'QED':2})

GC_437 = Coupling(name = 'GC_437',
                  value = '-((cHL*DEL1x1*complex(0,1))/vev**2) - (cpHL*DEL1x1*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_438 = Coupling(name = 'GC_438',
                  value = '-((cHL*DEL1x1*complex(0,1))/vev**2) + (cpHL*DEL1x1*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_439 = Coupling(name = 'GC_439',
                  value = '(cHL*DEL1x1)/vev**2 + (cpHL*DEL1x1)/vev**2',
                  order = {'NP':1,'QED':2})

GC_440 = Coupling(name = 'GC_440',
                  value = '(cHQ*DEL1x1)/vev**2 - (cpHQ*DEL1x1)/vev**2',
                  order = {'NP':1,'QED':2})

GC_441 = Coupling(name = 'GC_441',
                  value = '-((cHQ*DEL1x1*complex(0,1))/vev**2) - (cpHQ*DEL1x1*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_442 = Coupling(name = 'GC_442',
                  value = '(cHL*DEL1x2)/vev**2 - (cpHL*DEL1x2)/vev**2',
                  order = {'NP':1,'QED':2})

GC_443 = Coupling(name = 'GC_443',
                  value = '-((cHL*DEL1x2*complex(0,1))/vev**2) - (cpHL*DEL1x2*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_444 = Coupling(name = 'GC_444',
                  value = '-((cHL*DEL1x2*complex(0,1))/vev**2) + (cpHL*DEL1x2*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_445 = Coupling(name = 'GC_445',
                  value = '(cHL*DEL1x2)/vev**2 + (cpHL*DEL1x2)/vev**2',
                  order = {'NP':1,'QED':2})

GC_446 = Coupling(name = 'GC_446',
                  value = '(cHQ*DEL1x2)/vev**2 - (cpHQ*DEL1x2)/vev**2',
                  order = {'NP':1,'QED':2})

GC_447 = Coupling(name = 'GC_447',
                  value = '-((cHQ*DEL1x2*complex(0,1))/vev**2) - (cpHQ*DEL1x2*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_448 = Coupling(name = 'GC_448',
                  value = '(cHL*DEL1x3)/vev**2 - (cpHL*DEL1x3)/vev**2',
                  order = {'NP':1,'QED':2})

GC_449 = Coupling(name = 'GC_449',
                  value = '-((cHL*DEL1x3*complex(0,1))/vev**2) - (cpHL*DEL1x3*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_450 = Coupling(name = 'GC_450',
                  value = '-((cHL*DEL1x3*complex(0,1))/vev**2) + (cpHL*DEL1x3*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_451 = Coupling(name = 'GC_451',
                  value = '(cHL*DEL1x3)/vev**2 + (cpHL*DEL1x3)/vev**2',
                  order = {'NP':1,'QED':2})

GC_452 = Coupling(name = 'GC_452',
                  value = '(cHQ*DEL1x3)/vev**2 - (cpHQ*DEL1x3)/vev**2',
                  order = {'NP':1,'QED':2})

GC_453 = Coupling(name = 'GC_453',
                  value = '-((cHQ*DEL1x3*complex(0,1))/vev**2) - (cpHQ*DEL1x3*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_454 = Coupling(name = 'GC_454',
                  value = '(cHL*DEL2x1)/vev**2 - (cpHL*DEL2x1)/vev**2',
                  order = {'NP':1,'QED':2})

GC_455 = Coupling(name = 'GC_455',
                  value = '-((cHL*DEL2x1*complex(0,1))/vev**2) - (cpHL*DEL2x1*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_456 = Coupling(name = 'GC_456',
                  value = '-((cHL*DEL2x1*complex(0,1))/vev**2) + (cpHL*DEL2x1*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_457 = Coupling(name = 'GC_457',
                  value = '(cHL*DEL2x1)/vev**2 + (cpHL*DEL2x1)/vev**2',
                  order = {'NP':1,'QED':2})

GC_458 = Coupling(name = 'GC_458',
                  value = '(cHQ*DEL2x1)/vev**2 - (cpHQ*DEL2x1)/vev**2',
                  order = {'NP':1,'QED':2})

GC_459 = Coupling(name = 'GC_459',
                  value = '-((cHQ*DEL2x1*complex(0,1))/vev**2) - (cpHQ*DEL2x1*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_460 = Coupling(name = 'GC_460',
                  value = '(cHL*DEL2x2)/vev**2 - (cpHL*DEL2x2)/vev**2',
                  order = {'NP':1,'QED':2})

GC_461 = Coupling(name = 'GC_461',
                  value = '-((cHL*DEL2x2*complex(0,1))/vev**2) - (cpHL*DEL2x2*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_462 = Coupling(name = 'GC_462',
                  value = '-((cHL*DEL2x2*complex(0,1))/vev**2) + (cpHL*DEL2x2*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_463 = Coupling(name = 'GC_463',
                  value = '(cHL*DEL2x2)/vev**2 + (cpHL*DEL2x2)/vev**2',
                  order = {'NP':1,'QED':2})

GC_464 = Coupling(name = 'GC_464',
                  value = '(cHQ*DEL2x2)/vev**2 - (cpHQ*DEL2x2)/vev**2',
                  order = {'NP':1,'QED':2})

GC_465 = Coupling(name = 'GC_465',
                  value = '-((cHQ*DEL2x2*complex(0,1))/vev**2) - (cpHQ*DEL2x2*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_466 = Coupling(name = 'GC_466',
                  value = '(cHL*DEL2x3)/vev**2 - (cpHL*DEL2x3)/vev**2',
                  order = {'NP':1,'QED':2})

GC_467 = Coupling(name = 'GC_467',
                  value = '-((cHL*DEL2x3*complex(0,1))/vev**2) - (cpHL*DEL2x3*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_468 = Coupling(name = 'GC_468',
                  value = '-((cHL*DEL2x3*complex(0,1))/vev**2) + (cpHL*DEL2x3*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_469 = Coupling(name = 'GC_469',
                  value = '(cHL*DEL2x3)/vev**2 + (cpHL*DEL2x3)/vev**2',
                  order = {'NP':1,'QED':2})

GC_470 = Coupling(name = 'GC_470',
                  value = '(cHQ*DEL2x3)/vev**2 - (cpHQ*DEL2x3)/vev**2',
                  order = {'NP':1,'QED':2})

GC_471 = Coupling(name = 'GC_471',
                  value = '-((cHQ*DEL2x3*complex(0,1))/vev**2) - (cpHQ*DEL2x3*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_472 = Coupling(name = 'GC_472',
                  value = '(cHL*DEL3x1)/vev**2 - (cpHL*DEL3x1)/vev**2',
                  order = {'NP':1,'QED':2})

GC_473 = Coupling(name = 'GC_473',
                  value = '-((cHL*DEL3x1*complex(0,1))/vev**2) - (cpHL*DEL3x1*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_474 = Coupling(name = 'GC_474',
                  value = '-((cHL*DEL3x1*complex(0,1))/vev**2) + (cpHL*DEL3x1*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_475 = Coupling(name = 'GC_475',
                  value = '(cHL*DEL3x1)/vev**2 + (cpHL*DEL3x1)/vev**2',
                  order = {'NP':1,'QED':2})

GC_476 = Coupling(name = 'GC_476',
                  value = '(cHQ*DEL3x1)/vev**2 - (cpHQ*DEL3x1)/vev**2',
                  order = {'NP':1,'QED':2})

GC_477 = Coupling(name = 'GC_477',
                  value = '-((cHQ*DEL3x1*complex(0,1))/vev**2) - (cpHQ*DEL3x1*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_478 = Coupling(name = 'GC_478',
                  value = '(cHL*DEL3x2)/vev**2 - (cpHL*DEL3x2)/vev**2',
                  order = {'NP':1,'QED':2})

GC_479 = Coupling(name = 'GC_479',
                  value = '-((cHL*DEL3x2*complex(0,1))/vev**2) - (cpHL*DEL3x2*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_480 = Coupling(name = 'GC_480',
                  value = '-((cHL*DEL3x2*complex(0,1))/vev**2) + (cpHL*DEL3x2*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_481 = Coupling(name = 'GC_481',
                  value = '(cHL*DEL3x2)/vev**2 + (cpHL*DEL3x2)/vev**2',
                  order = {'NP':1,'QED':2})

GC_482 = Coupling(name = 'GC_482',
                  value = '(cHQ*DEL3x2)/vev**2 - (cpHQ*DEL3x2)/vev**2',
                  order = {'NP':1,'QED':2})

GC_483 = Coupling(name = 'GC_483',
                  value = '-((cHQ*DEL3x2*complex(0,1))/vev**2) - (cpHQ*DEL3x2*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_484 = Coupling(name = 'GC_484',
                  value = '(cHL*DEL3x3)/vev**2 - (cpHL*DEL3x3)/vev**2',
                  order = {'NP':1,'QED':2})

GC_485 = Coupling(name = 'GC_485',
                  value = '-((cHL*DEL3x3*complex(0,1))/vev**2) - (cpHL*DEL3x3*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_486 = Coupling(name = 'GC_486',
                  value = '-((cHL*DEL3x3*complex(0,1))/vev**2) + (cpHL*DEL3x3*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_487 = Coupling(name = 'GC_487',
                  value = '(cHL*DEL3x3)/vev**2 + (cpHL*DEL3x3)/vev**2',
                  order = {'NP':1,'QED':2})

GC_488 = Coupling(name = 'GC_488',
                  value = '(cHQ*DEL3x3)/vev**2 - (cpHQ*DEL3x3)/vev**2',
                  order = {'NP':1,'QED':2})

GC_489 = Coupling(name = 'GC_489',
                  value = '-((cHQ*DEL3x3*complex(0,1))/vev**2) - (cpHQ*DEL3x3*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_490 = Coupling(name = 'GC_490',
                  value = '(2*cHL*DEL1x1*ee*complex(0,1))/vev**2 - (2*cpHL*DEL1x1*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_491 = Coupling(name = 'GC_491',
                  value = '(2*cHL*DEL1x1*ee*complex(0,1))/vev**2 + (2*cpHL*DEL1x1*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_492 = Coupling(name = 'GC_492',
                  value = '(2*cHQ*DEL1x1*ee*complex(0,1))/vev**2 + (2*cpHQ*DEL1x1*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_493 = Coupling(name = 'GC_493',
                  value = '(2*cHL*DEL1x2*ee*complex(0,1))/vev**2 - (2*cpHL*DEL1x2*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_494 = Coupling(name = 'GC_494',
                  value = '(2*cHL*DEL1x2*ee*complex(0,1))/vev**2 + (2*cpHL*DEL1x2*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_495 = Coupling(name = 'GC_495',
                  value = '(2*cHQ*DEL1x2*ee*complex(0,1))/vev**2 + (2*cpHQ*DEL1x2*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_496 = Coupling(name = 'GC_496',
                  value = '(2*cHL*DEL1x3*ee*complex(0,1))/vev**2 - (2*cpHL*DEL1x3*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_497 = Coupling(name = 'GC_497',
                  value = '(2*cHL*DEL1x3*ee*complex(0,1))/vev**2 + (2*cpHL*DEL1x3*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_498 = Coupling(name = 'GC_498',
                  value = '(2*cHQ*DEL1x3*ee*complex(0,1))/vev**2 + (2*cpHQ*DEL1x3*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_499 = Coupling(name = 'GC_499',
                  value = '(2*cHL*DEL2x1*ee*complex(0,1))/vev**2 - (2*cpHL*DEL2x1*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_500 = Coupling(name = 'GC_500',
                  value = '(2*cHL*DEL2x1*ee*complex(0,1))/vev**2 + (2*cpHL*DEL2x1*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_501 = Coupling(name = 'GC_501',
                  value = '(2*cHQ*DEL2x1*ee*complex(0,1))/vev**2 + (2*cpHQ*DEL2x1*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_502 = Coupling(name = 'GC_502',
                  value = '(2*cHL*DEL2x2*ee*complex(0,1))/vev**2 - (2*cpHL*DEL2x2*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_503 = Coupling(name = 'GC_503',
                  value = '(2*cHL*DEL2x2*ee*complex(0,1))/vev**2 + (2*cpHL*DEL2x2*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_504 = Coupling(name = 'GC_504',
                  value = '(2*cHQ*DEL2x2*ee*complex(0,1))/vev**2 + (2*cpHQ*DEL2x2*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_505 = Coupling(name = 'GC_505',
                  value = '(2*cHL*DEL2x3*ee*complex(0,1))/vev**2 - (2*cpHL*DEL2x3*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_506 = Coupling(name = 'GC_506',
                  value = '(2*cHL*DEL2x3*ee*complex(0,1))/vev**2 + (2*cpHL*DEL2x3*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_507 = Coupling(name = 'GC_507',
                  value = '(2*cHQ*DEL2x3*ee*complex(0,1))/vev**2 + (2*cpHQ*DEL2x3*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_508 = Coupling(name = 'GC_508',
                  value = '(2*cHL*DEL3x1*ee*complex(0,1))/vev**2 - (2*cpHL*DEL3x1*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_509 = Coupling(name = 'GC_509',
                  value = '(2*cHL*DEL3x1*ee*complex(0,1))/vev**2 + (2*cpHL*DEL3x1*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_510 = Coupling(name = 'GC_510',
                  value = '(2*cHQ*DEL3x1*ee*complex(0,1))/vev**2 + (2*cpHQ*DEL3x1*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_511 = Coupling(name = 'GC_511',
                  value = '(2*cHL*DEL3x2*ee*complex(0,1))/vev**2 - (2*cpHL*DEL3x2*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_512 = Coupling(name = 'GC_512',
                  value = '(2*cHL*DEL3x2*ee*complex(0,1))/vev**2 + (2*cpHL*DEL3x2*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_513 = Coupling(name = 'GC_513',
                  value = '(2*cHQ*DEL3x2*ee*complex(0,1))/vev**2 + (2*cpHQ*DEL3x2*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_514 = Coupling(name = 'GC_514',
                  value = '(2*cHL*DEL3x3*ee*complex(0,1))/vev**2 - (2*cpHL*DEL3x3*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_515 = Coupling(name = 'GC_515',
                  value = '(2*cHL*DEL3x3*ee*complex(0,1))/vev**2 + (2*cpHL*DEL3x3*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_516 = Coupling(name = 'GC_516',
                  value = '(2*cHQ*DEL3x3*ee*complex(0,1))/vev**2 + (2*cpHQ*DEL3x3*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_517 = Coupling(name = 'GC_517',
                  value = '-((cHQ*complex(0,1)*I1a11)/vev**2) + (cpHQ*complex(0,1)*I1a11)/vev**2',
                  order = {'NP':1,'QED':2})

GC_518 = Coupling(name = 'GC_518',
                  value = '(cHQ*I1a11)/vev**2 + (cpHQ*I1a11)/vev**2',
                  order = {'NP':1,'QED':2})

GC_519 = Coupling(name = 'GC_519',
                  value = '(2*cHQ*ee*complex(0,1)*I1a11)/vev**2 - (2*cpHQ*ee*complex(0,1)*I1a11)/vev**2',
                  order = {'NP':1,'QED':3})

GC_520 = Coupling(name = 'GC_520',
                  value = '-((cHQ*complex(0,1)*I1a12)/vev**2) + (cpHQ*complex(0,1)*I1a12)/vev**2',
                  order = {'NP':1,'QED':2})

GC_521 = Coupling(name = 'GC_521',
                  value = '(cHQ*I1a12)/vev**2 + (cpHQ*I1a12)/vev**2',
                  order = {'NP':1,'QED':2})

GC_522 = Coupling(name = 'GC_522',
                  value = '(2*cHQ*ee*complex(0,1)*I1a12)/vev**2 - (2*cpHQ*ee*complex(0,1)*I1a12)/vev**2',
                  order = {'NP':1,'QED':3})

GC_523 = Coupling(name = 'GC_523',
                  value = '-((cHQ*complex(0,1)*I1a13)/vev**2) + (cpHQ*complex(0,1)*I1a13)/vev**2',
                  order = {'NP':1,'QED':2})

GC_524 = Coupling(name = 'GC_524',
                  value = '(cHQ*I1a13)/vev**2 + (cpHQ*I1a13)/vev**2',
                  order = {'NP':1,'QED':2})

GC_525 = Coupling(name = 'GC_525',
                  value = '(2*cHQ*ee*complex(0,1)*I1a13)/vev**2 - (2*cpHQ*ee*complex(0,1)*I1a13)/vev**2',
                  order = {'NP':1,'QED':3})

GC_526 = Coupling(name = 'GC_526',
                  value = '-((cHQ*complex(0,1)*I1a21)/vev**2) + (cpHQ*complex(0,1)*I1a21)/vev**2',
                  order = {'NP':1,'QED':2})

GC_527 = Coupling(name = 'GC_527',
                  value = '(cHQ*I1a21)/vev**2 + (cpHQ*I1a21)/vev**2',
                  order = {'NP':1,'QED':2})

GC_528 = Coupling(name = 'GC_528',
                  value = '(2*cHQ*ee*complex(0,1)*I1a21)/vev**2 - (2*cpHQ*ee*complex(0,1)*I1a21)/vev**2',
                  order = {'NP':1,'QED':3})

GC_529 = Coupling(name = 'GC_529',
                  value = '-((cHQ*complex(0,1)*I1a22)/vev**2) + (cpHQ*complex(0,1)*I1a22)/vev**2',
                  order = {'NP':1,'QED':2})

GC_530 = Coupling(name = 'GC_530',
                  value = '(cHQ*I1a22)/vev**2 + (cpHQ*I1a22)/vev**2',
                  order = {'NP':1,'QED':2})

GC_531 = Coupling(name = 'GC_531',
                  value = '(2*cHQ*ee*complex(0,1)*I1a22)/vev**2 - (2*cpHQ*ee*complex(0,1)*I1a22)/vev**2',
                  order = {'NP':1,'QED':3})

GC_532 = Coupling(name = 'GC_532',
                  value = '-((cHQ*complex(0,1)*I1a23)/vev**2) + (cpHQ*complex(0,1)*I1a23)/vev**2',
                  order = {'NP':1,'QED':2})

GC_533 = Coupling(name = 'GC_533',
                  value = '(cHQ*I1a23)/vev**2 + (cpHQ*I1a23)/vev**2',
                  order = {'NP':1,'QED':2})

GC_534 = Coupling(name = 'GC_534',
                  value = '(2*cHQ*ee*complex(0,1)*I1a23)/vev**2 - (2*cpHQ*ee*complex(0,1)*I1a23)/vev**2',
                  order = {'NP':1,'QED':3})

GC_535 = Coupling(name = 'GC_535',
                  value = '-((cHQ*complex(0,1)*I1a31)/vev**2) + (cpHQ*complex(0,1)*I1a31)/vev**2',
                  order = {'NP':1,'QED':2})

GC_536 = Coupling(name = 'GC_536',
                  value = '(cHQ*I1a31)/vev**2 + (cpHQ*I1a31)/vev**2',
                  order = {'NP':1,'QED':2})

GC_537 = Coupling(name = 'GC_537',
                  value = '(2*cHQ*ee*complex(0,1)*I1a31)/vev**2 - (2*cpHQ*ee*complex(0,1)*I1a31)/vev**2',
                  order = {'NP':1,'QED':3})

GC_538 = Coupling(name = 'GC_538',
                  value = '-((cHQ*complex(0,1)*I1a32)/vev**2) + (cpHQ*complex(0,1)*I1a32)/vev**2',
                  order = {'NP':1,'QED':2})

GC_539 = Coupling(name = 'GC_539',
                  value = '(cHQ*I1a32)/vev**2 + (cpHQ*I1a32)/vev**2',
                  order = {'NP':1,'QED':2})

GC_540 = Coupling(name = 'GC_540',
                  value = '(2*cHQ*ee*complex(0,1)*I1a32)/vev**2 - (2*cpHQ*ee*complex(0,1)*I1a32)/vev**2',
                  order = {'NP':1,'QED':3})

GC_541 = Coupling(name = 'GC_541',
                  value = '-((cHQ*complex(0,1)*I1a33)/vev**2) + (cpHQ*complex(0,1)*I1a33)/vev**2',
                  order = {'NP':1,'QED':2})

GC_542 = Coupling(name = 'GC_542',
                  value = '(cHQ*I1a33)/vev**2 + (cpHQ*I1a33)/vev**2',
                  order = {'NP':1,'QED':2})

GC_543 = Coupling(name = 'GC_543',
                  value = '(2*cHQ*ee*complex(0,1)*I1a33)/vev**2 - (2*cpHQ*ee*complex(0,1)*I1a33)/vev**2',
                  order = {'NP':1,'QED':3})

GC_544 = Coupling(name = 'GC_544',
                  value = '(c6*complex(0,1)*MH**2)/(8.*vev**2) - (cH*complex(0,1)*MH**2)/vev**2',
                  order = {'NP':1,'QED':2})

GC_545 = Coupling(name = 'GC_545',
                  value = '(c6*complex(0,1)*MH**2)/(4.*vev**2) - (2*cH*complex(0,1)*MH**2)/vev**2',
                  order = {'NP':1,'QED':2})

GC_546 = Coupling(name = 'GC_546',
                  value = '(3*c6*complex(0,1)*MH**2)/(8.*vev**2) - (3*cH*complex(0,1)*MH**2)/vev**2',
                  order = {'NP':1,'QED':2})

GC_547 = Coupling(name = 'GC_547',
                  value = '(-141*c6*complex(0,1)*MH**2)/(8.*vev**2) + (3*cH*complex(0,1)*MH**2)/vev**2',
                  order = {'NP':1,'QED':2})

GC_548 = Coupling(name = 'GC_548',
                  value = '(-3*cT*ee**2)/(cw*vev**2) - (3*cT*cw*ee**2)/(sw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_549 = Coupling(name = 'GC_549',
                  value = '(2*cT*ee**2)/(cw*vev**2) - (2*cT*cw*ee**2)/(sw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_550 = Coupling(name = 'GC_550',
                  value = '-((cT*ee**2)/(cw*vev**2)) - (cT*cw*ee**2)/(sw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_551 = Coupling(name = 'GC_551',
                  value = '-((cT*ee**2*complex(0,1))/(cw*vev**2)) - (cT*cw*ee**2*complex(0,1))/(sw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_552 = Coupling(name = 'GC_552',
                  value = '(-2*cT*ee**2*complex(0,1))/(cw*vev**2) + (2*cT*cw*ee**2*complex(0,1))/(sw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_553 = Coupling(name = 'GC_553',
                  value = '(-3*cT*ee**2*complex(0,1))/(cw*vev**2) - (3*cT*cw*ee**2*complex(0,1))/(sw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_554 = Coupling(name = 'GC_554',
                  value = '(cT*ee**2)/(cw*vev**2) + (cT*cw*ee**2)/(sw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_555 = Coupling(name = 'GC_555',
                  value = '(-2*cT*ee**2)/(cw*vev**2) + (2*cT*cw*ee**2)/(sw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_556 = Coupling(name = 'GC_556',
                  value = '(3*cT*ee**2)/(cw*vev**2) + (3*cT*cw*ee**2)/(sw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_557 = Coupling(name = 'GC_557',
                  value = '-((cT*cw*ee*complex(0,1))/(sw*vev**2)) - (cT*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_558 = Coupling(name = 'GC_558',
                  value = '(2*cT*cw*ee*complex(0,1))/(sw*vev**2) - (2*cT*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_559 = Coupling(name = 'GC_559',
                  value = '-((cT*cw*ee)/(sw*vev**2)) + (cT*ee*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_560 = Coupling(name = 'GC_560',
                  value = '(cT*cw*ee)/(sw*vev**2) + (cT*ee*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_561 = Coupling(name = 'GC_561',
                  value = '(3*cT*cw*ee)/(sw*vev**2) + (3*cT*ee*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_562 = Coupling(name = 'GC_562',
                  value = '-(cHe*cw*DEL1x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL1x1*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_563 = Coupling(name = 'GC_563',
                  value = '(cHe*cw*DEL1x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL1x1*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_564 = Coupling(name = 'GC_564',
                  value = '-((cHL*cw*DEL1x1*ee*complex(0,1))/(sw*vev**2)) - (cpHL*cw*DEL1x1*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL1x1*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL1x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_565 = Coupling(name = 'GC_565',
                  value = '(cHL*cw*DEL1x1*ee*complex(0,1))/(sw*vev**2) + (cpHL*cw*DEL1x1*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL1x1*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL1x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_566 = Coupling(name = 'GC_566',
                  value = '(cHL*cw*DEL1x1*ee*complex(0,1))/(sw*vev**2) - (cpHL*cw*DEL1x1*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL1x1*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL1x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_567 = Coupling(name = 'GC_567',
                  value = '-((cHL*cw*DEL1x1*ee*complex(0,1))/(sw*vev**2)) + (cpHL*cw*DEL1x1*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL1x1*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL1x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_568 = Coupling(name = 'GC_568',
                  value = '(cHQ*cw*DEL1x1*ee*complex(0,1))/(sw*vev**2) + (cpHQ*cw*DEL1x1*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL1x1*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHQ*DEL1x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_569 = Coupling(name = 'GC_569',
                  value = '-((cHQ*cw*DEL1x1*ee*complex(0,1))/(sw*vev**2)) + (cpHQ*cw*DEL1x1*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL1x1*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHQ*DEL1x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_570 = Coupling(name = 'GC_570',
                  value = '-(cHe*cw*DEL1x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL1x2*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_571 = Coupling(name = 'GC_571',
                  value = '(cHe*cw*DEL1x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL1x2*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_572 = Coupling(name = 'GC_572',
                  value = '-((cHL*cw*DEL1x2*ee*complex(0,1))/(sw*vev**2)) - (cpHL*cw*DEL1x2*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL1x2*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL1x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_573 = Coupling(name = 'GC_573',
                  value = '(cHL*cw*DEL1x2*ee*complex(0,1))/(sw*vev**2) + (cpHL*cw*DEL1x2*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL1x2*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL1x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_574 = Coupling(name = 'GC_574',
                  value = '(cHL*cw*DEL1x2*ee*complex(0,1))/(sw*vev**2) - (cpHL*cw*DEL1x2*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL1x2*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL1x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_575 = Coupling(name = 'GC_575',
                  value = '-((cHL*cw*DEL1x2*ee*complex(0,1))/(sw*vev**2)) + (cpHL*cw*DEL1x2*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL1x2*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL1x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_576 = Coupling(name = 'GC_576',
                  value = '(cHQ*cw*DEL1x2*ee*complex(0,1))/(sw*vev**2) + (cpHQ*cw*DEL1x2*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL1x2*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHQ*DEL1x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_577 = Coupling(name = 'GC_577',
                  value = '-((cHQ*cw*DEL1x2*ee*complex(0,1))/(sw*vev**2)) + (cpHQ*cw*DEL1x2*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL1x2*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHQ*DEL1x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_578 = Coupling(name = 'GC_578',
                  value = '-(cHe*cw*DEL1x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL1x3*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_579 = Coupling(name = 'GC_579',
                  value = '(cHe*cw*DEL1x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL1x3*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_580 = Coupling(name = 'GC_580',
                  value = '-((cHL*cw*DEL1x3*ee*complex(0,1))/(sw*vev**2)) - (cpHL*cw*DEL1x3*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL1x3*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL1x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_581 = Coupling(name = 'GC_581',
                  value = '(cHL*cw*DEL1x3*ee*complex(0,1))/(sw*vev**2) + (cpHL*cw*DEL1x3*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL1x3*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL1x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_582 = Coupling(name = 'GC_582',
                  value = '(cHL*cw*DEL1x3*ee*complex(0,1))/(sw*vev**2) - (cpHL*cw*DEL1x3*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL1x3*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL1x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_583 = Coupling(name = 'GC_583',
                  value = '-((cHL*cw*DEL1x3*ee*complex(0,1))/(sw*vev**2)) + (cpHL*cw*DEL1x3*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL1x3*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL1x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_584 = Coupling(name = 'GC_584',
                  value = '(cHQ*cw*DEL1x3*ee*complex(0,1))/(sw*vev**2) + (cpHQ*cw*DEL1x3*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL1x3*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHQ*DEL1x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_585 = Coupling(name = 'GC_585',
                  value = '-((cHQ*cw*DEL1x3*ee*complex(0,1))/(sw*vev**2)) + (cpHQ*cw*DEL1x3*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL1x3*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHQ*DEL1x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_586 = Coupling(name = 'GC_586',
                  value = '-(cHe*cw*DEL2x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL2x1*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_587 = Coupling(name = 'GC_587',
                  value = '(cHe*cw*DEL2x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL2x1*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_588 = Coupling(name = 'GC_588',
                  value = '-((cHL*cw*DEL2x1*ee*complex(0,1))/(sw*vev**2)) - (cpHL*cw*DEL2x1*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL2x1*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL2x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_589 = Coupling(name = 'GC_589',
                  value = '(cHL*cw*DEL2x1*ee*complex(0,1))/(sw*vev**2) + (cpHL*cw*DEL2x1*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL2x1*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL2x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_590 = Coupling(name = 'GC_590',
                  value = '(cHL*cw*DEL2x1*ee*complex(0,1))/(sw*vev**2) - (cpHL*cw*DEL2x1*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL2x1*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL2x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_591 = Coupling(name = 'GC_591',
                  value = '-((cHL*cw*DEL2x1*ee*complex(0,1))/(sw*vev**2)) + (cpHL*cw*DEL2x1*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL2x1*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL2x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_592 = Coupling(name = 'GC_592',
                  value = '(cHQ*cw*DEL2x1*ee*complex(0,1))/(sw*vev**2) + (cpHQ*cw*DEL2x1*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL2x1*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHQ*DEL2x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_593 = Coupling(name = 'GC_593',
                  value = '-((cHQ*cw*DEL2x1*ee*complex(0,1))/(sw*vev**2)) + (cpHQ*cw*DEL2x1*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL2x1*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHQ*DEL2x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_594 = Coupling(name = 'GC_594',
                  value = '-(cHe*cw*DEL2x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL2x2*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_595 = Coupling(name = 'GC_595',
                  value = '(cHe*cw*DEL2x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL2x2*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_596 = Coupling(name = 'GC_596',
                  value = '-((cHL*cw*DEL2x2*ee*complex(0,1))/(sw*vev**2)) - (cpHL*cw*DEL2x2*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL2x2*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL2x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_597 = Coupling(name = 'GC_597',
                  value = '(cHL*cw*DEL2x2*ee*complex(0,1))/(sw*vev**2) + (cpHL*cw*DEL2x2*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL2x2*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL2x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_598 = Coupling(name = 'GC_598',
                  value = '(cHL*cw*DEL2x2*ee*complex(0,1))/(sw*vev**2) - (cpHL*cw*DEL2x2*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL2x2*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL2x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_599 = Coupling(name = 'GC_599',
                  value = '-((cHL*cw*DEL2x2*ee*complex(0,1))/(sw*vev**2)) + (cpHL*cw*DEL2x2*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL2x2*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL2x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_600 = Coupling(name = 'GC_600',
                  value = '(cHQ*cw*DEL2x2*ee*complex(0,1))/(sw*vev**2) + (cpHQ*cw*DEL2x2*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL2x2*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHQ*DEL2x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_601 = Coupling(name = 'GC_601',
                  value = '-((cHQ*cw*DEL2x2*ee*complex(0,1))/(sw*vev**2)) + (cpHQ*cw*DEL2x2*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL2x2*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHQ*DEL2x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_602 = Coupling(name = 'GC_602',
                  value = '-(cHe*cw*DEL2x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL2x3*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_603 = Coupling(name = 'GC_603',
                  value = '(cHe*cw*DEL2x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL2x3*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_604 = Coupling(name = 'GC_604',
                  value = '-((cHL*cw*DEL2x3*ee*complex(0,1))/(sw*vev**2)) - (cpHL*cw*DEL2x3*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL2x3*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL2x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_605 = Coupling(name = 'GC_605',
                  value = '(cHL*cw*DEL2x3*ee*complex(0,1))/(sw*vev**2) + (cpHL*cw*DEL2x3*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL2x3*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL2x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_606 = Coupling(name = 'GC_606',
                  value = '(cHL*cw*DEL2x3*ee*complex(0,1))/(sw*vev**2) - (cpHL*cw*DEL2x3*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL2x3*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL2x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_607 = Coupling(name = 'GC_607',
                  value = '-((cHL*cw*DEL2x3*ee*complex(0,1))/(sw*vev**2)) + (cpHL*cw*DEL2x3*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL2x3*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL2x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_608 = Coupling(name = 'GC_608',
                  value = '(cHQ*cw*DEL2x3*ee*complex(0,1))/(sw*vev**2) + (cpHQ*cw*DEL2x3*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL2x3*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHQ*DEL2x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_609 = Coupling(name = 'GC_609',
                  value = '-((cHQ*cw*DEL2x3*ee*complex(0,1))/(sw*vev**2)) + (cpHQ*cw*DEL2x3*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL2x3*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHQ*DEL2x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_610 = Coupling(name = 'GC_610',
                  value = '-(cHe*cw*DEL3x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL3x1*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_611 = Coupling(name = 'GC_611',
                  value = '(cHe*cw*DEL3x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL3x1*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_612 = Coupling(name = 'GC_612',
                  value = '-((cHL*cw*DEL3x1*ee*complex(0,1))/(sw*vev**2)) - (cpHL*cw*DEL3x1*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL3x1*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL3x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_613 = Coupling(name = 'GC_613',
                  value = '(cHL*cw*DEL3x1*ee*complex(0,1))/(sw*vev**2) + (cpHL*cw*DEL3x1*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL3x1*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL3x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_614 = Coupling(name = 'GC_614',
                  value = '(cHL*cw*DEL3x1*ee*complex(0,1))/(sw*vev**2) - (cpHL*cw*DEL3x1*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL3x1*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL3x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_615 = Coupling(name = 'GC_615',
                  value = '-((cHL*cw*DEL3x1*ee*complex(0,1))/(sw*vev**2)) + (cpHL*cw*DEL3x1*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL3x1*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL3x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_616 = Coupling(name = 'GC_616',
                  value = '(cHQ*cw*DEL3x1*ee*complex(0,1))/(sw*vev**2) + (cpHQ*cw*DEL3x1*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL3x1*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHQ*DEL3x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_617 = Coupling(name = 'GC_617',
                  value = '-((cHQ*cw*DEL3x1*ee*complex(0,1))/(sw*vev**2)) + (cpHQ*cw*DEL3x1*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL3x1*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHQ*DEL3x1*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_618 = Coupling(name = 'GC_618',
                  value = '-(cHe*cw*DEL3x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL3x2*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_619 = Coupling(name = 'GC_619',
                  value = '(cHe*cw*DEL3x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL3x2*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_620 = Coupling(name = 'GC_620',
                  value = '-((cHL*cw*DEL3x2*ee*complex(0,1))/(sw*vev**2)) - (cpHL*cw*DEL3x2*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL3x2*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL3x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_621 = Coupling(name = 'GC_621',
                  value = '(cHL*cw*DEL3x2*ee*complex(0,1))/(sw*vev**2) + (cpHL*cw*DEL3x2*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL3x2*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL3x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_622 = Coupling(name = 'GC_622',
                  value = '(cHL*cw*DEL3x2*ee*complex(0,1))/(sw*vev**2) - (cpHL*cw*DEL3x2*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL3x2*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL3x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_623 = Coupling(name = 'GC_623',
                  value = '-((cHL*cw*DEL3x2*ee*complex(0,1))/(sw*vev**2)) + (cpHL*cw*DEL3x2*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL3x2*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL3x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_624 = Coupling(name = 'GC_624',
                  value = '(cHQ*cw*DEL3x2*ee*complex(0,1))/(sw*vev**2) + (cpHQ*cw*DEL3x2*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL3x2*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHQ*DEL3x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_625 = Coupling(name = 'GC_625',
                  value = '-((cHQ*cw*DEL3x2*ee*complex(0,1))/(sw*vev**2)) + (cpHQ*cw*DEL3x2*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL3x2*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHQ*DEL3x2*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_626 = Coupling(name = 'GC_626',
                  value = '-(cHe*cw*DEL3x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL3x3*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_627 = Coupling(name = 'GC_627',
                  value = '(cHe*cw*DEL3x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHe*DEL3x3*ee*complex(0,1)*sw)/(2.*cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_628 = Coupling(name = 'GC_628',
                  value = '-((cHL*cw*DEL3x3*ee*complex(0,1))/(sw*vev**2)) - (cpHL*cw*DEL3x3*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL3x3*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL3x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_629 = Coupling(name = 'GC_629',
                  value = '(cHL*cw*DEL3x3*ee*complex(0,1))/(sw*vev**2) + (cpHL*cw*DEL3x3*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL3x3*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHL*DEL3x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_630 = Coupling(name = 'GC_630',
                  value = '(cHL*cw*DEL3x3*ee*complex(0,1))/(sw*vev**2) - (cpHL*cw*DEL3x3*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL3x3*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL3x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_631 = Coupling(name = 'GC_631',
                  value = '-((cHL*cw*DEL3x3*ee*complex(0,1))/(sw*vev**2)) + (cpHL*cw*DEL3x3*ee*complex(0,1))/(sw*vev**2) - (cHL*DEL3x3*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHL*DEL3x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_632 = Coupling(name = 'GC_632',
                  value = '(cHQ*cw*DEL3x3*ee*complex(0,1))/(sw*vev**2) + (cpHQ*cw*DEL3x3*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL3x3*ee*complex(0,1)*sw)/(cw*vev**2) - (cpHQ*DEL3x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_633 = Coupling(name = 'GC_633',
                  value = '-((cHQ*cw*DEL3x3*ee*complex(0,1))/(sw*vev**2)) + (cpHQ*cw*DEL3x3*ee*complex(0,1))/(sw*vev**2) - (cHQ*DEL3x3*ee*complex(0,1)*sw)/(cw*vev**2) + (cpHQ*DEL3x3*ee*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_634 = Coupling(name = 'GC_634',
                  value = '(2*cT*cw*ee**2*complex(0,1))/(sw*vev**2) + (2*cT*ee**2*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':4})

GC_635 = Coupling(name = 'GC_635',
                  value = '(-8*cT*cw*ee**2*complex(0,1))/(sw*vev**2) + (8*cT*ee**2*complex(0,1)*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':4})

GC_636 = Coupling(name = 'GC_636',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a11)/(sw*vev**2)) - (cpHQ*cw*ee*complex(0,1)*I1a11)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a11*sw)/(cw*vev**2) - (cpHQ*ee*complex(0,1)*I1a11*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_637 = Coupling(name = 'GC_637',
                  value = '(cHQ*cw*ee*complex(0,1)*I1a11)/(sw*vev**2) - (cpHQ*cw*ee*complex(0,1)*I1a11)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a11*sw)/(cw*vev**2) + (cpHQ*ee*complex(0,1)*I1a11*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_638 = Coupling(name = 'GC_638',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a12)/(sw*vev**2)) - (cpHQ*cw*ee*complex(0,1)*I1a12)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a12*sw)/(cw*vev**2) - (cpHQ*ee*complex(0,1)*I1a12*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_639 = Coupling(name = 'GC_639',
                  value = '(cHQ*cw*ee*complex(0,1)*I1a12)/(sw*vev**2) - (cpHQ*cw*ee*complex(0,1)*I1a12)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a12*sw)/(cw*vev**2) + (cpHQ*ee*complex(0,1)*I1a12*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_640 = Coupling(name = 'GC_640',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a13)/(sw*vev**2)) - (cpHQ*cw*ee*complex(0,1)*I1a13)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a13*sw)/(cw*vev**2) - (cpHQ*ee*complex(0,1)*I1a13*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_641 = Coupling(name = 'GC_641',
                  value = '(cHQ*cw*ee*complex(0,1)*I1a13)/(sw*vev**2) - (cpHQ*cw*ee*complex(0,1)*I1a13)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a13*sw)/(cw*vev**2) + (cpHQ*ee*complex(0,1)*I1a13*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_642 = Coupling(name = 'GC_642',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a21)/(sw*vev**2)) - (cpHQ*cw*ee*complex(0,1)*I1a21)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a21*sw)/(cw*vev**2) - (cpHQ*ee*complex(0,1)*I1a21*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_643 = Coupling(name = 'GC_643',
                  value = '(cHQ*cw*ee*complex(0,1)*I1a21)/(sw*vev**2) - (cpHQ*cw*ee*complex(0,1)*I1a21)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a21*sw)/(cw*vev**2) + (cpHQ*ee*complex(0,1)*I1a21*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_644 = Coupling(name = 'GC_644',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a22)/(sw*vev**2)) - (cpHQ*cw*ee*complex(0,1)*I1a22)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a22*sw)/(cw*vev**2) - (cpHQ*ee*complex(0,1)*I1a22*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_645 = Coupling(name = 'GC_645',
                  value = '(cHQ*cw*ee*complex(0,1)*I1a22)/(sw*vev**2) - (cpHQ*cw*ee*complex(0,1)*I1a22)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a22*sw)/(cw*vev**2) + (cpHQ*ee*complex(0,1)*I1a22*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_646 = Coupling(name = 'GC_646',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a23)/(sw*vev**2)) - (cpHQ*cw*ee*complex(0,1)*I1a23)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a23*sw)/(cw*vev**2) - (cpHQ*ee*complex(0,1)*I1a23*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_647 = Coupling(name = 'GC_647',
                  value = '(cHQ*cw*ee*complex(0,1)*I1a23)/(sw*vev**2) - (cpHQ*cw*ee*complex(0,1)*I1a23)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a23*sw)/(cw*vev**2) + (cpHQ*ee*complex(0,1)*I1a23*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_648 = Coupling(name = 'GC_648',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a31)/(sw*vev**2)) - (cpHQ*cw*ee*complex(0,1)*I1a31)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a31*sw)/(cw*vev**2) - (cpHQ*ee*complex(0,1)*I1a31*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_649 = Coupling(name = 'GC_649',
                  value = '(cHQ*cw*ee*complex(0,1)*I1a31)/(sw*vev**2) - (cpHQ*cw*ee*complex(0,1)*I1a31)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a31*sw)/(cw*vev**2) + (cpHQ*ee*complex(0,1)*I1a31*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_650 = Coupling(name = 'GC_650',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a32)/(sw*vev**2)) - (cpHQ*cw*ee*complex(0,1)*I1a32)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a32*sw)/(cw*vev**2) - (cpHQ*ee*complex(0,1)*I1a32*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_651 = Coupling(name = 'GC_651',
                  value = '(cHQ*cw*ee*complex(0,1)*I1a32)/(sw*vev**2) - (cpHQ*cw*ee*complex(0,1)*I1a32)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a32*sw)/(cw*vev**2) + (cpHQ*ee*complex(0,1)*I1a32*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_652 = Coupling(name = 'GC_652',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a33)/(sw*vev**2)) - (cpHQ*cw*ee*complex(0,1)*I1a33)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a33*sw)/(cw*vev**2) - (cpHQ*ee*complex(0,1)*I1a33*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_653 = Coupling(name = 'GC_653',
                  value = '(cHQ*cw*ee*complex(0,1)*I1a33)/(sw*vev**2) - (cpHQ*cw*ee*complex(0,1)*I1a33)/(sw*vev**2) - (cHQ*ee*complex(0,1)*I1a33*sw)/(cw*vev**2) + (cpHQ*ee*complex(0,1)*I1a33*sw)/(cw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_654 = Coupling(name = 'GC_654',
                  value = '(-4*cT*ee**2*complex(0,1))/vev**2 - (2*cT*cw**2*ee**2*complex(0,1))/(sw**2*vev**2) - (2*cT*ee**2*complex(0,1)*sw**2)/(cw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_655 = Coupling(name = 'GC_655',
                  value = '(2*cT*cw**2*ee**2*complex(0,1))/(sw**2*vev**2) - (2*cT*ee**2*complex(0,1)*sw**2)/(cw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_656 = Coupling(name = 'GC_656',
                  value = '(8*cT*ee**2*complex(0,1))/vev**2 - (4*cT*cw**2*ee**2*complex(0,1))/(sw**2*vev**2) - (4*cT*ee**2*complex(0,1)*sw**2)/(cw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_657 = Coupling(name = 'GC_657',
                  value = '(-12*cT*ee**2*complex(0,1))/vev**2 - (6*cT*cw**2*ee**2*complex(0,1))/(sw**2*vev**2) - (6*cT*ee**2*complex(0,1)*sw**2)/(cw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_658 = Coupling(name = 'GC_658',
                  value = '(cHL*DEL1x1)/vev - (cpHL*DEL1x1)/vev',
                  order = {'NP':1,'QED':1})

GC_659 = Coupling(name = 'GC_659',
                  value = '(cHL*DEL1x1)/vev + (cpHL*DEL1x1)/vev',
                  order = {'NP':1,'QED':1})

GC_660 = Coupling(name = 'GC_660',
                  value = '(cHQ*DEL1x1)/vev - (cpHQ*DEL1x1)/vev',
                  order = {'NP':1,'QED':1})

GC_661 = Coupling(name = 'GC_661',
                  value = '(cHL*DEL1x2)/vev - (cpHL*DEL1x2)/vev',
                  order = {'NP':1,'QED':1})

GC_662 = Coupling(name = 'GC_662',
                  value = '(cHL*DEL1x2)/vev + (cpHL*DEL1x2)/vev',
                  order = {'NP':1,'QED':1})

GC_663 = Coupling(name = 'GC_663',
                  value = '(cHQ*DEL1x2)/vev - (cpHQ*DEL1x2)/vev',
                  order = {'NP':1,'QED':1})

GC_664 = Coupling(name = 'GC_664',
                  value = '(cHL*DEL1x3)/vev - (cpHL*DEL1x3)/vev',
                  order = {'NP':1,'QED':1})

GC_665 = Coupling(name = 'GC_665',
                  value = '(cHL*DEL1x3)/vev + (cpHL*DEL1x3)/vev',
                  order = {'NP':1,'QED':1})

GC_666 = Coupling(name = 'GC_666',
                  value = '(cHQ*DEL1x3)/vev - (cpHQ*DEL1x3)/vev',
                  order = {'NP':1,'QED':1})

GC_667 = Coupling(name = 'GC_667',
                  value = '(cHL*DEL2x1)/vev - (cpHL*DEL2x1)/vev',
                  order = {'NP':1,'QED':1})

GC_668 = Coupling(name = 'GC_668',
                  value = '(cHL*DEL2x1)/vev + (cpHL*DEL2x1)/vev',
                  order = {'NP':1,'QED':1})

GC_669 = Coupling(name = 'GC_669',
                  value = '(cHQ*DEL2x1)/vev - (cpHQ*DEL2x1)/vev',
                  order = {'NP':1,'QED':1})

GC_670 = Coupling(name = 'GC_670',
                  value = '(cHL*DEL2x2)/vev - (cpHL*DEL2x2)/vev',
                  order = {'NP':1,'QED':1})

GC_671 = Coupling(name = 'GC_671',
                  value = '(cHL*DEL2x2)/vev + (cpHL*DEL2x2)/vev',
                  order = {'NP':1,'QED':1})

GC_672 = Coupling(name = 'GC_672',
                  value = '(cHQ*DEL2x2)/vev - (cpHQ*DEL2x2)/vev',
                  order = {'NP':1,'QED':1})

GC_673 = Coupling(name = 'GC_673',
                  value = '(cHL*DEL2x3)/vev - (cpHL*DEL2x3)/vev',
                  order = {'NP':1,'QED':1})

GC_674 = Coupling(name = 'GC_674',
                  value = '(cHL*DEL2x3)/vev + (cpHL*DEL2x3)/vev',
                  order = {'NP':1,'QED':1})

GC_675 = Coupling(name = 'GC_675',
                  value = '(cHQ*DEL2x3)/vev - (cpHQ*DEL2x3)/vev',
                  order = {'NP':1,'QED':1})

GC_676 = Coupling(name = 'GC_676',
                  value = '(cHL*DEL3x1)/vev - (cpHL*DEL3x1)/vev',
                  order = {'NP':1,'QED':1})

GC_677 = Coupling(name = 'GC_677',
                  value = '(cHL*DEL3x1)/vev + (cpHL*DEL3x1)/vev',
                  order = {'NP':1,'QED':1})

GC_678 = Coupling(name = 'GC_678',
                  value = '(cHQ*DEL3x1)/vev - (cpHQ*DEL3x1)/vev',
                  order = {'NP':1,'QED':1})

GC_679 = Coupling(name = 'GC_679',
                  value = '(cHL*DEL3x2)/vev - (cpHL*DEL3x2)/vev',
                  order = {'NP':1,'QED':1})

GC_680 = Coupling(name = 'GC_680',
                  value = '(cHL*DEL3x2)/vev + (cpHL*DEL3x2)/vev',
                  order = {'NP':1,'QED':1})

GC_681 = Coupling(name = 'GC_681',
                  value = '(cHQ*DEL3x2)/vev - (cpHQ*DEL3x2)/vev',
                  order = {'NP':1,'QED':1})

GC_682 = Coupling(name = 'GC_682',
                  value = '(cHL*DEL3x3)/vev - (cpHL*DEL3x3)/vev',
                  order = {'NP':1,'QED':1})

GC_683 = Coupling(name = 'GC_683',
                  value = '(cHL*DEL3x3)/vev + (cpHL*DEL3x3)/vev',
                  order = {'NP':1,'QED':1})

GC_684 = Coupling(name = 'GC_684',
                  value = '(cHQ*DEL3x3)/vev - (cpHQ*DEL3x3)/vev',
                  order = {'NP':1,'QED':1})

GC_685 = Coupling(name = 'GC_685',
                  value = '(cHQ*I1a11)/vev + (cpHQ*I1a11)/vev',
                  order = {'NP':1,'QED':1})

GC_686 = Coupling(name = 'GC_686',
                  value = '(cHQ*I1a12)/vev + (cpHQ*I1a12)/vev',
                  order = {'NP':1,'QED':1})

GC_687 = Coupling(name = 'GC_687',
                  value = '(cHQ*I1a13)/vev + (cpHQ*I1a13)/vev',
                  order = {'NP':1,'QED':1})

GC_688 = Coupling(name = 'GC_688',
                  value = '(cHQ*I1a21)/vev + (cpHQ*I1a21)/vev',
                  order = {'NP':1,'QED':1})

GC_689 = Coupling(name = 'GC_689',
                  value = '(cHQ*I1a22)/vev + (cpHQ*I1a22)/vev',
                  order = {'NP':1,'QED':1})

GC_690 = Coupling(name = 'GC_690',
                  value = '(cHQ*I1a23)/vev + (cpHQ*I1a23)/vev',
                  order = {'NP':1,'QED':1})

GC_691 = Coupling(name = 'GC_691',
                  value = '(cHQ*I1a31)/vev + (cpHQ*I1a31)/vev',
                  order = {'NP':1,'QED':1})

GC_692 = Coupling(name = 'GC_692',
                  value = '(cHQ*I1a32)/vev + (cpHQ*I1a32)/vev',
                  order = {'NP':1,'QED':1})

GC_693 = Coupling(name = 'GC_693',
                  value = '(cHQ*I1a33)/vev + (cpHQ*I1a33)/vev',
                  order = {'NP':1,'QED':1})

GC_694 = Coupling(name = 'GC_694',
                  value = '(c6*complex(0,1)*MH**2)/(8.*vev) - (cH*complex(0,1)*MH**2)/(2.*vev)',
                  order = {'NP':1,'QED':1})

GC_695 = Coupling(name = 'GC_695',
                  value = '(-21*c6*complex(0,1)*MH**2)/(8.*vev) + (3*cH*complex(0,1)*MH**2)/(2.*vev)',
                  order = {'NP':1,'QED':1})

GC_696 = Coupling(name = 'GC_696',
                  value = '(-3*cT*ee**2)/(cw*vev) - (3*cT*cw*ee**2)/(sw**2*vev)',
                  order = {'NP':1,'QED':3})

GC_697 = Coupling(name = 'GC_697',
                  value = '(2*cT*ee**2)/(cw*vev) - (2*cT*cw*ee**2)/(sw**2*vev)',
                  order = {'NP':1,'QED':3})

GC_698 = Coupling(name = 'GC_698',
                  value = '-((cT*ee**2)/(cw*vev)) - (cT*cw*ee**2)/(sw**2*vev)',
                  order = {'NP':1,'QED':3})

GC_699 = Coupling(name = 'GC_699',
                  value = '-((cT*ee**2*complex(0,1))/(cw*vev)) - (cT*cw*ee**2*complex(0,1))/(sw**2*vev)',
                  order = {'NP':1,'QED':3})

GC_700 = Coupling(name = 'GC_700',
                  value = '(cT*ee**2)/(cw*vev) + (cT*cw*ee**2)/(sw**2*vev)',
                  order = {'NP':1,'QED':3})

GC_701 = Coupling(name = 'GC_701',
                  value = '(-2*cT*ee**2)/(cw*vev) + (2*cT*cw*ee**2)/(sw**2*vev)',
                  order = {'NP':1,'QED':3})

GC_702 = Coupling(name = 'GC_702',
                  value = '(3*cT*ee**2)/(cw*vev) + (3*cT*cw*ee**2)/(sw**2*vev)',
                  order = {'NP':1,'QED':3})

GC_703 = Coupling(name = 'GC_703',
                  value = '-((cT*cw*ee*complex(0,1))/(sw*vev)) - (cT*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_704 = Coupling(name = 'GC_704',
                  value = '-((cT*cw*ee)/(sw*vev)) + (cT*ee*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_705 = Coupling(name = 'GC_705',
                  value = '(cT*cw*ee)/(sw*vev) + (cT*ee*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_706 = Coupling(name = 'GC_706',
                  value = '(3*cT*cw*ee)/(sw*vev) + (3*cT*ee*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_707 = Coupling(name = 'GC_707',
                  value = '-(cHe*cw*DEL1x1*ee*complex(0,1))/(2.*sw*vev) - (cHe*DEL1x1*ee*complex(0,1)*sw)/(2.*cw*vev)',
                  order = {'NP':1,'QED':2})

GC_708 = Coupling(name = 'GC_708',
                  value = '-((cHL*cw*DEL1x1*ee*complex(0,1))/(sw*vev)) - (cpHL*cw*DEL1x1*ee*complex(0,1))/(sw*vev) - (cHL*DEL1x1*ee*complex(0,1)*sw)/(cw*vev) - (cpHL*DEL1x1*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_709 = Coupling(name = 'GC_709',
                  value = '-((cHL*cw*DEL1x1*ee*complex(0,1))/(sw*vev)) + (cpHL*cw*DEL1x1*ee*complex(0,1))/(sw*vev) - (cHL*DEL1x1*ee*complex(0,1)*sw)/(cw*vev) + (cpHL*DEL1x1*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_710 = Coupling(name = 'GC_710',
                  value = '-((cHQ*cw*DEL1x1*ee*complex(0,1))/(sw*vev)) + (cpHQ*cw*DEL1x1*ee*complex(0,1))/(sw*vev) - (cHQ*DEL1x1*ee*complex(0,1)*sw)/(cw*vev) + (cpHQ*DEL1x1*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_711 = Coupling(name = 'GC_711',
                  value = '-(cHe*cw*DEL1x2*ee*complex(0,1))/(2.*sw*vev) - (cHe*DEL1x2*ee*complex(0,1)*sw)/(2.*cw*vev)',
                  order = {'NP':1,'QED':2})

GC_712 = Coupling(name = 'GC_712',
                  value = '-((cHL*cw*DEL1x2*ee*complex(0,1))/(sw*vev)) - (cpHL*cw*DEL1x2*ee*complex(0,1))/(sw*vev) - (cHL*DEL1x2*ee*complex(0,1)*sw)/(cw*vev) - (cpHL*DEL1x2*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_713 = Coupling(name = 'GC_713',
                  value = '-((cHL*cw*DEL1x2*ee*complex(0,1))/(sw*vev)) + (cpHL*cw*DEL1x2*ee*complex(0,1))/(sw*vev) - (cHL*DEL1x2*ee*complex(0,1)*sw)/(cw*vev) + (cpHL*DEL1x2*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_714 = Coupling(name = 'GC_714',
                  value = '-((cHQ*cw*DEL1x2*ee*complex(0,1))/(sw*vev)) + (cpHQ*cw*DEL1x2*ee*complex(0,1))/(sw*vev) - (cHQ*DEL1x2*ee*complex(0,1)*sw)/(cw*vev) + (cpHQ*DEL1x2*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_715 = Coupling(name = 'GC_715',
                  value = '-(cHe*cw*DEL1x3*ee*complex(0,1))/(2.*sw*vev) - (cHe*DEL1x3*ee*complex(0,1)*sw)/(2.*cw*vev)',
                  order = {'NP':1,'QED':2})

GC_716 = Coupling(name = 'GC_716',
                  value = '-((cHL*cw*DEL1x3*ee*complex(0,1))/(sw*vev)) - (cpHL*cw*DEL1x3*ee*complex(0,1))/(sw*vev) - (cHL*DEL1x3*ee*complex(0,1)*sw)/(cw*vev) - (cpHL*DEL1x3*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_717 = Coupling(name = 'GC_717',
                  value = '-((cHL*cw*DEL1x3*ee*complex(0,1))/(sw*vev)) + (cpHL*cw*DEL1x3*ee*complex(0,1))/(sw*vev) - (cHL*DEL1x3*ee*complex(0,1)*sw)/(cw*vev) + (cpHL*DEL1x3*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_718 = Coupling(name = 'GC_718',
                  value = '-((cHQ*cw*DEL1x3*ee*complex(0,1))/(sw*vev)) + (cpHQ*cw*DEL1x3*ee*complex(0,1))/(sw*vev) - (cHQ*DEL1x3*ee*complex(0,1)*sw)/(cw*vev) + (cpHQ*DEL1x3*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_719 = Coupling(name = 'GC_719',
                  value = '-(cHe*cw*DEL2x1*ee*complex(0,1))/(2.*sw*vev) - (cHe*DEL2x1*ee*complex(0,1)*sw)/(2.*cw*vev)',
                  order = {'NP':1,'QED':2})

GC_720 = Coupling(name = 'GC_720',
                  value = '-((cHL*cw*DEL2x1*ee*complex(0,1))/(sw*vev)) - (cpHL*cw*DEL2x1*ee*complex(0,1))/(sw*vev) - (cHL*DEL2x1*ee*complex(0,1)*sw)/(cw*vev) - (cpHL*DEL2x1*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_721 = Coupling(name = 'GC_721',
                  value = '-((cHL*cw*DEL2x1*ee*complex(0,1))/(sw*vev)) + (cpHL*cw*DEL2x1*ee*complex(0,1))/(sw*vev) - (cHL*DEL2x1*ee*complex(0,1)*sw)/(cw*vev) + (cpHL*DEL2x1*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_722 = Coupling(name = 'GC_722',
                  value = '-((cHQ*cw*DEL2x1*ee*complex(0,1))/(sw*vev)) + (cpHQ*cw*DEL2x1*ee*complex(0,1))/(sw*vev) - (cHQ*DEL2x1*ee*complex(0,1)*sw)/(cw*vev) + (cpHQ*DEL2x1*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_723 = Coupling(name = 'GC_723',
                  value = '-(cHe*cw*DEL2x2*ee*complex(0,1))/(2.*sw*vev) - (cHe*DEL2x2*ee*complex(0,1)*sw)/(2.*cw*vev)',
                  order = {'NP':1,'QED':2})

GC_724 = Coupling(name = 'GC_724',
                  value = '-((cHL*cw*DEL2x2*ee*complex(0,1))/(sw*vev)) - (cpHL*cw*DEL2x2*ee*complex(0,1))/(sw*vev) - (cHL*DEL2x2*ee*complex(0,1)*sw)/(cw*vev) - (cpHL*DEL2x2*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_725 = Coupling(name = 'GC_725',
                  value = '-((cHL*cw*DEL2x2*ee*complex(0,1))/(sw*vev)) + (cpHL*cw*DEL2x2*ee*complex(0,1))/(sw*vev) - (cHL*DEL2x2*ee*complex(0,1)*sw)/(cw*vev) + (cpHL*DEL2x2*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_726 = Coupling(name = 'GC_726',
                  value = '-((cHQ*cw*DEL2x2*ee*complex(0,1))/(sw*vev)) + (cpHQ*cw*DEL2x2*ee*complex(0,1))/(sw*vev) - (cHQ*DEL2x2*ee*complex(0,1)*sw)/(cw*vev) + (cpHQ*DEL2x2*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_727 = Coupling(name = 'GC_727',
                  value = '-(cHe*cw*DEL2x3*ee*complex(0,1))/(2.*sw*vev) - (cHe*DEL2x3*ee*complex(0,1)*sw)/(2.*cw*vev)',
                  order = {'NP':1,'QED':2})

GC_728 = Coupling(name = 'GC_728',
                  value = '-((cHL*cw*DEL2x3*ee*complex(0,1))/(sw*vev)) - (cpHL*cw*DEL2x3*ee*complex(0,1))/(sw*vev) - (cHL*DEL2x3*ee*complex(0,1)*sw)/(cw*vev) - (cpHL*DEL2x3*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_729 = Coupling(name = 'GC_729',
                  value = '-((cHL*cw*DEL2x3*ee*complex(0,1))/(sw*vev)) + (cpHL*cw*DEL2x3*ee*complex(0,1))/(sw*vev) - (cHL*DEL2x3*ee*complex(0,1)*sw)/(cw*vev) + (cpHL*DEL2x3*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_730 = Coupling(name = 'GC_730',
                  value = '-((cHQ*cw*DEL2x3*ee*complex(0,1))/(sw*vev)) + (cpHQ*cw*DEL2x3*ee*complex(0,1))/(sw*vev) - (cHQ*DEL2x3*ee*complex(0,1)*sw)/(cw*vev) + (cpHQ*DEL2x3*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_731 = Coupling(name = 'GC_731',
                  value = '-(cHe*cw*DEL3x1*ee*complex(0,1))/(2.*sw*vev) - (cHe*DEL3x1*ee*complex(0,1)*sw)/(2.*cw*vev)',
                  order = {'NP':1,'QED':2})

GC_732 = Coupling(name = 'GC_732',
                  value = '-((cHL*cw*DEL3x1*ee*complex(0,1))/(sw*vev)) - (cpHL*cw*DEL3x1*ee*complex(0,1))/(sw*vev) - (cHL*DEL3x1*ee*complex(0,1)*sw)/(cw*vev) - (cpHL*DEL3x1*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_733 = Coupling(name = 'GC_733',
                  value = '-((cHL*cw*DEL3x1*ee*complex(0,1))/(sw*vev)) + (cpHL*cw*DEL3x1*ee*complex(0,1))/(sw*vev) - (cHL*DEL3x1*ee*complex(0,1)*sw)/(cw*vev) + (cpHL*DEL3x1*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_734 = Coupling(name = 'GC_734',
                  value = '-((cHQ*cw*DEL3x1*ee*complex(0,1))/(sw*vev)) + (cpHQ*cw*DEL3x1*ee*complex(0,1))/(sw*vev) - (cHQ*DEL3x1*ee*complex(0,1)*sw)/(cw*vev) + (cpHQ*DEL3x1*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_735 = Coupling(name = 'GC_735',
                  value = '-(cHe*cw*DEL3x2*ee*complex(0,1))/(2.*sw*vev) - (cHe*DEL3x2*ee*complex(0,1)*sw)/(2.*cw*vev)',
                  order = {'NP':1,'QED':2})

GC_736 = Coupling(name = 'GC_736',
                  value = '-((cHL*cw*DEL3x2*ee*complex(0,1))/(sw*vev)) - (cpHL*cw*DEL3x2*ee*complex(0,1))/(sw*vev) - (cHL*DEL3x2*ee*complex(0,1)*sw)/(cw*vev) - (cpHL*DEL3x2*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_737 = Coupling(name = 'GC_737',
                  value = '-((cHL*cw*DEL3x2*ee*complex(0,1))/(sw*vev)) + (cpHL*cw*DEL3x2*ee*complex(0,1))/(sw*vev) - (cHL*DEL3x2*ee*complex(0,1)*sw)/(cw*vev) + (cpHL*DEL3x2*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_738 = Coupling(name = 'GC_738',
                  value = '-((cHQ*cw*DEL3x2*ee*complex(0,1))/(sw*vev)) + (cpHQ*cw*DEL3x2*ee*complex(0,1))/(sw*vev) - (cHQ*DEL3x2*ee*complex(0,1)*sw)/(cw*vev) + (cpHQ*DEL3x2*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_739 = Coupling(name = 'GC_739',
                  value = '-(cHe*cw*DEL3x3*ee*complex(0,1))/(2.*sw*vev) - (cHe*DEL3x3*ee*complex(0,1)*sw)/(2.*cw*vev)',
                  order = {'NP':1,'QED':2})

GC_740 = Coupling(name = 'GC_740',
                  value = '-((cHL*cw*DEL3x3*ee*complex(0,1))/(sw*vev)) - (cpHL*cw*DEL3x3*ee*complex(0,1))/(sw*vev) - (cHL*DEL3x3*ee*complex(0,1)*sw)/(cw*vev) - (cpHL*DEL3x3*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_741 = Coupling(name = 'GC_741',
                  value = '-((cHL*cw*DEL3x3*ee*complex(0,1))/(sw*vev)) + (cpHL*cw*DEL3x3*ee*complex(0,1))/(sw*vev) - (cHL*DEL3x3*ee*complex(0,1)*sw)/(cw*vev) + (cpHL*DEL3x3*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_742 = Coupling(name = 'GC_742',
                  value = '-((cHQ*cw*DEL3x3*ee*complex(0,1))/(sw*vev)) + (cpHQ*cw*DEL3x3*ee*complex(0,1))/(sw*vev) - (cHQ*DEL3x3*ee*complex(0,1)*sw)/(cw*vev) + (cpHQ*DEL3x3*ee*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_743 = Coupling(name = 'GC_743',
                  value = '(2*cT*cw*ee**2*complex(0,1))/(sw*vev) + (2*cT*ee**2*complex(0,1)*sw)/(cw*vev)',
                  order = {'NP':1,'QED':3})

GC_744 = Coupling(name = 'GC_744',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a11)/(sw*vev)) - (cpHQ*cw*ee*complex(0,1)*I1a11)/(sw*vev) - (cHQ*ee*complex(0,1)*I1a11*sw)/(cw*vev) - (cpHQ*ee*complex(0,1)*I1a11*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_745 = Coupling(name = 'GC_745',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a12)/(sw*vev)) - (cpHQ*cw*ee*complex(0,1)*I1a12)/(sw*vev) - (cHQ*ee*complex(0,1)*I1a12*sw)/(cw*vev) - (cpHQ*ee*complex(0,1)*I1a12*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_746 = Coupling(name = 'GC_746',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a13)/(sw*vev)) - (cpHQ*cw*ee*complex(0,1)*I1a13)/(sw*vev) - (cHQ*ee*complex(0,1)*I1a13*sw)/(cw*vev) - (cpHQ*ee*complex(0,1)*I1a13*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_747 = Coupling(name = 'GC_747',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a21)/(sw*vev)) - (cpHQ*cw*ee*complex(0,1)*I1a21)/(sw*vev) - (cHQ*ee*complex(0,1)*I1a21*sw)/(cw*vev) - (cpHQ*ee*complex(0,1)*I1a21*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_748 = Coupling(name = 'GC_748',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a22)/(sw*vev)) - (cpHQ*cw*ee*complex(0,1)*I1a22)/(sw*vev) - (cHQ*ee*complex(0,1)*I1a22*sw)/(cw*vev) - (cpHQ*ee*complex(0,1)*I1a22*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_749 = Coupling(name = 'GC_749',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a23)/(sw*vev)) - (cpHQ*cw*ee*complex(0,1)*I1a23)/(sw*vev) - (cHQ*ee*complex(0,1)*I1a23*sw)/(cw*vev) - (cpHQ*ee*complex(0,1)*I1a23*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_750 = Coupling(name = 'GC_750',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a31)/(sw*vev)) - (cpHQ*cw*ee*complex(0,1)*I1a31)/(sw*vev) - (cHQ*ee*complex(0,1)*I1a31*sw)/(cw*vev) - (cpHQ*ee*complex(0,1)*I1a31*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_751 = Coupling(name = 'GC_751',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a32)/(sw*vev)) - (cpHQ*cw*ee*complex(0,1)*I1a32)/(sw*vev) - (cHQ*ee*complex(0,1)*I1a32*sw)/(cw*vev) - (cpHQ*ee*complex(0,1)*I1a32*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_752 = Coupling(name = 'GC_752',
                  value = '-((cHQ*cw*ee*complex(0,1)*I1a33)/(sw*vev)) - (cpHQ*cw*ee*complex(0,1)*I1a33)/(sw*vev) - (cHQ*ee*complex(0,1)*I1a33*sw)/(cw*vev) - (cpHQ*ee*complex(0,1)*I1a33*sw)/(cw*vev)',
                  order = {'NP':1,'QED':2})

GC_753 = Coupling(name = 'GC_753',
                  value = '(-4*cT*ee**2*complex(0,1))/vev - (2*cT*cw**2*ee**2*complex(0,1))/(sw**2*vev) - (2*cT*ee**2*complex(0,1)*sw**2)/(cw**2*vev)',
                  order = {'NP':1,'QED':3})

GC_754 = Coupling(name = 'GC_754',
                  value = '(2*cT*cw**2*ee**2*complex(0,1))/(sw**2*vev) - (2*cT*ee**2*complex(0,1)*sw**2)/(cw**2*vev)',
                  order = {'NP':1,'QED':3})

GC_755 = Coupling(name = 'GC_755',
                  value = '(-12*cT*ee**2*complex(0,1))/vev - (6*cT*cw**2*ee**2*complex(0,1))/(sw**2*vev) - (6*cT*ee**2*complex(0,1)*sw**2)/(cw**2*vev)',
                  order = {'NP':1,'QED':3})

GC_756 = Coupling(name = 'GC_756',
                  value = '(-3*c6*complex(0,1)*MH**2)/vev**4',
                  order = {'NP':1,'QED':4})

GC_757 = Coupling(name = 'GC_757',
                  value = '(-6*c6*complex(0,1)*MH**2)/vev**4',
                  order = {'NP':1,'QED':4})

GC_758 = Coupling(name = 'GC_758',
                  value = '(-9*c6*complex(0,1)*MH**2)/vev**4',
                  order = {'NP':1,'QED':4})

GC_759 = Coupling(name = 'GC_759',
                  value = '(-18*c6*complex(0,1)*MH**2)/vev**4',
                  order = {'NP':1,'QED':4})

GC_760 = Coupling(name = 'GC_760',
                  value = '(-45*c6*complex(0,1)*MH**2)/vev**4',
                  order = {'NP':1,'QED':4})

GC_761 = Coupling(name = 'GC_761',
                  value = '(-3*c6*complex(0,1)*MH**2)/vev**3',
                  order = {'NP':1,'QED':3})

GC_762 = Coupling(name = 'GC_762',
                  value = '(-6*c6*complex(0,1)*MH**2)/vev**3',
                  order = {'NP':1,'QED':3})

GC_763 = Coupling(name = 'GC_763',
                  value = '(-9*c6*complex(0,1)*MH**2)/vev**3',
                  order = {'NP':1,'QED':3})

GC_764 = Coupling(name = 'GC_764',
                  value = '(-45*c6*complex(0,1)*MH**2)/vev**3',
                  order = {'NP':1,'QED':3})

GC_765 = Coupling(name = 'GC_765',
                  value = '-((cH*complex(0,1))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_766 = Coupling(name = 'GC_766',
                  value = '(-2*cH*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_767 = Coupling(name = 'GC_767',
                  value = '(-2*cT*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_768 = Coupling(name = 'GC_768',
                  value = '(2*cT*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':2})

GC_769 = Coupling(name = 'GC_769',
                  value = 'cT/vev**2',
                  order = {'NP':1,'QED':2})

GC_770 = Coupling(name = 'GC_770',
                  value = '-(cHe*DEL1x1*complex(0,1))/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_771 = Coupling(name = 'GC_771',
                  value = '(cHe*DEL1x1)/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_772 = Coupling(name = 'GC_772',
                  value = '-((cHud*DEL1x1*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_773 = Coupling(name = 'GC_773',
                  value = '(cHud*DEL1x1*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_774 = Coupling(name = 'GC_774',
                  value = '-((cpHL*DEL1x1*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_775 = Coupling(name = 'GC_775',
                  value = '-((cpHL*DEL1x1*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_776 = Coupling(name = 'GC_776',
                  value = '(cpHL*DEL1x1*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_777 = Coupling(name = 'GC_777',
                  value = '-(cHe*DEL1x2*complex(0,1))/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_778 = Coupling(name = 'GC_778',
                  value = '(cHe*DEL1x2)/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_779 = Coupling(name = 'GC_779',
                  value = '-((cHud*DEL1x2*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_780 = Coupling(name = 'GC_780',
                  value = '(cHud*DEL1x2*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_781 = Coupling(name = 'GC_781',
                  value = '-((cpHL*DEL1x2*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_782 = Coupling(name = 'GC_782',
                  value = '-((cpHL*DEL1x2*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_783 = Coupling(name = 'GC_783',
                  value = '(cpHL*DEL1x2*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_784 = Coupling(name = 'GC_784',
                  value = '-(cHe*DEL1x3*complex(0,1))/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_785 = Coupling(name = 'GC_785',
                  value = '(cHe*DEL1x3)/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_786 = Coupling(name = 'GC_786',
                  value = '-((cHud*DEL1x3*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_787 = Coupling(name = 'GC_787',
                  value = '(cHud*DEL1x3*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_788 = Coupling(name = 'GC_788',
                  value = '-((cpHL*DEL1x3*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_789 = Coupling(name = 'GC_789',
                  value = '-((cpHL*DEL1x3*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_790 = Coupling(name = 'GC_790',
                  value = '(cpHL*DEL1x3*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_791 = Coupling(name = 'GC_791',
                  value = '-(cHe*DEL2x1*complex(0,1))/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_792 = Coupling(name = 'GC_792',
                  value = '(cHe*DEL2x1)/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_793 = Coupling(name = 'GC_793',
                  value = '-((cHud*DEL2x1*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_794 = Coupling(name = 'GC_794',
                  value = '(cHud*DEL2x1*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_795 = Coupling(name = 'GC_795',
                  value = '-((cpHL*DEL2x1*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_796 = Coupling(name = 'GC_796',
                  value = '-((cpHL*DEL2x1*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_797 = Coupling(name = 'GC_797',
                  value = '(cpHL*DEL2x1*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_798 = Coupling(name = 'GC_798',
                  value = '-(cHe*DEL2x2*complex(0,1))/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_799 = Coupling(name = 'GC_799',
                  value = '(cHe*DEL2x2)/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_800 = Coupling(name = 'GC_800',
                  value = '-((cHud*DEL2x2*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_801 = Coupling(name = 'GC_801',
                  value = '(cHud*DEL2x2*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_802 = Coupling(name = 'GC_802',
                  value = '-((cpHL*DEL2x2*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_803 = Coupling(name = 'GC_803',
                  value = '-((cpHL*DEL2x2*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_804 = Coupling(name = 'GC_804',
                  value = '(cpHL*DEL2x2*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_805 = Coupling(name = 'GC_805',
                  value = '-(cHe*DEL2x3*complex(0,1))/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_806 = Coupling(name = 'GC_806',
                  value = '(cHe*DEL2x3)/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_807 = Coupling(name = 'GC_807',
                  value = '-((cHud*DEL2x3*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_808 = Coupling(name = 'GC_808',
                  value = '(cHud*DEL2x3*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_809 = Coupling(name = 'GC_809',
                  value = '-((cpHL*DEL2x3*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_810 = Coupling(name = 'GC_810',
                  value = '-((cpHL*DEL2x3*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_811 = Coupling(name = 'GC_811',
                  value = '(cpHL*DEL2x3*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_812 = Coupling(name = 'GC_812',
                  value = '-(cHe*DEL3x1*complex(0,1))/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_813 = Coupling(name = 'GC_813',
                  value = '(cHe*DEL3x1)/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_814 = Coupling(name = 'GC_814',
                  value = '-((cHud*DEL3x1*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_815 = Coupling(name = 'GC_815',
                  value = '(cHud*DEL3x1*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_816 = Coupling(name = 'GC_816',
                  value = '-((cpHL*DEL3x1*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_817 = Coupling(name = 'GC_817',
                  value = '-((cpHL*DEL3x1*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_818 = Coupling(name = 'GC_818',
                  value = '(cpHL*DEL3x1*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_819 = Coupling(name = 'GC_819',
                  value = '-(cHe*DEL3x2*complex(0,1))/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_820 = Coupling(name = 'GC_820',
                  value = '(cHe*DEL3x2)/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_821 = Coupling(name = 'GC_821',
                  value = '-((cHud*DEL3x2*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_822 = Coupling(name = 'GC_822',
                  value = '(cHud*DEL3x2*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_823 = Coupling(name = 'GC_823',
                  value = '-((cpHL*DEL3x2*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_824 = Coupling(name = 'GC_824',
                  value = '-((cpHL*DEL3x2*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_825 = Coupling(name = 'GC_825',
                  value = '(cpHL*DEL3x2*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_826 = Coupling(name = 'GC_826',
                  value = '-(cHe*DEL3x3*complex(0,1))/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_827 = Coupling(name = 'GC_827',
                  value = '(cHe*DEL3x3)/(2.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_828 = Coupling(name = 'GC_828',
                  value = '-((cHud*DEL3x3*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_829 = Coupling(name = 'GC_829',
                  value = '(cHud*DEL3x3*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_830 = Coupling(name = 'GC_830',
                  value = '-((cpHL*DEL3x3*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_831 = Coupling(name = 'GC_831',
                  value = '-((cpHL*DEL3x3*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_832 = Coupling(name = 'GC_832',
                  value = '(cpHL*DEL3x3*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_833 = Coupling(name = 'GC_833',
                  value = '(-2*cT*ee)/vev**2',
                  order = {'NP':1,'QED':3})

GC_834 = Coupling(name = 'GC_834',
                  value = '(4*cT*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_835 = Coupling(name = 'GC_835',
                  value = '(cHe*DEL1x1*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_836 = Coupling(name = 'GC_836',
                  value = '(cHud*DEL1x1*ee*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_837 = Coupling(name = 'GC_837',
                  value = '(cHud*DEL1x1*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_838 = Coupling(name = 'GC_838',
                  value = '-((cpHL*DEL1x1*ee*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_839 = Coupling(name = 'GC_839',
                  value = '-((cpHL*DEL1x1*ee*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_840 = Coupling(name = 'GC_840',
                  value = '(cpHL*DEL1x1*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_841 = Coupling(name = 'GC_841',
                  value = '(cHe*DEL1x2*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_842 = Coupling(name = 'GC_842',
                  value = '(cHud*DEL1x2*ee*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_843 = Coupling(name = 'GC_843',
                  value = '(cHud*DEL1x2*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_844 = Coupling(name = 'GC_844',
                  value = '-((cpHL*DEL1x2*ee*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_845 = Coupling(name = 'GC_845',
                  value = '-((cpHL*DEL1x2*ee*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_846 = Coupling(name = 'GC_846',
                  value = '(cpHL*DEL1x2*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_847 = Coupling(name = 'GC_847',
                  value = '(cHe*DEL1x3*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_848 = Coupling(name = 'GC_848',
                  value = '(cHud*DEL1x3*ee*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_849 = Coupling(name = 'GC_849',
                  value = '(cHud*DEL1x3*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_850 = Coupling(name = 'GC_850',
                  value = '-((cpHL*DEL1x3*ee*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_851 = Coupling(name = 'GC_851',
                  value = '-((cpHL*DEL1x3*ee*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_852 = Coupling(name = 'GC_852',
                  value = '(cpHL*DEL1x3*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_853 = Coupling(name = 'GC_853',
                  value = '(cHe*DEL2x1*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_854 = Coupling(name = 'GC_854',
                  value = '(cHud*DEL2x1*ee*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_855 = Coupling(name = 'GC_855',
                  value = '(cHud*DEL2x1*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_856 = Coupling(name = 'GC_856',
                  value = '-((cpHL*DEL2x1*ee*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_857 = Coupling(name = 'GC_857',
                  value = '-((cpHL*DEL2x1*ee*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_858 = Coupling(name = 'GC_858',
                  value = '(cpHL*DEL2x1*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_859 = Coupling(name = 'GC_859',
                  value = '(cHe*DEL2x2*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_860 = Coupling(name = 'GC_860',
                  value = '(cHud*DEL2x2*ee*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_861 = Coupling(name = 'GC_861',
                  value = '(cHud*DEL2x2*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_862 = Coupling(name = 'GC_862',
                  value = '-((cpHL*DEL2x2*ee*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_863 = Coupling(name = 'GC_863',
                  value = '-((cpHL*DEL2x2*ee*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_864 = Coupling(name = 'GC_864',
                  value = '(cpHL*DEL2x2*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_865 = Coupling(name = 'GC_865',
                  value = '(cHe*DEL2x3*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_866 = Coupling(name = 'GC_866',
                  value = '(cHud*DEL2x3*ee*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_867 = Coupling(name = 'GC_867',
                  value = '(cHud*DEL2x3*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_868 = Coupling(name = 'GC_868',
                  value = '-((cpHL*DEL2x3*ee*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_869 = Coupling(name = 'GC_869',
                  value = '-((cpHL*DEL2x3*ee*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_870 = Coupling(name = 'GC_870',
                  value = '(cpHL*DEL2x3*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_871 = Coupling(name = 'GC_871',
                  value = '(cHe*DEL3x1*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_872 = Coupling(name = 'GC_872',
                  value = '(cHud*DEL3x1*ee*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_873 = Coupling(name = 'GC_873',
                  value = '(cHud*DEL3x1*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_874 = Coupling(name = 'GC_874',
                  value = '-((cpHL*DEL3x1*ee*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_875 = Coupling(name = 'GC_875',
                  value = '-((cpHL*DEL3x1*ee*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_876 = Coupling(name = 'GC_876',
                  value = '(cpHL*DEL3x1*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_877 = Coupling(name = 'GC_877',
                  value = '(cHe*DEL3x2*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_878 = Coupling(name = 'GC_878',
                  value = '(cHud*DEL3x2*ee*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_879 = Coupling(name = 'GC_879',
                  value = '(cHud*DEL3x2*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_880 = Coupling(name = 'GC_880',
                  value = '-((cpHL*DEL3x2*ee*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_881 = Coupling(name = 'GC_881',
                  value = '-((cpHL*DEL3x2*ee*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_882 = Coupling(name = 'GC_882',
                  value = '(cpHL*DEL3x2*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_883 = Coupling(name = 'GC_883',
                  value = '(cHe*DEL3x3*ee*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':3})

GC_884 = Coupling(name = 'GC_884',
                  value = '(cHud*DEL3x3*ee*complex(0,1)*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_885 = Coupling(name = 'GC_885',
                  value = '(cHud*DEL3x3*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_886 = Coupling(name = 'GC_886',
                  value = '-((cpHL*DEL3x3*ee*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_887 = Coupling(name = 'GC_887',
                  value = '-((cpHL*DEL3x3*ee*complex(0,1)*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_888 = Coupling(name = 'GC_888',
                  value = '(cpHL*DEL3x3*ee*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_889 = Coupling(name = 'GC_889',
                  value = '(-16*cT*ee**2*complex(0,1))/vev**2',
                  order = {'NP':1,'QED':4})

GC_890 = Coupling(name = 'GC_890',
                  value = '(cd*I2a33)/vev**2',
                  order = {'NP':1,'QED':3})

GC_891 = Coupling(name = 'GC_891',
                  value = '(2*cd*I2a33)/vev**2',
                  order = {'NP':1,'QED':3})

GC_892 = Coupling(name = 'GC_892',
                  value = '(-2*cu*I3a33)/vev**2',
                  order = {'NP':1,'QED':3})

GC_893 = Coupling(name = 'GC_893',
                  value = '-((cu*I3a33)/vev**2)',
                  order = {'NP':1,'QED':3})

GC_894 = Coupling(name = 'GC_894',
                  value = '-((cpHQ*I4a11*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_895 = Coupling(name = 'GC_895',
                  value = '(cpHQ*complex(0,1)*I4a11*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_896 = Coupling(name = 'GC_896',
                  value = '-((cpHQ*ee*I4a11*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_897 = Coupling(name = 'GC_897',
                  value = '-((cpHQ*ee*complex(0,1)*I4a11*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_898 = Coupling(name = 'GC_898',
                  value = '-((cpHQ*I4a12*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_899 = Coupling(name = 'GC_899',
                  value = '(cpHQ*complex(0,1)*I4a12*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_900 = Coupling(name = 'GC_900',
                  value = '-((cpHQ*ee*I4a12*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_901 = Coupling(name = 'GC_901',
                  value = '-((cpHQ*ee*complex(0,1)*I4a12*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_902 = Coupling(name = 'GC_902',
                  value = '-((cpHQ*I4a13*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_903 = Coupling(name = 'GC_903',
                  value = '(cpHQ*complex(0,1)*I4a13*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_904 = Coupling(name = 'GC_904',
                  value = '-((cpHQ*ee*I4a13*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_905 = Coupling(name = 'GC_905',
                  value = '-((cpHQ*ee*complex(0,1)*I4a13*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_906 = Coupling(name = 'GC_906',
                  value = '-((cpHQ*I4a21*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_907 = Coupling(name = 'GC_907',
                  value = '(cpHQ*complex(0,1)*I4a21*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_908 = Coupling(name = 'GC_908',
                  value = '-((cpHQ*ee*I4a21*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_909 = Coupling(name = 'GC_909',
                  value = '-((cpHQ*ee*complex(0,1)*I4a21*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_910 = Coupling(name = 'GC_910',
                  value = '-((cpHQ*I4a22*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_911 = Coupling(name = 'GC_911',
                  value = '(cpHQ*complex(0,1)*I4a22*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_912 = Coupling(name = 'GC_912',
                  value = '-((cpHQ*ee*I4a22*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_913 = Coupling(name = 'GC_913',
                  value = '-((cpHQ*ee*complex(0,1)*I4a22*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_914 = Coupling(name = 'GC_914',
                  value = '-((cpHQ*I4a23*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_915 = Coupling(name = 'GC_915',
                  value = '(cpHQ*complex(0,1)*I4a23*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_916 = Coupling(name = 'GC_916',
                  value = '-((cpHQ*ee*I4a23*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_917 = Coupling(name = 'GC_917',
                  value = '-((cpHQ*ee*complex(0,1)*I4a23*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_918 = Coupling(name = 'GC_918',
                  value = '-((cpHQ*I4a31*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_919 = Coupling(name = 'GC_919',
                  value = '(cpHQ*complex(0,1)*I4a31*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_920 = Coupling(name = 'GC_920',
                  value = '-((cpHQ*ee*I4a31*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_921 = Coupling(name = 'GC_921',
                  value = '-((cpHQ*ee*complex(0,1)*I4a31*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_922 = Coupling(name = 'GC_922',
                  value = '-((cpHQ*I4a32*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_923 = Coupling(name = 'GC_923',
                  value = '(cpHQ*complex(0,1)*I4a32*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_924 = Coupling(name = 'GC_924',
                  value = '-((cpHQ*ee*I4a32*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_925 = Coupling(name = 'GC_925',
                  value = '-((cpHQ*ee*complex(0,1)*I4a32*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_926 = Coupling(name = 'GC_926',
                  value = '-((cpHQ*I4a33*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_927 = Coupling(name = 'GC_927',
                  value = '(cpHQ*complex(0,1)*I4a33*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':2})

GC_928 = Coupling(name = 'GC_928',
                  value = '-((cpHQ*ee*I4a33*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_929 = Coupling(name = 'GC_929',
                  value = '-((cpHQ*ee*complex(0,1)*I4a33*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_930 = Coupling(name = 'GC_930',
                  value = '(cu*I5a33)/vev**2',
                  order = {'NP':1,'QED':3})

GC_931 = Coupling(name = 'GC_931',
                  value = '(2*cu*I5a33)/vev**2',
                  order = {'NP':1,'QED':3})

GC_932 = Coupling(name = 'GC_932',
                  value = '(-2*cd*I6a33)/vev**2',
                  order = {'NP':1,'QED':3})

GC_933 = Coupling(name = 'GC_933',
                  value = '-((cd*I6a33)/vev**2)',
                  order = {'NP':1,'QED':3})

GC_934 = Coupling(name = 'GC_934',
                  value = '-((cpHQ*I7a11*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_935 = Coupling(name = 'GC_935',
                  value = '-((cpHQ*complex(0,1)*I7a11*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_936 = Coupling(name = 'GC_936',
                  value = '-((cpHQ*ee*complex(0,1)*I7a11*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_937 = Coupling(name = 'GC_937',
                  value = '(cpHQ*ee*I7a11*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_938 = Coupling(name = 'GC_938',
                  value = '-((cpHQ*I7a12*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_939 = Coupling(name = 'GC_939',
                  value = '-((cpHQ*complex(0,1)*I7a12*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_940 = Coupling(name = 'GC_940',
                  value = '-((cpHQ*ee*complex(0,1)*I7a12*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_941 = Coupling(name = 'GC_941',
                  value = '(cpHQ*ee*I7a12*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_942 = Coupling(name = 'GC_942',
                  value = '-((cpHQ*I7a13*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_943 = Coupling(name = 'GC_943',
                  value = '-((cpHQ*complex(0,1)*I7a13*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_944 = Coupling(name = 'GC_944',
                  value = '-((cpHQ*ee*complex(0,1)*I7a13*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_945 = Coupling(name = 'GC_945',
                  value = '(cpHQ*ee*I7a13*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_946 = Coupling(name = 'GC_946',
                  value = '-((cpHQ*I7a21*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_947 = Coupling(name = 'GC_947',
                  value = '-((cpHQ*complex(0,1)*I7a21*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_948 = Coupling(name = 'GC_948',
                  value = '-((cpHQ*ee*complex(0,1)*I7a21*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_949 = Coupling(name = 'GC_949',
                  value = '(cpHQ*ee*I7a21*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_950 = Coupling(name = 'GC_950',
                  value = '-((cpHQ*I7a22*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_951 = Coupling(name = 'GC_951',
                  value = '-((cpHQ*complex(0,1)*I7a22*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_952 = Coupling(name = 'GC_952',
                  value = '-((cpHQ*ee*complex(0,1)*I7a22*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_953 = Coupling(name = 'GC_953',
                  value = '(cpHQ*ee*I7a22*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_954 = Coupling(name = 'GC_954',
                  value = '-((cpHQ*I7a23*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_955 = Coupling(name = 'GC_955',
                  value = '-((cpHQ*complex(0,1)*I7a23*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_956 = Coupling(name = 'GC_956',
                  value = '-((cpHQ*ee*complex(0,1)*I7a23*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_957 = Coupling(name = 'GC_957',
                  value = '(cpHQ*ee*I7a23*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_958 = Coupling(name = 'GC_958',
                  value = '-((cpHQ*I7a31*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_959 = Coupling(name = 'GC_959',
                  value = '-((cpHQ*complex(0,1)*I7a31*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_960 = Coupling(name = 'GC_960',
                  value = '-((cpHQ*ee*complex(0,1)*I7a31*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_961 = Coupling(name = 'GC_961',
                  value = '(cpHQ*ee*I7a31*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_962 = Coupling(name = 'GC_962',
                  value = '-((cpHQ*I7a32*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_963 = Coupling(name = 'GC_963',
                  value = '-((cpHQ*complex(0,1)*I7a32*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_964 = Coupling(name = 'GC_964',
                  value = '-((cpHQ*ee*complex(0,1)*I7a32*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_965 = Coupling(name = 'GC_965',
                  value = '(cpHQ*ee*I7a32*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_966 = Coupling(name = 'GC_966',
                  value = '-((cpHQ*I7a33*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_967 = Coupling(name = 'GC_967',
                  value = '-((cpHQ*complex(0,1)*I7a33*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':2})

GC_968 = Coupling(name = 'GC_968',
                  value = '-((cpHQ*ee*complex(0,1)*I7a33*cmath.sqrt(2))/vev**2)',
                  order = {'NP':1,'QED':3})

GC_969 = Coupling(name = 'GC_969',
                  value = '(cpHQ*ee*I7a33*cmath.sqrt(2))/vev**2',
                  order = {'NP':1,'QED':3})

GC_970 = Coupling(name = 'GC_970',
                  value = '-((complex(0,1)*MH**2)/vev**2)',
                  order = {'QED':2})

GC_971 = Coupling(name = 'GC_971',
                  value = '(-2*complex(0,1)*MH**2)/vev**2',
                  order = {'QED':2})

GC_972 = Coupling(name = 'GC_972',
                  value = '(-3*complex(0,1)*MH**2)/vev**2',
                  order = {'QED':2})

GC_973 = Coupling(name = 'GC_973',
                  value = '(-23*c6*complex(0,1)*MH**2)/(8.*vev**2)',
                  order = {'NP':1,'QED':2})

GC_974 = Coupling(name = 'GC_974',
                  value = '(-4*cT*ee**2)/(sw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_975 = Coupling(name = 'GC_975',
                  value = '(-2*cT*ee**2*complex(0,1))/(sw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_976 = Coupling(name = 'GC_976',
                  value = '(-4*cT*ee**2*complex(0,1))/(sw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_977 = Coupling(name = 'GC_977',
                  value = '(4*cT*ee**2*complex(0,1))/(sw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_978 = Coupling(name = 'GC_978',
                  value = '(4*cT*ee**2)/(sw**2*vev**2)',
                  order = {'NP':1,'QED':4})

GC_979 = Coupling(name = 'GC_979',
                  value = '(-2*cT*ee)/(sw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_980 = Coupling(name = 'GC_980',
                  value = '-((cT*ee*complex(0,1))/(sw*vev**2))',
                  order = {'NP':1,'QED':3})

GC_981 = Coupling(name = 'GC_981',
                  value = '(-2*cT*ee*complex(0,1))/(sw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_982 = Coupling(name = 'GC_982',
                  value = '(2*cT*ee*complex(0,1))/(sw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_983 = Coupling(name = 'GC_983',
                  value = '(cT*ee)/(sw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_984 = Coupling(name = 'GC_984',
                  value = '-(cHe*DEL1x1*ee)/(2.*sw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_985 = Coupling(name = 'GC_985',
                  value = '-(cHe*DEL1x1*ee*complex(0,1))/(2.*sw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_986 = Coupling(name = 'GC_986',
                  value = '(cHe*DEL1x1*ee)/(2.*sw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_987 = Coupling(name = 'GC_987',
                  value = '-((cHL*DEL1x1*ee)/(sw*vev**2))',
                  order = {'NP':1,'QED':3})

GC_988 = Coupling(name = 'GC_988',
                  value = '-((cHL*DEL1x1*ee*complex(0,1))/(sw*vev**2))',
                  order = {'NP':1,'QED':3})

GC_989 = Coupling(name = 'GC_989',
                  value = '(cHL*DEL1x1*ee)/(sw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_990 = Coupling(name = 'GC_990',
                  value = '-((cHQ*DEL1x1*ee)/(sw*vev**2))',
                  order = {'NP':1,'QED':3})

GC_991 = Coupling(name = 'GC_991',
                  value = '-((cHQ*DEL1x1*ee*complex(0,1))/(sw*vev**2))',
                  order = {'NP':1,'QED':3})

GC_992 = Coupling(name = 'GC_992',
                  value = '(cHQ*DEL1x1*ee)/(sw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_993 = Coupling(name = 'GC_993',
                  value = '-((cHud*DEL1x1*ee*cmath.sqrt(2))/(sw*vev**2))',
                  order = {'NP':1,'QED':3})

GC_994 = Coupling(name = 'GC_994',
                  value = '-((cHud*DEL1x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2))',
                  order = {'NP':1,'QED':3})

GC_995 = Coupling(name = 'GC_995',
                  value = '(cHud*DEL1x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_996 = Coupling(name = 'GC_996',
                  value = '(2*cHud*DEL1x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_997 = Coupling(name = 'GC_997',
                  value = '(cpHL*DEL1x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_998 = Coupling(name = 'GC_998',
                  value = '(cHud*cw*DEL1x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_999 = Coupling(name = 'GC_999',
                  value = '(cHud*cw*DEL1x1*ee*cmath.sqrt(2))/(sw*vev**2)',
                  order = {'NP':1,'QED':3})

GC_1000 = Coupling(name = 'GC_1000',
                   value = '-(cHe*DEL1x2*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1001 = Coupling(name = 'GC_1001',
                   value = '-(cHe*DEL1x2*ee*complex(0,1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1002 = Coupling(name = 'GC_1002',
                   value = '(cHe*DEL1x2*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1003 = Coupling(name = 'GC_1003',
                   value = '-((cHL*DEL1x2*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1004 = Coupling(name = 'GC_1004',
                   value = '-((cHL*DEL1x2*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1005 = Coupling(name = 'GC_1005',
                   value = '(cHL*DEL1x2*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1006 = Coupling(name = 'GC_1006',
                   value = '-((cHQ*DEL1x2*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1007 = Coupling(name = 'GC_1007',
                   value = '-((cHQ*DEL1x2*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1008 = Coupling(name = 'GC_1008',
                   value = '(cHQ*DEL1x2*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1009 = Coupling(name = 'GC_1009',
                   value = '-((cHud*DEL1x2*ee*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1010 = Coupling(name = 'GC_1010',
                   value = '-((cHud*DEL1x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1011 = Coupling(name = 'GC_1011',
                   value = '(cHud*DEL1x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1012 = Coupling(name = 'GC_1012',
                   value = '(2*cHud*DEL1x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1013 = Coupling(name = 'GC_1013',
                   value = '(cpHL*DEL1x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1014 = Coupling(name = 'GC_1014',
                   value = '(cHud*cw*DEL1x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1015 = Coupling(name = 'GC_1015',
                   value = '(cHud*cw*DEL1x2*ee*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1016 = Coupling(name = 'GC_1016',
                   value = '-(cHe*DEL1x3*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1017 = Coupling(name = 'GC_1017',
                   value = '-(cHe*DEL1x3*ee*complex(0,1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1018 = Coupling(name = 'GC_1018',
                   value = '(cHe*DEL1x3*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1019 = Coupling(name = 'GC_1019',
                   value = '-((cHL*DEL1x3*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1020 = Coupling(name = 'GC_1020',
                   value = '-((cHL*DEL1x3*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1021 = Coupling(name = 'GC_1021',
                   value = '(cHL*DEL1x3*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1022 = Coupling(name = 'GC_1022',
                   value = '-((cHQ*DEL1x3*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1023 = Coupling(name = 'GC_1023',
                   value = '-((cHQ*DEL1x3*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1024 = Coupling(name = 'GC_1024',
                   value = '(cHQ*DEL1x3*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1025 = Coupling(name = 'GC_1025',
                   value = '-((cHud*DEL1x3*ee*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1026 = Coupling(name = 'GC_1026',
                   value = '-((cHud*DEL1x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1027 = Coupling(name = 'GC_1027',
                   value = '(cHud*DEL1x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1028 = Coupling(name = 'GC_1028',
                   value = '(2*cHud*DEL1x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1029 = Coupling(name = 'GC_1029',
                   value = '(cpHL*DEL1x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1030 = Coupling(name = 'GC_1030',
                   value = '(cHud*cw*DEL1x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1031 = Coupling(name = 'GC_1031',
                   value = '(cHud*cw*DEL1x3*ee*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1032 = Coupling(name = 'GC_1032',
                   value = '-(cHe*DEL2x1*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1033 = Coupling(name = 'GC_1033',
                   value = '-(cHe*DEL2x1*ee*complex(0,1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1034 = Coupling(name = 'GC_1034',
                   value = '(cHe*DEL2x1*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1035 = Coupling(name = 'GC_1035',
                   value = '-((cHL*DEL2x1*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1036 = Coupling(name = 'GC_1036',
                   value = '-((cHL*DEL2x1*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1037 = Coupling(name = 'GC_1037',
                   value = '(cHL*DEL2x1*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1038 = Coupling(name = 'GC_1038',
                   value = '-((cHQ*DEL2x1*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1039 = Coupling(name = 'GC_1039',
                   value = '-((cHQ*DEL2x1*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1040 = Coupling(name = 'GC_1040',
                   value = '(cHQ*DEL2x1*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1041 = Coupling(name = 'GC_1041',
                   value = '-((cHud*DEL2x1*ee*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1042 = Coupling(name = 'GC_1042',
                   value = '-((cHud*DEL2x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1043 = Coupling(name = 'GC_1043',
                   value = '(cHud*DEL2x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1044 = Coupling(name = 'GC_1044',
                   value = '(2*cHud*DEL2x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1045 = Coupling(name = 'GC_1045',
                   value = '(cpHL*DEL2x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1046 = Coupling(name = 'GC_1046',
                   value = '(cHud*cw*DEL2x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1047 = Coupling(name = 'GC_1047',
                   value = '(cHud*cw*DEL2x1*ee*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1048 = Coupling(name = 'GC_1048',
                   value = '-(cHe*DEL2x2*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1049 = Coupling(name = 'GC_1049',
                   value = '-(cHe*DEL2x2*ee*complex(0,1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1050 = Coupling(name = 'GC_1050',
                   value = '(cHe*DEL2x2*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1051 = Coupling(name = 'GC_1051',
                   value = '-((cHL*DEL2x2*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1052 = Coupling(name = 'GC_1052',
                   value = '-((cHL*DEL2x2*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1053 = Coupling(name = 'GC_1053',
                   value = '(cHL*DEL2x2*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1054 = Coupling(name = 'GC_1054',
                   value = '-((cHQ*DEL2x2*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1055 = Coupling(name = 'GC_1055',
                   value = '-((cHQ*DEL2x2*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1056 = Coupling(name = 'GC_1056',
                   value = '(cHQ*DEL2x2*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1057 = Coupling(name = 'GC_1057',
                   value = '-((cHud*DEL2x2*ee*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1058 = Coupling(name = 'GC_1058',
                   value = '-((cHud*DEL2x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1059 = Coupling(name = 'GC_1059',
                   value = '(cHud*DEL2x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1060 = Coupling(name = 'GC_1060',
                   value = '(2*cHud*DEL2x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1061 = Coupling(name = 'GC_1061',
                   value = '(cpHL*DEL2x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1062 = Coupling(name = 'GC_1062',
                   value = '(cHud*cw*DEL2x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1063 = Coupling(name = 'GC_1063',
                   value = '(cHud*cw*DEL2x2*ee*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1064 = Coupling(name = 'GC_1064',
                   value = '-(cHe*DEL2x3*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1065 = Coupling(name = 'GC_1065',
                   value = '-(cHe*DEL2x3*ee*complex(0,1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1066 = Coupling(name = 'GC_1066',
                   value = '(cHe*DEL2x3*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1067 = Coupling(name = 'GC_1067',
                   value = '-((cHL*DEL2x3*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1068 = Coupling(name = 'GC_1068',
                   value = '-((cHL*DEL2x3*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1069 = Coupling(name = 'GC_1069',
                   value = '(cHL*DEL2x3*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1070 = Coupling(name = 'GC_1070',
                   value = '-((cHQ*DEL2x3*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1071 = Coupling(name = 'GC_1071',
                   value = '-((cHQ*DEL2x3*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1072 = Coupling(name = 'GC_1072',
                   value = '(cHQ*DEL2x3*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1073 = Coupling(name = 'GC_1073',
                   value = '-((cHud*DEL2x3*ee*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1074 = Coupling(name = 'GC_1074',
                   value = '-((cHud*DEL2x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1075 = Coupling(name = 'GC_1075',
                   value = '(cHud*DEL2x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1076 = Coupling(name = 'GC_1076',
                   value = '(2*cHud*DEL2x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1077 = Coupling(name = 'GC_1077',
                   value = '(cpHL*DEL2x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1078 = Coupling(name = 'GC_1078',
                   value = '(cHud*cw*DEL2x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1079 = Coupling(name = 'GC_1079',
                   value = '(cHud*cw*DEL2x3*ee*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1080 = Coupling(name = 'GC_1080',
                   value = '-(cHe*DEL3x1*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1081 = Coupling(name = 'GC_1081',
                   value = '-(cHe*DEL3x1*ee*complex(0,1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1082 = Coupling(name = 'GC_1082',
                   value = '(cHe*DEL3x1*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1083 = Coupling(name = 'GC_1083',
                   value = '-((cHL*DEL3x1*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1084 = Coupling(name = 'GC_1084',
                   value = '-((cHL*DEL3x1*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1085 = Coupling(name = 'GC_1085',
                   value = '(cHL*DEL3x1*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1086 = Coupling(name = 'GC_1086',
                   value = '-((cHQ*DEL3x1*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1087 = Coupling(name = 'GC_1087',
                   value = '-((cHQ*DEL3x1*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1088 = Coupling(name = 'GC_1088',
                   value = '(cHQ*DEL3x1*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1089 = Coupling(name = 'GC_1089',
                   value = '-((cHud*DEL3x1*ee*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1090 = Coupling(name = 'GC_1090',
                   value = '-((cHud*DEL3x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1091 = Coupling(name = 'GC_1091',
                   value = '(cHud*DEL3x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1092 = Coupling(name = 'GC_1092',
                   value = '(2*cHud*DEL3x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1093 = Coupling(name = 'GC_1093',
                   value = '(cpHL*DEL3x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1094 = Coupling(name = 'GC_1094',
                   value = '(cHud*cw*DEL3x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1095 = Coupling(name = 'GC_1095',
                   value = '(cHud*cw*DEL3x1*ee*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1096 = Coupling(name = 'GC_1096',
                   value = '-(cHe*DEL3x2*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1097 = Coupling(name = 'GC_1097',
                   value = '-(cHe*DEL3x2*ee*complex(0,1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1098 = Coupling(name = 'GC_1098',
                   value = '(cHe*DEL3x2*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1099 = Coupling(name = 'GC_1099',
                   value = '-((cHL*DEL3x2*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1100 = Coupling(name = 'GC_1100',
                   value = '-((cHL*DEL3x2*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1101 = Coupling(name = 'GC_1101',
                   value = '(cHL*DEL3x2*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1102 = Coupling(name = 'GC_1102',
                   value = '-((cHQ*DEL3x2*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1103 = Coupling(name = 'GC_1103',
                   value = '-((cHQ*DEL3x2*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1104 = Coupling(name = 'GC_1104',
                   value = '(cHQ*DEL3x2*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1105 = Coupling(name = 'GC_1105',
                   value = '-((cHud*DEL3x2*ee*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1106 = Coupling(name = 'GC_1106',
                   value = '-((cHud*DEL3x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1107 = Coupling(name = 'GC_1107',
                   value = '(cHud*DEL3x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1108 = Coupling(name = 'GC_1108',
                   value = '(2*cHud*DEL3x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1109 = Coupling(name = 'GC_1109',
                   value = '(cpHL*DEL3x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1110 = Coupling(name = 'GC_1110',
                   value = '(cHud*cw*DEL3x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1111 = Coupling(name = 'GC_1111',
                   value = '(cHud*cw*DEL3x2*ee*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1112 = Coupling(name = 'GC_1112',
                   value = '-(cHe*DEL3x3*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1113 = Coupling(name = 'GC_1113',
                   value = '-(cHe*DEL3x3*ee*complex(0,1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1114 = Coupling(name = 'GC_1114',
                   value = '(cHe*DEL3x3*ee)/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1115 = Coupling(name = 'GC_1115',
                   value = '-((cHL*DEL3x3*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1116 = Coupling(name = 'GC_1116',
                   value = '-((cHL*DEL3x3*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1117 = Coupling(name = 'GC_1117',
                   value = '(cHL*DEL3x3*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1118 = Coupling(name = 'GC_1118',
                   value = '-((cHQ*DEL3x3*ee)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1119 = Coupling(name = 'GC_1119',
                   value = '-((cHQ*DEL3x3*ee*complex(0,1))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1120 = Coupling(name = 'GC_1120',
                   value = '(cHQ*DEL3x3*ee)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1121 = Coupling(name = 'GC_1121',
                   value = '-((cHud*DEL3x3*ee*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1122 = Coupling(name = 'GC_1122',
                   value = '-((cHud*DEL3x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1123 = Coupling(name = 'GC_1123',
                   value = '(cHud*DEL3x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1124 = Coupling(name = 'GC_1124',
                   value = '(2*cHud*DEL3x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1125 = Coupling(name = 'GC_1125',
                   value = '(cpHL*DEL3x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1126 = Coupling(name = 'GC_1126',
                   value = '(cHud*cw*DEL3x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1127 = Coupling(name = 'GC_1127',
                   value = '(cHud*cw*DEL3x3*ee*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1128 = Coupling(name = 'GC_1128',
                   value = '(-4*cT*ee**2)/(sw*vev**2)',
                   order = {'NP':1,'QED':4})

GC_1129 = Coupling(name = 'GC_1129',
                   value = '(4*cT*ee**2*complex(0,1))/(sw*vev**2)',
                   order = {'NP':1,'QED':4})

GC_1130 = Coupling(name = 'GC_1130',
                   value = '(4*cT*ee**2)/(sw*vev**2)',
                   order = {'NP':1,'QED':4})

GC_1131 = Coupling(name = 'GC_1131',
                   value = '-((cHQ*ee*I1a11)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1132 = Coupling(name = 'GC_1132',
                   value = '-((cHQ*ee*complex(0,1)*I1a11)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1133 = Coupling(name = 'GC_1133',
                   value = '(cHQ*ee*I1a11)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1134 = Coupling(name = 'GC_1134',
                   value = '-((cHQ*ee*I1a12)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1135 = Coupling(name = 'GC_1135',
                   value = '-((cHQ*ee*complex(0,1)*I1a12)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1136 = Coupling(name = 'GC_1136',
                   value = '(cHQ*ee*I1a12)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1137 = Coupling(name = 'GC_1137',
                   value = '-((cHQ*ee*I1a13)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1138 = Coupling(name = 'GC_1138',
                   value = '-((cHQ*ee*complex(0,1)*I1a13)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1139 = Coupling(name = 'GC_1139',
                   value = '(cHQ*ee*I1a13)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1140 = Coupling(name = 'GC_1140',
                   value = '-((cHQ*ee*I1a21)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1141 = Coupling(name = 'GC_1141',
                   value = '-((cHQ*ee*complex(0,1)*I1a21)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1142 = Coupling(name = 'GC_1142',
                   value = '(cHQ*ee*I1a21)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1143 = Coupling(name = 'GC_1143',
                   value = '-((cHQ*ee*I1a22)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1144 = Coupling(name = 'GC_1144',
                   value = '-((cHQ*ee*complex(0,1)*I1a22)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1145 = Coupling(name = 'GC_1145',
                   value = '(cHQ*ee*I1a22)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1146 = Coupling(name = 'GC_1146',
                   value = '-((cHQ*ee*I1a23)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1147 = Coupling(name = 'GC_1147',
                   value = '-((cHQ*ee*complex(0,1)*I1a23)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1148 = Coupling(name = 'GC_1148',
                   value = '(cHQ*ee*I1a23)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1149 = Coupling(name = 'GC_1149',
                   value = '-((cHQ*ee*I1a31)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1150 = Coupling(name = 'GC_1150',
                   value = '-((cHQ*ee*complex(0,1)*I1a31)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1151 = Coupling(name = 'GC_1151',
                   value = '(cHQ*ee*I1a31)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1152 = Coupling(name = 'GC_1152',
                   value = '-((cHQ*ee*I1a32)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1153 = Coupling(name = 'GC_1153',
                   value = '-((cHQ*ee*complex(0,1)*I1a32)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1154 = Coupling(name = 'GC_1154',
                   value = '(cHQ*ee*I1a32)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1155 = Coupling(name = 'GC_1155',
                   value = '-((cHQ*ee*I1a33)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1156 = Coupling(name = 'GC_1156',
                   value = '-((cHQ*ee*complex(0,1)*I1a33)/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1157 = Coupling(name = 'GC_1157',
                   value = '(cHQ*ee*I1a33)/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1158 = Coupling(name = 'GC_1158',
                   value = '(cpHQ*ee*complex(0,1)*I4a11*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1159 = Coupling(name = 'GC_1159',
                   value = '(cpHQ*ee*complex(0,1)*I4a12*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1160 = Coupling(name = 'GC_1160',
                   value = '(cpHQ*ee*complex(0,1)*I4a13*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1161 = Coupling(name = 'GC_1161',
                   value = '(cpHQ*ee*complex(0,1)*I4a21*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1162 = Coupling(name = 'GC_1162',
                   value = '(cpHQ*ee*complex(0,1)*I4a22*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1163 = Coupling(name = 'GC_1163',
                   value = '(cpHQ*ee*complex(0,1)*I4a23*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1164 = Coupling(name = 'GC_1164',
                   value = '(cpHQ*ee*complex(0,1)*I4a31*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1165 = Coupling(name = 'GC_1165',
                   value = '(cpHQ*ee*complex(0,1)*I4a32*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1166 = Coupling(name = 'GC_1166',
                   value = '(cpHQ*ee*complex(0,1)*I4a33*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1167 = Coupling(name = 'GC_1167',
                   value = '(cpHQ*ee*complex(0,1)*I7a11*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1168 = Coupling(name = 'GC_1168',
                   value = '(cpHQ*ee*complex(0,1)*I7a12*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1169 = Coupling(name = 'GC_1169',
                   value = '(cpHQ*ee*complex(0,1)*I7a13*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1170 = Coupling(name = 'GC_1170',
                   value = '(cpHQ*ee*complex(0,1)*I7a21*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1171 = Coupling(name = 'GC_1171',
                   value = '(cpHQ*ee*complex(0,1)*I7a22*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1172 = Coupling(name = 'GC_1172',
                   value = '(cpHQ*ee*complex(0,1)*I7a23*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1173 = Coupling(name = 'GC_1173',
                   value = '(cpHQ*ee*complex(0,1)*I7a31*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1174 = Coupling(name = 'GC_1174',
                   value = '(cpHQ*ee*complex(0,1)*I7a32*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1175 = Coupling(name = 'GC_1175',
                   value = '(cpHQ*ee*complex(0,1)*I7a33*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1176 = Coupling(name = 'GC_1176',
                   value = '-((cpHL*DEL1x1*ee*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1177 = Coupling(name = 'GC_1177',
                   value = '(cpHL*DEL1x1*ee*complex(0,1)*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1178 = Coupling(name = 'GC_1178',
                   value = '(cpHL*DEL1x1*ee*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1179 = Coupling(name = 'GC_1179',
                   value = '-((cpHL*DEL1x2*ee*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1180 = Coupling(name = 'GC_1180',
                   value = '(cpHL*DEL1x2*ee*complex(0,1)*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1181 = Coupling(name = 'GC_1181',
                   value = '(cpHL*DEL1x2*ee*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1182 = Coupling(name = 'GC_1182',
                   value = '-((cpHL*DEL1x3*ee*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1183 = Coupling(name = 'GC_1183',
                   value = '(cpHL*DEL1x3*ee*complex(0,1)*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1184 = Coupling(name = 'GC_1184',
                   value = '(cpHL*DEL1x3*ee*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1185 = Coupling(name = 'GC_1185',
                   value = '-((cpHL*DEL2x1*ee*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1186 = Coupling(name = 'GC_1186',
                   value = '(cpHL*DEL2x1*ee*complex(0,1)*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1187 = Coupling(name = 'GC_1187',
                   value = '(cpHL*DEL2x1*ee*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1188 = Coupling(name = 'GC_1188',
                   value = '-((cpHL*DEL2x2*ee*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1189 = Coupling(name = 'GC_1189',
                   value = '(cpHL*DEL2x2*ee*complex(0,1)*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1190 = Coupling(name = 'GC_1190',
                   value = '(cpHL*DEL2x2*ee*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1191 = Coupling(name = 'GC_1191',
                   value = '-((cpHL*DEL2x3*ee*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1192 = Coupling(name = 'GC_1192',
                   value = '(cpHL*DEL2x3*ee*complex(0,1)*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1193 = Coupling(name = 'GC_1193',
                   value = '(cpHL*DEL2x3*ee*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1194 = Coupling(name = 'GC_1194',
                   value = '-((cpHL*DEL3x1*ee*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1195 = Coupling(name = 'GC_1195',
                   value = '(cpHL*DEL3x1*ee*complex(0,1)*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1196 = Coupling(name = 'GC_1196',
                   value = '(cpHL*DEL3x1*ee*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1197 = Coupling(name = 'GC_1197',
                   value = '-((cpHL*DEL3x2*ee*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1198 = Coupling(name = 'GC_1198',
                   value = '(cpHL*DEL3x2*ee*complex(0,1)*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1199 = Coupling(name = 'GC_1199',
                   value = '(cpHL*DEL3x2*ee*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1200 = Coupling(name = 'GC_1200',
                   value = '-((cpHL*DEL3x3*ee*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1201 = Coupling(name = 'GC_1201',
                   value = '(cpHL*DEL3x3*ee*complex(0,1)*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1202 = Coupling(name = 'GC_1202',
                   value = '(cpHL*DEL3x3*ee*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1203 = Coupling(name = 'GC_1203',
                   value = '(cpHQ*ee*complex(0,1)*I4a11*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1204 = Coupling(name = 'GC_1204',
                   value = '(cpHQ*ee*I4a11*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1205 = Coupling(name = 'GC_1205',
                   value = '(cpHQ*ee*complex(0,1)*I4a12*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1206 = Coupling(name = 'GC_1206',
                   value = '(cpHQ*ee*I4a12*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1207 = Coupling(name = 'GC_1207',
                   value = '(cpHQ*ee*complex(0,1)*I4a13*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1208 = Coupling(name = 'GC_1208',
                   value = '(cpHQ*ee*I4a13*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1209 = Coupling(name = 'GC_1209',
                   value = '(cpHQ*ee*complex(0,1)*I4a21*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1210 = Coupling(name = 'GC_1210',
                   value = '(cpHQ*ee*I4a21*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1211 = Coupling(name = 'GC_1211',
                   value = '(cpHQ*ee*complex(0,1)*I4a22*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1212 = Coupling(name = 'GC_1212',
                   value = '(cpHQ*ee*I4a22*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1213 = Coupling(name = 'GC_1213',
                   value = '(cpHQ*ee*complex(0,1)*I4a23*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1214 = Coupling(name = 'GC_1214',
                   value = '(cpHQ*ee*I4a23*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1215 = Coupling(name = 'GC_1215',
                   value = '(cpHQ*ee*complex(0,1)*I4a31*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1216 = Coupling(name = 'GC_1216',
                   value = '(cpHQ*ee*I4a31*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1217 = Coupling(name = 'GC_1217',
                   value = '(cpHQ*ee*complex(0,1)*I4a32*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1218 = Coupling(name = 'GC_1218',
                   value = '(cpHQ*ee*I4a32*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1219 = Coupling(name = 'GC_1219',
                   value = '(cpHQ*ee*complex(0,1)*I4a33*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1220 = Coupling(name = 'GC_1220',
                   value = '(cpHQ*ee*I4a33*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1221 = Coupling(name = 'GC_1221',
                   value = '-((cpHQ*ee*I7a11*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1222 = Coupling(name = 'GC_1222',
                   value = '(cpHQ*ee*complex(0,1)*I7a11*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1223 = Coupling(name = 'GC_1223',
                   value = '-((cpHQ*ee*I7a12*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1224 = Coupling(name = 'GC_1224',
                   value = '(cpHQ*ee*complex(0,1)*I7a12*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1225 = Coupling(name = 'GC_1225',
                   value = '-((cpHQ*ee*I7a13*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1226 = Coupling(name = 'GC_1226',
                   value = '(cpHQ*ee*complex(0,1)*I7a13*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1227 = Coupling(name = 'GC_1227',
                   value = '-((cpHQ*ee*I7a21*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1228 = Coupling(name = 'GC_1228',
                   value = '(cpHQ*ee*complex(0,1)*I7a21*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1229 = Coupling(name = 'GC_1229',
                   value = '-((cpHQ*ee*I7a22*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1230 = Coupling(name = 'GC_1230',
                   value = '(cpHQ*ee*complex(0,1)*I7a22*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1231 = Coupling(name = 'GC_1231',
                   value = '-((cpHQ*ee*I7a23*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1232 = Coupling(name = 'GC_1232',
                   value = '(cpHQ*ee*complex(0,1)*I7a23*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1233 = Coupling(name = 'GC_1233',
                   value = '-((cpHQ*ee*I7a31*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1234 = Coupling(name = 'GC_1234',
                   value = '(cpHQ*ee*complex(0,1)*I7a31*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1235 = Coupling(name = 'GC_1235',
                   value = '-((cpHQ*ee*I7a32*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1236 = Coupling(name = 'GC_1236',
                   value = '(cpHQ*ee*complex(0,1)*I7a32*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1237 = Coupling(name = 'GC_1237',
                   value = '-((cpHQ*ee*I7a33*sw*cmath.sqrt(2))/(cw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1238 = Coupling(name = 'GC_1238',
                   value = '(cpHQ*ee*complex(0,1)*I7a33*sw*cmath.sqrt(2))/(cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1239 = Coupling(name = 'GC_1239',
                   value = '-((cH*complex(0,1))/vev)',
                   order = {'NP':1,'QED':1})

GC_1240 = Coupling(name = 'GC_1240',
                   value = '(-2*cH*complex(0,1))/vev',
                   order = {'NP':1,'QED':1})

GC_1241 = Coupling(name = 'GC_1241',
                   value = '(2*cT*complex(0,1))/vev',
                   order = {'NP':1,'QED':1})

GC_1242 = Coupling(name = 'GC_1242',
                   value = 'cT/vev',
                   order = {'NP':1,'QED':1})

GC_1243 = Coupling(name = 'GC_1243',
                   value = '(cHe*DEL1x1)/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1244 = Coupling(name = 'GC_1244',
                   value = '-((cHud*DEL1x1*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1245 = Coupling(name = 'GC_1245',
                   value = '-((cpHL*DEL1x1*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1246 = Coupling(name = 'GC_1246',
                   value = '(cHe*DEL1x2)/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1247 = Coupling(name = 'GC_1247',
                   value = '-((cHud*DEL1x2*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1248 = Coupling(name = 'GC_1248',
                   value = '-((cpHL*DEL1x2*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1249 = Coupling(name = 'GC_1249',
                   value = '(cHe*DEL1x3)/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1250 = Coupling(name = 'GC_1250',
                   value = '-((cHud*DEL1x3*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1251 = Coupling(name = 'GC_1251',
                   value = '-((cpHL*DEL1x3*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1252 = Coupling(name = 'GC_1252',
                   value = '(cHe*DEL2x1)/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1253 = Coupling(name = 'GC_1253',
                   value = '-((cHud*DEL2x1*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1254 = Coupling(name = 'GC_1254',
                   value = '-((cpHL*DEL2x1*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1255 = Coupling(name = 'GC_1255',
                   value = '(cHe*DEL2x2)/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1256 = Coupling(name = 'GC_1256',
                   value = '-((cHud*DEL2x2*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1257 = Coupling(name = 'GC_1257',
                   value = '-((cpHL*DEL2x2*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1258 = Coupling(name = 'GC_1258',
                   value = '(cHe*DEL2x3)/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1259 = Coupling(name = 'GC_1259',
                   value = '-((cHud*DEL2x3*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1260 = Coupling(name = 'GC_1260',
                   value = '-((cpHL*DEL2x3*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1261 = Coupling(name = 'GC_1261',
                   value = '(cHe*DEL3x1)/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1262 = Coupling(name = 'GC_1262',
                   value = '-((cHud*DEL3x1*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1263 = Coupling(name = 'GC_1263',
                   value = '-((cpHL*DEL3x1*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1264 = Coupling(name = 'GC_1264',
                   value = '(cHe*DEL3x2)/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1265 = Coupling(name = 'GC_1265',
                   value = '-((cHud*DEL3x2*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1266 = Coupling(name = 'GC_1266',
                   value = '-((cpHL*DEL3x2*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1267 = Coupling(name = 'GC_1267',
                   value = '(cHe*DEL3x3)/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1268 = Coupling(name = 'GC_1268',
                   value = '-((cHud*DEL3x3*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1269 = Coupling(name = 'GC_1269',
                   value = '-((cpHL*DEL3x3*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1270 = Coupling(name = 'GC_1270',
                   value = '(-2*cT*ee)/vev',
                   order = {'NP':1,'QED':2})

GC_1271 = Coupling(name = 'GC_1271',
                   value = '(cHud*DEL1x1*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1272 = Coupling(name = 'GC_1272',
                   value = '-((cpHL*DEL1x1*ee*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1273 = Coupling(name = 'GC_1273',
                   value = '(cpHL*DEL1x1*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1274 = Coupling(name = 'GC_1274',
                   value = '(cHud*DEL1x2*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1275 = Coupling(name = 'GC_1275',
                   value = '-((cpHL*DEL1x2*ee*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1276 = Coupling(name = 'GC_1276',
                   value = '(cpHL*DEL1x2*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1277 = Coupling(name = 'GC_1277',
                   value = '(cHud*DEL1x3*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1278 = Coupling(name = 'GC_1278',
                   value = '-((cpHL*DEL1x3*ee*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1279 = Coupling(name = 'GC_1279',
                   value = '(cpHL*DEL1x3*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1280 = Coupling(name = 'GC_1280',
                   value = '(cHud*DEL2x1*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1281 = Coupling(name = 'GC_1281',
                   value = '-((cpHL*DEL2x1*ee*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1282 = Coupling(name = 'GC_1282',
                   value = '(cpHL*DEL2x1*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1283 = Coupling(name = 'GC_1283',
                   value = '(cHud*DEL2x2*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1284 = Coupling(name = 'GC_1284',
                   value = '-((cpHL*DEL2x2*ee*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1285 = Coupling(name = 'GC_1285',
                   value = '(cpHL*DEL2x2*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1286 = Coupling(name = 'GC_1286',
                   value = '(cHud*DEL2x3*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1287 = Coupling(name = 'GC_1287',
                   value = '-((cpHL*DEL2x3*ee*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1288 = Coupling(name = 'GC_1288',
                   value = '(cpHL*DEL2x3*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1289 = Coupling(name = 'GC_1289',
                   value = '(cHud*DEL3x1*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1290 = Coupling(name = 'GC_1290',
                   value = '-((cpHL*DEL3x1*ee*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1291 = Coupling(name = 'GC_1291',
                   value = '(cpHL*DEL3x1*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1292 = Coupling(name = 'GC_1292',
                   value = '(cHud*DEL3x2*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1293 = Coupling(name = 'GC_1293',
                   value = '-((cpHL*DEL3x2*ee*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1294 = Coupling(name = 'GC_1294',
                   value = '(cpHL*DEL3x2*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1295 = Coupling(name = 'GC_1295',
                   value = '(cHud*DEL3x3*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1296 = Coupling(name = 'GC_1296',
                   value = '-((cpHL*DEL3x3*ee*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1297 = Coupling(name = 'GC_1297',
                   value = '(cpHL*DEL3x3*ee*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1298 = Coupling(name = 'GC_1298',
                   value = '(cd*I2a33)/vev',
                   order = {'NP':1,'QED':2})

GC_1299 = Coupling(name = 'GC_1299',
                   value = '-((cu*I3a33)/vev)',
                   order = {'NP':1,'QED':2})

GC_1300 = Coupling(name = 'GC_1300',
                   value = '-((cpHQ*I4a11*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1301 = Coupling(name = 'GC_1301',
                   value = '-((cpHQ*ee*I4a11*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1302 = Coupling(name = 'GC_1302',
                   value = '-((cpHQ*I4a12*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1303 = Coupling(name = 'GC_1303',
                   value = '-((cpHQ*ee*I4a12*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1304 = Coupling(name = 'GC_1304',
                   value = '-((cpHQ*I4a13*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1305 = Coupling(name = 'GC_1305',
                   value = '-((cpHQ*ee*I4a13*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1306 = Coupling(name = 'GC_1306',
                   value = '-((cpHQ*I4a21*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1307 = Coupling(name = 'GC_1307',
                   value = '-((cpHQ*ee*I4a21*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1308 = Coupling(name = 'GC_1308',
                   value = '-((cpHQ*I4a22*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1309 = Coupling(name = 'GC_1309',
                   value = '-((cpHQ*ee*I4a22*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1310 = Coupling(name = 'GC_1310',
                   value = '-((cpHQ*I4a23*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1311 = Coupling(name = 'GC_1311',
                   value = '-((cpHQ*ee*I4a23*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1312 = Coupling(name = 'GC_1312',
                   value = '-((cpHQ*I4a31*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1313 = Coupling(name = 'GC_1313',
                   value = '-((cpHQ*ee*I4a31*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1314 = Coupling(name = 'GC_1314',
                   value = '-((cpHQ*I4a32*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1315 = Coupling(name = 'GC_1315',
                   value = '-((cpHQ*ee*I4a32*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1316 = Coupling(name = 'GC_1316',
                   value = '-((cpHQ*I4a33*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1317 = Coupling(name = 'GC_1317',
                   value = '-((cpHQ*ee*I4a33*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1318 = Coupling(name = 'GC_1318',
                   value = '(cu*I5a33)/vev',
                   order = {'NP':1,'QED':2})

GC_1319 = Coupling(name = 'GC_1319',
                   value = '-((cd*I6a33)/vev)',
                   order = {'NP':1,'QED':2})

GC_1320 = Coupling(name = 'GC_1320',
                   value = '-((cpHQ*I7a11*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1321 = Coupling(name = 'GC_1321',
                   value = '(cpHQ*ee*I7a11*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1322 = Coupling(name = 'GC_1322',
                   value = '-((cpHQ*I7a12*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1323 = Coupling(name = 'GC_1323',
                   value = '(cpHQ*ee*I7a12*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1324 = Coupling(name = 'GC_1324',
                   value = '-((cpHQ*I7a13*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1325 = Coupling(name = 'GC_1325',
                   value = '(cpHQ*ee*I7a13*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1326 = Coupling(name = 'GC_1326',
                   value = '-((cpHQ*I7a21*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1327 = Coupling(name = 'GC_1327',
                   value = '(cpHQ*ee*I7a21*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1328 = Coupling(name = 'GC_1328',
                   value = '-((cpHQ*I7a22*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1329 = Coupling(name = 'GC_1329',
                   value = '(cpHQ*ee*I7a22*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1330 = Coupling(name = 'GC_1330',
                   value = '-((cpHQ*I7a23*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1331 = Coupling(name = 'GC_1331',
                   value = '(cpHQ*ee*I7a23*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1332 = Coupling(name = 'GC_1332',
                   value = '-((cpHQ*I7a31*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1333 = Coupling(name = 'GC_1333',
                   value = '(cpHQ*ee*I7a31*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1334 = Coupling(name = 'GC_1334',
                   value = '-((cpHQ*I7a32*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1335 = Coupling(name = 'GC_1335',
                   value = '(cpHQ*ee*I7a32*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1336 = Coupling(name = 'GC_1336',
                   value = '-((cpHQ*I7a33*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1337 = Coupling(name = 'GC_1337',
                   value = '(cpHQ*ee*I7a33*cmath.sqrt(2))/vev',
                   order = {'NP':1,'QED':2})

GC_1338 = Coupling(name = 'GC_1338',
                   value = '-((complex(0,1)*MH**2)/vev)',
                   order = {'QED':1})

GC_1339 = Coupling(name = 'GC_1339',
                   value = '(-3*complex(0,1)*MH**2)/vev',
                   order = {'QED':1})

GC_1340 = Coupling(name = 'GC_1340',
                   value = '(-4*cT*ee**2)/(sw**2*vev)',
                   order = {'NP':1,'QED':3})

GC_1341 = Coupling(name = 'GC_1341',
                   value = '(-2*cT*ee**2*complex(0,1))/(sw**2*vev)',
                   order = {'NP':1,'QED':3})

GC_1342 = Coupling(name = 'GC_1342',
                   value = '(4*cT*ee**2*complex(0,1))/(sw**2*vev)',
                   order = {'NP':1,'QED':3})

GC_1343 = Coupling(name = 'GC_1343',
                   value = '(4*cT*ee**2)/(sw**2*vev)',
                   order = {'NP':1,'QED':3})

GC_1344 = Coupling(name = 'GC_1344',
                   value = '(-2*cT*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1345 = Coupling(name = 'GC_1345',
                   value = '(-2*cT*ee*complex(0,1))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1346 = Coupling(name = 'GC_1346',
                   value = '(2*cT*ee*complex(0,1))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1347 = Coupling(name = 'GC_1347',
                   value = '(cT*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1348 = Coupling(name = 'GC_1348',
                   value = '-(cHe*DEL1x1*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1349 = Coupling(name = 'GC_1349',
                   value = '(cHe*DEL1x1*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1350 = Coupling(name = 'GC_1350',
                   value = '-((cHL*DEL1x1*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1351 = Coupling(name = 'GC_1351',
                   value = '(cHL*DEL1x1*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1352 = Coupling(name = 'GC_1352',
                   value = '-((cHQ*DEL1x1*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1353 = Coupling(name = 'GC_1353',
                   value = '(cHQ*DEL1x1*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1354 = Coupling(name = 'GC_1354',
                   value = '-((cHud*DEL1x1*ee*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1355 = Coupling(name = 'GC_1355',
                   value = '(cHud*DEL1x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1356 = Coupling(name = 'GC_1356',
                   value = '(cpHL*DEL1x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1357 = Coupling(name = 'GC_1357',
                   value = '(cHud*cw*DEL1x1*ee*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1358 = Coupling(name = 'GC_1358',
                   value = '-(cHe*DEL1x2*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1359 = Coupling(name = 'GC_1359',
                   value = '(cHe*DEL1x2*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1360 = Coupling(name = 'GC_1360',
                   value = '-((cHL*DEL1x2*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1361 = Coupling(name = 'GC_1361',
                   value = '(cHL*DEL1x2*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1362 = Coupling(name = 'GC_1362',
                   value = '-((cHQ*DEL1x2*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1363 = Coupling(name = 'GC_1363',
                   value = '(cHQ*DEL1x2*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1364 = Coupling(name = 'GC_1364',
                   value = '-((cHud*DEL1x2*ee*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1365 = Coupling(name = 'GC_1365',
                   value = '(cHud*DEL1x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1366 = Coupling(name = 'GC_1366',
                   value = '(cpHL*DEL1x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1367 = Coupling(name = 'GC_1367',
                   value = '(cHud*cw*DEL1x2*ee*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1368 = Coupling(name = 'GC_1368',
                   value = '-(cHe*DEL1x3*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1369 = Coupling(name = 'GC_1369',
                   value = '(cHe*DEL1x3*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1370 = Coupling(name = 'GC_1370',
                   value = '-((cHL*DEL1x3*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1371 = Coupling(name = 'GC_1371',
                   value = '(cHL*DEL1x3*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1372 = Coupling(name = 'GC_1372',
                   value = '-((cHQ*DEL1x3*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1373 = Coupling(name = 'GC_1373',
                   value = '(cHQ*DEL1x3*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1374 = Coupling(name = 'GC_1374',
                   value = '-((cHud*DEL1x3*ee*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1375 = Coupling(name = 'GC_1375',
                   value = '(cHud*DEL1x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1376 = Coupling(name = 'GC_1376',
                   value = '(cpHL*DEL1x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1377 = Coupling(name = 'GC_1377',
                   value = '(cHud*cw*DEL1x3*ee*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1378 = Coupling(name = 'GC_1378',
                   value = '-(cHe*DEL2x1*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1379 = Coupling(name = 'GC_1379',
                   value = '(cHe*DEL2x1*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1380 = Coupling(name = 'GC_1380',
                   value = '-((cHL*DEL2x1*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1381 = Coupling(name = 'GC_1381',
                   value = '(cHL*DEL2x1*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1382 = Coupling(name = 'GC_1382',
                   value = '-((cHQ*DEL2x1*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1383 = Coupling(name = 'GC_1383',
                   value = '(cHQ*DEL2x1*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1384 = Coupling(name = 'GC_1384',
                   value = '-((cHud*DEL2x1*ee*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1385 = Coupling(name = 'GC_1385',
                   value = '(cHud*DEL2x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1386 = Coupling(name = 'GC_1386',
                   value = '(cpHL*DEL2x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1387 = Coupling(name = 'GC_1387',
                   value = '(cHud*cw*DEL2x1*ee*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1388 = Coupling(name = 'GC_1388',
                   value = '-(cHe*DEL2x2*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1389 = Coupling(name = 'GC_1389',
                   value = '(cHe*DEL2x2*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1390 = Coupling(name = 'GC_1390',
                   value = '-((cHL*DEL2x2*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1391 = Coupling(name = 'GC_1391',
                   value = '(cHL*DEL2x2*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1392 = Coupling(name = 'GC_1392',
                   value = '-((cHQ*DEL2x2*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1393 = Coupling(name = 'GC_1393',
                   value = '(cHQ*DEL2x2*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1394 = Coupling(name = 'GC_1394',
                   value = '-((cHud*DEL2x2*ee*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1395 = Coupling(name = 'GC_1395',
                   value = '(cHud*DEL2x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1396 = Coupling(name = 'GC_1396',
                   value = '(cpHL*DEL2x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1397 = Coupling(name = 'GC_1397',
                   value = '(cHud*cw*DEL2x2*ee*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1398 = Coupling(name = 'GC_1398',
                   value = '-(cHe*DEL2x3*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1399 = Coupling(name = 'GC_1399',
                   value = '(cHe*DEL2x3*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1400 = Coupling(name = 'GC_1400',
                   value = '-((cHL*DEL2x3*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1401 = Coupling(name = 'GC_1401',
                   value = '(cHL*DEL2x3*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1402 = Coupling(name = 'GC_1402',
                   value = '-((cHQ*DEL2x3*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1403 = Coupling(name = 'GC_1403',
                   value = '(cHQ*DEL2x3*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1404 = Coupling(name = 'GC_1404',
                   value = '-((cHud*DEL2x3*ee*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1405 = Coupling(name = 'GC_1405',
                   value = '(cHud*DEL2x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1406 = Coupling(name = 'GC_1406',
                   value = '(cpHL*DEL2x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1407 = Coupling(name = 'GC_1407',
                   value = '(cHud*cw*DEL2x3*ee*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1408 = Coupling(name = 'GC_1408',
                   value = '-(cHe*DEL3x1*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1409 = Coupling(name = 'GC_1409',
                   value = '(cHe*DEL3x1*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1410 = Coupling(name = 'GC_1410',
                   value = '-((cHL*DEL3x1*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1411 = Coupling(name = 'GC_1411',
                   value = '(cHL*DEL3x1*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1412 = Coupling(name = 'GC_1412',
                   value = '-((cHQ*DEL3x1*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1413 = Coupling(name = 'GC_1413',
                   value = '(cHQ*DEL3x1*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1414 = Coupling(name = 'GC_1414',
                   value = '-((cHud*DEL3x1*ee*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1415 = Coupling(name = 'GC_1415',
                   value = '(cHud*DEL3x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1416 = Coupling(name = 'GC_1416',
                   value = '(cpHL*DEL3x1*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1417 = Coupling(name = 'GC_1417',
                   value = '(cHud*cw*DEL3x1*ee*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1418 = Coupling(name = 'GC_1418',
                   value = '-(cHe*DEL3x2*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1419 = Coupling(name = 'GC_1419',
                   value = '(cHe*DEL3x2*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1420 = Coupling(name = 'GC_1420',
                   value = '-((cHL*DEL3x2*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1421 = Coupling(name = 'GC_1421',
                   value = '(cHL*DEL3x2*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1422 = Coupling(name = 'GC_1422',
                   value = '-((cHQ*DEL3x2*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1423 = Coupling(name = 'GC_1423',
                   value = '(cHQ*DEL3x2*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1424 = Coupling(name = 'GC_1424',
                   value = '-((cHud*DEL3x2*ee*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1425 = Coupling(name = 'GC_1425',
                   value = '(cHud*DEL3x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1426 = Coupling(name = 'GC_1426',
                   value = '(cpHL*DEL3x2*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1427 = Coupling(name = 'GC_1427',
                   value = '(cHud*cw*DEL3x2*ee*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1428 = Coupling(name = 'GC_1428',
                   value = '-(cHe*DEL3x3*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1429 = Coupling(name = 'GC_1429',
                   value = '(cHe*DEL3x3*ee)/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1430 = Coupling(name = 'GC_1430',
                   value = '-((cHL*DEL3x3*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1431 = Coupling(name = 'GC_1431',
                   value = '(cHL*DEL3x3*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1432 = Coupling(name = 'GC_1432',
                   value = '-((cHQ*DEL3x3*ee)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1433 = Coupling(name = 'GC_1433',
                   value = '(cHQ*DEL3x3*ee)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1434 = Coupling(name = 'GC_1434',
                   value = '-((cHud*DEL3x3*ee*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1435 = Coupling(name = 'GC_1435',
                   value = '(cHud*DEL3x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1436 = Coupling(name = 'GC_1436',
                   value = '(cpHL*DEL3x3*ee*complex(0,1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1437 = Coupling(name = 'GC_1437',
                   value = '(cHud*cw*DEL3x3*ee*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1438 = Coupling(name = 'GC_1438',
                   value = '(-4*cT*ee**2)/(sw*vev)',
                   order = {'NP':1,'QED':3})

GC_1439 = Coupling(name = 'GC_1439',
                   value = '(4*cT*ee**2)/(sw*vev)',
                   order = {'NP':1,'QED':3})

GC_1440 = Coupling(name = 'GC_1440',
                   value = '-((cHQ*ee*I1a11)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1441 = Coupling(name = 'GC_1441',
                   value = '(cHQ*ee*I1a11)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1442 = Coupling(name = 'GC_1442',
                   value = '-((cHQ*ee*I1a12)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1443 = Coupling(name = 'GC_1443',
                   value = '(cHQ*ee*I1a12)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1444 = Coupling(name = 'GC_1444',
                   value = '-((cHQ*ee*I1a13)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1445 = Coupling(name = 'GC_1445',
                   value = '(cHQ*ee*I1a13)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1446 = Coupling(name = 'GC_1446',
                   value = '-((cHQ*ee*I1a21)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1447 = Coupling(name = 'GC_1447',
                   value = '(cHQ*ee*I1a21)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1448 = Coupling(name = 'GC_1448',
                   value = '-((cHQ*ee*I1a22)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1449 = Coupling(name = 'GC_1449',
                   value = '(cHQ*ee*I1a22)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1450 = Coupling(name = 'GC_1450',
                   value = '-((cHQ*ee*I1a23)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1451 = Coupling(name = 'GC_1451',
                   value = '(cHQ*ee*I1a23)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1452 = Coupling(name = 'GC_1452',
                   value = '-((cHQ*ee*I1a31)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1453 = Coupling(name = 'GC_1453',
                   value = '(cHQ*ee*I1a31)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1454 = Coupling(name = 'GC_1454',
                   value = '-((cHQ*ee*I1a32)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1455 = Coupling(name = 'GC_1455',
                   value = '(cHQ*ee*I1a32)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1456 = Coupling(name = 'GC_1456',
                   value = '-((cHQ*ee*I1a33)/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1457 = Coupling(name = 'GC_1457',
                   value = '(cHQ*ee*I1a33)/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1458 = Coupling(name = 'GC_1458',
                   value = '(cpHQ*ee*complex(0,1)*I4a11*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1459 = Coupling(name = 'GC_1459',
                   value = '(cpHQ*ee*complex(0,1)*I4a12*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1460 = Coupling(name = 'GC_1460',
                   value = '(cpHQ*ee*complex(0,1)*I4a13*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1461 = Coupling(name = 'GC_1461',
                   value = '(cpHQ*ee*complex(0,1)*I4a21*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1462 = Coupling(name = 'GC_1462',
                   value = '(cpHQ*ee*complex(0,1)*I4a22*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1463 = Coupling(name = 'GC_1463',
                   value = '(cpHQ*ee*complex(0,1)*I4a23*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1464 = Coupling(name = 'GC_1464',
                   value = '(cpHQ*ee*complex(0,1)*I4a31*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1465 = Coupling(name = 'GC_1465',
                   value = '(cpHQ*ee*complex(0,1)*I4a32*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1466 = Coupling(name = 'GC_1466',
                   value = '(cpHQ*ee*complex(0,1)*I4a33*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1467 = Coupling(name = 'GC_1467',
                   value = '(cpHQ*ee*complex(0,1)*I7a11*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1468 = Coupling(name = 'GC_1468',
                   value = '(cpHQ*ee*complex(0,1)*I7a12*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1469 = Coupling(name = 'GC_1469',
                   value = '(cpHQ*ee*complex(0,1)*I7a13*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1470 = Coupling(name = 'GC_1470',
                   value = '(cpHQ*ee*complex(0,1)*I7a21*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1471 = Coupling(name = 'GC_1471',
                   value = '(cpHQ*ee*complex(0,1)*I7a22*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1472 = Coupling(name = 'GC_1472',
                   value = '(cpHQ*ee*complex(0,1)*I7a23*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1473 = Coupling(name = 'GC_1473',
                   value = '(cpHQ*ee*complex(0,1)*I7a31*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1474 = Coupling(name = 'GC_1474',
                   value = '(cpHQ*ee*complex(0,1)*I7a32*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1475 = Coupling(name = 'GC_1475',
                   value = '(cpHQ*ee*complex(0,1)*I7a33*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1476 = Coupling(name = 'GC_1476',
                   value = '-((cpHL*DEL1x1*ee*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1477 = Coupling(name = 'GC_1477',
                   value = '(cpHL*DEL1x1*ee*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1478 = Coupling(name = 'GC_1478',
                   value = '-((cpHL*DEL1x2*ee*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1479 = Coupling(name = 'GC_1479',
                   value = '(cpHL*DEL1x2*ee*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1480 = Coupling(name = 'GC_1480',
                   value = '-((cpHL*DEL1x3*ee*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1481 = Coupling(name = 'GC_1481',
                   value = '(cpHL*DEL1x3*ee*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1482 = Coupling(name = 'GC_1482',
                   value = '-((cpHL*DEL2x1*ee*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1483 = Coupling(name = 'GC_1483',
                   value = '(cpHL*DEL2x1*ee*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1484 = Coupling(name = 'GC_1484',
                   value = '-((cpHL*DEL2x2*ee*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1485 = Coupling(name = 'GC_1485',
                   value = '(cpHL*DEL2x2*ee*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1486 = Coupling(name = 'GC_1486',
                   value = '-((cpHL*DEL2x3*ee*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1487 = Coupling(name = 'GC_1487',
                   value = '(cpHL*DEL2x3*ee*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1488 = Coupling(name = 'GC_1488',
                   value = '-((cpHL*DEL3x1*ee*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1489 = Coupling(name = 'GC_1489',
                   value = '(cpHL*DEL3x1*ee*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1490 = Coupling(name = 'GC_1490',
                   value = '-((cpHL*DEL3x2*ee*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1491 = Coupling(name = 'GC_1491',
                   value = '(cpHL*DEL3x2*ee*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1492 = Coupling(name = 'GC_1492',
                   value = '-((cpHL*DEL3x3*ee*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1493 = Coupling(name = 'GC_1493',
                   value = '(cpHL*DEL3x3*ee*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1494 = Coupling(name = 'GC_1494',
                   value = '(cpHQ*ee*I4a11*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1495 = Coupling(name = 'GC_1495',
                   value = '(cpHQ*ee*I4a12*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1496 = Coupling(name = 'GC_1496',
                   value = '(cpHQ*ee*I4a13*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1497 = Coupling(name = 'GC_1497',
                   value = '(cpHQ*ee*I4a21*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1498 = Coupling(name = 'GC_1498',
                   value = '(cpHQ*ee*I4a22*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1499 = Coupling(name = 'GC_1499',
                   value = '(cpHQ*ee*I4a23*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1500 = Coupling(name = 'GC_1500',
                   value = '(cpHQ*ee*I4a31*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1501 = Coupling(name = 'GC_1501',
                   value = '(cpHQ*ee*I4a32*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1502 = Coupling(name = 'GC_1502',
                   value = '(cpHQ*ee*I4a33*sw*cmath.sqrt(2))/(cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1503 = Coupling(name = 'GC_1503',
                   value = '-((cpHQ*ee*I7a11*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1504 = Coupling(name = 'GC_1504',
                   value = '-((cpHQ*ee*I7a12*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1505 = Coupling(name = 'GC_1505',
                   value = '-((cpHQ*ee*I7a13*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1506 = Coupling(name = 'GC_1506',
                   value = '-((cpHQ*ee*I7a21*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1507 = Coupling(name = 'GC_1507',
                   value = '-((cpHQ*ee*I7a22*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1508 = Coupling(name = 'GC_1508',
                   value = '-((cpHQ*ee*I7a23*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1509 = Coupling(name = 'GC_1509',
                   value = '-((cpHQ*ee*I7a31*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1510 = Coupling(name = 'GC_1510',
                   value = '-((cpHQ*ee*I7a32*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1511 = Coupling(name = 'GC_1511',
                   value = '-((cpHQ*ee*I7a33*sw*cmath.sqrt(2))/(cw*vev))',
                   order = {'NP':1,'QED':2})

GC_1512 = Coupling(name = 'GC_1512',
                   value = '-(ee**2*vev)/(2.*cw)',
                   order = {'QED':1})

GC_1513 = Coupling(name = 'GC_1513',
                   value = '(ee**2*vev)/(2.*cw)',
                   order = {'QED':1})

GC_1514 = Coupling(name = 'GC_1514',
                   value = '(4*cA*ee**2*complex(0,1)*vev)/MW**2',
                   order = {'NP':1,'QED':1})

GC_1515 = Coupling(name = 'GC_1515',
                   value = '-(cB*ee**2*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1516 = Coupling(name = 'GC_1516',
                   value = '(cB*ee**2*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1517 = Coupling(name = 'GC_1517',
                   value = '-(cHB*ee**2*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1518 = Coupling(name = 'GC_1518',
                   value = '(cHB*ee**2*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1519 = Coupling(name = 'GC_1519',
                   value = '-(cHW*ee**2*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1520 = Coupling(name = 'GC_1520',
                   value = '(cHW*ee**2*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1521 = Coupling(name = 'GC_1521',
                   value = '-(cWW*ee**2*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1522 = Coupling(name = 'GC_1522',
                   value = '(cWW*ee**2*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1523 = Coupling(name = 'GC_1523',
                   value = '(cHB*ee**3*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1524 = Coupling(name = 'GC_1524',
                   value = '-(cHW*ee**3*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1525 = Coupling(name = 'GC_1525',
                   value = '-(cWW*ee**3*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1526 = Coupling(name = 'GC_1526',
                   value = '(4*cG*dum**2*complex(0,1)*G**2*vev)/MW**2',
                   order = {'NP':1,'QCD':2,'QED':1})

GC_1527 = Coupling(name = 'GC_1527',
                   value = '(4*cG*dum**2*G**3*vev)/MW**2',
                   order = {'NP':1,'QCD':3,'QED':1})

GC_1528 = Coupling(name = 'GC_1528',
                   value = '(-4*cG*dum**2*complex(0,1)*G**4*vev)/MW**2',
                   order = {'NP':1,'QCD':4,'QED':1})

GC_1529 = Coupling(name = 'GC_1529',
                   value = '-(ee**2*vev)/(4.*sw**2)',
                   order = {'QED':1})

GC_1530 = Coupling(name = 'GC_1530',
                   value = '-(ee**2*complex(0,1)*vev)/(4.*sw**2)',
                   order = {'QED':1})

GC_1531 = Coupling(name = 'GC_1531',
                   value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                   order = {'QED':1})

GC_1532 = Coupling(name = 'GC_1532',
                   value = '(ee**2*vev)/(4.*sw**2)',
                   order = {'QED':1})

GC_1533 = Coupling(name = 'GC_1533',
                   value = '(cH*ee**2*complex(0,1)*vev)/(8.*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1534 = Coupling(name = 'GC_1534',
                   value = '-(cH*ee**2*complex(0,1)*vev)/(4.*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1535 = Coupling(name = 'GC_1535',
                   value = '-(cHW*ee**2*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1536 = Coupling(name = 'GC_1536',
                   value = '(cHW*ee**2*complex(0,1)*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1537 = Coupling(name = 'GC_1537',
                   value = '-(cHW*cw*ee**2*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1538 = Coupling(name = 'GC_1538',
                   value = '(cHW*cw*ee**2*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1539 = Coupling(name = 'GC_1539',
                   value = '-((cWW*ee**2*vev)/(MW**2*sw**2))',
                   order = {'NP':1,'QED':1})

GC_1540 = Coupling(name = 'GC_1540',
                   value = '-(cWW*ee**2*complex(0,1)*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1541 = Coupling(name = 'GC_1541',
                   value = '-((cw*cWW*ee**2*vev)/(MW**2*sw**2))',
                   order = {'NP':1,'QED':1})

GC_1542 = Coupling(name = 'GC_1542',
                   value = '(cw*cWW*ee**2*vev)/(MW**2*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1543 = Coupling(name = 'GC_1543',
                   value = '-(cHB*ee**3*complex(0,1)*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1544 = Coupling(name = 'GC_1544',
                   value = '-(cHW*ee**3*complex(0,1)*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1545 = Coupling(name = 'GC_1545',
                   value = '(cHB*cw*ee**3*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1546 = Coupling(name = 'GC_1546',
                   value = '(cHW*cw*ee**3*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1547 = Coupling(name = 'GC_1547',
                   value = '(-3*cWW*ee**3*complex(0,1)*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1548 = Coupling(name = 'GC_1548',
                   value = '(cw*cWW*ee**3*vev)/(MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1549 = Coupling(name = 'GC_1549',
                   value = '-((cWW*ee**4*complex(0,1)*vev)/(MW**2*sw**2))',
                   order = {'NP':1,'QED':3})

GC_1550 = Coupling(name = 'GC_1550',
                   value = '(2*cdW*cw*ee**2*complex(0,1)*I2a33*vev)/(MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1551 = Coupling(name = 'GC_1551',
                   value = '(2*cuW*cw*ee**2*complex(0,1)*I3a33*vev)/(MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1552 = Coupling(name = 'GC_1552',
                   value = '(-2*cuW*cw*ee**2*complex(0,1)*I5a33*vev)/(MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1553 = Coupling(name = 'GC_1553',
                   value = '(-2*cdW*cw*ee**2*complex(0,1)*I6a33*vev)/(MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1554 = Coupling(name = 'GC_1554',
                   value = '-(ee**2*vev)/(2.*sw)',
                   order = {'QED':1})

GC_1555 = Coupling(name = 'GC_1555',
                   value = '(ee**2*vev)/(2.*sw)',
                   order = {'QED':1})

GC_1556 = Coupling(name = 'GC_1556',
                   value = '-(cB*ee**2*vev)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1557 = Coupling(name = 'GC_1557',
                   value = '(cB*ee**2*vev)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1558 = Coupling(name = 'GC_1558',
                   value = '-(cWW*ee**2*vev)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1559 = Coupling(name = 'GC_1559',
                   value = '(cWW*ee**2*vev)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1560 = Coupling(name = 'GC_1560',
                   value = '-(cHB*ee**3*vev)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1561 = Coupling(name = 'GC_1561',
                   value = '-(cHW*ee**3*vev)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1562 = Coupling(name = 'GC_1562',
                   value = '(cHB*ee**3*complex(0,1)*vev)/(2.*cw*MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1563 = Coupling(name = 'GC_1563',
                   value = '-(cHW*ee**3*complex(0,1)*vev)/(2.*cw*MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1564 = Coupling(name = 'GC_1564',
                   value = '-((cWW*ee**3*vev)/(MW**2*sw))',
                   order = {'NP':1,'QED':2})

GC_1565 = Coupling(name = 'GC_1565',
                   value = '-(cWW*ee**3*vev)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1566 = Coupling(name = 'GC_1566',
                   value = '-(cWW*ee**3*complex(0,1)*vev)/(2.*cw*MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1567 = Coupling(name = 'GC_1567',
                   value = '(-2*cdW*ee*complex(0,1)*I2a33*vev)/(MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1568 = Coupling(name = 'GC_1568',
                   value = '(-2*cdW*ee**2*complex(0,1)*I2a33*vev)/(MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1569 = Coupling(name = 'GC_1569',
                   value = '(-2*cuW*ee*complex(0,1)*I3a33*vev)/(MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1570 = Coupling(name = 'GC_1570',
                   value = '(-2*cuW*ee**2*complex(0,1)*I3a33*vev)/(MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1571 = Coupling(name = 'GC_1571',
                   value = '(-2*cuW*ee*complex(0,1)*I5a33*vev)/(MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1572 = Coupling(name = 'GC_1572',
                   value = '(2*cuW*ee**2*complex(0,1)*I5a33*vev)/(MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1573 = Coupling(name = 'GC_1573',
                   value = '(-2*cdW*ee*complex(0,1)*I6a33*vev)/(MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1574 = Coupling(name = 'GC_1574',
                   value = '(2*cdW*ee**2*complex(0,1)*I6a33*vev)/(MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1575 = Coupling(name = 'GC_1575',
                   value = '(-4*cA*ee**2*complex(0,1)*sw*vev)/(cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1576 = Coupling(name = 'GC_1576',
                   value = '(4*cA*ee**2*complex(0,1)*sw**2*vev)/(cw**2*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1577 = Coupling(name = 'GC_1577',
                   value = '(-2*ee**2*complex(0,1)*tcA*vev)/MW**2',
                   order = {'NP':1,'QED':1})

GC_1578 = Coupling(name = 'GC_1578',
                   value = '(-4*ee**2*complex(0,1)*sw*tcA*vev)/(cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1579 = Coupling(name = 'GC_1579',
                   value = '(-2*ee**2*complex(0,1)*sw**2*tcA*vev)/(cw**2*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1580 = Coupling(name = 'GC_1580',
                   value = '(-2*dum**2*complex(0,1)*G**2*tcG*vev)/MW**2',
                   order = {'NP':1,'QCD':2,'QED':1})

GC_1581 = Coupling(name = 'GC_1581',
                   value = '(-4*dum**2*G**3*tcG*vev)/MW**2',
                   order = {'NP':1,'QCD':3,'QED':1})

GC_1582 = Coupling(name = 'GC_1582',
                   value = '-(ee**2*tcHB*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1583 = Coupling(name = 'GC_1583',
                   value = '(ee**2*tcHB*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1584 = Coupling(name = 'GC_1584',
                   value = '-(ee**3*tcHB*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1585 = Coupling(name = 'GC_1585',
                   value = '(ee**3*complex(0,1)*tcHB*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1586 = Coupling(name = 'GC_1586',
                   value = '-(cw*ee**3*tcHB*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1587 = Coupling(name = 'GC_1587',
                   value = '-(ee**3*complex(0,1)*tcHB*vev)/(2.*cw*MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1588 = Coupling(name = 'GC_1588',
                   value = '-(ee**2*tcHW*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1589 = Coupling(name = 'GC_1589',
                   value = '(ee**2*tcHW*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1590 = Coupling(name = 'GC_1590',
                   value = '(ee**3*tcHW*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1591 = Coupling(name = 'GC_1591',
                   value = '(cw*ee**3*complex(0,1)*tcHW*vev)/(2.*MW**2*sw**3)',
                   order = {'NP':1,'QED':2})

GC_1592 = Coupling(name = 'GC_1592',
                   value = '-(ee**2*complex(0,1)*tcHW*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1593 = Coupling(name = 'GC_1593',
                   value = '(ee**2*tcHW*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1594 = Coupling(name = 'GC_1594',
                   value = '-(cw*ee**2*tcHW*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1595 = Coupling(name = 'GC_1595',
                   value = '(cw*ee**2*tcHW*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1596 = Coupling(name = 'GC_1596',
                   value = '(ee**3*complex(0,1)*tcHW*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1597 = Coupling(name = 'GC_1597',
                   value = '(cw*ee**3*tcHW*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1598 = Coupling(name = 'GC_1598',
                   value = '(ee**3*complex(0,1)*tcHW*vev)/(2.*cw*MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1599 = Coupling(name = 'GC_1599',
                   value = '-(cA*ee**3*complex(0,1)*vev**2)/(3.*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1600 = Coupling(name = 'GC_1600',
                   value = '(2*cA*ee**3*complex(0,1)*vev**2)/(3.*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1601 = Coupling(name = 'GC_1601',
                   value = '-((cA*ee**3*complex(0,1)*vev**2)/MW**2)',
                   order = {'NP':1,'QED':1})

GC_1602 = Coupling(name = 'GC_1602',
                   value = '(cA*ee**3*complex(0,1)*vev**2)/MW**2',
                   order = {'NP':1,'QED':1})

GC_1603 = Coupling(name = 'GC_1603',
                   value = '(4*cA*ee**4*complex(0,1)*vev**2)/MW**2',
                   order = {'NP':1,'QED':2})

GC_1604 = Coupling(name = 'GC_1604',
                   value = '-((cG*dum**2*G**3*vev**2)/MW**2)',
                   order = {'NP':1,'QCD':3})

GC_1605 = Coupling(name = 'GC_1605',
                   value = '(cG*dum**2*complex(0,1)*G**3*vev**2)/MW**2',
                   order = {'NP':1,'QCD':3})

GC_1606 = Coupling(name = 'GC_1606',
                   value = '(2*cG*dum**2*complex(0,1)*G**4*vev**2)/MW**2',
                   order = {'NP':1,'QCD':4})

GC_1607 = Coupling(name = 'GC_1607',
                   value = '(-3*cWW*ee**3*complex(0,1)*vev**2)/(4.*MW**2*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1608 = Coupling(name = 'GC_1608',
                   value = '(cHB*ee**3*complex(0,1)*vev**2)/(4.*cw*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1609 = Coupling(name = 'GC_1609',
                   value = '-(cHW*ee**3*complex(0,1)*vev**2)/(4.*cw*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1610 = Coupling(name = 'GC_1610',
                   value = '-(cWW*ee**3*complex(0,1)*vev**2)/(4.*cw*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1611 = Coupling(name = 'GC_1611',
                   value = '-(cA*ee**4*complex(0,1)*vev**2)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1612 = Coupling(name = 'GC_1612',
                   value = '-(cA*ee**3*complex(0,1)*sw*vev**2)/(6.*cw**3*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1613 = Coupling(name = 'GC_1613',
                   value = '(cA*ee**3*complex(0,1)*sw*vev**2)/(2.*cw**3*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1614 = Coupling(name = 'GC_1614',
                   value = '(5*cA*ee**3*complex(0,1)*sw*vev**2)/(6.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1615 = Coupling(name = 'GC_1615',
                   value = '(-7*cA*ee**3*complex(0,1)*sw*vev**2)/(6.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1616 = Coupling(name = 'GC_1616',
                   value = '(3*cA*ee**3*complex(0,1)*sw*vev**2)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1617 = Coupling(name = 'GC_1617',
                   value = '(-2*dum**2*G**3*tcG*vev**2)/MW**2',
                   order = {'NP':1,'QCD':3})

GC_1618 = Coupling(name = 'GC_1618',
                   value = '-(ee**3*complex(0,1)*tcHB*vev**2)/(4.*cw*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1619 = Coupling(name = 'GC_1619',
                   value = '(cw*ee**3*complex(0,1)*tcHW*vev**2)/(4.*MW**2*sw**3)',
                   order = {'NP':1,'QED':1})

GC_1620 = Coupling(name = 'GC_1620',
                   value = '(ee**3*complex(0,1)*tcHW*vev**2)/(4.*cw*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1621 = Coupling(name = 'GC_1621',
                   value = '-(cA*ee**4*vev**3)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1622 = Coupling(name = 'GC_1622',
                   value = '(cA*ee**4*vev**3)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1623 = Coupling(name = 'GC_1623',
                   value = '(-2*c2G*cG**6*dum**12*complex(0,1)*G**16*vev**12)/MW**14',
                   order = {'NP':7,'QCD':16})

GC_1624 = Coupling(name = 'GC_1624',
                   value = '(2*c2G*cG**6*dum**12*complex(0,1)*G**16*vev**12)/MW**14',
                   order = {'NP':7,'QCD':16})

GC_1625 = Coupling(name = 'GC_1625',
                   value = '-((c3G*cG**6*dum**12*complex(0,1)*G**18*vev**12)/MW**14)',
                   order = {'NP':7,'QCD':18})

GC_1626 = Coupling(name = 'GC_1626',
                   value = '(c3G*cG**6*dum**12*complex(0,1)*G**18*vev**12)/MW**14',
                   order = {'NP':7,'QCD':18})

GC_1627 = Coupling(name = 'GC_1627',
                   value = '-((cG**6*dum**12*complex(0,1)*G**18*tc3G*vev**12)/MW**14)',
                   order = {'NP':7,'QCD':18})

GC_1628 = Coupling(name = 'GC_1628',
                   value = '(cG**6*dum**12*complex(0,1)*G**18*tc3G*vev**12)/MW**14',
                   order = {'NP':7,'QCD':18})

GC_1629 = Coupling(name = 'GC_1629',
                   value = '(cHW*ee**4*complex(0,1)*vev)/(MW**2*sw**4) + (2*cWW*ee**4*complex(0,1)*vev)/(MW**2*sw**4)',
                   order = {'NP':1,'QED':3})

GC_1630 = Coupling(name = 'GC_1630',
                   value = '-(cHW*ee**3*vev)/(2.*MW**2*sw**3) - (cWW*ee**3*vev)/(2.*MW**2*sw**3)',
                   order = {'NP':1,'QED':2})

GC_1631 = Coupling(name = 'GC_1631',
                   value = '(cHW*ee**3*vev)/(MW**2*sw**3) + (cWW*ee**3*vev)/(MW**2*sw**3)',
                   order = {'NP':1,'QED':2})

GC_1632 = Coupling(name = 'GC_1632',
                   value = '-((cHW*cw*ee**3*vev)/(MW**2*sw**3)) - (cw*cWW*ee**3*vev)/(MW**2*sw**3)',
                   order = {'NP':1,'QED':2})

GC_1633 = Coupling(name = 'GC_1633',
                   value = '-(cHW*cw*ee**3*complex(0,1)*vev)/(2.*MW**2*sw**3) - (3*cw*cWW*ee**3*complex(0,1)*vev)/(2.*MW**2*sw**3)',
                   order = {'NP':1,'QED':2})

GC_1634 = Coupling(name = 'GC_1634',
                   value = '(cHW*cw**2*ee**3*vev)/(2.*MW**2*sw**3) + (cw**2*cWW*ee**3*vev)/(2.*MW**2*sw**3)',
                   order = {'NP':1,'QED':2})

GC_1635 = Coupling(name = 'GC_1635',
                   value = '(cHW*ee**4*vev)/(2.*MW**2*sw**3) + (cWW*ee**4*vev)/(2.*MW**2*sw**3)',
                   order = {'NP':1,'QED':3})

GC_1636 = Coupling(name = 'GC_1636',
                   value = '(cHW*ee**4*vev)/(MW**2*sw**3) + (cWW*ee**4*vev)/(MW**2*sw**3)',
                   order = {'NP':1,'QED':3})

GC_1637 = Coupling(name = 'GC_1637',
                   value = '-(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                   order = {'QED':1})

GC_1638 = Coupling(name = 'GC_1638',
                   value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                   order = {'QED':1})

GC_1639 = Coupling(name = 'GC_1639',
                   value = '-(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                   order = {'QED':1})

GC_1640 = Coupling(name = 'GC_1640',
                   value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                   order = {'QED':1})

GC_1641 = Coupling(name = 'GC_1641',
                   value = '(cHW*ee**3*vev)/(2.*MW**2*sw**2) + (cWW*ee**3*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1642 = Coupling(name = 'GC_1642',
                   value = '-((cHW*cw**2*ee**4*complex(0,1)*vev)/(MW**2*sw**4)) - (2*cw**2*cWW*ee**4*complex(0,1)*vev)/(MW**2*sw**4) - (cHW*ee**4*complex(0,1)*vev)/(MW**2*sw**2) - (cWW*ee**4*complex(0,1)*vev)/(MW**2*sw**2)',
                   order = {'NP':1,'QED':3})

GC_1643 = Coupling(name = 'GC_1643',
                   value = '(cHW*ee**4*vev)/(2.*cw*MW**2*sw**2) + (cWW*ee**4*vev)/(2.*cw*MW**2*sw**2)',
                   order = {'NP':1,'QED':3})

GC_1644 = Coupling(name = 'GC_1644',
                   value = '(cHW*ee**4*vev)/(cw*MW**2*sw**2) + (cWW*ee**4*vev)/(cw*MW**2*sw**2)',
                   order = {'NP':1,'QED':3})

GC_1645 = Coupling(name = 'GC_1645',
                   value = '-(cHW*ee**4*vev)/(2.*cw*MW**2) - (cWW*ee**4*vev)/(2.*cw*MW**2) - (cHW*cw*ee**4*vev)/(2.*MW**2*sw**2) - (cw*cWW*ee**4*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':3})

GC_1646 = Coupling(name = 'GC_1646',
                   value = '(cHW*ee**4*vev)/(2.*cw*MW**2) + (cWW*ee**4*vev)/(2.*cw*MW**2) + (cHW*cw*ee**4*vev)/(2.*MW**2*sw**2) + (cw*cWW*ee**4*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':3})

GC_1647 = Coupling(name = 'GC_1647',
                   value = '-(cHB*ee**2*vev)/(2.*MW**2*sw) - (cHW*ee**2*vev)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1648 = Coupling(name = 'GC_1648',
                   value = '(cHB*ee**2*vev)/(2.*MW**2*sw) + (cHW*ee**2*vev)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1649 = Coupling(name = 'GC_1649',
                   value = '-(cHB*ee**3*vev)/(2.*MW**2*sw) - (cHW*ee**3*vev)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1650 = Coupling(name = 'GC_1650',
                   value = '-(cHW*cw**2*ee**4*vev)/(2.*MW**2*sw**3) - (cw**2*cWW*ee**4*vev)/(2.*MW**2*sw**3) - (cHW*ee**4*vev)/(2.*MW**2*sw) - (cWW*ee**4*vev)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':3})

GC_1651 = Coupling(name = 'GC_1651',
                   value = '(cHW*cw**2*ee**4*vev)/(2.*MW**2*sw**3) + (cw**2*cWW*ee**4*vev)/(2.*MW**2*sw**3) + (cHW*ee**4*vev)/(2.*MW**2*sw) + (cWW*ee**4*vev)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':3})

GC_1652 = Coupling(name = 'GC_1652',
                   value = '(cHW*cw*ee**4*complex(0,1)*vev)/(MW**2*sw**3) + (3*cw*cWW*ee**4*complex(0,1)*vev)/(MW**2*sw**3) + (cHW*ee**4*complex(0,1)*vev)/(cw*MW**2*sw) + (cWW*ee**4*complex(0,1)*vev)/(cw*MW**2*sw)',
                   order = {'NP':1,'QED':3})

GC_1653 = Coupling(name = 'GC_1653',
                   value = '-(cHB*cw*ee**2*complex(0,1)*vev)/(2.*MW**2*sw) + (cHW*cw*ee**2*complex(0,1)*vev)/(2.*MW**2*sw) - (cHB*ee**2*complex(0,1)*sw*vev)/(2.*cw*MW**2) + (cHW*ee**2*complex(0,1)*sw*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1654 = Coupling(name = 'GC_1654',
                   value = '(cB*cw*ee**2*complex(0,1)*vev)/(2.*MW**2*sw) - (cw*cWW*ee**2*complex(0,1)*vev)/(2.*MW**2*sw) + (cB*ee**2*complex(0,1)*sw*vev)/(2.*cw*MW**2) - (cWW*ee**2*complex(0,1)*sw*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1655 = Coupling(name = 'GC_1655',
                   value = '-(ee**2*complex(0,1)*vev)/2. - (cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                   order = {'QED':1})

GC_1656 = Coupling(name = 'GC_1656',
                   value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                   order = {'QED':1})

GC_1657 = Coupling(name = 'GC_1657',
                   value = '(cH*ee**2*complex(0,1)*vev)/4. + (cH*cw**2*ee**2*complex(0,1)*vev)/(8.*sw**2) + (cH*ee**2*complex(0,1)*sw**2*vev)/(8.*cw**2)',
                   order = {'NP':1,'QED':1})

GC_1658 = Coupling(name = 'GC_1658',
                   value = '-(cB*ee**2*complex(0,1)*vev)/(2.*MW**2) - (cWW*ee**2*complex(0,1)*vev)/(2.*MW**2) - (cw**2*cWW*ee**2*complex(0,1)*vev)/(2.*MW**2*sw**2) - (cB*ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1659 = Coupling(name = 'GC_1659',
                   value = '(cHB*ee**2*complex(0,1)*vev)/(2.*MW**2) + (cHW*ee**2*complex(0,1)*vev)/(2.*MW**2) + (cHW*cw**2*ee**2*complex(0,1)*vev)/(2.*MW**2*sw**2) + (cHB*ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1660 = Coupling(name = 'GC_1660',
                   value = '-(ee**2*complex(0,1)*tcHB*vev)/(2.*MW**2) - (ee**2*complex(0,1)*sw**2*tcHB*vev)/(2.*cw**2*MW**2) - (ee**2*complex(0,1)*tcHW*vev)/(2.*MW**2) - (cw**2*ee**2*complex(0,1)*tcHW*vev)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1661 = Coupling(name = 'GC_1661',
                   value = '-(ee**3*tcHB*vev)/(2.*MW**2*sw) - (ee**3*tcHW*vev)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1662 = Coupling(name = 'GC_1662',
                   value = '(ee**3*tcHB*vev)/(2.*MW**2*sw) + (ee**3*tcHW*vev)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1663 = Coupling(name = 'GC_1663',
                   value = '(cw*ee**2*complex(0,1)*tcHB*vev)/(2.*MW**2*sw) + (ee**2*complex(0,1)*sw*tcHB*vev)/(2.*cw*MW**2) - (cw*ee**2*complex(0,1)*tcHW*vev)/(2.*MW**2*sw) - (ee**2*complex(0,1)*sw*tcHW*vev)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1664 = Coupling(name = 'GC_1664',
                   value = '(cH*ee**2)/(4.*cw) + (3*cT*ee**2)/(2.*cw) + (3*cT*cw*ee**2)/(2.*sw**2) - (cA*ee**4*vev**2)/(2.*cw**3*MW**2) - (cA*ee**4*vev**2)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1665 = Coupling(name = 'GC_1665',
                   value = '-(cT*ee**2*complex(0,1))/(2.*cw) - (cT*cw*ee**2*complex(0,1))/(2.*sw**2) + (cA*ee**4*complex(0,1)*vev**2)/(2.*cw**3*MW**2) + (cA*ee**4*complex(0,1)*vev**2)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1666 = Coupling(name = 'GC_1666',
                   value = '-(cH*ee**2)/(4.*cw) - (3*cT*ee**2)/(2.*cw) - (3*cT*cw*ee**2)/(2.*sw**2) + (cA*ee**4*vev**2)/(2.*cw**3*MW**2) + (cA*ee**4*vev**2)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1667 = Coupling(name = 'GC_1667',
                   value = '(cHW*ee**4*complex(0,1)*vev**2)/(2.*MW**2*sw**4) + (cWW*ee**4*complex(0,1)*vev**2)/(MW**2*sw**4)',
                   order = {'NP':1,'QED':2})

GC_1668 = Coupling(name = 'GC_1668',
                   value = '-(cHB*ee**3*complex(0,1)*vev**2)/(4.*MW**2*sw**2) - (cHW*ee**3*complex(0,1)*vev**2)/(4.*MW**2*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1669 = Coupling(name = 'GC_1669',
                   value = '(2*cA*ee**4*complex(0,1)*vev**2)/MW**2 - (cWW*ee**4*complex(0,1)*vev**2)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1670 = Coupling(name = 'GC_1670',
                   value = '(-4*cA*ee**4*complex(0,1)*vev**2)/MW**2 - (cHW*cw**2*ee**4*complex(0,1)*vev**2)/(2.*MW**2*sw**4) - (cw**2*cWW*ee**4*complex(0,1)*vev**2)/(MW**2*sw**4) + (2*cA*ee**4*complex(0,1)*vev**2)/(MW**2*sw**2) - (cHW*ee**4*complex(0,1)*vev**2)/(2.*MW**2*sw**2) - (2*cA*cw**2*ee**4*complex(0,1)*vev**2)/(MW**2*sw**2) - (cWW*ee**4*complex(0,1)*vev**2)/(2.*MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1671 = Coupling(name = 'GC_1671',
                   value = '-(cHQ*cw*DEL1x1*ee*complex(0,1))/(2.*sw) + (cpHQ*cw*DEL1x1*ee*complex(0,1))/(2.*sw) - (cHQ*DEL1x1*ee*complex(0,1)*sw)/(2.*cw) + (cpHQ*DEL1x1*ee*complex(0,1)*sw)/(2.*cw) + (cA*ee**3*complex(0,1)*vev**2)/(2.*cw*MW**2*sw) - (cA*cw*ee**3*complex(0,1)*vev**2)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1672 = Coupling(name = 'GC_1672',
                   value = '-(cHQ*cw*DEL2x2*ee*complex(0,1))/(2.*sw) + (cpHQ*cw*DEL2x2*ee*complex(0,1))/(2.*sw) - (cHQ*DEL2x2*ee*complex(0,1)*sw)/(2.*cw) + (cpHQ*DEL2x2*ee*complex(0,1)*sw)/(2.*cw) + (cA*ee**3*complex(0,1)*vev**2)/(2.*cw*MW**2*sw) - (cA*cw*ee**3*complex(0,1)*vev**2)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1673 = Coupling(name = 'GC_1673',
                   value = '-(cHQ*cw*DEL3x3*ee*complex(0,1))/(2.*sw) + (cpHQ*cw*DEL3x3*ee*complex(0,1))/(2.*sw) - (cHQ*DEL3x3*ee*complex(0,1)*sw)/(2.*cw) + (cpHQ*DEL3x3*ee*complex(0,1)*sw)/(2.*cw) + (cA*ee**3*complex(0,1)*vev**2)/(2.*cw*MW**2*sw) - (cA*cw*ee**3*complex(0,1)*vev**2)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1674 = Coupling(name = 'GC_1674',
                   value = '-(cHL*cw*DEL1x1*ee*complex(0,1))/(2.*sw) - (cpHL*cw*DEL1x1*ee*complex(0,1))/(2.*sw) - (cHL*DEL1x1*ee*complex(0,1)*sw)/(2.*cw) - (cpHL*DEL1x1*ee*complex(0,1)*sw)/(2.*cw) - (cA*ee**3*complex(0,1)*vev**2)/(2.*cw*MW**2*sw) + (cA*cw*ee**3*complex(0,1)*vev**2)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1675 = Coupling(name = 'GC_1675',
                   value = '-(cHL*cw*DEL2x2*ee*complex(0,1))/(2.*sw) - (cpHL*cw*DEL2x2*ee*complex(0,1))/(2.*sw) - (cHL*DEL2x2*ee*complex(0,1)*sw)/(2.*cw) - (cpHL*DEL2x2*ee*complex(0,1)*sw)/(2.*cw) - (cA*ee**3*complex(0,1)*vev**2)/(2.*cw*MW**2*sw) + (cA*cw*ee**3*complex(0,1)*vev**2)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1676 = Coupling(name = 'GC_1676',
                   value = '-(cHL*cw*DEL3x3*ee*complex(0,1))/(2.*sw) - (cpHL*cw*DEL3x3*ee*complex(0,1))/(2.*sw) - (cHL*DEL3x3*ee*complex(0,1)*sw)/(2.*cw) - (cpHL*DEL3x3*ee*complex(0,1)*sw)/(2.*cw) - (cA*ee**3*complex(0,1)*vev**2)/(2.*cw*MW**2*sw) + (cA*cw*ee**3*complex(0,1)*vev**2)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1677 = Coupling(name = 'GC_1677',
                   value = '-(cHQ*cw*ee*complex(0,1)*I1a11)/(2.*sw) - (cpHQ*cw*ee*complex(0,1)*I1a11)/(2.*sw) - (cHQ*ee*complex(0,1)*I1a11*sw)/(2.*cw) - (cpHQ*ee*complex(0,1)*I1a11*sw)/(2.*cw) - (cA*ee**3*complex(0,1)*vev**2)/(2.*cw*MW**2*sw) + (cA*cw*ee**3*complex(0,1)*vev**2)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1678 = Coupling(name = 'GC_1678',
                   value = '-(cHQ*cw*ee*complex(0,1)*I1a22)/(2.*sw) - (cpHQ*cw*ee*complex(0,1)*I1a22)/(2.*sw) - (cHQ*ee*complex(0,1)*I1a22*sw)/(2.*cw) - (cpHQ*ee*complex(0,1)*I1a22*sw)/(2.*cw) - (cA*ee**3*complex(0,1)*vev**2)/(2.*cw*MW**2*sw) + (cA*cw*ee**3*complex(0,1)*vev**2)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1679 = Coupling(name = 'GC_1679',
                   value = '-(cHQ*cw*ee*complex(0,1)*I1a33)/(2.*sw) - (cpHQ*cw*ee*complex(0,1)*I1a33)/(2.*sw) - (cHQ*ee*complex(0,1)*I1a33*sw)/(2.*cw) - (cpHQ*ee*complex(0,1)*I1a33*sw)/(2.*cw) - (cA*ee**3*complex(0,1)*vev**2)/(2.*cw*MW**2*sw) + (cA*cw*ee**3*complex(0,1)*vev**2)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1680 = Coupling(name = 'GC_1680',
                   value = '(cH*ee**2)/(4.*sw) - (cA*ee**4*vev**2)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1681 = Coupling(name = 'GC_1681',
                   value = '-(cH*ee**2)/(4.*sw) + (cA*ee**4*vev**2)/(2.*MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1682 = Coupling(name = 'GC_1682',
                   value = '-(cHL*cw*DEL1x1*ee*complex(0,1))/(2.*sw) + (cpHL*cw*DEL1x1*ee*complex(0,1))/(2.*sw) - (cHL*DEL1x1*ee*complex(0,1)*sw)/(2.*cw) + (cpHL*DEL1x1*ee*complex(0,1)*sw)/(2.*cw) + (cA*ee**3*complex(0,1)*vev**2)/(2.*cw*MW**2*sw) - (cA*cw*ee**3*complex(0,1)*vev**2)/(2.*MW**2*sw) + (cA*ee**3*complex(0,1)*sw*vev**2)/(2.*cw**3*MW**2) - (cA*ee**3*complex(0,1)*sw*vev**2)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1683 = Coupling(name = 'GC_1683',
                   value = '-(cHL*cw*DEL2x2*ee*complex(0,1))/(2.*sw) + (cpHL*cw*DEL2x2*ee*complex(0,1))/(2.*sw) - (cHL*DEL2x2*ee*complex(0,1)*sw)/(2.*cw) + (cpHL*DEL2x2*ee*complex(0,1)*sw)/(2.*cw) + (cA*ee**3*complex(0,1)*vev**2)/(2.*cw*MW**2*sw) - (cA*cw*ee**3*complex(0,1)*vev**2)/(2.*MW**2*sw) + (cA*ee**3*complex(0,1)*sw*vev**2)/(2.*cw**3*MW**2) - (cA*ee**3*complex(0,1)*sw*vev**2)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1684 = Coupling(name = 'GC_1684',
                   value = '-(cHL*cw*DEL3x3*ee*complex(0,1))/(2.*sw) + (cpHL*cw*DEL3x3*ee*complex(0,1))/(2.*sw) - (cHL*DEL3x3*ee*complex(0,1)*sw)/(2.*cw) + (cpHL*DEL3x3*ee*complex(0,1)*sw)/(2.*cw) + (cA*ee**3*complex(0,1)*vev**2)/(2.*cw*MW**2*sw) - (cA*cw*ee**3*complex(0,1)*vev**2)/(2.*MW**2*sw) + (cA*ee**3*complex(0,1)*sw*vev**2)/(2.*cw**3*MW**2) - (cA*ee**3*complex(0,1)*sw*vev**2)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1685 = Coupling(name = 'GC_1685',
                   value = '-(cT*cw*ee*complex(0,1))/(2.*sw) - (cT*ee*complex(0,1)*sw)/(2.*cw) - (cA*ee**3*complex(0,1)*vev**2)/(2.*cw*MW**2*sw) + (cA*cw*ee**3*complex(0,1)*vev**2)/(2.*MW**2*sw) + (cA*ee**3*complex(0,1)*sw*vev**2)/(2.*cw**3*MW**2) + (3*cA*ee**3*complex(0,1)*sw*vev**2)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1686 = Coupling(name = 'GC_1686',
                   value = '(cA*ee**3*complex(0,1)*vev**2)/(cw*MW**2*sw) - (cA*cw*ee**3*complex(0,1)*vev**2)/(MW**2*sw) - (2*cA*ee**3*complex(0,1)*sw*vev**2)/(cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1687 = Coupling(name = 'GC_1687',
                   value = '-(cHW*cw*ee**3*complex(0,1)*vev**2)/(4.*MW**2*sw**3) - (3*cw*cWW*ee**3*complex(0,1)*vev**2)/(4.*MW**2*sw**3) + (cA*ee**3*complex(0,1)*vev**2)/(cw*MW**2*sw) - (cA*cw*ee**3*complex(0,1)*vev**2)/(MW**2*sw) - (2*cA*ee**3*complex(0,1)*sw*vev**2)/(cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1688 = Coupling(name = 'GC_1688',
                   value = '-((cA*ee**3*complex(0,1)*vev**2)/(cw*MW**2*sw)) + (cA*cw*ee**3*complex(0,1)*vev**2)/(MW**2*sw) + (2*cA*ee**3*complex(0,1)*sw*vev**2)/(cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1689 = Coupling(name = 'GC_1689',
                   value = '(cH*cw*ee)/(4.*sw) + (cH*ee*sw)/(4.*cw) - (cA*ee**3*vev**2)/(2.*cw*MW**2*sw) + (cA*cw*ee**3*vev**2)/(2.*MW**2*sw) - (cA*ee**3*sw*vev**2)/(2.*cw**3*MW**2) + (cA*ee**3*sw*vev**2)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1690 = Coupling(name = 'GC_1690',
                   value = '(cT*cw*ee**2*complex(0,1))/sw + (cT*ee**2*complex(0,1)*sw)/cw + (cA*ee**4*complex(0,1)*vev**2)/(cw*MW**2*sw) - (cA*ee**4*complex(0,1)*sw*vev**2)/(cw**3*MW**2) - (4*cA*ee**4*complex(0,1)*sw*vev**2)/(cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1691 = Coupling(name = 'GC_1691',
                   value = '(cHW*cw*ee**4*complex(0,1)*vev**2)/(2.*MW**2*sw**3) + (3*cw*cWW*ee**4*complex(0,1)*vev**2)/(2.*MW**2*sw**3) - (2*cA*ee**4*complex(0,1)*vev**2)/(cw*MW**2*sw) + (cHW*ee**4*complex(0,1)*vev**2)/(2.*cw*MW**2*sw) + (cWW*ee**4*complex(0,1)*vev**2)/(2.*cw*MW**2*sw) + (4*cA*ee**4*complex(0,1)*sw*vev**2)/(cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1692 = Coupling(name = 'GC_1692',
                   value = '-2*cT*ee**2*complex(0,1) - (cT*cw**2*ee**2*complex(0,1))/sw**2 - (cT*ee**2*complex(0,1)*sw**2)/cw**2 - (2*cA*ee**4*complex(0,1)*vev**2)/MW**2 + (2*cA*ee**4*complex(0,1)*vev**2)/(cw**2*MW**2) + (cA*ee**4*complex(0,1)*vev**2)/(MW**2*sw**2) - (cA*cw**2*ee**4*complex(0,1)*vev**2)/(MW**2*sw**2) + (cA*ee**4*complex(0,1)*sw**2*vev**2)/(cw**4*MW**2) - (cA*ee**4*complex(0,1)*sw**2*vev**2)/(cw**2*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1693 = Coupling(name = 'GC_1693',
                   value = '-(cH*ee**2*complex(0,1)) - 6*cT*ee**2*complex(0,1) - (cH*cw**2*ee**2*complex(0,1))/(2.*sw**2) - (3*cT*cw**2*ee**2*complex(0,1))/sw**2 - (cH*ee**2*complex(0,1)*sw**2)/(2.*cw**2) - (3*cT*ee**2*complex(0,1)*sw**2)/cw**2 - (2*cA*ee**4*complex(0,1)*vev**2)/MW**2 + (2*cA*ee**4*complex(0,1)*vev**2)/(cw**2*MW**2) + (cA*ee**4*complex(0,1)*vev**2)/(MW**2*sw**2) - (cA*cw**2*ee**4*complex(0,1)*vev**2)/(MW**2*sw**2) + (cA*ee**4*complex(0,1)*sw**2*vev**2)/(cw**4*MW**2) - (cA*ee**4*complex(0,1)*sw**2*vev**2)/(cw**2*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1694 = Coupling(name = 'GC_1694',
                   value = '(cT*cw**2*ee**2*complex(0,1))/sw**2 - (cT*ee**2*complex(0,1)*sw**2)/cw**2 - (2*cA*ee**4*complex(0,1)*vev**2)/MW**2 - (2*cA*ee**4*complex(0,1)*vev**2)/(cw**2*MW**2) + (cA*ee**4*complex(0,1)*vev**2)/(MW**2*sw**2) - (cA*cw**2*ee**4*complex(0,1)*vev**2)/(MW**2*sw**2) + (cA*ee**4*complex(0,1)*sw**2*vev**2)/(cw**4*MW**2) + (3*cA*ee**4*complex(0,1)*sw**2*vev**2)/(cw**2*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1695 = Coupling(name = 'GC_1695',
                   value = '(ee**3*complex(0,1)*tcHB*vev**2)/(4.*MW**2*sw**2) + (ee**3*complex(0,1)*tcHW*vev**2)/(4.*MW**2*sw**2)',
                   order = {'NP':1,'QED':1})

GC_1696 = Coupling(name = 'GC_1696',
                   value = '(cT*ee**2*vev)/(2.*cw) + (cT*cw*ee**2*vev)/(2.*sw**2) - (cA*ee**4*vev**3)/(2.*cw**3*MW**2) - (cA*ee**4*vev**3)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1697 = Coupling(name = 'GC_1697',
                   value = '-(cT*ee**2*vev)/(2.*cw) - (cT*cw*ee**2*vev)/(2.*sw**2) + (cA*ee**4*vev**3)/(2.*cw**3*MW**2) + (cA*ee**4*vev**3)/(2.*cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1698 = Coupling(name = 'GC_1698',
                   value = '-(cH*ee**2*complex(0,1)*vev)/2. - 2*cT*ee**2*complex(0,1)*vev - (cH*cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (cT*cw**2*ee**2*complex(0,1)*vev)/sw**2 - (cH*ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2) - (cT*ee**2*complex(0,1)*sw**2*vev)/cw**2 - (2*cA*ee**4*complex(0,1)*vev**3)/MW**2 + (2*cA*ee**4*complex(0,1)*vev**3)/(cw**2*MW**2) + (cA*ee**4*complex(0,1)*vev**3)/(MW**2*sw**2) - (cA*cw**2*ee**4*complex(0,1)*vev**3)/(MW**2*sw**2) + (cA*ee**4*complex(0,1)*sw**2*vev**3)/(cw**4*MW**2) - (cA*ee**4*complex(0,1)*sw**2*vev**3)/(cw**2*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1699 = Coupling(name = 'GC_1699',
                   value = '-(yb/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1700 = Coupling(name = 'GC_1700',
                   value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1701 = Coupling(name = 'GC_1701',
                   value = '-(cd*yb)/(2.*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1702 = Coupling(name = 'GC_1702',
                   value = '(-2*cdG*G*yb*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_1703 = Coupling(name = 'GC_1703',
                   value = '(-2*cdG*complex(0,1)*G*yb*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_1704 = Coupling(name = 'GC_1704',
                   value = '(-2*cdG*G**2*yb*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QCD':2,'QED':1})

GC_1705 = Coupling(name = 'GC_1705',
                   value = '(2*cdG*complex(0,1)*G**2*yb*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QCD':2,'QED':1})

GC_1706 = Coupling(name = 'GC_1706',
                   value = '-((cdW*ee**2*yb*cmath.sqrt(2))/(MW**2*sw**2))',
                   order = {'NP':1,'QED':3})

GC_1707 = Coupling(name = 'GC_1707',
                   value = '-((cdW*ee**2*complex(0,1)*yb*cmath.sqrt(2))/(MW**2*sw**2))',
                   order = {'NP':1,'QED':3})

GC_1708 = Coupling(name = 'GC_1708',
                   value = '(2*cdW*cw*ee**2*yb*cmath.sqrt(2))/(MW**2*sw**2)',
                   order = {'NP':1,'QED':3})

GC_1709 = Coupling(name = 'GC_1709',
                   value = '(-2*cdW*ee*yb*cmath.sqrt(2))/(MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1710 = Coupling(name = 'GC_1710',
                   value = '(2*cdW*ee*yb*cmath.sqrt(2))/(MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1711 = Coupling(name = 'GC_1711',
                   value = '(-2*cdW*ee**2*yb*cmath.sqrt(2))/(MW**2*sw)',
                   order = {'NP':1,'QED':3})

GC_1712 = Coupling(name = 'GC_1712',
                   value = '(-3*cd*yb)/(vev**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1713 = Coupling(name = 'GC_1713',
                   value = '-((cd*yb)/(vev**2*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':3})

GC_1714 = Coupling(name = 'GC_1714',
                   value = '-((cd*complex(0,1)*yb)/(vev**2*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':3})

GC_1715 = Coupling(name = 'GC_1715',
                   value = '(-3*cd*complex(0,1)*yb)/(vev**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1716 = Coupling(name = 'GC_1716',
                   value = '-((cd*yb)/(vev*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_1717 = Coupling(name = 'GC_1717',
                   value = '-((cd*complex(0,1)*yb)/(vev*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_1718 = Coupling(name = 'GC_1718',
                   value = '(-3*cd*complex(0,1)*yb)/(vev*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1719 = Coupling(name = 'GC_1719',
                   value = '(-2*cdG*complex(0,1)*G*vev*yb*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QCD':1})

GC_1720 = Coupling(name = 'GC_1720',
                   value = '(-2*cdG*G**2*vev*yb*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QCD':2})

GC_1721 = Coupling(name = 'GC_1721',
                   value = '-((cdW*ee**2*complex(0,1)*vev*yb*cmath.sqrt(2))/(MW**2*sw**2))',
                   order = {'NP':1,'QED':2})

GC_1722 = Coupling(name = 'GC_1722',
                   value = '(-3*cd*complex(0,1)*yb)/(2.*cmath.sqrt(2)) + (cH*complex(0,1)*yb)/(2.*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1723 = Coupling(name = 'GC_1723',
                   value = '-((cdB*ee*complex(0,1)*yb*cmath.sqrt(2))/MW**2) + (cdW*ee*complex(0,1)*yb*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QED':2})

GC_1724 = Coupling(name = 'GC_1724',
                   value = '-((cdB*ee*yb*cmath.sqrt(2))/MW**2) + (cdW*ee*yb*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QED':2})

GC_1725 = Coupling(name = 'GC_1725',
                   value = '(cdW*cw*ee*complex(0,1)*yb*cmath.sqrt(2))/(MW**2*sw) + (cdB*ee*complex(0,1)*sw*yb*cmath.sqrt(2))/(cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1726 = Coupling(name = 'GC_1726',
                   value = '(cdW*cw*ee*yb*cmath.sqrt(2))/(MW**2*sw) + (cdB*ee*sw*yb*cmath.sqrt(2))/(cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1727 = Coupling(name = 'GC_1727',
                   value = '-((cdB*ee*complex(0,1)*vev*yb*cmath.sqrt(2))/MW**2) + (cdW*ee*complex(0,1)*vev*yb*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QED':1})

GC_1728 = Coupling(name = 'GC_1728',
                   value = '(cdW*cw*ee*complex(0,1)*vev*yb*cmath.sqrt(2))/(MW**2*sw) + (cdB*ee*complex(0,1)*sw*vev*yb*cmath.sqrt(2))/(cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1729 = Coupling(name = 'GC_1729',
                   value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1730 = Coupling(name = 'GC_1730',
                   value = 'yt/cmath.sqrt(2)',
                   order = {'QED':1})

GC_1731 = Coupling(name = 'GC_1731',
                   value = '(cu*yt)/(2.*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1732 = Coupling(name = 'GC_1732',
                   value = '(-2*cuG*complex(0,1)*G*yt*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_1733 = Coupling(name = 'GC_1733',
                   value = '(2*cuG*G*yt*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QCD':1,'QED':1})

GC_1734 = Coupling(name = 'GC_1734',
                   value = '(-2*cuG*G**2*yt*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QCD':2,'QED':1})

GC_1735 = Coupling(name = 'GC_1735',
                   value = '(-2*cuG*complex(0,1)*G**2*yt*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QCD':2,'QED':1})

GC_1736 = Coupling(name = 'GC_1736',
                   value = '-((cuW*ee**2*yt*cmath.sqrt(2))/(MW**2*sw**2))',
                   order = {'NP':1,'QED':3})

GC_1737 = Coupling(name = 'GC_1737',
                   value = '(cuW*ee**2*complex(0,1)*yt*cmath.sqrt(2))/(MW**2*sw**2)',
                   order = {'NP':1,'QED':3})

GC_1738 = Coupling(name = 'GC_1738',
                   value = '(-2*cuW*cw*ee**2*yt*cmath.sqrt(2))/(MW**2*sw**2)',
                   order = {'NP':1,'QED':3})

GC_1739 = Coupling(name = 'GC_1739',
                   value = '(-2*cuW*ee*yt*cmath.sqrt(2))/(MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1740 = Coupling(name = 'GC_1740',
                   value = '(2*cuW*ee*yt*cmath.sqrt(2))/(MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1741 = Coupling(name = 'GC_1741',
                   value = '(2*cuW*ee**2*yt*cmath.sqrt(2))/(MW**2*sw)',
                   order = {'NP':1,'QED':3})

GC_1742 = Coupling(name = 'GC_1742',
                   value = '-((cu*complex(0,1)*yt)/(vev**2*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':3})

GC_1743 = Coupling(name = 'GC_1743',
                   value = '(-3*cu*complex(0,1)*yt)/(vev**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1744 = Coupling(name = 'GC_1744',
                   value = '(cu*yt)/(vev**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1745 = Coupling(name = 'GC_1745',
                   value = '(3*cu*yt)/(vev**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1746 = Coupling(name = 'GC_1746',
                   value = '-((cu*complex(0,1)*yt)/(vev*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_1747 = Coupling(name = 'GC_1747',
                   value = '(-3*cu*complex(0,1)*yt)/(vev*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1748 = Coupling(name = 'GC_1748',
                   value = '(cu*yt)/(vev*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1749 = Coupling(name = 'GC_1749',
                   value = '(-2*cuG*complex(0,1)*G*vev*yt*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QCD':1})

GC_1750 = Coupling(name = 'GC_1750',
                   value = '(-2*cuG*G**2*vev*yt*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QCD':2})

GC_1751 = Coupling(name = 'GC_1751',
                   value = '(cuW*ee**2*complex(0,1)*vev*yt*cmath.sqrt(2))/(MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1752 = Coupling(name = 'GC_1752',
                   value = '(cH*complex(0,1)*yt)/(2.*cmath.sqrt(2)) - (3*cu*complex(0,1)*yt)/(2.*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1753 = Coupling(name = 'GC_1753',
                   value = '-((cuB*ee*complex(0,1)*yt*cmath.sqrt(2))/MW**2) - (cuW*ee*complex(0,1)*yt*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QED':2})

GC_1754 = Coupling(name = 'GC_1754',
                   value = '(cuB*ee*yt*cmath.sqrt(2))/MW**2 + (cuW*ee*yt*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QED':2})

GC_1755 = Coupling(name = 'GC_1755',
                   value = '(cuW*cw*ee*yt*cmath.sqrt(2))/(MW**2*sw) - (cuB*ee*sw*yt*cmath.sqrt(2))/(cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1756 = Coupling(name = 'GC_1756',
                   value = '-((cuW*cw*ee*complex(0,1)*yt*cmath.sqrt(2))/(MW**2*sw)) + (cuB*ee*complex(0,1)*sw*yt*cmath.sqrt(2))/(cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1757 = Coupling(name = 'GC_1757',
                   value = '-((cuB*ee*complex(0,1)*vev*yt*cmath.sqrt(2))/MW**2) - (cuW*ee*complex(0,1)*vev*yt*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QED':1})

GC_1758 = Coupling(name = 'GC_1758',
                   value = '-((cuW*cw*ee*complex(0,1)*vev*yt*cmath.sqrt(2))/(MW**2*sw)) + (cuB*ee*complex(0,1)*sw*vev*yt*cmath.sqrt(2))/(cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1759 = Coupling(name = 'GC_1759',
                   value = '-ytau',
                   order = {'QED':1})

GC_1760 = Coupling(name = 'GC_1760',
                   value = 'ytau',
                   order = {'QED':1})

GC_1761 = Coupling(name = 'GC_1761',
                   value = '-(ytau/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1762 = Coupling(name = 'GC_1762',
                   value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1763 = Coupling(name = 'GC_1763',
                   value = '-(cl*ytau)/2.',
                   order = {'NP':1,'QED':1})

GC_1764 = Coupling(name = 'GC_1764',
                   value = '(cl*ytau)/2.',
                   order = {'NP':1,'QED':1})

GC_1765 = Coupling(name = 'GC_1765',
                   value = '-(cl*ytau)/(2.*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1766 = Coupling(name = 'GC_1766',
                   value = '(-2*clW*ee**2*ytau)/(MW**2*sw**2)',
                   order = {'NP':1,'QED':3})

GC_1767 = Coupling(name = 'GC_1767',
                   value = '(2*clW*ee**2*ytau)/(MW**2*sw**2)',
                   order = {'NP':1,'QED':3})

GC_1768 = Coupling(name = 'GC_1768',
                   value = '-((clW*ee**2*ytau*cmath.sqrt(2))/(MW**2*sw**2))',
                   order = {'NP':1,'QED':3})

GC_1769 = Coupling(name = 'GC_1769',
                   value = '-((clW*ee**2*complex(0,1)*ytau*cmath.sqrt(2))/(MW**2*sw**2))',
                   order = {'NP':1,'QED':3})

GC_1770 = Coupling(name = 'GC_1770',
                   value = '(-2*clW*cw*ee**2*complex(0,1)*ytau)/(MW**2*sw**2)',
                   order = {'NP':1,'QED':3})

GC_1771 = Coupling(name = 'GC_1771',
                   value = '(2*clW*cw*ee**2*complex(0,1)*ytau)/(MW**2*sw**2)',
                   order = {'NP':1,'QED':3})

GC_1772 = Coupling(name = 'GC_1772',
                   value = '(2*clW*cw*ee**2*ytau)/(MW**2*sw**2)',
                   order = {'NP':1,'QED':3})

GC_1773 = Coupling(name = 'GC_1773',
                   value = '(2*clW*cw*ee**2*ytau*cmath.sqrt(2))/(MW**2*sw**2)',
                   order = {'NP':1,'QED':3})

GC_1774 = Coupling(name = 'GC_1774',
                   value = '(-2*clW*ee*ytau)/(MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1775 = Coupling(name = 'GC_1775',
                   value = '(-2*clW*ee*complex(0,1)*ytau)/(MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1776 = Coupling(name = 'GC_1776',
                   value = '(2*clW*ee*ytau)/(MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1777 = Coupling(name = 'GC_1777',
                   value = '(-2*clW*ee*ytau*cmath.sqrt(2))/(MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1778 = Coupling(name = 'GC_1778',
                   value = '(2*clW*ee*ytau*cmath.sqrt(2))/(MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1779 = Coupling(name = 'GC_1779',
                   value = '(-2*clW*ee**2*ytau)/(MW**2*sw)',
                   order = {'NP':1,'QED':3})

GC_1780 = Coupling(name = 'GC_1780',
                   value = '(-2*clW*ee**2*complex(0,1)*ytau)/(MW**2*sw)',
                   order = {'NP':1,'QED':3})

GC_1781 = Coupling(name = 'GC_1781',
                   value = '(2*clW*ee**2*complex(0,1)*ytau)/(MW**2*sw)',
                   order = {'NP':1,'QED':3})

GC_1782 = Coupling(name = 'GC_1782',
                   value = '(-2*clW*ee**2*ytau*cmath.sqrt(2))/(MW**2*sw)',
                   order = {'NP':1,'QED':3})

GC_1783 = Coupling(name = 'GC_1783',
                   value = '(-2*cl*ytau)/vev**2',
                   order = {'NP':1,'QED':3})

GC_1784 = Coupling(name = 'GC_1784',
                   value = '-((cl*ytau)/vev**2)',
                   order = {'NP':1,'QED':3})

GC_1785 = Coupling(name = 'GC_1785',
                   value = '(cl*ytau)/vev**2',
                   order = {'NP':1,'QED':3})

GC_1786 = Coupling(name = 'GC_1786',
                   value = '(2*cl*ytau)/vev**2',
                   order = {'NP':1,'QED':3})

GC_1787 = Coupling(name = 'GC_1787',
                   value = '(-3*cl*ytau)/(vev**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1788 = Coupling(name = 'GC_1788',
                   value = '-((cl*ytau)/(vev**2*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':3})

GC_1789 = Coupling(name = 'GC_1789',
                   value = '-((cl*complex(0,1)*ytau)/(vev**2*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':3})

GC_1790 = Coupling(name = 'GC_1790',
                   value = '(-3*cl*complex(0,1)*ytau)/(vev**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1791 = Coupling(name = 'GC_1791',
                   value = '-((cl*ytau)/vev)',
                   order = {'NP':1,'QED':2})

GC_1792 = Coupling(name = 'GC_1792',
                   value = '(cl*ytau)/vev',
                   order = {'NP':1,'QED':2})

GC_1793 = Coupling(name = 'GC_1793',
                   value = '-((cl*ytau)/(vev*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_1794 = Coupling(name = 'GC_1794',
                   value = '-((cl*complex(0,1)*ytau)/(vev*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':2})

GC_1795 = Coupling(name = 'GC_1795',
                   value = '(-3*cl*complex(0,1)*ytau)/(vev*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1796 = Coupling(name = 'GC_1796',
                   value = '-((clW*ee**2*complex(0,1)*vev*ytau*cmath.sqrt(2))/(MW**2*sw**2))',
                   order = {'NP':1,'QED':2})

GC_1797 = Coupling(name = 'GC_1797',
                   value = '(-2*clW*cw*ee**2*complex(0,1)*vev*ytau)/(MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1798 = Coupling(name = 'GC_1798',
                   value = '(2*clW*cw*ee**2*complex(0,1)*vev*ytau)/(MW**2*sw**2)',
                   order = {'NP':1,'QED':2})

GC_1799 = Coupling(name = 'GC_1799',
                   value = '(-2*clW*ee*complex(0,1)*vev*ytau)/(MW**2*sw)',
                   order = {'NP':1,'QED':1})

GC_1800 = Coupling(name = 'GC_1800',
                   value = '(-2*clW*ee**2*complex(0,1)*vev*ytau)/(MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1801 = Coupling(name = 'GC_1801',
                   value = '(2*clW*ee**2*complex(0,1)*vev*ytau)/(MW**2*sw)',
                   order = {'NP':1,'QED':2})

GC_1802 = Coupling(name = 'GC_1802',
                   value = '(cH*complex(0,1)*ytau)/(2.*cmath.sqrt(2)) - (3*cl*complex(0,1)*ytau)/(2.*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1803 = Coupling(name = 'GC_1803',
                   value = '(-2*clB*ee*ytau)/MW**2 - (2*clW*ee*ytau)/MW**2',
                   order = {'NP':1,'QED':2})

GC_1804 = Coupling(name = 'GC_1804',
                   value = '(2*clB*ee*ytau)/MW**2 + (2*clW*ee*ytau)/MW**2',
                   order = {'NP':1,'QED':2})

GC_1805 = Coupling(name = 'GC_1805',
                   value = '-((clB*ee*complex(0,1)*ytau*cmath.sqrt(2))/MW**2) + (clW*ee*complex(0,1)*ytau*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QED':2})

GC_1806 = Coupling(name = 'GC_1806',
                   value = '-((clB*ee*ytau*cmath.sqrt(2))/MW**2) + (clW*ee*ytau*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QED':2})

GC_1807 = Coupling(name = 'GC_1807',
                   value = '(2*clW*cw*ee*ytau)/(MW**2*sw) - (2*clB*ee*sw*ytau)/(cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1808 = Coupling(name = 'GC_1808',
                   value = '(-2*clW*cw*ee*ytau)/(MW**2*sw) + (2*clB*ee*sw*ytau)/(cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1809 = Coupling(name = 'GC_1809',
                   value = '(clW*cw*ee*complex(0,1)*ytau*cmath.sqrt(2))/(MW**2*sw) + (clB*ee*complex(0,1)*sw*ytau*cmath.sqrt(2))/(cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1810 = Coupling(name = 'GC_1810',
                   value = '(clW*cw*ee*ytau*cmath.sqrt(2))/(MW**2*sw) + (clB*ee*sw*ytau*cmath.sqrt(2))/(cw*MW**2)',
                   order = {'NP':1,'QED':2})

GC_1811 = Coupling(name = 'GC_1811',
                   value = '-((clB*ee*complex(0,1)*vev*ytau*cmath.sqrt(2))/MW**2) + (clW*ee*complex(0,1)*vev*ytau*cmath.sqrt(2))/MW**2',
                   order = {'NP':1,'QED':1})

GC_1812 = Coupling(name = 'GC_1812',
                   value = '(clW*cw*ee*complex(0,1)*vev*ytau*cmath.sqrt(2))/(MW**2*sw) + (clB*ee*complex(0,1)*sw*vev*ytau*cmath.sqrt(2))/(cw*MW**2)',
                   order = {'NP':1,'QED':1})

GC_1813 = Coupling(name = 'GC_1813',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL1x1))/(sw*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1814 = Coupling(name = 'GC_1814',
                   value = '-((cHud*complexconjugate(DEL1x1)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_1815 = Coupling(name = 'GC_1815',
                   value = '-((cHud*complex(0,1)*complexconjugate(DEL1x1)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_1816 = Coupling(name = 'GC_1816',
                   value = '-((cHud*ee*complexconjugate(DEL1x1)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':3})

GC_1817 = Coupling(name = 'GC_1817',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL1x1)*cmath.sqrt(2))/vev**2',
                   order = {'NP':1,'QED':3})

GC_1818 = Coupling(name = 'GC_1818',
                   value = '-((cHud*ee*complex(0,1)*complexconjugate(DEL1x1)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1819 = Coupling(name = 'GC_1819',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL1x1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1820 = Coupling(name = 'GC_1820',
                   value = '(2*cHud*ee*complex(0,1)*complexconjugate(DEL1x1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1821 = Coupling(name = 'GC_1821',
                   value = '(cHud*ee*complexconjugate(DEL1x1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1822 = Coupling(name = 'GC_1822',
                   value = '-((cHud*cw*ee*complexconjugate(DEL1x1)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1823 = Coupling(name = 'GC_1823',
                   value = '(cHud*cw*ee*complex(0,1)*complexconjugate(DEL1x1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1824 = Coupling(name = 'GC_1824',
                   value = '-((cHud*complexconjugate(DEL1x1)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1825 = Coupling(name = 'GC_1825',
                   value = '-((cHud*ee*complexconjugate(DEL1x1)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1826 = Coupling(name = 'GC_1826',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL1x1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1827 = Coupling(name = 'GC_1827',
                   value = '(cHud*ee*complexconjugate(DEL1x1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1828 = Coupling(name = 'GC_1828',
                   value = '-((cHud*cw*ee*complexconjugate(DEL1x1)*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1829 = Coupling(name = 'GC_1829',
                   value = '-(cHd*cw*DEL1x1*ee*complex(0,1))/(4.*sw) - (cHd*DEL1x1*ee*complex(0,1)*sw)/(4.*cw) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL1x1))/(4.*sw) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL1x1))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_1830 = Coupling(name = 'GC_1830',
                   value = '-(cHu*cw*DEL1x1*ee*complex(0,1))/(4.*sw) - (cHu*DEL1x1*ee*complex(0,1)*sw)/(4.*cw) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL1x1))/(4.*sw) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL1x1))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_1831 = Coupling(name = 'GC_1831',
                   value = '-(cHd*DEL1x1*complex(0,1))/(2.*vev**2) - (cHd*complex(0,1)*complexconjugate(DEL1x1))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1832 = Coupling(name = 'GC_1832',
                   value = '(cHd*DEL1x1)/(2.*vev**2) + (cHd*complexconjugate(DEL1x1))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1833 = Coupling(name = 'GC_1833',
                   value = '-(cHu*DEL1x1*complex(0,1))/(2.*vev**2) - (cHu*complex(0,1)*complexconjugate(DEL1x1))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1834 = Coupling(name = 'GC_1834',
                   value = '(cHu*DEL1x1)/(2.*vev**2) + (cHu*complexconjugate(DEL1x1))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1835 = Coupling(name = 'GC_1835',
                   value = '(cHd*DEL1x1*ee*complex(0,1))/vev**2 + (cHd*ee*complex(0,1)*complexconjugate(DEL1x1))/vev**2',
                   order = {'NP':1,'QED':3})

GC_1836 = Coupling(name = 'GC_1836',
                   value = '(cHu*DEL1x1*ee*complex(0,1))/vev**2 + (cHu*ee*complex(0,1)*complexconjugate(DEL1x1))/vev**2',
                   order = {'NP':1,'QED':3})

GC_1837 = Coupling(name = 'GC_1837',
                   value = '-(cHd*DEL1x1*ee)/(2.*sw*vev**2) - (cHd*ee*complexconjugate(DEL1x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1838 = Coupling(name = 'GC_1838',
                   value = '-(cHd*DEL1x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*complexconjugate(DEL1x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1839 = Coupling(name = 'GC_1839',
                   value = '(cHd*DEL1x1*ee)/(2.*sw*vev**2) + (cHd*ee*complexconjugate(DEL1x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1840 = Coupling(name = 'GC_1840',
                   value = '-(cHu*DEL1x1*ee)/(2.*sw*vev**2) - (cHu*ee*complexconjugate(DEL1x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1841 = Coupling(name = 'GC_1841',
                   value = '-(cHu*DEL1x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*complexconjugate(DEL1x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1842 = Coupling(name = 'GC_1842',
                   value = '(cHu*DEL1x1*ee)/(2.*sw*vev**2) + (cHu*ee*complexconjugate(DEL1x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1843 = Coupling(name = 'GC_1843',
                   value = '-(cHd*cw*DEL1x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL1x1*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL1x1))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL1x1))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1844 = Coupling(name = 'GC_1844',
                   value = '(cHd*cw*DEL1x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL1x1*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHd*cw*ee*complex(0,1)*complexconjugate(DEL1x1))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL1x1))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1845 = Coupling(name = 'GC_1845',
                   value = '-(cHu*cw*DEL1x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL1x1*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL1x1))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL1x1))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1846 = Coupling(name = 'GC_1846',
                   value = '(cHu*cw*DEL1x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL1x1*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHu*cw*ee*complex(0,1)*complexconjugate(DEL1x1))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL1x1))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1847 = Coupling(name = 'GC_1847',
                   value = '(cHd*DEL1x1)/(2.*vev) + (cHd*complexconjugate(DEL1x1))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1848 = Coupling(name = 'GC_1848',
                   value = '(cHu*DEL1x1)/(2.*vev) + (cHu*complexconjugate(DEL1x1))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1849 = Coupling(name = 'GC_1849',
                   value = '-(cHd*DEL1x1*ee)/(2.*sw*vev) - (cHd*ee*complexconjugate(DEL1x1))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1850 = Coupling(name = 'GC_1850',
                   value = '(cHd*DEL1x1*ee)/(2.*sw*vev) + (cHd*ee*complexconjugate(DEL1x1))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1851 = Coupling(name = 'GC_1851',
                   value = '-(cHu*DEL1x1*ee)/(2.*sw*vev) - (cHu*ee*complexconjugate(DEL1x1))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1852 = Coupling(name = 'GC_1852',
                   value = '(cHu*DEL1x1*ee)/(2.*sw*vev) + (cHu*ee*complexconjugate(DEL1x1))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1853 = Coupling(name = 'GC_1853',
                   value = '-(cHd*cw*DEL1x1*ee*complex(0,1))/(2.*sw*vev) - (cHd*DEL1x1*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL1x1))/(2.*sw*vev) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL1x1))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1854 = Coupling(name = 'GC_1854',
                   value = '-(cHu*cw*DEL1x1*ee*complex(0,1))/(2.*sw*vev) - (cHu*DEL1x1*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL1x1))/(2.*sw*vev) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL1x1))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1855 = Coupling(name = 'GC_1855',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL1x2))/(sw*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1856 = Coupling(name = 'GC_1856',
                   value = '-((cHud*complexconjugate(DEL1x2)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_1857 = Coupling(name = 'GC_1857',
                   value = '-((cHud*complex(0,1)*complexconjugate(DEL1x2)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_1858 = Coupling(name = 'GC_1858',
                   value = '-((cHud*ee*complexconjugate(DEL1x2)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':3})

GC_1859 = Coupling(name = 'GC_1859',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL1x2)*cmath.sqrt(2))/vev**2',
                   order = {'NP':1,'QED':3})

GC_1860 = Coupling(name = 'GC_1860',
                   value = '-((cHud*ee*complex(0,1)*complexconjugate(DEL1x2)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1861 = Coupling(name = 'GC_1861',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL1x2)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1862 = Coupling(name = 'GC_1862',
                   value = '(2*cHud*ee*complex(0,1)*complexconjugate(DEL1x2)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1863 = Coupling(name = 'GC_1863',
                   value = '(cHud*ee*complexconjugate(DEL1x2)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1864 = Coupling(name = 'GC_1864',
                   value = '-((cHud*cw*ee*complexconjugate(DEL1x2)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1865 = Coupling(name = 'GC_1865',
                   value = '(cHud*cw*ee*complex(0,1)*complexconjugate(DEL1x2)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1866 = Coupling(name = 'GC_1866',
                   value = '-((cHud*complexconjugate(DEL1x2)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1867 = Coupling(name = 'GC_1867',
                   value = '-((cHud*ee*complexconjugate(DEL1x2)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1868 = Coupling(name = 'GC_1868',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL1x2)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1869 = Coupling(name = 'GC_1869',
                   value = '(cHud*ee*complexconjugate(DEL1x2)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1870 = Coupling(name = 'GC_1870',
                   value = '-((cHud*cw*ee*complexconjugate(DEL1x2)*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1871 = Coupling(name = 'GC_1871',
                   value = '-(cHd*cw*DEL2x1*ee*complex(0,1))/(4.*sw) - (cHd*DEL2x1*ee*complex(0,1)*sw)/(4.*cw) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL1x2))/(4.*sw) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL1x2))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_1872 = Coupling(name = 'GC_1872',
                   value = '-(cHu*cw*DEL2x1*ee*complex(0,1))/(4.*sw) - (cHu*DEL2x1*ee*complex(0,1)*sw)/(4.*cw) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL1x2))/(4.*sw) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL1x2))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_1873 = Coupling(name = 'GC_1873',
                   value = '-(cHd*DEL2x1*complex(0,1))/(2.*vev**2) - (cHd*complex(0,1)*complexconjugate(DEL1x2))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1874 = Coupling(name = 'GC_1874',
                   value = '(cHd*DEL2x1)/(2.*vev**2) + (cHd*complexconjugate(DEL1x2))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1875 = Coupling(name = 'GC_1875',
                   value = '-(cHu*DEL2x1*complex(0,1))/(2.*vev**2) - (cHu*complex(0,1)*complexconjugate(DEL1x2))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1876 = Coupling(name = 'GC_1876',
                   value = '(cHu*DEL2x1)/(2.*vev**2) + (cHu*complexconjugate(DEL1x2))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1877 = Coupling(name = 'GC_1877',
                   value = '(cHd*DEL2x1*ee*complex(0,1))/vev**2 + (cHd*ee*complex(0,1)*complexconjugate(DEL1x2))/vev**2',
                   order = {'NP':1,'QED':3})

GC_1878 = Coupling(name = 'GC_1878',
                   value = '(cHu*DEL2x1*ee*complex(0,1))/vev**2 + (cHu*ee*complex(0,1)*complexconjugate(DEL1x2))/vev**2',
                   order = {'NP':1,'QED':3})

GC_1879 = Coupling(name = 'GC_1879',
                   value = '-(cHd*DEL2x1*ee)/(2.*sw*vev**2) - (cHd*ee*complexconjugate(DEL1x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1880 = Coupling(name = 'GC_1880',
                   value = '-(cHd*DEL2x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*complexconjugate(DEL1x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1881 = Coupling(name = 'GC_1881',
                   value = '(cHd*DEL2x1*ee)/(2.*sw*vev**2) + (cHd*ee*complexconjugate(DEL1x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1882 = Coupling(name = 'GC_1882',
                   value = '-(cHu*DEL2x1*ee)/(2.*sw*vev**2) - (cHu*ee*complexconjugate(DEL1x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1883 = Coupling(name = 'GC_1883',
                   value = '-(cHu*DEL2x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*complexconjugate(DEL1x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1884 = Coupling(name = 'GC_1884',
                   value = '(cHu*DEL2x1*ee)/(2.*sw*vev**2) + (cHu*ee*complexconjugate(DEL1x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1885 = Coupling(name = 'GC_1885',
                   value = '-(cHd*cw*DEL2x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL2x1*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL1x2))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL1x2))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1886 = Coupling(name = 'GC_1886',
                   value = '(cHd*cw*DEL2x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL2x1*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHd*cw*ee*complex(0,1)*complexconjugate(DEL1x2))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL1x2))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1887 = Coupling(name = 'GC_1887',
                   value = '-(cHu*cw*DEL2x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL2x1*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL1x2))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL1x2))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1888 = Coupling(name = 'GC_1888',
                   value = '(cHu*cw*DEL2x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL2x1*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHu*cw*ee*complex(0,1)*complexconjugate(DEL1x2))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL1x2))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1889 = Coupling(name = 'GC_1889',
                   value = '(cHd*DEL2x1)/(2.*vev) + (cHd*complexconjugate(DEL1x2))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1890 = Coupling(name = 'GC_1890',
                   value = '(cHu*DEL2x1)/(2.*vev) + (cHu*complexconjugate(DEL1x2))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1891 = Coupling(name = 'GC_1891',
                   value = '-(cHd*DEL2x1*ee)/(2.*sw*vev) - (cHd*ee*complexconjugate(DEL1x2))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1892 = Coupling(name = 'GC_1892',
                   value = '(cHd*DEL2x1*ee)/(2.*sw*vev) + (cHd*ee*complexconjugate(DEL1x2))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1893 = Coupling(name = 'GC_1893',
                   value = '-(cHu*DEL2x1*ee)/(2.*sw*vev) - (cHu*ee*complexconjugate(DEL1x2))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1894 = Coupling(name = 'GC_1894',
                   value = '(cHu*DEL2x1*ee)/(2.*sw*vev) + (cHu*ee*complexconjugate(DEL1x2))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1895 = Coupling(name = 'GC_1895',
                   value = '-(cHd*cw*DEL2x1*ee*complex(0,1))/(2.*sw*vev) - (cHd*DEL2x1*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL1x2))/(2.*sw*vev) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL1x2))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1896 = Coupling(name = 'GC_1896',
                   value = '-(cHu*cw*DEL2x1*ee*complex(0,1))/(2.*sw*vev) - (cHu*DEL2x1*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL1x2))/(2.*sw*vev) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL1x2))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1897 = Coupling(name = 'GC_1897',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL1x3))/(sw*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1898 = Coupling(name = 'GC_1898',
                   value = '-((cHud*complexconjugate(DEL1x3)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_1899 = Coupling(name = 'GC_1899',
                   value = '-((cHud*complex(0,1)*complexconjugate(DEL1x3)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_1900 = Coupling(name = 'GC_1900',
                   value = '-((cHud*ee*complexconjugate(DEL1x3)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':3})

GC_1901 = Coupling(name = 'GC_1901',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL1x3)*cmath.sqrt(2))/vev**2',
                   order = {'NP':1,'QED':3})

GC_1902 = Coupling(name = 'GC_1902',
                   value = '-((cHud*ee*complex(0,1)*complexconjugate(DEL1x3)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1903 = Coupling(name = 'GC_1903',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL1x3)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1904 = Coupling(name = 'GC_1904',
                   value = '(2*cHud*ee*complex(0,1)*complexconjugate(DEL1x3)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1905 = Coupling(name = 'GC_1905',
                   value = '(cHud*ee*complexconjugate(DEL1x3)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1906 = Coupling(name = 'GC_1906',
                   value = '-((cHud*cw*ee*complexconjugate(DEL1x3)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1907 = Coupling(name = 'GC_1907',
                   value = '(cHud*cw*ee*complex(0,1)*complexconjugate(DEL1x3)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1908 = Coupling(name = 'GC_1908',
                   value = '-((cHud*complexconjugate(DEL1x3)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1909 = Coupling(name = 'GC_1909',
                   value = '-((cHud*ee*complexconjugate(DEL1x3)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1910 = Coupling(name = 'GC_1910',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL1x3)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1911 = Coupling(name = 'GC_1911',
                   value = '(cHud*ee*complexconjugate(DEL1x3)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1912 = Coupling(name = 'GC_1912',
                   value = '-((cHud*cw*ee*complexconjugate(DEL1x3)*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1913 = Coupling(name = 'GC_1913',
                   value = '-(cHd*cw*DEL3x1*ee*complex(0,1))/(4.*sw) - (cHd*DEL3x1*ee*complex(0,1)*sw)/(4.*cw) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL1x3))/(4.*sw) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL1x3))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_1914 = Coupling(name = 'GC_1914',
                   value = '-(cHu*cw*DEL3x1*ee*complex(0,1))/(4.*sw) - (cHu*DEL3x1*ee*complex(0,1)*sw)/(4.*cw) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL1x3))/(4.*sw) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL1x3))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_1915 = Coupling(name = 'GC_1915',
                   value = '-(cHd*DEL3x1*complex(0,1))/(2.*vev**2) - (cHd*complex(0,1)*complexconjugate(DEL1x3))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1916 = Coupling(name = 'GC_1916',
                   value = '(cHd*DEL3x1)/(2.*vev**2) + (cHd*complexconjugate(DEL1x3))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1917 = Coupling(name = 'GC_1917',
                   value = '-(cHu*DEL3x1*complex(0,1))/(2.*vev**2) - (cHu*complex(0,1)*complexconjugate(DEL1x3))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1918 = Coupling(name = 'GC_1918',
                   value = '(cHu*DEL3x1)/(2.*vev**2) + (cHu*complexconjugate(DEL1x3))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1919 = Coupling(name = 'GC_1919',
                   value = '(cHd*DEL3x1*ee*complex(0,1))/vev**2 + (cHd*ee*complex(0,1)*complexconjugate(DEL1x3))/vev**2',
                   order = {'NP':1,'QED':3})

GC_1920 = Coupling(name = 'GC_1920',
                   value = '(cHu*DEL3x1*ee*complex(0,1))/vev**2 + (cHu*ee*complex(0,1)*complexconjugate(DEL1x3))/vev**2',
                   order = {'NP':1,'QED':3})

GC_1921 = Coupling(name = 'GC_1921',
                   value = '-(cHd*DEL3x1*ee)/(2.*sw*vev**2) - (cHd*ee*complexconjugate(DEL1x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1922 = Coupling(name = 'GC_1922',
                   value = '-(cHd*DEL3x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*complexconjugate(DEL1x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1923 = Coupling(name = 'GC_1923',
                   value = '(cHd*DEL3x1*ee)/(2.*sw*vev**2) + (cHd*ee*complexconjugate(DEL1x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1924 = Coupling(name = 'GC_1924',
                   value = '-(cHu*DEL3x1*ee)/(2.*sw*vev**2) - (cHu*ee*complexconjugate(DEL1x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1925 = Coupling(name = 'GC_1925',
                   value = '-(cHu*DEL3x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*complexconjugate(DEL1x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1926 = Coupling(name = 'GC_1926',
                   value = '(cHu*DEL3x1*ee)/(2.*sw*vev**2) + (cHu*ee*complexconjugate(DEL1x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1927 = Coupling(name = 'GC_1927',
                   value = '-(cHd*cw*DEL3x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL3x1*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL1x3))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL1x3))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1928 = Coupling(name = 'GC_1928',
                   value = '(cHd*cw*DEL3x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL3x1*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHd*cw*ee*complex(0,1)*complexconjugate(DEL1x3))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL1x3))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1929 = Coupling(name = 'GC_1929',
                   value = '-(cHu*cw*DEL3x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL3x1*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL1x3))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL1x3))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1930 = Coupling(name = 'GC_1930',
                   value = '(cHu*cw*DEL3x1*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL3x1*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHu*cw*ee*complex(0,1)*complexconjugate(DEL1x3))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL1x3))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1931 = Coupling(name = 'GC_1931',
                   value = '(cHd*DEL3x1)/(2.*vev) + (cHd*complexconjugate(DEL1x3))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1932 = Coupling(name = 'GC_1932',
                   value = '(cHu*DEL3x1)/(2.*vev) + (cHu*complexconjugate(DEL1x3))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1933 = Coupling(name = 'GC_1933',
                   value = '-(cHd*DEL3x1*ee)/(2.*sw*vev) - (cHd*ee*complexconjugate(DEL1x3))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1934 = Coupling(name = 'GC_1934',
                   value = '(cHd*DEL3x1*ee)/(2.*sw*vev) + (cHd*ee*complexconjugate(DEL1x3))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1935 = Coupling(name = 'GC_1935',
                   value = '-(cHu*DEL3x1*ee)/(2.*sw*vev) - (cHu*ee*complexconjugate(DEL1x3))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1936 = Coupling(name = 'GC_1936',
                   value = '(cHu*DEL3x1*ee)/(2.*sw*vev) + (cHu*ee*complexconjugate(DEL1x3))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1937 = Coupling(name = 'GC_1937',
                   value = '-(cHd*cw*DEL3x1*ee*complex(0,1))/(2.*sw*vev) - (cHd*DEL3x1*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL1x3))/(2.*sw*vev) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL1x3))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1938 = Coupling(name = 'GC_1938',
                   value = '-(cHu*cw*DEL3x1*ee*complex(0,1))/(2.*sw*vev) - (cHu*DEL3x1*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL1x3))/(2.*sw*vev) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL1x3))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1939 = Coupling(name = 'GC_1939',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL2x1))/(sw*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1940 = Coupling(name = 'GC_1940',
                   value = '-((cHud*complexconjugate(DEL2x1)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_1941 = Coupling(name = 'GC_1941',
                   value = '-((cHud*complex(0,1)*complexconjugate(DEL2x1)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_1942 = Coupling(name = 'GC_1942',
                   value = '-((cHud*ee*complexconjugate(DEL2x1)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':3})

GC_1943 = Coupling(name = 'GC_1943',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL2x1)*cmath.sqrt(2))/vev**2',
                   order = {'NP':1,'QED':3})

GC_1944 = Coupling(name = 'GC_1944',
                   value = '-((cHud*ee*complex(0,1)*complexconjugate(DEL2x1)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1945 = Coupling(name = 'GC_1945',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL2x1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1946 = Coupling(name = 'GC_1946',
                   value = '(2*cHud*ee*complex(0,1)*complexconjugate(DEL2x1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1947 = Coupling(name = 'GC_1947',
                   value = '(cHud*ee*complexconjugate(DEL2x1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1948 = Coupling(name = 'GC_1948',
                   value = '-((cHud*cw*ee*complexconjugate(DEL2x1)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1949 = Coupling(name = 'GC_1949',
                   value = '(cHud*cw*ee*complex(0,1)*complexconjugate(DEL2x1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1950 = Coupling(name = 'GC_1950',
                   value = '-((cHud*complexconjugate(DEL2x1)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1951 = Coupling(name = 'GC_1951',
                   value = '-((cHud*ee*complexconjugate(DEL2x1)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1952 = Coupling(name = 'GC_1952',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL2x1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1953 = Coupling(name = 'GC_1953',
                   value = '(cHud*ee*complexconjugate(DEL2x1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1954 = Coupling(name = 'GC_1954',
                   value = '-((cHud*cw*ee*complexconjugate(DEL2x1)*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1955 = Coupling(name = 'GC_1955',
                   value = '-(cHd*cw*DEL1x2*ee*complex(0,1))/(4.*sw) - (cHd*DEL1x2*ee*complex(0,1)*sw)/(4.*cw) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL2x1))/(4.*sw) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL2x1))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_1956 = Coupling(name = 'GC_1956',
                   value = '-(cHu*cw*DEL1x2*ee*complex(0,1))/(4.*sw) - (cHu*DEL1x2*ee*complex(0,1)*sw)/(4.*cw) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL2x1))/(4.*sw) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL2x1))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_1957 = Coupling(name = 'GC_1957',
                   value = '-(cHd*DEL1x2*complex(0,1))/(2.*vev**2) - (cHd*complex(0,1)*complexconjugate(DEL2x1))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1958 = Coupling(name = 'GC_1958',
                   value = '(cHd*DEL1x2)/(2.*vev**2) + (cHd*complexconjugate(DEL2x1))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1959 = Coupling(name = 'GC_1959',
                   value = '-(cHu*DEL1x2*complex(0,1))/(2.*vev**2) - (cHu*complex(0,1)*complexconjugate(DEL2x1))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1960 = Coupling(name = 'GC_1960',
                   value = '(cHu*DEL1x2)/(2.*vev**2) + (cHu*complexconjugate(DEL2x1))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_1961 = Coupling(name = 'GC_1961',
                   value = '(cHd*DEL1x2*ee*complex(0,1))/vev**2 + (cHd*ee*complex(0,1)*complexconjugate(DEL2x1))/vev**2',
                   order = {'NP':1,'QED':3})

GC_1962 = Coupling(name = 'GC_1962',
                   value = '(cHu*DEL1x2*ee*complex(0,1))/vev**2 + (cHu*ee*complex(0,1)*complexconjugate(DEL2x1))/vev**2',
                   order = {'NP':1,'QED':3})

GC_1963 = Coupling(name = 'GC_1963',
                   value = '-(cHd*DEL1x2*ee)/(2.*sw*vev**2) - (cHd*ee*complexconjugate(DEL2x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1964 = Coupling(name = 'GC_1964',
                   value = '-(cHd*DEL1x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*complexconjugate(DEL2x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1965 = Coupling(name = 'GC_1965',
                   value = '(cHd*DEL1x2*ee)/(2.*sw*vev**2) + (cHd*ee*complexconjugate(DEL2x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1966 = Coupling(name = 'GC_1966',
                   value = '-(cHu*DEL1x2*ee)/(2.*sw*vev**2) - (cHu*ee*complexconjugate(DEL2x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1967 = Coupling(name = 'GC_1967',
                   value = '-(cHu*DEL1x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*complexconjugate(DEL2x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1968 = Coupling(name = 'GC_1968',
                   value = '(cHu*DEL1x2*ee)/(2.*sw*vev**2) + (cHu*ee*complexconjugate(DEL2x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1969 = Coupling(name = 'GC_1969',
                   value = '-(cHd*cw*DEL1x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL1x2*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL2x1))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL2x1))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1970 = Coupling(name = 'GC_1970',
                   value = '(cHd*cw*DEL1x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL1x2*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHd*cw*ee*complex(0,1)*complexconjugate(DEL2x1))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL2x1))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1971 = Coupling(name = 'GC_1971',
                   value = '-(cHu*cw*DEL1x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL1x2*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL2x1))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL2x1))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1972 = Coupling(name = 'GC_1972',
                   value = '(cHu*cw*DEL1x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL1x2*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHu*cw*ee*complex(0,1)*complexconjugate(DEL2x1))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL2x1))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1973 = Coupling(name = 'GC_1973',
                   value = '(cHd*DEL1x2)/(2.*vev) + (cHd*complexconjugate(DEL2x1))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1974 = Coupling(name = 'GC_1974',
                   value = '(cHu*DEL1x2)/(2.*vev) + (cHu*complexconjugate(DEL2x1))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_1975 = Coupling(name = 'GC_1975',
                   value = '-(cHd*DEL1x2*ee)/(2.*sw*vev) - (cHd*ee*complexconjugate(DEL2x1))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1976 = Coupling(name = 'GC_1976',
                   value = '(cHd*DEL1x2*ee)/(2.*sw*vev) + (cHd*ee*complexconjugate(DEL2x1))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1977 = Coupling(name = 'GC_1977',
                   value = '-(cHu*DEL1x2*ee)/(2.*sw*vev) - (cHu*ee*complexconjugate(DEL2x1))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1978 = Coupling(name = 'GC_1978',
                   value = '(cHu*DEL1x2*ee)/(2.*sw*vev) + (cHu*ee*complexconjugate(DEL2x1))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1979 = Coupling(name = 'GC_1979',
                   value = '-(cHd*cw*DEL1x2*ee*complex(0,1))/(2.*sw*vev) - (cHd*DEL1x2*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL2x1))/(2.*sw*vev) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL2x1))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1980 = Coupling(name = 'GC_1980',
                   value = '-(cHu*cw*DEL1x2*ee*complex(0,1))/(2.*sw*vev) - (cHu*DEL1x2*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL2x1))/(2.*sw*vev) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL2x1))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_1981 = Coupling(name = 'GC_1981',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL2x2))/(sw*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1982 = Coupling(name = 'GC_1982',
                   value = '-((cHud*complexconjugate(DEL2x2)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_1983 = Coupling(name = 'GC_1983',
                   value = '-((cHud*complex(0,1)*complexconjugate(DEL2x2)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_1984 = Coupling(name = 'GC_1984',
                   value = '-((cHud*ee*complexconjugate(DEL2x2)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':3})

GC_1985 = Coupling(name = 'GC_1985',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL2x2)*cmath.sqrt(2))/vev**2',
                   order = {'NP':1,'QED':3})

GC_1986 = Coupling(name = 'GC_1986',
                   value = '-((cHud*ee*complex(0,1)*complexconjugate(DEL2x2)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1987 = Coupling(name = 'GC_1987',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL2x2)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1988 = Coupling(name = 'GC_1988',
                   value = '(2*cHud*ee*complex(0,1)*complexconjugate(DEL2x2)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1989 = Coupling(name = 'GC_1989',
                   value = '(cHud*ee*complexconjugate(DEL2x2)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1990 = Coupling(name = 'GC_1990',
                   value = '-((cHud*cw*ee*complexconjugate(DEL2x2)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_1991 = Coupling(name = 'GC_1991',
                   value = '(cHud*cw*ee*complex(0,1)*complexconjugate(DEL2x2)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_1992 = Coupling(name = 'GC_1992',
                   value = '-((cHud*complexconjugate(DEL2x2)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_1993 = Coupling(name = 'GC_1993',
                   value = '-((cHud*ee*complexconjugate(DEL2x2)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_1994 = Coupling(name = 'GC_1994',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL2x2)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1995 = Coupling(name = 'GC_1995',
                   value = '(cHud*ee*complexconjugate(DEL2x2)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_1996 = Coupling(name = 'GC_1996',
                   value = '-((cHud*cw*ee*complexconjugate(DEL2x2)*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_1997 = Coupling(name = 'GC_1997',
                   value = '-(cHd*cw*DEL2x2*ee*complex(0,1))/(4.*sw) - (cHd*DEL2x2*ee*complex(0,1)*sw)/(4.*cw) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL2x2))/(4.*sw) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL2x2))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_1998 = Coupling(name = 'GC_1998',
                   value = '-(cHu*cw*DEL2x2*ee*complex(0,1))/(4.*sw) - (cHu*DEL2x2*ee*complex(0,1)*sw)/(4.*cw) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL2x2))/(4.*sw) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL2x2))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_1999 = Coupling(name = 'GC_1999',
                   value = '-(cHd*DEL2x2*complex(0,1))/(2.*vev**2) - (cHd*complex(0,1)*complexconjugate(DEL2x2))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2000 = Coupling(name = 'GC_2000',
                   value = '(cHd*DEL2x2)/(2.*vev**2) + (cHd*complexconjugate(DEL2x2))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2001 = Coupling(name = 'GC_2001',
                   value = '-(cHu*DEL2x2*complex(0,1))/(2.*vev**2) - (cHu*complex(0,1)*complexconjugate(DEL2x2))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2002 = Coupling(name = 'GC_2002',
                   value = '(cHu*DEL2x2)/(2.*vev**2) + (cHu*complexconjugate(DEL2x2))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2003 = Coupling(name = 'GC_2003',
                   value = '(cHd*DEL2x2*ee*complex(0,1))/vev**2 + (cHd*ee*complex(0,1)*complexconjugate(DEL2x2))/vev**2',
                   order = {'NP':1,'QED':3})

GC_2004 = Coupling(name = 'GC_2004',
                   value = '(cHu*DEL2x2*ee*complex(0,1))/vev**2 + (cHu*ee*complex(0,1)*complexconjugate(DEL2x2))/vev**2',
                   order = {'NP':1,'QED':3})

GC_2005 = Coupling(name = 'GC_2005',
                   value = '-(cHd*DEL2x2*ee)/(2.*sw*vev**2) - (cHd*ee*complexconjugate(DEL2x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2006 = Coupling(name = 'GC_2006',
                   value = '-(cHd*DEL2x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*complexconjugate(DEL2x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2007 = Coupling(name = 'GC_2007',
                   value = '(cHd*DEL2x2*ee)/(2.*sw*vev**2) + (cHd*ee*complexconjugate(DEL2x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2008 = Coupling(name = 'GC_2008',
                   value = '-(cHu*DEL2x2*ee)/(2.*sw*vev**2) - (cHu*ee*complexconjugate(DEL2x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2009 = Coupling(name = 'GC_2009',
                   value = '-(cHu*DEL2x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*complexconjugate(DEL2x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2010 = Coupling(name = 'GC_2010',
                   value = '(cHu*DEL2x2*ee)/(2.*sw*vev**2) + (cHu*ee*complexconjugate(DEL2x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2011 = Coupling(name = 'GC_2011',
                   value = '-(cHd*cw*DEL2x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL2x2*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL2x2))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL2x2))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2012 = Coupling(name = 'GC_2012',
                   value = '(cHd*cw*DEL2x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL2x2*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHd*cw*ee*complex(0,1)*complexconjugate(DEL2x2))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL2x2))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2013 = Coupling(name = 'GC_2013',
                   value = '-(cHu*cw*DEL2x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL2x2*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL2x2))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL2x2))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2014 = Coupling(name = 'GC_2014',
                   value = '(cHu*cw*DEL2x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL2x2*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHu*cw*ee*complex(0,1)*complexconjugate(DEL2x2))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL2x2))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2015 = Coupling(name = 'GC_2015',
                   value = '(cHd*DEL2x2)/(2.*vev) + (cHd*complexconjugate(DEL2x2))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_2016 = Coupling(name = 'GC_2016',
                   value = '(cHu*DEL2x2)/(2.*vev) + (cHu*complexconjugate(DEL2x2))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_2017 = Coupling(name = 'GC_2017',
                   value = '-(cHd*DEL2x2*ee)/(2.*sw*vev) - (cHd*ee*complexconjugate(DEL2x2))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2018 = Coupling(name = 'GC_2018',
                   value = '(cHd*DEL2x2*ee)/(2.*sw*vev) + (cHd*ee*complexconjugate(DEL2x2))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2019 = Coupling(name = 'GC_2019',
                   value = '-(cHu*DEL2x2*ee)/(2.*sw*vev) - (cHu*ee*complexconjugate(DEL2x2))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2020 = Coupling(name = 'GC_2020',
                   value = '(cHu*DEL2x2*ee)/(2.*sw*vev) + (cHu*ee*complexconjugate(DEL2x2))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2021 = Coupling(name = 'GC_2021',
                   value = '-(cHd*cw*DEL2x2*ee*complex(0,1))/(2.*sw*vev) - (cHd*DEL2x2*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL2x2))/(2.*sw*vev) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL2x2))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_2022 = Coupling(name = 'GC_2022',
                   value = '-(cHu*cw*DEL2x2*ee*complex(0,1))/(2.*sw*vev) - (cHu*DEL2x2*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL2x2))/(2.*sw*vev) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL2x2))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_2023 = Coupling(name = 'GC_2023',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL2x3))/(sw*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2024 = Coupling(name = 'GC_2024',
                   value = '-((cHud*complexconjugate(DEL2x3)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_2025 = Coupling(name = 'GC_2025',
                   value = '-((cHud*complex(0,1)*complexconjugate(DEL2x3)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_2026 = Coupling(name = 'GC_2026',
                   value = '-((cHud*ee*complexconjugate(DEL2x3)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':3})

GC_2027 = Coupling(name = 'GC_2027',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL2x3)*cmath.sqrt(2))/vev**2',
                   order = {'NP':1,'QED':3})

GC_2028 = Coupling(name = 'GC_2028',
                   value = '-((cHud*ee*complex(0,1)*complexconjugate(DEL2x3)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_2029 = Coupling(name = 'GC_2029',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL2x3)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2030 = Coupling(name = 'GC_2030',
                   value = '(2*cHud*ee*complex(0,1)*complexconjugate(DEL2x3)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2031 = Coupling(name = 'GC_2031',
                   value = '(cHud*ee*complexconjugate(DEL2x3)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2032 = Coupling(name = 'GC_2032',
                   value = '-((cHud*cw*ee*complexconjugate(DEL2x3)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_2033 = Coupling(name = 'GC_2033',
                   value = '(cHud*cw*ee*complex(0,1)*complexconjugate(DEL2x3)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2034 = Coupling(name = 'GC_2034',
                   value = '-((cHud*complexconjugate(DEL2x3)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_2035 = Coupling(name = 'GC_2035',
                   value = '-((cHud*ee*complexconjugate(DEL2x3)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_2036 = Coupling(name = 'GC_2036',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL2x3)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2037 = Coupling(name = 'GC_2037',
                   value = '(cHud*ee*complexconjugate(DEL2x3)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2038 = Coupling(name = 'GC_2038',
                   value = '-((cHud*cw*ee*complexconjugate(DEL2x3)*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_2039 = Coupling(name = 'GC_2039',
                   value = '-(cHd*cw*DEL3x2*ee*complex(0,1))/(4.*sw) - (cHd*DEL3x2*ee*complex(0,1)*sw)/(4.*cw) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL2x3))/(4.*sw) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL2x3))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_2040 = Coupling(name = 'GC_2040',
                   value = '-(cHu*cw*DEL3x2*ee*complex(0,1))/(4.*sw) - (cHu*DEL3x2*ee*complex(0,1)*sw)/(4.*cw) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL2x3))/(4.*sw) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL2x3))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_2041 = Coupling(name = 'GC_2041',
                   value = '-(cHd*DEL3x2*complex(0,1))/(2.*vev**2) - (cHd*complex(0,1)*complexconjugate(DEL2x3))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2042 = Coupling(name = 'GC_2042',
                   value = '(cHd*DEL3x2)/(2.*vev**2) + (cHd*complexconjugate(DEL2x3))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2043 = Coupling(name = 'GC_2043',
                   value = '-(cHu*DEL3x2*complex(0,1))/(2.*vev**2) - (cHu*complex(0,1)*complexconjugate(DEL2x3))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2044 = Coupling(name = 'GC_2044',
                   value = '(cHu*DEL3x2)/(2.*vev**2) + (cHu*complexconjugate(DEL2x3))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2045 = Coupling(name = 'GC_2045',
                   value = '(cHd*DEL3x2*ee*complex(0,1))/vev**2 + (cHd*ee*complex(0,1)*complexconjugate(DEL2x3))/vev**2',
                   order = {'NP':1,'QED':3})

GC_2046 = Coupling(name = 'GC_2046',
                   value = '(cHu*DEL3x2*ee*complex(0,1))/vev**2 + (cHu*ee*complex(0,1)*complexconjugate(DEL2x3))/vev**2',
                   order = {'NP':1,'QED':3})

GC_2047 = Coupling(name = 'GC_2047',
                   value = '-(cHd*DEL3x2*ee)/(2.*sw*vev**2) - (cHd*ee*complexconjugate(DEL2x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2048 = Coupling(name = 'GC_2048',
                   value = '-(cHd*DEL3x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*complexconjugate(DEL2x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2049 = Coupling(name = 'GC_2049',
                   value = '(cHd*DEL3x2*ee)/(2.*sw*vev**2) + (cHd*ee*complexconjugate(DEL2x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2050 = Coupling(name = 'GC_2050',
                   value = '-(cHu*DEL3x2*ee)/(2.*sw*vev**2) - (cHu*ee*complexconjugate(DEL2x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2051 = Coupling(name = 'GC_2051',
                   value = '-(cHu*DEL3x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*complexconjugate(DEL2x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2052 = Coupling(name = 'GC_2052',
                   value = '(cHu*DEL3x2*ee)/(2.*sw*vev**2) + (cHu*ee*complexconjugate(DEL2x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2053 = Coupling(name = 'GC_2053',
                   value = '-(cHd*cw*DEL3x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL3x2*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL2x3))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL2x3))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2054 = Coupling(name = 'GC_2054',
                   value = '(cHd*cw*DEL3x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL3x2*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHd*cw*ee*complex(0,1)*complexconjugate(DEL2x3))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL2x3))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2055 = Coupling(name = 'GC_2055',
                   value = '-(cHu*cw*DEL3x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL3x2*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL2x3))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL2x3))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2056 = Coupling(name = 'GC_2056',
                   value = '(cHu*cw*DEL3x2*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL3x2*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHu*cw*ee*complex(0,1)*complexconjugate(DEL2x3))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL2x3))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2057 = Coupling(name = 'GC_2057',
                   value = '(cHd*DEL3x2)/(2.*vev) + (cHd*complexconjugate(DEL2x3))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_2058 = Coupling(name = 'GC_2058',
                   value = '(cHu*DEL3x2)/(2.*vev) + (cHu*complexconjugate(DEL2x3))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_2059 = Coupling(name = 'GC_2059',
                   value = '-(cHd*DEL3x2*ee)/(2.*sw*vev) - (cHd*ee*complexconjugate(DEL2x3))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2060 = Coupling(name = 'GC_2060',
                   value = '(cHd*DEL3x2*ee)/(2.*sw*vev) + (cHd*ee*complexconjugate(DEL2x3))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2061 = Coupling(name = 'GC_2061',
                   value = '-(cHu*DEL3x2*ee)/(2.*sw*vev) - (cHu*ee*complexconjugate(DEL2x3))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2062 = Coupling(name = 'GC_2062',
                   value = '(cHu*DEL3x2*ee)/(2.*sw*vev) + (cHu*ee*complexconjugate(DEL2x3))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2063 = Coupling(name = 'GC_2063',
                   value = '-(cHd*cw*DEL3x2*ee*complex(0,1))/(2.*sw*vev) - (cHd*DEL3x2*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL2x3))/(2.*sw*vev) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL2x3))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_2064 = Coupling(name = 'GC_2064',
                   value = '-(cHu*cw*DEL3x2*ee*complex(0,1))/(2.*sw*vev) - (cHu*DEL3x2*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL2x3))/(2.*sw*vev) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL2x3))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_2065 = Coupling(name = 'GC_2065',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL3x1))/(sw*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2066 = Coupling(name = 'GC_2066',
                   value = '-((cHud*complexconjugate(DEL3x1)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_2067 = Coupling(name = 'GC_2067',
                   value = '-((cHud*complex(0,1)*complexconjugate(DEL3x1)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_2068 = Coupling(name = 'GC_2068',
                   value = '-((cHud*ee*complexconjugate(DEL3x1)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':3})

GC_2069 = Coupling(name = 'GC_2069',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL3x1)*cmath.sqrt(2))/vev**2',
                   order = {'NP':1,'QED':3})

GC_2070 = Coupling(name = 'GC_2070',
                   value = '-((cHud*ee*complex(0,1)*complexconjugate(DEL3x1)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_2071 = Coupling(name = 'GC_2071',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL3x1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2072 = Coupling(name = 'GC_2072',
                   value = '(2*cHud*ee*complex(0,1)*complexconjugate(DEL3x1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2073 = Coupling(name = 'GC_2073',
                   value = '(cHud*ee*complexconjugate(DEL3x1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2074 = Coupling(name = 'GC_2074',
                   value = '-((cHud*cw*ee*complexconjugate(DEL3x1)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_2075 = Coupling(name = 'GC_2075',
                   value = '(cHud*cw*ee*complex(0,1)*complexconjugate(DEL3x1)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2076 = Coupling(name = 'GC_2076',
                   value = '-((cHud*complexconjugate(DEL3x1)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_2077 = Coupling(name = 'GC_2077',
                   value = '-((cHud*ee*complexconjugate(DEL3x1)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_2078 = Coupling(name = 'GC_2078',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL3x1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2079 = Coupling(name = 'GC_2079',
                   value = '(cHud*ee*complexconjugate(DEL3x1)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2080 = Coupling(name = 'GC_2080',
                   value = '-((cHud*cw*ee*complexconjugate(DEL3x1)*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_2081 = Coupling(name = 'GC_2081',
                   value = '-(cHd*cw*DEL1x3*ee*complex(0,1))/(4.*sw) - (cHd*DEL1x3*ee*complex(0,1)*sw)/(4.*cw) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL3x1))/(4.*sw) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL3x1))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_2082 = Coupling(name = 'GC_2082',
                   value = '-(cHu*cw*DEL1x3*ee*complex(0,1))/(4.*sw) - (cHu*DEL1x3*ee*complex(0,1)*sw)/(4.*cw) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL3x1))/(4.*sw) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL3x1))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_2083 = Coupling(name = 'GC_2083',
                   value = '-(cHd*DEL1x3*complex(0,1))/(2.*vev**2) - (cHd*complex(0,1)*complexconjugate(DEL3x1))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2084 = Coupling(name = 'GC_2084',
                   value = '(cHd*DEL1x3)/(2.*vev**2) + (cHd*complexconjugate(DEL3x1))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2085 = Coupling(name = 'GC_2085',
                   value = '-(cHu*DEL1x3*complex(0,1))/(2.*vev**2) - (cHu*complex(0,1)*complexconjugate(DEL3x1))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2086 = Coupling(name = 'GC_2086',
                   value = '(cHu*DEL1x3)/(2.*vev**2) + (cHu*complexconjugate(DEL3x1))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2087 = Coupling(name = 'GC_2087',
                   value = '(cHd*DEL1x3*ee*complex(0,1))/vev**2 + (cHd*ee*complex(0,1)*complexconjugate(DEL3x1))/vev**2',
                   order = {'NP':1,'QED':3})

GC_2088 = Coupling(name = 'GC_2088',
                   value = '(cHu*DEL1x3*ee*complex(0,1))/vev**2 + (cHu*ee*complex(0,1)*complexconjugate(DEL3x1))/vev**2',
                   order = {'NP':1,'QED':3})

GC_2089 = Coupling(name = 'GC_2089',
                   value = '-(cHd*DEL1x3*ee)/(2.*sw*vev**2) - (cHd*ee*complexconjugate(DEL3x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2090 = Coupling(name = 'GC_2090',
                   value = '-(cHd*DEL1x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*complexconjugate(DEL3x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2091 = Coupling(name = 'GC_2091',
                   value = '(cHd*DEL1x3*ee)/(2.*sw*vev**2) + (cHd*ee*complexconjugate(DEL3x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2092 = Coupling(name = 'GC_2092',
                   value = '-(cHu*DEL1x3*ee)/(2.*sw*vev**2) - (cHu*ee*complexconjugate(DEL3x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2093 = Coupling(name = 'GC_2093',
                   value = '-(cHu*DEL1x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*complexconjugate(DEL3x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2094 = Coupling(name = 'GC_2094',
                   value = '(cHu*DEL1x3*ee)/(2.*sw*vev**2) + (cHu*ee*complexconjugate(DEL3x1))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2095 = Coupling(name = 'GC_2095',
                   value = '-(cHd*cw*DEL1x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL1x3*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL3x1))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL3x1))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2096 = Coupling(name = 'GC_2096',
                   value = '(cHd*cw*DEL1x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL1x3*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHd*cw*ee*complex(0,1)*complexconjugate(DEL3x1))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL3x1))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2097 = Coupling(name = 'GC_2097',
                   value = '-(cHu*cw*DEL1x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL1x3*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL3x1))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL3x1))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2098 = Coupling(name = 'GC_2098',
                   value = '(cHu*cw*DEL1x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL1x3*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHu*cw*ee*complex(0,1)*complexconjugate(DEL3x1))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL3x1))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2099 = Coupling(name = 'GC_2099',
                   value = '(cHd*DEL1x3)/(2.*vev) + (cHd*complexconjugate(DEL3x1))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_2100 = Coupling(name = 'GC_2100',
                   value = '(cHu*DEL1x3)/(2.*vev) + (cHu*complexconjugate(DEL3x1))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_2101 = Coupling(name = 'GC_2101',
                   value = '-(cHd*DEL1x3*ee)/(2.*sw*vev) - (cHd*ee*complexconjugate(DEL3x1))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2102 = Coupling(name = 'GC_2102',
                   value = '(cHd*DEL1x3*ee)/(2.*sw*vev) + (cHd*ee*complexconjugate(DEL3x1))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2103 = Coupling(name = 'GC_2103',
                   value = '-(cHu*DEL1x3*ee)/(2.*sw*vev) - (cHu*ee*complexconjugate(DEL3x1))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2104 = Coupling(name = 'GC_2104',
                   value = '(cHu*DEL1x3*ee)/(2.*sw*vev) + (cHu*ee*complexconjugate(DEL3x1))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2105 = Coupling(name = 'GC_2105',
                   value = '-(cHd*cw*DEL1x3*ee*complex(0,1))/(2.*sw*vev) - (cHd*DEL1x3*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL3x1))/(2.*sw*vev) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL3x1))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_2106 = Coupling(name = 'GC_2106',
                   value = '-(cHu*cw*DEL1x3*ee*complex(0,1))/(2.*sw*vev) - (cHu*DEL1x3*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL3x1))/(2.*sw*vev) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL3x1))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_2107 = Coupling(name = 'GC_2107',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL3x2))/(sw*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2108 = Coupling(name = 'GC_2108',
                   value = '-((cHud*complexconjugate(DEL3x2)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_2109 = Coupling(name = 'GC_2109',
                   value = '-((cHud*complex(0,1)*complexconjugate(DEL3x2)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_2110 = Coupling(name = 'GC_2110',
                   value = '-((cHud*ee*complexconjugate(DEL3x2)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':3})

GC_2111 = Coupling(name = 'GC_2111',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL3x2)*cmath.sqrt(2))/vev**2',
                   order = {'NP':1,'QED':3})

GC_2112 = Coupling(name = 'GC_2112',
                   value = '-((cHud*ee*complex(0,1)*complexconjugate(DEL3x2)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_2113 = Coupling(name = 'GC_2113',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL3x2)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2114 = Coupling(name = 'GC_2114',
                   value = '(2*cHud*ee*complex(0,1)*complexconjugate(DEL3x2)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2115 = Coupling(name = 'GC_2115',
                   value = '(cHud*ee*complexconjugate(DEL3x2)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2116 = Coupling(name = 'GC_2116',
                   value = '-((cHud*cw*ee*complexconjugate(DEL3x2)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_2117 = Coupling(name = 'GC_2117',
                   value = '(cHud*cw*ee*complex(0,1)*complexconjugate(DEL3x2)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2118 = Coupling(name = 'GC_2118',
                   value = '-((cHud*complexconjugate(DEL3x2)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_2119 = Coupling(name = 'GC_2119',
                   value = '-((cHud*ee*complexconjugate(DEL3x2)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_2120 = Coupling(name = 'GC_2120',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL3x2)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2121 = Coupling(name = 'GC_2121',
                   value = '(cHud*ee*complexconjugate(DEL3x2)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2122 = Coupling(name = 'GC_2122',
                   value = '-((cHud*cw*ee*complexconjugate(DEL3x2)*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_2123 = Coupling(name = 'GC_2123',
                   value = '-(cHd*cw*DEL2x3*ee*complex(0,1))/(4.*sw) - (cHd*DEL2x3*ee*complex(0,1)*sw)/(4.*cw) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL3x2))/(4.*sw) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL3x2))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_2124 = Coupling(name = 'GC_2124',
                   value = '-(cHu*cw*DEL2x3*ee*complex(0,1))/(4.*sw) - (cHu*DEL2x3*ee*complex(0,1)*sw)/(4.*cw) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL3x2))/(4.*sw) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL3x2))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_2125 = Coupling(name = 'GC_2125',
                   value = '-(cHd*DEL2x3*complex(0,1))/(2.*vev**2) - (cHd*complex(0,1)*complexconjugate(DEL3x2))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2126 = Coupling(name = 'GC_2126',
                   value = '(cHd*DEL2x3)/(2.*vev**2) + (cHd*complexconjugate(DEL3x2))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2127 = Coupling(name = 'GC_2127',
                   value = '-(cHu*DEL2x3*complex(0,1))/(2.*vev**2) - (cHu*complex(0,1)*complexconjugate(DEL3x2))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2128 = Coupling(name = 'GC_2128',
                   value = '(cHu*DEL2x3)/(2.*vev**2) + (cHu*complexconjugate(DEL3x2))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2129 = Coupling(name = 'GC_2129',
                   value = '(cHd*DEL2x3*ee*complex(0,1))/vev**2 + (cHd*ee*complex(0,1)*complexconjugate(DEL3x2))/vev**2',
                   order = {'NP':1,'QED':3})

GC_2130 = Coupling(name = 'GC_2130',
                   value = '(cHu*DEL2x3*ee*complex(0,1))/vev**2 + (cHu*ee*complex(0,1)*complexconjugate(DEL3x2))/vev**2',
                   order = {'NP':1,'QED':3})

GC_2131 = Coupling(name = 'GC_2131',
                   value = '-(cHd*DEL2x3*ee)/(2.*sw*vev**2) - (cHd*ee*complexconjugate(DEL3x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2132 = Coupling(name = 'GC_2132',
                   value = '-(cHd*DEL2x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*complexconjugate(DEL3x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2133 = Coupling(name = 'GC_2133',
                   value = '(cHd*DEL2x3*ee)/(2.*sw*vev**2) + (cHd*ee*complexconjugate(DEL3x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2134 = Coupling(name = 'GC_2134',
                   value = '-(cHu*DEL2x3*ee)/(2.*sw*vev**2) - (cHu*ee*complexconjugate(DEL3x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2135 = Coupling(name = 'GC_2135',
                   value = '-(cHu*DEL2x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*complexconjugate(DEL3x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2136 = Coupling(name = 'GC_2136',
                   value = '(cHu*DEL2x3*ee)/(2.*sw*vev**2) + (cHu*ee*complexconjugate(DEL3x2))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2137 = Coupling(name = 'GC_2137',
                   value = '-(cHd*cw*DEL2x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL2x3*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL3x2))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL3x2))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2138 = Coupling(name = 'GC_2138',
                   value = '(cHd*cw*DEL2x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL2x3*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHd*cw*ee*complex(0,1)*complexconjugate(DEL3x2))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL3x2))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2139 = Coupling(name = 'GC_2139',
                   value = '-(cHu*cw*DEL2x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL2x3*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL3x2))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL3x2))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2140 = Coupling(name = 'GC_2140',
                   value = '(cHu*cw*DEL2x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL2x3*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHu*cw*ee*complex(0,1)*complexconjugate(DEL3x2))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL3x2))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2141 = Coupling(name = 'GC_2141',
                   value = '(cHd*DEL2x3)/(2.*vev) + (cHd*complexconjugate(DEL3x2))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_2142 = Coupling(name = 'GC_2142',
                   value = '(cHu*DEL2x3)/(2.*vev) + (cHu*complexconjugate(DEL3x2))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_2143 = Coupling(name = 'GC_2143',
                   value = '-(cHd*DEL2x3*ee)/(2.*sw*vev) - (cHd*ee*complexconjugate(DEL3x2))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2144 = Coupling(name = 'GC_2144',
                   value = '(cHd*DEL2x3*ee)/(2.*sw*vev) + (cHd*ee*complexconjugate(DEL3x2))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2145 = Coupling(name = 'GC_2145',
                   value = '-(cHu*DEL2x3*ee)/(2.*sw*vev) - (cHu*ee*complexconjugate(DEL3x2))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2146 = Coupling(name = 'GC_2146',
                   value = '(cHu*DEL2x3*ee)/(2.*sw*vev) + (cHu*ee*complexconjugate(DEL3x2))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2147 = Coupling(name = 'GC_2147',
                   value = '-(cHd*cw*DEL2x3*ee*complex(0,1))/(2.*sw*vev) - (cHd*DEL2x3*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL3x2))/(2.*sw*vev) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL3x2))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_2148 = Coupling(name = 'GC_2148',
                   value = '-(cHu*cw*DEL2x3*ee*complex(0,1))/(2.*sw*vev) - (cHu*DEL2x3*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL3x2))/(2.*sw*vev) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL3x2))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_2149 = Coupling(name = 'GC_2149',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL3x3))/(sw*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_2150 = Coupling(name = 'GC_2150',
                   value = '-((cHud*complexconjugate(DEL3x3)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_2151 = Coupling(name = 'GC_2151',
                   value = '-((cHud*complex(0,1)*complexconjugate(DEL3x3)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':2})

GC_2152 = Coupling(name = 'GC_2152',
                   value = '-((cHud*ee*complexconjugate(DEL3x3)*cmath.sqrt(2))/vev**2)',
                   order = {'NP':1,'QED':3})

GC_2153 = Coupling(name = 'GC_2153',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL3x3)*cmath.sqrt(2))/vev**2',
                   order = {'NP':1,'QED':3})

GC_2154 = Coupling(name = 'GC_2154',
                   value = '-((cHud*ee*complex(0,1)*complexconjugate(DEL3x3)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_2155 = Coupling(name = 'GC_2155',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL3x3)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2156 = Coupling(name = 'GC_2156',
                   value = '(2*cHud*ee*complex(0,1)*complexconjugate(DEL3x3)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2157 = Coupling(name = 'GC_2157',
                   value = '(cHud*ee*complexconjugate(DEL3x3)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2158 = Coupling(name = 'GC_2158',
                   value = '-((cHud*cw*ee*complexconjugate(DEL3x3)*cmath.sqrt(2))/(sw*vev**2))',
                   order = {'NP':1,'QED':3})

GC_2159 = Coupling(name = 'GC_2159',
                   value = '(cHud*cw*ee*complex(0,1)*complexconjugate(DEL3x3)*cmath.sqrt(2))/(sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2160 = Coupling(name = 'GC_2160',
                   value = '-((cHud*complexconjugate(DEL3x3)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':1})

GC_2161 = Coupling(name = 'GC_2161',
                   value = '-((cHud*ee*complexconjugate(DEL3x3)*cmath.sqrt(2))/vev)',
                   order = {'NP':1,'QED':2})

GC_2162 = Coupling(name = 'GC_2162',
                   value = '(cHud*ee*complex(0,1)*complexconjugate(DEL3x3)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2163 = Coupling(name = 'GC_2163',
                   value = '(cHud*ee*complexconjugate(DEL3x3)*cmath.sqrt(2))/(sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2164 = Coupling(name = 'GC_2164',
                   value = '-((cHud*cw*ee*complexconjugate(DEL3x3)*cmath.sqrt(2))/(sw*vev))',
                   order = {'NP':1,'QED':2})

GC_2165 = Coupling(name = 'GC_2165',
                   value = '-(cHd*cw*DEL3x3*ee*complex(0,1))/(4.*sw) - (cHd*DEL3x3*ee*complex(0,1)*sw)/(4.*cw) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL3x3))/(4.*sw) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL3x3))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_2166 = Coupling(name = 'GC_2166',
                   value = '-(cHu*cw*DEL3x3*ee*complex(0,1))/(4.*sw) - (cHu*DEL3x3*ee*complex(0,1)*sw)/(4.*cw) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL3x3))/(4.*sw) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL3x3))/(4.*cw)',
                   order = {'NP':1,'QED':1})

GC_2167 = Coupling(name = 'GC_2167',
                   value = '-(cHd*DEL3x3*complex(0,1))/(2.*vev**2) - (cHd*complex(0,1)*complexconjugate(DEL3x3))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2168 = Coupling(name = 'GC_2168',
                   value = '(cHd*DEL3x3)/(2.*vev**2) + (cHd*complexconjugate(DEL3x3))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2169 = Coupling(name = 'GC_2169',
                   value = '-(cHu*DEL3x3*complex(0,1))/(2.*vev**2) - (cHu*complex(0,1)*complexconjugate(DEL3x3))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2170 = Coupling(name = 'GC_2170',
                   value = '(cHu*DEL3x3)/(2.*vev**2) + (cHu*complexconjugate(DEL3x3))/(2.*vev**2)',
                   order = {'NP':1,'QED':2})

GC_2171 = Coupling(name = 'GC_2171',
                   value = '(cHd*DEL3x3*ee*complex(0,1))/vev**2 + (cHd*ee*complex(0,1)*complexconjugate(DEL3x3))/vev**2',
                   order = {'NP':1,'QED':3})

GC_2172 = Coupling(name = 'GC_2172',
                   value = '(cHu*DEL3x3*ee*complex(0,1))/vev**2 + (cHu*ee*complex(0,1)*complexconjugate(DEL3x3))/vev**2',
                   order = {'NP':1,'QED':3})

GC_2173 = Coupling(name = 'GC_2173',
                   value = '-(cHd*DEL3x3*ee)/(2.*sw*vev**2) - (cHd*ee*complexconjugate(DEL3x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2174 = Coupling(name = 'GC_2174',
                   value = '-(cHd*DEL3x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*complexconjugate(DEL3x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2175 = Coupling(name = 'GC_2175',
                   value = '(cHd*DEL3x3*ee)/(2.*sw*vev**2) + (cHd*ee*complexconjugate(DEL3x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2176 = Coupling(name = 'GC_2176',
                   value = '-(cHu*DEL3x3*ee)/(2.*sw*vev**2) - (cHu*ee*complexconjugate(DEL3x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2177 = Coupling(name = 'GC_2177',
                   value = '-(cHu*DEL3x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*complexconjugate(DEL3x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2178 = Coupling(name = 'GC_2178',
                   value = '(cHu*DEL3x3*ee)/(2.*sw*vev**2) + (cHu*ee*complexconjugate(DEL3x3))/(2.*sw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2179 = Coupling(name = 'GC_2179',
                   value = '-(cHd*cw*DEL3x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL3x3*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL3x3))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL3x3))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2180 = Coupling(name = 'GC_2180',
                   value = '(cHd*cw*DEL3x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHd*DEL3x3*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHd*cw*ee*complex(0,1)*complexconjugate(DEL3x3))/(2.*sw*vev**2) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL3x3))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2181 = Coupling(name = 'GC_2181',
                   value = '-(cHu*cw*DEL3x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL3x3*ee*complex(0,1)*sw)/(2.*cw*vev**2) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL3x3))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL3x3))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2182 = Coupling(name = 'GC_2182',
                   value = '(cHu*cw*DEL3x3*ee*complex(0,1))/(2.*sw*vev**2) - (cHu*DEL3x3*ee*complex(0,1)*sw)/(2.*cw*vev**2) + (cHu*cw*ee*complex(0,1)*complexconjugate(DEL3x3))/(2.*sw*vev**2) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL3x3))/(2.*cw*vev**2)',
                   order = {'NP':1,'QED':3})

GC_2183 = Coupling(name = 'GC_2183',
                   value = '(cHd*DEL3x3)/(2.*vev) + (cHd*complexconjugate(DEL3x3))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_2184 = Coupling(name = 'GC_2184',
                   value = '(cHu*DEL3x3)/(2.*vev) + (cHu*complexconjugate(DEL3x3))/(2.*vev)',
                   order = {'NP':1,'QED':1})

GC_2185 = Coupling(name = 'GC_2185',
                   value = '-(cHd*DEL3x3*ee)/(2.*sw*vev) - (cHd*ee*complexconjugate(DEL3x3))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2186 = Coupling(name = 'GC_2186',
                   value = '(cHd*DEL3x3*ee)/(2.*sw*vev) + (cHd*ee*complexconjugate(DEL3x3))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2187 = Coupling(name = 'GC_2187',
                   value = '-(cHu*DEL3x3*ee)/(2.*sw*vev) - (cHu*ee*complexconjugate(DEL3x3))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2188 = Coupling(name = 'GC_2188',
                   value = '(cHu*DEL3x3*ee)/(2.*sw*vev) + (cHu*ee*complexconjugate(DEL3x3))/(2.*sw*vev)',
                   order = {'NP':1,'QED':2})

GC_2189 = Coupling(name = 'GC_2189',
                   value = '-(cHd*cw*DEL3x3*ee*complex(0,1))/(2.*sw*vev) - (cHd*DEL3x3*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHd*cw*ee*complex(0,1)*complexconjugate(DEL3x3))/(2.*sw*vev) - (cHd*ee*complex(0,1)*sw*complexconjugate(DEL3x3))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

GC_2190 = Coupling(name = 'GC_2190',
                   value = '-(cHu*cw*DEL3x3*ee*complex(0,1))/(2.*sw*vev) - (cHu*DEL3x3*ee*complex(0,1)*sw)/(2.*cw*vev) - (cHu*cw*ee*complex(0,1)*complexconjugate(DEL3x3))/(2.*sw*vev) - (cHu*ee*complex(0,1)*sw*complexconjugate(DEL3x3))/(2.*cw*vev)',
                   order = {'NP':1,'QED':2})

