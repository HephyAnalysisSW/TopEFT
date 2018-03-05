# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 10.2.0 for Linux x86 (64-bit) (July 28, 2015)
# Date: Tue 19 Dec 2017 19:54:36


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_9})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_651})

V_3 = Vertex(name = 'V_3',
             particles = [ P.ghA, P.ghWm__tilde__, P.W__minus__ ],
             color = [ '1' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_3})

V_4 = Vertex(name = 'V_4',
             particles = [ P.ghA, P.ghWp__tilde__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_4})

V_5 = Vertex(name = 'V_5',
             particles = [ P.ghWm, P.ghA__tilde__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_3})

V_6 = Vertex(name = 'V_6',
             particles = [ P.ghWm, P.ghWm__tilde__, P.H ],
             color = [ '1' ],
             lorentz = [ L.UUS1 ],
             couplings = {(0,0):C.GC_662})

V_7 = Vertex(name = 'V_7',
             particles = [ P.ghWm, P.ghWm__tilde__, P.a ],
             color = [ '1' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_4})

V_8 = Vertex(name = 'V_8',
             particles = [ P.ghWm, P.ghWm__tilde__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_635})

V_9 = Vertex(name = 'V_9',
             particles = [ P.ghWm, P.ghZ__tilde__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_634})

V_10 = Vertex(name = 'V_10',
              particles = [ P.ghWp, P.ghA__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_4})

V_11 = Vertex(name = 'V_11',
              particles = [ P.ghWp, P.ghWp__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_662})

V_12 = Vertex(name = 'V_12',
              particles = [ P.ghWp, P.ghWp__tilde__, P.a ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_3})

V_13 = Vertex(name = 'V_13',
              particles = [ P.ghWp, P.ghWp__tilde__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_634})

V_14 = Vertex(name = 'V_14',
              particles = [ P.ghWp, P.ghZ__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_635})

V_15 = Vertex(name = 'V_15',
              particles = [ P.ghZ, P.ghWm__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_634})

V_16 = Vertex(name = 'V_16',
              particles = [ P.ghZ, P.ghWp__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_635})

V_17 = Vertex(name = 'V_17',
              particles = [ P.ghZ, P.ghZ__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_842})

V_18 = Vertex(name = 'V_18',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_6})

V_19 = Vertex(name = 'V_19',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_6})

V_20 = Vertex(name = 'V_20',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_8,(0,0):C.GC_8,(2,2):C.GC_8})

V_21 = Vertex(name = 'V_21',
              particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
              couplings = {(0,3):C.GC_104,(0,1):C.GC_509,(0,2):C.GC_777,(0,0):C.GC_666})

V_22 = Vertex(name = 'V_22',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
              couplings = {(0,2):C.GC_701,(0,0):C.GC_674,(0,1):C.GC_631,(0,3):C.GC_857})

V_23 = Vertex(name = 'V_23',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_673})

V_24 = Vertex(name = 'V_24',
              particles = [ P.t__tilde__, P.t, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS4, L.FFVS6 ],
              couplings = {(0,1):C.GC_619,(0,0):C.GC_620})

V_25 = Vertex(name = 'V_25',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV6, L.FFV9 ],
              couplings = {(0,1):C.GC_2,(0,0):C.GC_754,(0,2):C.GC_755})

V_26 = Vertex(name = 'V_26',
              particles = [ P.t__tilde__, P.t, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4, L.FFVS6 ],
              couplings = {(0,0):C.GC_827,(0,1):C.GC_837,(0,3):C.GC_614,(0,2):C.GC_615})

V_27 = Vertex(name = 'V_27',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV2, L.FFV4, L.FFV8, L.FFV9 ],
              couplings = {(0,1):C.GC_633,(0,3):C.GC_637,(0,2):C.GC_881,(0,0):C.GC_656,(0,4):C.GC_657})

V_28 = Vertex(name = 'V_28',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_871})

V_29 = Vertex(name = 'V_29',
              particles = [ P.c__tilde__, P.t, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS5 ],
              couplings = {(0,0):C.GC_623,(0,1):C.GC_628})

V_30 = Vertex(name = 'V_30',
              particles = [ P.c__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV3 ],
              couplings = {(0,1):C.GC_758,(0,0):C.GC_763})

V_31 = Vertex(name = 'V_31',
              particles = [ P.t__tilde__, P.c, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS5 ],
              couplings = {(0,0):C.GC_627,(0,1):C.GC_624})

V_32 = Vertex(name = 'V_32',
              particles = [ P.t__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV3 ],
              couplings = {(0,1):C.GC_762,(0,0):C.GC_759})

V_33 = Vertex(name = 'V_33',
              particles = [ P.t__tilde__, P.u, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS5 ],
              couplings = {(0,0):C.GC_625,(0,1):C.GC_622})

V_34 = Vertex(name = 'V_34',
              particles = [ P.t__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV3 ],
              couplings = {(0,1):C.GC_760,(0,0):C.GC_757})

V_35 = Vertex(name = 'V_35',
              particles = [ P.u__tilde__, P.t, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS5 ],
              couplings = {(0,0):C.GC_621,(0,1):C.GC_626})

V_36 = Vertex(name = 'V_36',
              particles = [ P.u__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV3 ],
              couplings = {(0,1):C.GC_756,(0,0):C.GC_761})

V_37 = Vertex(name = 'V_37',
              particles = [ P.c__tilde__, P.t, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
              couplings = {(0,0):C.GC_835,(0,2):C.GC_841,(0,1):C.GC_521,(0,3):C.GC_524})

V_38 = Vertex(name = 'V_38',
              particles = [ P.c__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
              couplings = {(0,1):C.GC_879,(0,3):C.GC_885,(0,2):C.GC_713,(0,0):C.GC_716})

V_39 = Vertex(name = 'V_39',
              particles = [ P.t__tilde__, P.c, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
              couplings = {(0,0):C.GC_833,(0,2):C.GC_840,(0,1):C.GC_525,(0,3):C.GC_520})

V_40 = Vertex(name = 'V_40',
              particles = [ P.t__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
              couplings = {(0,1):C.GC_877,(0,3):C.GC_884,(0,2):C.GC_717,(0,0):C.GC_712})

V_41 = Vertex(name = 'V_41',
              particles = [ P.t__tilde__, P.u, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
              couplings = {(0,0):C.GC_829,(0,2):C.GC_838,(0,1):C.GC_523,(0,3):C.GC_518})

V_42 = Vertex(name = 'V_42',
              particles = [ P.t__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
              couplings = {(0,1):C.GC_873,(0,3):C.GC_882,(0,2):C.GC_715,(0,0):C.GC_710})

V_43 = Vertex(name = 'V_43',
              particles = [ P.u__tilde__, P.t, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
              couplings = {(0,0):C.GC_831,(0,2):C.GC_839,(0,1):C.GC_519,(0,3):C.GC_522})

V_44 = Vertex(name = 'V_44',
              particles = [ P.u__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
              couplings = {(0,1):C.GC_875,(0,3):C.GC_883,(0,2):C.GC_711,(0,0):C.GC_714})

V_45 = Vertex(name = 'V_45',
              particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF16, L.FFFF18, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF3, L.FFFF30, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,10):C.GC_177,(0,11):C.GC_407,(0,9):C.GC_404,(0,7):C.GC_404,(0,2):C.GC_411,(0,4):C.GC_148,(0,5):C.GC_494,(0,6):C.GC_354,(0,8):C.GC_422,(0,3):C.GC_421,(0,1):C.GC_421,(0,0):C.GC_426})

V_46 = Vertex(name = 'V_46',
              particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF16, L.FFFF18, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF3, L.FFFF30, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,10):C.GC_185,(0,11):C.GC_439,(0,9):C.GC_436,(0,7):C.GC_436,(0,2):C.GC_443,(0,4):C.GC_152,(0,5):C.GC_498,(0,6):C.GC_358,(0,8):C.GC_454,(0,3):C.GC_453,(0,1):C.GC_453,(0,0):C.GC_458})

V_47 = Vertex(name = 'V_47',
              particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF16, L.FFFF18, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF3, L.FFFF30, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,10):C.GC_193,(0,11):C.GC_471,(0,9):C.GC_468,(0,7):C.GC_468,(0,2):C.GC_475,(0,4):C.GC_156,(0,5):C.GC_502,(0,6):C.GC_362,(0,8):C.GC_486,(0,3):C.GC_485,(0,1):C.GC_485,(0,0):C.GC_490})

V_48 = Vertex(name = 'V_48',
              particles = [ P.t__tilde__, P.c, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF18, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF3, L.FFFF30, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,10):C.GC_179,(0,11):C.GC_423,(0,9):C.GC_420,(0,7):C.GC_420,(0,2):C.GC_427,(0,4):C.GC_495,(0,5):C.GC_149,(0,6):C.GC_355,(0,8):C.GC_406,(0,3):C.GC_405,(0,1):C.GC_405,(0,0):C.GC_410})

V_49 = Vertex(name = 'V_49',
              particles = [ P.t__tilde__, P.c, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF18, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF3, L.FFFF30, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,10):C.GC_187,(0,11):C.GC_455,(0,9):C.GC_452,(0,7):C.GC_452,(0,2):C.GC_459,(0,4):C.GC_499,(0,5):C.GC_153,(0,6):C.GC_359,(0,8):C.GC_438,(0,3):C.GC_437,(0,1):C.GC_437,(0,0):C.GC_442})

V_50 = Vertex(name = 'V_50',
              particles = [ P.t__tilde__, P.c, P.ta__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF16, L.FFFF18, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF3, L.FFFF30, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,10):C.GC_195,(0,11):C.GC_487,(0,9):C.GC_484,(0,7):C.GC_484,(0,2):C.GC_491,(0,4):C.GC_503,(0,5):C.GC_157,(0,6):C.GC_363,(0,8):C.GC_470,(0,3):C.GC_469,(0,1):C.GC_469,(0,0):C.GC_474})

V_51 = Vertex(name = 'V_51',
              particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF16, L.FFFF18, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF3, L.FFFF30, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,10):C.GC_175,(0,11):C.GC_415,(0,9):C.GC_412,(0,7):C.GC_412,(0,2):C.GC_419,(0,4):C.GC_147,(0,5):C.GC_493,(0,6):C.GC_353,(0,8):C.GC_398,(0,3):C.GC_397,(0,1):C.GC_397,(0,0):C.GC_402})

V_52 = Vertex(name = 'V_52',
              particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF16, L.FFFF18, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF3, L.FFFF30, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,10):C.GC_183,(0,11):C.GC_447,(0,9):C.GC_444,(0,7):C.GC_444,(0,2):C.GC_451,(0,4):C.GC_151,(0,5):C.GC_497,(0,6):C.GC_357,(0,8):C.GC_430,(0,3):C.GC_429,(0,1):C.GC_429,(0,0):C.GC_434})

V_53 = Vertex(name = 'V_53',
              particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF16, L.FFFF18, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF3, L.FFFF30, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,12):C.GC_479,(0,11):C.GC_191,(0,9):C.GC_476,(0,7):C.GC_608,(0,10):C.GC_607,(0,2):C.GC_483,(0,8):C.GC_462,(0,4):C.GC_155,(0,5):C.GC_501,(0,6):C.GC_361,(0,3):C.GC_461,(0,1):C.GC_461,(0,0):C.GC_466})

V_54 = Vertex(name = 'V_54',
              particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF16, L.FFFF18, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF3, L.FFFF30, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,10):C.GC_173,(0,11):C.GC_399,(0,9):C.GC_396,(0,7):C.GC_396,(0,2):C.GC_403,(0,4):C.GC_146,(0,5):C.GC_492,(0,6):C.GC_352,(0,8):C.GC_414,(0,3):C.GC_413,(0,1):C.GC_413,(0,0):C.GC_418})

V_55 = Vertex(name = 'V_55',
              particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF16, L.FFFF18, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF3, L.FFFF30, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,10):C.GC_181,(0,11):C.GC_431,(0,9):C.GC_428,(0,7):C.GC_428,(0,2):C.GC_435,(0,4):C.GC_150,(0,5):C.GC_496,(0,6):C.GC_356,(0,8):C.GC_446,(0,3):C.GC_445,(0,1):C.GC_445,(0,0):C.GC_450})

V_56 = Vertex(name = 'V_56',
              particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF16, L.FFFF18, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF3, L.FFFF30, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,10):C.GC_189,(0,11):C.GC_463,(0,9):C.GC_460,(0,7):C.GC_460,(0,2):C.GC_467,(0,4):C.GC_154,(0,5):C.GC_500,(0,6):C.GC_360,(0,8):C.GC_478,(0,3):C.GC_477,(0,1):C.GC_477,(0,0):C.GC_482})

V_57 = Vertex(name = 'V_57',
              particles = [ P.b__tilde__, P.c, P.ve__tilde__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF17, L.FFFF2, L.FFFF28, L.FFFF3, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_161,(0,8):C.GC_420,(0,6):C.GC_423,(0,5):C.GC_423,(0,3):C.GC_424,(0,2):C.GC_49,(0,4):C.GC_46,(0,1):C.GC_49,(0,0):C.GC_50})

V_58 = Vertex(name = 'V_58',
              particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF14, L.FFFF19, L.FFFF2, L.FFFF29, L.FFFF3, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_159,(0,8):C.GC_412,(0,6):C.GC_415,(0,5):C.GC_415,(0,3):C.GC_416,(0,2):C.GC_43,(0,4):C.GC_40,(0,1):C.GC_43,(0,0):C.GC_44})

V_59 = Vertex(name = 'V_59',
              particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF14, L.FFFF19, L.FFFF2, L.FFFF29, L.FFFF3, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_158,(0,8):C.GC_396,(0,6):C.GC_399,(0,5):C.GC_399,(0,3):C.GC_400,(0,2):C.GC_31,(0,4):C.GC_28,(0,1):C.GC_31,(0,0):C.GC_32})

V_60 = Vertex(name = 'V_60',
              particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF14, L.FFFF19, L.FFFF2, L.FFFF29, L.FFFF3, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_160,(0,8):C.GC_404,(0,6):C.GC_407,(0,5):C.GC_407,(0,3):C.GC_408,(0,2):C.GC_37,(0,4):C.GC_34,(0,1):C.GC_37,(0,0):C.GC_38})

V_61 = Vertex(name = 'V_61',
              particles = [ P.b__tilde__, P.c, P.vm__tilde__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF17, L.FFFF2, L.FFFF28, L.FFFF3, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_165,(0,8):C.GC_452,(0,6):C.GC_455,(0,5):C.GC_455,(0,3):C.GC_456,(0,2):C.GC_73,(0,4):C.GC_70,(0,1):C.GC_73,(0,0):C.GC_74})

V_62 = Vertex(name = 'V_62',
              particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF14, L.FFFF19, L.FFFF2, L.FFFF29, L.FFFF3, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_163,(0,8):C.GC_444,(0,6):C.GC_447,(0,5):C.GC_447,(0,3):C.GC_448,(0,2):C.GC_67,(0,4):C.GC_64,(0,1):C.GC_67,(0,0):C.GC_68})

V_63 = Vertex(name = 'V_63',
              particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF14, L.FFFF19, L.FFFF2, L.FFFF29, L.FFFF3, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_162,(0,8):C.GC_428,(0,6):C.GC_431,(0,5):C.GC_431,(0,3):C.GC_432,(0,2):C.GC_55,(0,4):C.GC_52,(0,1):C.GC_55,(0,0):C.GC_56})

V_64 = Vertex(name = 'V_64',
              particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF14, L.FFFF19, L.FFFF2, L.FFFF29, L.FFFF3, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_164,(0,8):C.GC_436,(0,6):C.GC_439,(0,5):C.GC_439,(0,3):C.GC_440,(0,2):C.GC_61,(0,4):C.GC_58,(0,1):C.GC_61,(0,0):C.GC_62})

V_65 = Vertex(name = 'V_65',
              particles = [ P.b__tilde__, P.c, P.vt__tilde__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF17, L.FFFF2, L.FFFF28, L.FFFF3, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_169,(0,8):C.GC_484,(0,6):C.GC_487,(0,5):C.GC_487,(0,3):C.GC_488,(0,2):C.GC_97,(0,4):C.GC_94,(0,1):C.GC_97,(0,0):C.GC_98})

V_66 = Vertex(name = 'V_66',
              particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF14, L.FFFF19, L.FFFF2, L.FFFF29, L.FFFF3, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_167,(0,8):C.GC_476,(0,6):C.GC_479,(0,5):C.GC_479,(0,3):C.GC_480,(0,2):C.GC_91,(0,4):C.GC_88,(0,1):C.GC_91,(0,0):C.GC_92})

V_67 = Vertex(name = 'V_67',
              particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF14, L.FFFF19, L.FFFF2, L.FFFF29, L.FFFF3, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_166,(0,8):C.GC_460,(0,6):C.GC_463,(0,5):C.GC_463,(0,3):C.GC_464,(0,2):C.GC_79,(0,4):C.GC_76,(0,1):C.GC_79,(0,0):C.GC_80})

V_68 = Vertex(name = 'V_68',
              particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF14, L.FFFF19, L.FFFF2, L.FFFF29, L.FFFF3, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_168,(0,8):C.GC_468,(0,6):C.GC_471,(0,5):C.GC_471,(0,3):C.GC_472,(0,2):C.GC_85,(0,4):C.GC_82,(0,1):C.GC_85,(0,0):C.GC_86})

V_69 = Vertex(name = 'V_69',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,1):C.GC_671,(0,0):C.GC_672})

V_70 = Vertex(name = 'V_70',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_887})

V_71 = Vertex(name = 'V_71',
              particles = [ P.t__tilde__, P.t, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS4 ],
              couplings = {(0,1):C.GC_654,(0,0):C.GC_655})

V_72 = Vertex(name = 'V_72',
              particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
              couplings = {(0,1):C.GC_105,(0,3):C.GC_508,(0,2):C.GC_776,(0,0):C.GC_666})

V_73 = Vertex(name = 'V_73',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
              couplings = {(0,2):C.GC_675,(0,0):C.GC_700,(0,1):C.GC_631,(0,3):C.GC_856})

V_74 = Vertex(name = 'V_74',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_673})

V_75 = Vertex(name = 'V_75',
              particles = [ P.b__tilde__, P.b, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS4, L.FFVS6 ],
              couplings = {(0,1):C.GC_639,(0,0):C.GC_640})

V_76 = Vertex(name = 'V_76',
              particles = [ P.b__tilde__, P.b, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV6, L.FFV9 ],
              couplings = {(0,1):C.GC_1,(0,0):C.GC_669,(0,2):C.GC_670})

V_77 = Vertex(name = 'V_77',
              particles = [ P.b__tilde__, P.b, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4, L.FFVS6 ],
              couplings = {(0,0):C.GC_828,(0,1):C.GC_822,(0,3):C.GC_616,(0,2):C.GC_617})

V_78 = Vertex(name = 'V_78',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV2, L.FFV4, L.FFV5, L.FFV9 ],
              couplings = {(0,1):C.GC_632,(0,3):C.GC_637,(0,2):C.GC_866,(0,0):C.GC_658,(0,4):C.GC_659})

V_79 = Vertex(name = 'V_79',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_872})

V_80 = Vertex(name = 'V_80',
              particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
              lorentz = [ L.FFFF10, L.FFFF13, L.FFFF16, L.FFFF2, L.FFFF8 ],
              couplings = {(0,4):C.GC_587,(1,4):C.GC_589,(0,3):C.GC_248,(1,3):C.GC_252,(0,0):C.GC_504,(1,0):C.GC_506,(0,1):C.GC_101,(1,1):C.GC_103,(0,2):C.GC_116,(1,2):C.GC_120})

V_81 = Vertex(name = 'V_81',
              particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
              lorentz = [ L.FFFF10, L.FFFF13, L.FFFF16, L.FFFF2, L.FFFF8 ],
              couplings = {(0,4):C.GC_587,(1,4):C.GC_589,(0,3):C.GC_248,(1,3):C.GC_252,(0,0):C.GC_504,(1,0):C.GC_506,(0,1):C.GC_101,(1,1):C.GC_103,(0,2):C.GC_116,(1,2):C.GC_120})

V_82 = Vertex(name = 'V_82',
              particles = [ P.d__tilde__, P.d, P.t__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
              lorentz = [ L.FFFF16, L.FFFF2, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF8 ],
              couplings = {(0,5):C.GC_197,(1,5):C.GC_225,(0,1):C.GC_251,(1,1):C.GC_255,(0,2):C.GC_576,(1,2):C.GC_577,(0,3):C.GC_609,(1,3):C.GC_610,(0,4):C.GC_597,(1,4):C.GC_598,(0,0):C.GC_249,(1,0):C.GC_253})

V_83 = Vertex(name = 'V_83',
              particles = [ P.s__tilde__, P.s, P.t__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
              lorentz = [ L.FFFF16, L.FFFF2, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF8 ],
              couplings = {(0,5):C.GC_197,(1,5):C.GC_225,(0,1):C.GC_251,(1,1):C.GC_255,(0,2):C.GC_576,(1,2):C.GC_577,(0,3):C.GC_609,(1,3):C.GC_610,(0,4):C.GC_597,(1,4):C.GC_598,(0,0):C.GC_249,(1,0):C.GC_253})

V_84 = Vertex(name = 'V_84',
              particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF1, L.FFFF12, L.FFFF16, L.FFFF2, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF7, L.FFFF8 ],
              couplings = {(1,7):C.GC_211,(0,8):C.GC_216,(1,0):C.GC_315,(3,0):C.GC_347,(0,3):C.GC_312,(2,3):C.GC_344,(1,6):C.GC_131,(3,6):C.GC_143,(1,4):C.GC_257,(3,4):C.GC_273,(1,5):C.GC_535,(3,5):C.GC_547,(1,1):C.GC_306,(3,1):C.GC_338,(0,2):C.GC_289,(2,2):C.GC_321})

V_85 = Vertex(name = 'V_85',
              particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF1, L.FFFF12, L.FFFF16, L.FFFF2, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF7, L.FFFF8 ],
              couplings = {(1,7):C.GC_217,(0,8):C.GC_222,(1,0):C.GC_319,(3,0):C.GC_351,(0,3):C.GC_316,(2,3):C.GC_348,(1,6):C.GC_133,(3,6):C.GC_145,(1,4):C.GC_261,(3,4):C.GC_277,(1,5):C.GC_537,(3,5):C.GC_549,(1,1):C.GC_310,(3,1):C.GC_342,(0,2):C.GC_293,(2,2):C.GC_325})

V_86 = Vertex(name = 'V_86',
              particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF1, L.FFFF12, L.FFFF16, L.FFFF2, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF7, L.FFFF8 ],
              couplings = {(1,7):C.GC_217,(0,8):C.GC_222,(1,0):C.GC_303,(3,0):C.GC_335,(0,3):C.GC_300,(2,3):C.GC_332,(1,6):C.GC_127,(3,6):C.GC_139,(1,4):C.GC_267,(3,4):C.GC_283,(1,5):C.GC_531,(3,5):C.GC_543,(1,1):C.GC_294,(3,1):C.GC_326,(0,2):C.GC_309,(2,2):C.GC_341})

V_87 = Vertex(name = 'V_87',
              particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF1, L.FFFF12, L.FFFF16, L.FFFF2, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF7, L.FFFF8 ],
              couplings = {(1,7):C.GC_211,(0,8):C.GC_216,(1,0):C.GC_299,(3,0):C.GC_331,(0,3):C.GC_296,(2,3):C.GC_328,(1,6):C.GC_123,(3,6):C.GC_135,(1,4):C.GC_265,(3,4):C.GC_281,(1,5):C.GC_527,(3,5):C.GC_539,(1,1):C.GC_290,(3,1):C.GC_322,(0,2):C.GC_305,(2,2):C.GC_337})

V_88 = Vertex(name = 'V_88',
              particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF16, L.FFFF18, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF3, L.FFFF30, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,10):C.GC_584,(0,11):C.GC_377,(0,9):C.GC_374,(0,7):C.GC_374,(0,2):C.GC_379,(0,4):C.GC_578,(0,5):C.GC_604,(0,6):C.GC_599,(0,8):C.GC_375,(0,3):C.GC_376,(0,1):C.GC_376,(0,0):C.GC_373})

V_89 = Vertex(name = 'V_89',
              particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF16, L.FFFF18, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF3, L.FFFF30, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,10):C.GC_585,(0,11):C.GC_385,(0,9):C.GC_382,(0,7):C.GC_382,(0,2):C.GC_387,(0,4):C.GC_579,(0,5):C.GC_605,(0,6):C.GC_600,(0,8):C.GC_383,(0,3):C.GC_384,(0,1):C.GC_384,(0,0):C.GC_381})

V_90 = Vertex(name = 'V_90',
              particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF16, L.FFFF18, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF3, L.FFFF30, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,10):C.GC_586,(0,11):C.GC_393,(0,9):C.GC_390,(0,7):C.GC_390,(0,2):C.GC_395,(0,4):C.GC_580,(0,5):C.GC_606,(0,6):C.GC_601,(0,8):C.GC_391,(0,3):C.GC_392,(0,1):C.GC_392,(0,0):C.GC_389})

V_91 = Vertex(name = 'V_91',
              particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF14, L.FFFF19, L.FFFF2, L.FFFF29, L.FFFF3, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_581,(0,8):C.GC_374,(0,6):C.GC_377,(0,5):C.GC_377,(0,3):C.GC_372,(0,2):C.GC_14,(0,4):C.GC_11,(0,1):C.GC_14,(0,0):C.GC_10})

V_92 = Vertex(name = 'V_92',
              particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF14, L.FFFF19, L.FFFF2, L.FFFF29, L.FFFF3, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_582,(0,8):C.GC_382,(0,6):C.GC_385,(0,5):C.GC_385,(0,3):C.GC_380,(0,2):C.GC_20,(0,4):C.GC_17,(0,1):C.GC_20,(0,0):C.GC_16})

V_93 = Vertex(name = 'V_93',
              particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF14, L.FFFF19, L.FFFF2, L.FFFF29, L.FFFF3, L.FFFF4, L.FFFF8, L.FFFF9 ],
              couplings = {(0,7):C.GC_583,(0,8):C.GC_390,(0,6):C.GC_393,(0,5):C.GC_393,(0,3):C.GC_388,(0,2):C.GC_26,(0,4):C.GC_23,(0,1):C.GC_26,(0,0):C.GC_22})

V_94 = Vertex(name = 'V_94',
              particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
              lorentz = [ L.FFFF10, L.FFFF13, L.FFFF16, L.FFFF2, L.FFFF8 ],
              couplings = {(0,4):C.GC_587,(1,4):C.GC_589,(0,3):C.GC_114,(1,3):C.GC_118,(0,0):C.GC_505,(1,0):C.GC_507,(0,1):C.GC_100,(1,1):C.GC_102,(0,2):C.GC_250,(1,2):C.GC_254})

V_95 = Vertex(name = 'V_95',
              particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
              lorentz = [ L.FFFF10, L.FFFF13, L.FFFF16, L.FFFF2, L.FFFF8 ],
              couplings = {(0,4):C.GC_587,(1,4):C.GC_589,(0,3):C.GC_114,(1,3):C.GC_118,(0,0):C.GC_505,(1,0):C.GC_507,(0,1):C.GC_100,(1,1):C.GC_102,(0,2):C.GC_250,(1,2):C.GC_254})

V_96 = Vertex(name = 'V_96',
              particles = [ P.b__tilde__, P.b, P.c__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
              lorentz = [ L.FFFF16, L.FFFF2, L.FFFF25, L.FFFF8 ],
              couplings = {(0,3):C.GC_197,(1,3):C.GC_225,(0,1):C.GC_117,(1,1):C.GC_121,(0,2):C.GC_593,(1,2):C.GC_594,(0,0):C.GC_115,(1,0):C.GC_119})

V_97 = Vertex(name = 'V_97',
              particles = [ P.b__tilde__, P.b, P.u__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
              lorentz = [ L.FFFF16, L.FFFF2, L.FFFF25, L.FFFF8 ],
              couplings = {(0,3):C.GC_197,(1,3):C.GC_225,(0,1):C.GC_117,(1,1):C.GC_121,(0,2):C.GC_593,(1,2):C.GC_594,(0,0):C.GC_115,(1,0):C.GC_119})

V_98 = Vertex(name = 'V_98',
              particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF1, L.FFFF12, L.FFFF16, L.FFFF2, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF7, L.FFFF8 ],
              couplings = {(1,7):C.GC_218,(0,8):C.GC_221,(1,0):C.GC_295,(3,0):C.GC_327,(0,3):C.GC_308,(2,3):C.GC_340,(1,6):C.GC_126,(3,6):C.GC_138,(1,4):C.GC_266,(3,4):C.GC_282,(1,5):C.GC_530,(3,5):C.GC_542,(1,1):C.GC_302,(3,1):C.GC_334,(0,2):C.GC_301,(2,2):C.GC_333})

V_99 = Vertex(name = 'V_99',
              particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF1, L.FFFF12, L.FFFF16, L.FFFF2, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF7, L.FFFF8 ],
              couplings = {(1,7):C.GC_212,(0,8):C.GC_215,(1,0):C.GC_291,(3,0):C.GC_323,(0,3):C.GC_304,(2,3):C.GC_336,(1,6):C.GC_122,(3,6):C.GC_134,(1,4):C.GC_264,(3,4):C.GC_280,(1,5):C.GC_526,(3,5):C.GC_538,(1,1):C.GC_298,(3,1):C.GC_330,(0,2):C.GC_297,(2,2):C.GC_329})

V_100 = Vertex(name = 'V_100',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF12, L.FFFF16, L.FFFF2, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF7, L.FFFF8 ],
               couplings = {(1,7):C.GC_212,(0,8):C.GC_215,(1,0):C.GC_307,(3,0):C.GC_339,(0,3):C.GC_288,(2,3):C.GC_320,(1,6):C.GC_130,(3,6):C.GC_142,(1,4):C.GC_256,(3,4):C.GC_272,(1,5):C.GC_534,(3,5):C.GC_546,(1,1):C.GC_314,(3,1):C.GC_346,(0,2):C.GC_313,(2,2):C.GC_345})

V_101 = Vertex(name = 'V_101',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF12, L.FFFF16, L.FFFF2, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF7, L.FFFF8 ],
               couplings = {(1,7):C.GC_218,(0,8):C.GC_221,(1,0):C.GC_311,(3,0):C.GC_343,(0,3):C.GC_292,(2,3):C.GC_324,(1,6):C.GC_132,(3,6):C.GC_144,(1,4):C.GC_260,(3,4):C.GC_276,(1,5):C.GC_536,(3,5):C.GC_548,(1,1):C.GC_318,(3,1):C.GC_350,(0,2):C.GC_317,(2,2):C.GC_349})

V_102 = Vertex(name = 'V_102',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF12, L.FFFF16, L.FFFF2, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF7, L.FFFF8 ],
               couplings = {(1,7):C.GC_223,(0,8):C.GC_588,(1,0):C.GC_243,(3,0):C.GC_247,(0,3):C.GC_240,(2,3):C.GC_244,(1,6):C.GC_574,(3,6):C.GC_575,(1,4):C.GC_591,(3,4):C.GC_592,(1,5):C.GC_595,(3,5):C.GC_596,(1,1):C.GC_241,(3,1):C.GC_245,(0,2):C.GC_242,(2,2):C.GC_246})

V_103 = Vertex(name = 'V_103',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_886})

V_104 = Vertex(name = 'V_104',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_888})

V_105 = Vertex(name = 'V_105',
               particles = [ P.c__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_847,(0,1):C.GC_850})

V_106 = Vertex(name = 'V_106',
               particles = [ P.t__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_851,(0,1):C.GC_846})

V_107 = Vertex(name = 'V_107',
               particles = [ P.t__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_849,(0,1):C.GC_844})

V_108 = Vertex(name = 'V_108',
               particles = [ P.u__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_845,(0,1):C.GC_848})

V_109 = Vertex(name = 'V_109',
               particles = [ P.c__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS3 ],
               couplings = {(0,0):C.GC_695,(0,1):C.GC_698})

V_110 = Vertex(name = 'V_110',
               particles = [ P.t__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS3 ],
               couplings = {(0,0):C.GC_699,(0,1):C.GC_694})

V_111 = Vertex(name = 'V_111',
               particles = [ P.t__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS3 ],
               couplings = {(0,0):C.GC_697,(0,1):C.GC_692})

V_112 = Vertex(name = 'V_112',
               particles = [ P.u__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS3 ],
               couplings = {(0,0):C.GC_693,(0,1):C.GC_696})

V_113 = Vertex(name = 'V_113',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_109,(0,3):C.GC_516,(0,2):C.GC_780,(0,0):C.GC_774})

V_114 = Vertex(name = 'V_114',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_679,(0,0):C.GC_708,(0,1):C.GC_854,(0,3):C.GC_860})

V_115 = Vertex(name = 'V_115',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_111,(0,3):C.GC_510,(0,2):C.GC_782,(0,0):C.GC_773})

V_116 = Vertex(name = 'V_116',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_681,(0,0):C.GC_702,(0,1):C.GC_853,(0,3):C.GC_862})

V_117 = Vertex(name = 'V_117',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_113,(0,3):C.GC_512,(0,2):C.GC_784,(0,0):C.GC_775})

V_118 = Vertex(name = 'V_118',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_683,(0,0):C.GC_704,(0,1):C.GC_855,(0,3):C.GC_864})

V_119 = Vertex(name = 'V_119',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_107,(0,3):C.GC_514,(0,2):C.GC_778,(0,0):C.GC_772})

V_120 = Vertex(name = 'V_120',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_677,(0,0):C.GC_706,(0,1):C.GC_852,(0,3):C.GC_858})

V_121 = Vertex(name = 'V_121',
               particles = [ P.b__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_646,(0,1):C.GC_643})

V_122 = Vertex(name = 'V_122',
               particles = [ P.b__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,1):C.GC_818,(0,0):C.GC_815})

V_123 = Vertex(name = 'V_123',
               particles = [ P.b__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_648,(0,1):C.GC_645})

V_124 = Vertex(name = 'V_124',
               particles = [ P.b__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,1):C.GC_820,(0,0):C.GC_817})

V_125 = Vertex(name = 'V_125',
               particles = [ P.d__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_642,(0,1):C.GC_647})

V_126 = Vertex(name = 'V_126',
               particles = [ P.d__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,1):C.GC_814,(0,0):C.GC_819})

V_127 = Vertex(name = 'V_127',
               particles = [ P.s__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_644,(0,1):C.GC_649})

V_128 = Vertex(name = 'V_128',
               particles = [ P.s__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,1):C.GC_816,(0,0):C.GC_821})

V_129 = Vertex(name = 'V_129',
               particles = [ P.b__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,0):C.GC_830,(0,2):C.GC_823,(0,1):C.GC_566,(0,3):C.GC_563})

V_130 = Vertex(name = 'V_130',
               particles = [ P.b__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_874,(0,3):C.GC_867,(0,2):C.GC_722,(0,0):C.GC_719})

V_131 = Vertex(name = 'V_131',
               particles = [ P.b__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,0):C.GC_834,(0,2):C.GC_825,(0,1):C.GC_568,(0,3):C.GC_565})

V_132 = Vertex(name = 'V_132',
               particles = [ P.b__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_878,(0,3):C.GC_869,(0,2):C.GC_724,(0,0):C.GC_721})

V_133 = Vertex(name = 'V_133',
               particles = [ P.d__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,0):C.GC_832,(0,2):C.GC_824,(0,1):C.GC_562,(0,3):C.GC_567})

V_134 = Vertex(name = 'V_134',
               particles = [ P.d__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_876,(0,3):C.GC_868,(0,2):C.GC_718,(0,0):C.GC_723})

V_135 = Vertex(name = 'V_135',
               particles = [ P.s__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,0):C.GC_836,(0,2):C.GC_826,(0,1):C.GC_564,(0,3):C.GC_569})

V_136 = Vertex(name = 'V_136',
               particles = [ P.s__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_880,(0,3):C.GC_870,(0,2):C.GC_720,(0,0):C.GC_725})

V_137 = Vertex(name = 'V_137',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_517,(0,3):C.GC_108,(0,2):C.GC_781,(0,0):C.GC_775})

V_138 = Vertex(name = 'V_138',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_515,(0,3):C.GC_106,(0,2):C.GC_779,(0,0):C.GC_773})

V_139 = Vertex(name = 'V_139',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_511,(0,3):C.GC_110,(0,2):C.GC_783,(0,0):C.GC_772})

V_140 = Vertex(name = 'V_140',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_513,(0,3):C.GC_112,(0,2):C.GC_785,(0,0):C.GC_774})

V_141 = Vertex(name = 'V_141',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_709,(0,0):C.GC_678,(0,1):C.GC_855,(0,3):C.GC_861})

V_142 = Vertex(name = 'V_142',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_707,(0,0):C.GC_676,(0,1):C.GC_853,(0,3):C.GC_859})

V_143 = Vertex(name = 'V_143',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_703,(0,0):C.GC_680,(0,1):C.GC_852,(0,3):C.GC_863})

V_144 = Vertex(name = 'V_144',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_705,(0,0):C.GC_682,(0,1):C.GC_854,(0,3):C.GC_865})

V_145 = Vertex(name = 'V_145',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF19, L.FFFF21, L.FFFF28, L.FFFF29, L.FFFF8 ],
               couplings = {(0,9):C.GC_176,(0,6):C.GC_147,(0,4):C.GC_30,(0,5):C.GC_43,(0,7):C.GC_29,(0,8):C.GC_40,(0,1):C.GC_30,(0,0):C.GC_33,(0,3):C.GC_43,(0,2):C.GC_44})

V_146 = Vertex(name = 'V_146',
               particles = [ P.b__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF19, L.FFFF25, L.FFFF28, L.FFFF29, L.FFFF8 ],
               couplings = {(0,9):C.GC_180,(0,6):C.GC_149,(0,4):C.GC_49,(0,5):C.GC_36,(0,7):C.GC_46,(0,8):C.GC_35,(0,1):C.GC_49,(0,0):C.GC_50,(0,3):C.GC_36,(0,2):C.GC_39})

V_147 = Vertex(name = 'V_147',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF19, L.FFFF21, L.FFFF28, L.FFFF29, L.FFFF8 ],
               couplings = {(0,9):C.GC_174,(0,6):C.GC_146,(0,4):C.GC_42,(0,5):C.GC_31,(0,7):C.GC_41,(0,8):C.GC_28,(0,1):C.GC_42,(0,0):C.GC_45,(0,3):C.GC_31,(0,2):C.GC_32})

V_148 = Vertex(name = 'V_148',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF19, L.FFFF21, L.FFFF28, L.FFFF29, L.FFFF8 ],
               couplings = {(0,9):C.GC_184,(0,6):C.GC_151,(0,4):C.GC_54,(0,5):C.GC_67,(0,7):C.GC_53,(0,8):C.GC_64,(0,1):C.GC_54,(0,0):C.GC_57,(0,3):C.GC_67,(0,2):C.GC_68})

V_149 = Vertex(name = 'V_149',
               particles = [ P.b__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF19, L.FFFF25, L.FFFF28, L.FFFF29, L.FFFF8 ],
               couplings = {(0,9):C.GC_188,(0,6):C.GC_153,(0,4):C.GC_73,(0,5):C.GC_60,(0,7):C.GC_70,(0,8):C.GC_59,(0,1):C.GC_73,(0,0):C.GC_74,(0,3):C.GC_60,(0,2):C.GC_63})

V_150 = Vertex(name = 'V_150',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF19, L.FFFF21, L.FFFF28, L.FFFF29, L.FFFF8 ],
               couplings = {(0,9):C.GC_182,(0,6):C.GC_150,(0,4):C.GC_66,(0,5):C.GC_55,(0,7):C.GC_65,(0,8):C.GC_52,(0,1):C.GC_66,(0,0):C.GC_69,(0,3):C.GC_55,(0,2):C.GC_56})

V_151 = Vertex(name = 'V_151',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF19, L.FFFF21, L.FFFF28, L.FFFF29, L.FFFF8 ],
               couplings = {(0,9):C.GC_178,(0,6):C.GC_148,(0,4):C.GC_48,(0,5):C.GC_37,(0,7):C.GC_47,(0,8):C.GC_34,(0,1):C.GC_48,(0,0):C.GC_51,(0,3):C.GC_37,(0,2):C.GC_38})

V_152 = Vertex(name = 'V_152',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF19, L.FFFF21, L.FFFF28, L.FFFF29, L.FFFF8 ],
               couplings = {(0,9):C.GC_186,(0,6):C.GC_152,(0,4):C.GC_72,(0,5):C.GC_61,(0,7):C.GC_71,(0,8):C.GC_58,(0,1):C.GC_72,(0,0):C.GC_75,(0,3):C.GC_61,(0,2):C.GC_62})

V_153 = Vertex(name = 'V_153',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF19, L.FFFF21, L.FFFF28, L.FFFF29, L.FFFF8 ],
               couplings = {(0,9):C.GC_192,(0,6):C.GC_155,(0,4):C.GC_78,(0,5):C.GC_91,(0,7):C.GC_77,(0,8):C.GC_88,(0,1):C.GC_78,(0,0):C.GC_81,(0,3):C.GC_91,(0,2):C.GC_92})

V_154 = Vertex(name = 'V_154',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF19, L.FFFF21, L.FFFF28, L.FFFF29, L.FFFF8 ],
               couplings = {(0,9):C.GC_196,(0,6):C.GC_157,(0,4):C.GC_84,(0,5):C.GC_97,(0,7):C.GC_83,(0,8):C.GC_94,(0,1):C.GC_84,(0,0):C.GC_87,(0,3):C.GC_97,(0,2):C.GC_98})

V_155 = Vertex(name = 'V_155',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF19, L.FFFF21, L.FFFF28, L.FFFF29, L.FFFF8 ],
               couplings = {(0,9):C.GC_190,(0,6):C.GC_154,(0,4):C.GC_90,(0,5):C.GC_79,(0,7):C.GC_89,(0,8):C.GC_76,(0,1):C.GC_90,(0,0):C.GC_93,(0,3):C.GC_79,(0,2):C.GC_80})

V_156 = Vertex(name = 'V_156',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF19, L.FFFF21, L.FFFF28, L.FFFF29, L.FFFF8 ],
               couplings = {(0,9):C.GC_194,(0,6):C.GC_156,(0,4):C.GC_96,(0,5):C.GC_85,(0,7):C.GC_95,(0,8):C.GC_82,(0,1):C.GC_96,(0,0):C.GC_99,(0,3):C.GC_85,(0,2):C.GC_86})

V_157 = Vertex(name = 'V_157',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF19, L.FFFF21, L.FFFF28, L.FFFF29, L.FFFF8 ],
               couplings = {(0,9):C.GC_170,(0,6):C.GC_578,(0,4):C.GC_12,(0,5):C.GC_14,(0,7):C.GC_13,(0,8):C.GC_11,(0,1):C.GC_12,(0,0):C.GC_15,(0,3):C.GC_14,(0,2):C.GC_10})

V_158 = Vertex(name = 'V_158',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF19, L.FFFF21, L.FFFF28, L.FFFF29, L.FFFF8 ],
               couplings = {(0,9):C.GC_171,(0,6):C.GC_579,(0,4):C.GC_18,(0,5):C.GC_20,(0,7):C.GC_19,(0,8):C.GC_17,(0,1):C.GC_18,(0,0):C.GC_21,(0,3):C.GC_20,(0,2):C.GC_16})

V_159 = Vertex(name = 'V_159',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF19, L.FFFF21, L.FFFF28, L.FFFF29, L.FFFF8 ],
               couplings = {(0,9):C.GC_172,(0,6):C.GC_580,(0,4):C.GC_24,(0,5):C.GC_26,(0,7):C.GC_25,(0,8):C.GC_23,(0,1):C.GC_24,(0,0):C.GC_27,(0,3):C.GC_26,(0,2):C.GC_22})

V_160 = Vertex(name = 'V_160',
               particles = [ P.t__tilde__, P.t, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF10, L.FFFF13, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF8 ],
               couplings = {(0,5):C.GC_198,(1,5):C.GC_226,(0,2):C.GC_609,(1,2):C.GC_610,(0,3):C.GC_593,(1,3):C.GC_594,(0,4):C.GC_612,(1,4):C.GC_613,(0,0):C.GC_505,(1,0):C.GC_507,(0,1):C.GC_504,(1,1):C.GC_506})

V_161 = Vertex(name = 'V_161',
               particles = [ P.u__tilde__, P.u, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF10, L.FFFF13, L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF8 ],
               couplings = {(0,5):C.GC_198,(1,5):C.GC_226,(0,2):C.GC_593,(1,2):C.GC_594,(0,3):C.GC_609,(1,3):C.GC_610,(0,4):C.GC_612,(1,4):C.GC_613,(0,0):C.GC_504,(1,0):C.GC_506,(0,1):C.GC_505,(1,1):C.GC_507})

V_162 = Vertex(name = 'V_162',
               particles = [ P.d__tilde__, P.d, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF10, L.FFFF13, L.FFFF21, L.FFFF8 ],
               couplings = {(0,3):C.GC_198,(1,3):C.GC_226,(0,2):C.GC_576,(1,2):C.GC_577,(0,0):C.GC_100,(1,0):C.GC_102,(0,1):C.GC_101,(1,1):C.GC_103})

V_163 = Vertex(name = 'V_163',
               particles = [ P.s__tilde__, P.s, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF10, L.FFFF13, L.FFFF21, L.FFFF8 ],
               couplings = {(0,3):C.GC_198,(1,3):C.GC_226,(0,2):C.GC_576,(1,2):C.GC_577,(0,0):C.GC_100,(1,0):C.GC_102,(0,1):C.GC_101,(1,1):C.GC_103})

V_164 = Vertex(name = 'V_164',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF29, L.FFFF30, L.FFFF8 ],
               couplings = {(0,8):C.GC_160,(0,4):C.GC_48,(0,6):C.GC_47,(0,7):C.GC_421,(0,5):C.GC_422,(0,1):C.GC_48,(0,0):C.GC_51,(0,3):C.GC_422,(0,2):C.GC_425})

V_165 = Vertex(name = 'V_165',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF29, L.FFFF30, L.FFFF8 ],
               couplings = {(0,8):C.GC_581,(0,4):C.GC_12,(0,6):C.GC_13,(0,7):C.GC_376,(0,5):C.GC_375,(0,1):C.GC_12,(0,0):C.GC_15,(0,3):C.GC_375,(0,2):C.GC_378})

V_166 = Vertex(name = 'V_166',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF29, L.FFFF30, L.FFFF8 ],
               couplings = {(0,8):C.GC_158,(0,4):C.GC_42,(0,6):C.GC_41,(0,7):C.GC_413,(0,5):C.GC_414,(0,1):C.GC_42,(0,0):C.GC_45,(0,3):C.GC_414,(0,2):C.GC_417})

V_167 = Vertex(name = 'V_167',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF29, L.FFFF30, L.FFFF8 ],
               couplings = {(0,8):C.GC_159,(0,4):C.GC_30,(0,6):C.GC_29,(0,7):C.GC_397,(0,5):C.GC_398,(0,1):C.GC_30,(0,0):C.GC_33,(0,3):C.GC_398,(0,2):C.GC_401})

V_168 = Vertex(name = 'V_168',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF29, L.FFFF30, L.FFFF8 ],
               couplings = {(0,8):C.GC_161,(0,4):C.GC_36,(0,6):C.GC_35,(0,7):C.GC_405,(0,5):C.GC_406,(0,1):C.GC_36,(0,0):C.GC_39,(0,3):C.GC_406,(0,2):C.GC_409})

V_169 = Vertex(name = 'V_169',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF29, L.FFFF30, L.FFFF8 ],
               couplings = {(0,8):C.GC_164,(0,4):C.GC_72,(0,6):C.GC_71,(0,7):C.GC_453,(0,5):C.GC_454,(0,1):C.GC_72,(0,0):C.GC_75,(0,3):C.GC_454,(0,2):C.GC_457})

V_170 = Vertex(name = 'V_170',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF29, L.FFFF30, L.FFFF8 ],
               couplings = {(0,8):C.GC_582,(0,4):C.GC_18,(0,6):C.GC_19,(0,7):C.GC_384,(0,5):C.GC_383,(0,1):C.GC_18,(0,0):C.GC_21,(0,3):C.GC_383,(0,2):C.GC_386})

V_171 = Vertex(name = 'V_171',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF29, L.FFFF30, L.FFFF8 ],
               couplings = {(0,8):C.GC_162,(0,4):C.GC_66,(0,6):C.GC_65,(0,7):C.GC_445,(0,5):C.GC_446,(0,1):C.GC_66,(0,0):C.GC_69,(0,3):C.GC_446,(0,2):C.GC_449})

V_172 = Vertex(name = 'V_172',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF29, L.FFFF30, L.FFFF8 ],
               couplings = {(0,8):C.GC_163,(0,4):C.GC_54,(0,6):C.GC_53,(0,7):C.GC_429,(0,5):C.GC_430,(0,1):C.GC_54,(0,0):C.GC_57,(0,3):C.GC_430,(0,2):C.GC_433})

V_173 = Vertex(name = 'V_173',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF29, L.FFFF30, L.FFFF8 ],
               couplings = {(0,8):C.GC_165,(0,4):C.GC_60,(0,6):C.GC_59,(0,7):C.GC_437,(0,5):C.GC_438,(0,1):C.GC_60,(0,0):C.GC_63,(0,3):C.GC_438,(0,2):C.GC_441})

V_174 = Vertex(name = 'V_174',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF29, L.FFFF30, L.FFFF8 ],
               couplings = {(0,8):C.GC_168,(0,4):C.GC_96,(0,6):C.GC_95,(0,7):C.GC_485,(0,5):C.GC_486,(0,1):C.GC_96,(0,0):C.GC_99,(0,3):C.GC_486,(0,2):C.GC_489})

V_175 = Vertex(name = 'V_175',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF29, L.FFFF30, L.FFFF8 ],
               couplings = {(0,8):C.GC_583,(0,4):C.GC_24,(0,6):C.GC_25,(0,7):C.GC_392,(0,5):C.GC_391,(0,1):C.GC_24,(0,0):C.GC_27,(0,3):C.GC_391,(0,2):C.GC_394})

V_176 = Vertex(name = 'V_176',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF29, L.FFFF30, L.FFFF8 ],
               couplings = {(0,9):C.GC_166,(0,5):C.GC_90,(0,7):C.GC_89,(0,8):C.GC_477,(0,6):C.GC_478,(0,1):C.GC_571,(0,2):C.GC_573,(0,0):C.GC_93,(0,4):C.GC_478,(0,3):C.GC_481})

V_177 = Vertex(name = 'V_177',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF29, L.FFFF30, L.FFFF8 ],
               couplings = {(0,8):C.GC_167,(0,4):C.GC_78,(0,6):C.GC_77,(0,7):C.GC_461,(0,5):C.GC_462,(0,1):C.GC_78,(0,0):C.GC_81,(0,3):C.GC_462,(0,2):C.GC_465})

V_178 = Vertex(name = 'V_178',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF27, L.FFFF29, L.FFFF30, L.FFFF8 ],
               couplings = {(0,9):C.GC_169,(0,6):C.GC_572,(0,8):C.GC_469,(0,4):C.GC_84,(0,7):C.GC_570,(0,5):C.GC_470,(0,1):C.GC_84,(0,0):C.GC_87,(0,3):C.GC_470,(0,2):C.GC_473})

V_179 = Vertex(name = 'V_179',
               particles = [ P.t__tilde__, P.c, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_371,(0,1):C.GC_366})

V_180 = Vertex(name = 'V_180',
               particles = [ P.t__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,1):C.GC_691,(0,0):C.GC_686})

V_181 = Vertex(name = 'V_181',
               particles = [ P.c__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_367,(0,1):C.GC_370})

V_182 = Vertex(name = 'V_182',
               particles = [ P.c__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,1):C.GC_687,(0,0):C.GC_690})

V_183 = Vertex(name = 'V_183',
               particles = [ P.t__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_602,(0,0):C.GC_603})

V_184 = Vertex(name = 'V_184',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV11, L.FFV6, L.FFV9 ],
               couplings = {(0,1):C.GC_7,(0,0):C.GC_652,(0,2):C.GC_653})

V_185 = Vertex(name = 'V_185',
               particles = [ P.u__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_365,(0,1):C.GC_368})

V_186 = Vertex(name = 'V_186',
               particles = [ P.u__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,1):C.GC_685,(0,0):C.GC_688})

V_187 = Vertex(name = 'V_187',
               particles = [ P.t__tilde__, P.u, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_369,(0,1):C.GC_364})

V_188 = Vertex(name = 'V_188',
               particles = [ P.t__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,1):C.GC_689,(0,0):C.GC_684})

V_189 = Vertex(name = 'V_189',
               particles = [ P.t__tilde__, P.c, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_753,(0,1):C.GC_748})

V_190 = Vertex(name = 'V_190',
               particles = [ P.c__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_749,(0,1):C.GC_752})

V_191 = Vertex(name = 'V_191',
               particles = [ P.t__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,1):C.GC_660,(0,0):C.GC_661})

V_192 = Vertex(name = 'V_192',
               particles = [ P.u__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_747,(0,1):C.GC_750})

V_193 = Vertex(name = 'V_193',
               particles = [ P.t__tilde__, P.u, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_751,(0,1):C.GC_746})

V_194 = Vertex(name = 'V_194',
               particles = [ P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_4})

V_195 = Vertex(name = 'V_195',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_629})

V_196 = Vertex(name = 'V_196',
               particles = [ P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_663})

V_197 = Vertex(name = 'V_197',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_5})

V_198 = Vertex(name = 'V_198',
               particles = [ P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_635})

V_199 = Vertex(name = 'V_199',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_630})

V_200 = Vertex(name = 'V_200',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_636})

V_201 = Vertex(name = 'V_201',
               particles = [ P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_650})

V_202 = Vertex(name = 'V_202',
               particles = [ P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_843})

V_203 = Vertex(name = 'V_203',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_618})

V_204 = Vertex(name = 'V_204',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_180,(0,0):C.GC_495})

V_205 = Vertex(name = 'V_205',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_176,(0,0):C.GC_493})

V_206 = Vertex(name = 'V_206',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_188,(0,0):C.GC_499})

V_207 = Vertex(name = 'V_207',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_184,(0,0):C.GC_497})

V_208 = Vertex(name = 'V_208',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_196,(0,0):C.GC_503})

V_209 = Vertex(name = 'V_209',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_192,(0,0):C.GC_501})

V_210 = Vertex(name = 'V_210',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_175})

V_211 = Vertex(name = 'V_211',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_179})

V_212 = Vertex(name = 'V_212',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_183})

V_213 = Vertex(name = 'V_213',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_187})

V_214 = Vertex(name = 'V_214',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_191})

V_215 = Vertex(name = 'V_215',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_195})

V_216 = Vertex(name = 'V_216',
               particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF25, L.FFFF26, L.FFFF7, L.FFFF8 ],
               couplings = {(1,6):C.GC_220,(0,7):C.GC_220,(0,0):C.GC_267,(2,0):C.GC_283,(1,3):C.GC_267,(3,3):C.GC_283,(1,1):C.GC_261,(3,1):C.GC_277,(1,2):C.GC_557,(0,4):C.GC_261,(2,4):C.GC_277,(0,5):C.GC_557})

V_217 = Vertex(name = 'V_217',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF25, L.FFFF26, L.FFFF7, L.FFFF8 ],
               couplings = {(1,6):C.GC_214,(0,7):C.GC_214,(0,0):C.GC_257,(2,0):C.GC_273,(1,3):C.GC_257,(3,3):C.GC_273,(1,1):C.GC_265,(3,1):C.GC_281,(1,2):C.GC_555,(0,4):C.GC_265,(2,4):C.GC_281,(0,5):C.GC_555})

V_218 = Vertex(name = 'V_218',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF24, L.FFFF25, L.FFFF7, L.FFFF8 ],
               couplings = {(1,4):C.GC_214,(0,5):C.GC_214,(0,0):C.GC_123,(2,0):C.GC_135,(1,2):C.GC_123,(3,2):C.GC_135,(1,1):C.GC_131,(3,1):C.GC_143,(0,3):C.GC_131,(2,3):C.GC_143})

V_219 = Vertex(name = 'V_219',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF24, L.FFFF25, L.FFFF7, L.FFFF8 ],
               couplings = {(1,4):C.GC_220,(0,5):C.GC_220,(0,0):C.GC_127,(2,0):C.GC_139,(1,2):C.GC_127,(3,2):C.GC_139,(1,1):C.GC_133,(3,1):C.GC_145,(0,3):C.GC_133,(2,3):C.GC_145})

V_220 = Vertex(name = 'V_220',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF25, L.FFFF26, L.FFFF7, L.FFFF8 ],
               couplings = {(1,6):C.GC_208,(3,6):C.GC_237,(0,7):C.GC_208,(2,7):C.GC_237,(0,0):C.GC_271,(2,0):C.GC_287,(1,3):C.GC_263,(3,3):C.GC_279,(1,1):C.GC_271,(3,1):C.GC_287,(1,2):C.GC_553,(3,2):C.GC_561,(0,4):C.GC_263,(2,4):C.GC_279,(0,5):C.GC_553,(2,5):C.GC_561})

V_221 = Vertex(name = 'V_221',
               particles = [ P.c__tilde__, P.c, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF8 ],
               couplings = {(0,3):C.GC_202,(1,3):C.GC_231,(0,0):C.GC_259,(1,0):C.GC_275,(0,1):C.GC_269,(1,1):C.GC_285,(0,2):C.GC_551,(1,2):C.GC_559})

V_222 = Vertex(name = 'V_222',
               particles = [ P.t__tilde__, P.c, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF8 ],
               couplings = {(0,3):C.GC_208,(1,3):C.GC_237,(0,0):C.GC_271,(1,0):C.GC_287,(0,1):C.GC_263,(1,1):C.GC_279,(0,2):C.GC_553,(1,2):C.GC_561})

V_223 = Vertex(name = 'V_223',
               particles = [ P.u__tilde__, P.u, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF25, L.FFFF26, L.FFFF7, L.FFFF8 ],
               couplings = {(1,6):C.GC_202,(3,6):C.GC_231,(0,7):C.GC_202,(2,7):C.GC_231,(0,0):C.GC_259,(2,0):C.GC_275,(1,3):C.GC_269,(3,3):C.GC_285,(1,1):C.GC_259,(3,1):C.GC_275,(1,2):C.GC_551,(3,2):C.GC_559,(0,4):C.GC_269,(2,4):C.GC_285,(0,5):C.GC_551,(2,5):C.GC_559})

V_224 = Vertex(name = 'V_224',
               particles = [ P.c__tilde__, P.c, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_199,(1,1):C.GC_228,(0,0):C.GC_259,(1,0):C.GC_275})

V_225 = Vertex(name = 'V_225',
               particles = [ P.c__tilde__, P.c, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF7, L.FFFF8 ],
               couplings = {(1,1):C.GC_210,(3,1):C.GC_239,(0,2):C.GC_205,(2,2):C.GC_234,(0,0):C.GC_263,(2,0):C.GC_279})

V_226 = Vertex(name = 'V_226',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF22, L.FFFF7, L.FFFF8 ],
               couplings = {(1,1):C.GC_199,(3,1):C.GC_228,(0,2):C.GC_204,(2,2):C.GC_233,(1,0):C.GC_259,(3,0):C.GC_275})

V_227 = Vertex(name = 'V_227',
               particles = [ P.b__tilde__, P.s, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF25, L.FFFF6, L.FFFF8 ],
               couplings = {(0,2):C.GC_205,(1,2):C.GC_227,(1,1):C.GC_590,(0,0):C.GC_263,(1,0):C.GC_279})

V_228 = Vertex(name = 'V_228',
               particles = [ P.t__tilde__, P.c, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF8 ],
               couplings = {(0,3):C.GC_205,(1,3):C.GC_234,(0,0):C.GC_271,(1,0):C.GC_287,(0,1):C.GC_129,(1,1):C.GC_141,(0,2):C.GC_533,(1,2):C.GC_545})

V_229 = Vertex(name = 'V_229',
               particles = [ P.t__tilde__, P.c, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF7, L.FFFF8 ],
               couplings = {(1,3):C.GC_210,(3,3):C.GC_239,(0,4):C.GC_205,(2,4):C.GC_234,(0,0):C.GC_271,(2,0):C.GC_287,(0,1):C.GC_129,(2,1):C.GC_141,(0,2):C.GC_533,(2,2):C.GC_545})

V_230 = Vertex(name = 'V_230',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF7, L.FFFF8 ],
               couplings = {(1,3):C.GC_199,(3,3):C.GC_228,(0,4):C.GC_204,(2,4):C.GC_233,(1,2):C.GC_125,(3,2):C.GC_137,(1,0):C.GC_269,(3,0):C.GC_285,(1,1):C.GC_529,(3,1):C.GC_541})

V_231 = Vertex(name = 'V_231',
               particles = [ P.s__tilde__, P.s, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF8 ],
               couplings = {(0,3):C.GC_199,(1,3):C.GC_228,(0,0):C.GC_125,(1,0):C.GC_137,(0,1):C.GC_269,(1,1):C.GC_285,(0,2):C.GC_529,(1,2):C.GC_541})

V_232 = Vertex(name = 'V_232',
               particles = [ P.d__tilde__, P.d, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF7, L.FFFF8 ],
               couplings = {(1,2):C.GC_202,(3,2):C.GC_231,(0,3):C.GC_202,(2,3):C.GC_231,(0,0):C.GC_125,(2,0):C.GC_137,(1,1):C.GC_125,(3,1):C.GC_137})

V_233 = Vertex(name = 'V_233',
               particles = [ P.d__tilde__, P.d, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_208,(1,1):C.GC_237,(0,0):C.GC_129,(1,0):C.GC_141})

V_234 = Vertex(name = 'V_234',
               particles = [ P.b__tilde__, P.d, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF25, L.FFFF8 ],
               couplings = {(0,1):C.GC_202,(1,1):C.GC_231,(0,0):C.GC_125,(1,0):C.GC_137})

V_235 = Vertex(name = 'V_235',
               particles = [ P.s__tilde__, P.s, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF7, L.FFFF8 ],
               couplings = {(1,2):C.GC_208,(3,2):C.GC_237,(0,3):C.GC_208,(2,3):C.GC_237,(0,0):C.GC_129,(2,0):C.GC_141,(1,1):C.GC_129,(3,1):C.GC_141})

V_236 = Vertex(name = 'V_236',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_204,(1,0):C.GC_233})

V_237 = Vertex(name = 'V_237',
               particles = [ P.b__tilde__, P.c, P.u__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_210,(1,0):C.GC_239})

V_238 = Vertex(name = 'V_238',
               particles = [ P.s__tilde__, P.c, P.t__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_204,(1,0):C.GC_233})

V_239 = Vertex(name = 'V_239',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_210,(1,0):C.GC_239})

V_240 = Vertex(name = 'V_240',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF25, L.FFFF26, L.FFFF7, L.FFFF8 ],
               couplings = {(1,6):C.GC_207,(3,6):C.GC_236,(0,7):C.GC_207,(2,7):C.GC_236,(0,0):C.GC_262,(2,0):C.GC_278,(1,3):C.GC_262,(3,3):C.GC_278,(1,1):C.GC_270,(3,1):C.GC_286,(1,2):C.GC_552,(3,2):C.GC_560,(0,4):C.GC_270,(2,4):C.GC_286,(0,5):C.GC_552,(2,5):C.GC_560})

V_241 = Vertex(name = 'V_241',
               particles = [ P.c__tilde__, P.c, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF8 ],
               couplings = {(0,3):C.GC_201,(1,3):C.GC_230,(0,0):C.GC_258,(1,0):C.GC_274,(0,1):C.GC_268,(1,1):C.GC_284,(0,2):C.GC_550,(1,2):C.GC_558})

V_242 = Vertex(name = 'V_242',
               particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF25, L.FFFF26, L.FFFF7, L.FFFF8 ],
               couplings = {(1,6):C.GC_219,(0,7):C.GC_219,(0,0):C.GC_260,(2,0):C.GC_276,(1,3):C.GC_266,(3,3):C.GC_282,(1,1):C.GC_260,(3,1):C.GC_276,(1,2):C.GC_556,(0,4):C.GC_266,(2,4):C.GC_282,(0,5):C.GC_556})

V_243 = Vertex(name = 'V_243',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF25, L.FFFF26, L.FFFF7, L.FFFF8 ],
               couplings = {(1,6):C.GC_224,(0,7):C.GC_224,(0,0):C.GC_591,(2,0):C.GC_592,(1,3):C.GC_591,(3,3):C.GC_592,(1,1):C.GC_591,(3,1):C.GC_592,(1,2):C.GC_611,(0,4):C.GC_591,(2,4):C.GC_592,(0,5):C.GC_611})

V_244 = Vertex(name = 'V_244',
               particles = [ P.u__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF25, L.FFFF26, L.FFFF7, L.FFFF8 ],
               couplings = {(1,6):C.GC_213,(0,7):C.GC_213,(0,0):C.GC_264,(2,0):C.GC_280,(1,3):C.GC_256,(3,3):C.GC_272,(1,1):C.GC_264,(3,1):C.GC_280,(1,2):C.GC_554,(0,4):C.GC_256,(2,4):C.GC_272,(0,5):C.GC_554})

V_245 = Vertex(name = 'V_245',
               particles = [ P.c__tilde__, P.t, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF8 ],
               couplings = {(0,3):C.GC_207,(1,3):C.GC_236,(0,0):C.GC_270,(1,0):C.GC_286,(0,1):C.GC_262,(1,1):C.GC_278,(0,2):C.GC_552,(1,2):C.GC_560})

V_246 = Vertex(name = 'V_246',
               particles = [ P.u__tilde__, P.t, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF25, L.FFFF26, L.FFFF7, L.FFFF8 ],
               couplings = {(1,6):C.GC_201,(3,6):C.GC_230,(0,7):C.GC_201,(2,7):C.GC_230,(0,0):C.GC_268,(2,0):C.GC_284,(1,3):C.GC_268,(3,3):C.GC_284,(1,1):C.GC_258,(3,1):C.GC_274,(1,2):C.GC_550,(3,2):C.GC_558,(0,4):C.GC_258,(2,4):C.GC_274,(0,5):C.GC_550,(2,5):C.GC_558})

V_247 = Vertex(name = 'V_247',
               particles = [ P.d__tilde__, P.b, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF25, L.FFFF8 ],
               couplings = {(0,1):C.GC_200,(1,1):C.GC_229,(0,0):C.GC_258,(1,0):C.GC_274})

V_248 = Vertex(name = 'V_248',
               particles = [ P.s__tilde__, P.b, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF25, L.FFFF7, L.FFFF8 ],
               couplings = {(1,1):C.GC_209,(3,1):C.GC_238,(0,2):C.GC_206,(2,2):C.GC_235,(0,0):C.GC_262,(2,0):C.GC_278})

V_249 = Vertex(name = 'V_249',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF22, L.FFFF7, L.FFFF8 ],
               couplings = {(1,1):C.GC_200,(3,1):C.GC_229,(0,2):C.GC_203,(2,2):C.GC_232,(1,0):C.GC_258,(3,0):C.GC_274})

V_250 = Vertex(name = 'V_250',
               particles = [ P.s__tilde__, P.b, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF25, L.FFFF8 ],
               couplings = {(0,1):C.GC_206,(1,1):C.GC_235,(0,0):C.GC_262,(1,0):C.GC_278})

V_251 = Vertex(name = 'V_251',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_203,(1,0):C.GC_232})

V_252 = Vertex(name = 'V_252',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_209,(1,0):C.GC_238})

V_253 = Vertex(name = 'V_253',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF22, L.FFFF23, L.FFFF24, L.FFFF7, L.FFFF8 ],
               couplings = {(1,3):C.GC_200,(3,3):C.GC_229,(0,4):C.GC_203,(2,4):C.GC_232,(1,2):C.GC_124,(3,2):C.GC_136,(1,0):C.GC_268,(3,0):C.GC_284,(1,1):C.GC_528,(3,1):C.GC_540})

V_254 = Vertex(name = 'V_254',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_203,(1,0):C.GC_232})

V_255 = Vertex(name = 'V_255',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_209,(1,0):C.GC_238})

V_256 = Vertex(name = 'V_256',
               particles = [ P.s__tilde__, P.s, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF7, L.FFFF8 ],
               couplings = {(1,3):C.GC_209,(3,3):C.GC_238,(0,4):C.GC_206,(2,4):C.GC_235,(0,0):C.GC_128,(2,0):C.GC_140,(0,1):C.GC_270,(2,1):C.GC_286,(0,2):C.GC_532,(2,2):C.GC_544})

V_257 = Vertex(name = 'V_257',
               particles = [ P.d__tilde__, P.d, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF8 ],
               couplings = {(0,3):C.GC_206,(1,3):C.GC_235,(0,0):C.GC_128,(1,0):C.GC_140,(0,1):C.GC_270,(1,1):C.GC_286,(0,2):C.GC_532,(1,2):C.GC_544})

V_258 = Vertex(name = 'V_258',
               particles = [ P.s__tilde__, P.s, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF25, L.FFFF26, L.FFFF8 ],
               couplings = {(0,3):C.GC_200,(1,3):C.GC_229,(0,0):C.GC_124,(1,0):C.GC_136,(0,1):C.GC_268,(1,1):C.GC_284,(0,2):C.GC_528,(1,2):C.GC_540})

V_259 = Vertex(name = 'V_259',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF24, L.FFFF25, L.FFFF7, L.FFFF8 ],
               couplings = {(1,4):C.GC_224,(0,5):C.GC_224,(0,0):C.GC_574,(2,0):C.GC_575,(1,2):C.GC_574,(3,2):C.GC_575,(1,1):C.GC_574,(3,1):C.GC_575,(0,3):C.GC_574,(2,3):C.GC_575})

V_260 = Vertex(name = 'V_260',
               particles = [ P.d__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF24, L.FFFF25, L.FFFF7, L.FFFF8 ],
               couplings = {(1,4):C.GC_213,(0,5):C.GC_213,(0,0):C.GC_130,(2,0):C.GC_142,(1,2):C.GC_122,(3,2):C.GC_134,(1,1):C.GC_130,(3,1):C.GC_142,(0,3):C.GC_122,(2,3):C.GC_134})

V_261 = Vertex(name = 'V_261',
               particles = [ P.s__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF22, L.FFFF24, L.FFFF25, L.FFFF7, L.FFFF8 ],
               couplings = {(1,4):C.GC_219,(0,5):C.GC_219,(0,0):C.GC_132,(2,0):C.GC_144,(1,2):C.GC_126,(3,2):C.GC_138,(1,1):C.GC_132,(3,1):C.GC_144,(0,3):C.GC_126,(2,3):C.GC_138})

V_262 = Vertex(name = 'V_262',
               particles = [ P.d__tilde__, P.b, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF22, L.FFFF25, L.FFFF7, L.FFFF8 ],
               couplings = {(1,2):C.GC_201,(3,2):C.GC_230,(0,3):C.GC_201,(2,3):C.GC_230,(1,0):C.GC_124,(3,0):C.GC_136,(0,1):C.GC_124,(2,1):C.GC_136})

V_263 = Vertex(name = 'V_263',
               particles = [ P.s__tilde__, P.b, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF25, L.FFFF8 ],
               couplings = {(0,1):C.GC_207,(1,1):C.GC_236,(0,0):C.GC_128,(1,0):C.GC_140})

V_264 = Vertex(name = 'V_264',
               particles = [ P.d__tilde__, P.b, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF25, L.FFFF8 ],
               couplings = {(0,1):C.GC_201,(1,1):C.GC_230,(0,0):C.GC_124,(1,0):C.GC_136})

V_265 = Vertex(name = 'V_265',
               particles = [ P.s__tilde__, P.b, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF22, L.FFFF25, L.FFFF7, L.FFFF8 ],
               couplings = {(1,2):C.GC_207,(3,2):C.GC_236,(0,3):C.GC_207,(2,3):C.GC_236,(1,0):C.GC_128,(3,0):C.GC_140,(0,1):C.GC_128,(2,1):C.GC_140})

V_266 = Vertex(name = 'V_266',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_178,(0,0):C.GC_494})

V_267 = Vertex(name = 'V_267',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_170,(0,0):C.GC_604})

V_268 = Vertex(name = 'V_268',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_174,(0,0):C.GC_492})

V_269 = Vertex(name = 'V_269',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_186,(0,0):C.GC_498})

V_270 = Vertex(name = 'V_270',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_171,(0,0):C.GC_605})

V_271 = Vertex(name = 'V_271',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_182,(0,0):C.GC_496})

V_272 = Vertex(name = 'V_272',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_194,(0,0):C.GC_502})

V_273 = Vertex(name = 'V_273',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_172,(0,0):C.GC_606})

V_274 = Vertex(name = 'V_274',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF21, L.FFFF8 ],
               couplings = {(0,1):C.GC_190,(0,0):C.GC_500})

V_275 = Vertex(name = 'V_275',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_584})

V_276 = Vertex(name = 'V_276',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_173})

V_277 = Vertex(name = 'V_277',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_177})

V_278 = Vertex(name = 'V_278',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_585})

V_279 = Vertex(name = 'V_279',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_181})

V_280 = Vertex(name = 'V_280',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_185})

V_281 = Vertex(name = 'V_281',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_586})

V_282 = Vertex(name = 'V_282',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_189})

V_283 = Vertex(name = 'V_283',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF8 ],
               couplings = {(0,0):C.GC_193})

V_284 = Vertex(name = 'V_284',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_285 = Vertex(name = 'V_285',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_286 = Vertex(name = 'V_286',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_287 = Vertex(name = 'V_287',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_288 = Vertex(name = 'V_288',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_289 = Vertex(name = 'V_289',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_290 = Vertex(name = 'V_290',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_291 = Vertex(name = 'V_291',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_292 = Vertex(name = 'V_292',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_293 = Vertex(name = 'V_293',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_294 = Vertex(name = 'V_294',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_295 = Vertex(name = 'V_295',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_296 = Vertex(name = 'V_296',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_631})

V_297 = Vertex(name = 'V_297',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_631})

V_298 = Vertex(name = 'V_298',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_631})

V_299 = Vertex(name = 'V_299',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_631})

V_300 = Vertex(name = 'V_300',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_631})

V_301 = Vertex(name = 'V_301',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_631})

V_302 = Vertex(name = 'V_302',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_631})

V_303 = Vertex(name = 'V_303',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_631})

V_304 = Vertex(name = 'V_304',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_631})

V_305 = Vertex(name = 'V_305',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_631})

V_306 = Vertex(name = 'V_306',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_633,(0,1):C.GC_637})

V_307 = Vertex(name = 'V_307',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_633,(0,1):C.GC_637})

V_308 = Vertex(name = 'V_308',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV5 ],
               couplings = {(0,0):C.GC_632,(0,1):C.GC_637})

V_309 = Vertex(name = 'V_309',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV5 ],
               couplings = {(0,0):C.GC_632,(0,1):C.GC_637})

V_310 = Vertex(name = 'V_310',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_641})

V_311 = Vertex(name = 'V_311',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_641})

V_312 = Vertex(name = 'V_312',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_641})

V_313 = Vertex(name = 'V_313',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV7 ],
               couplings = {(0,0):C.GC_632,(0,1):C.GC_638})

V_314 = Vertex(name = 'V_314',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV7 ],
               couplings = {(0,0):C.GC_632,(0,1):C.GC_638})

V_315 = Vertex(name = 'V_315',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV7 ],
               couplings = {(0,0):C.GC_632,(0,1):C.GC_638})

V_316 = Vertex(name = 'V_316',
               particles = [ P.c__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_730,(0,1):C.GC_744})

V_317 = Vertex(name = 'V_317',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_726,(0,1):C.GC_736})

V_318 = Vertex(name = 'V_318',
               particles = [ P.u__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_728,(0,1):C.GC_742})

V_319 = Vertex(name = 'V_319',
               particles = [ P.t__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_732,(0,1):C.GC_738})

V_320 = Vertex(name = 'V_320',
               particles = [ P.t__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_734,(0,1):C.GC_740})

V_321 = Vertex(name = 'V_321',
               particles = [ P.t__tilde__, P.c, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_793,(0,1):C.GC_788})

V_322 = Vertex(name = 'V_322',
               particles = [ P.c__tilde__, P.t, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_789,(0,1):C.GC_792})

V_323 = Vertex(name = 'V_323',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,1):C.GC_667,(0,0):C.GC_668})

V_324 = Vertex(name = 'V_324',
               particles = [ P.u__tilde__, P.t, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_787,(0,1):C.GC_790})

V_325 = Vertex(name = 'V_325',
               particles = [ P.t__tilde__, P.u, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_791,(0,1):C.GC_786})

V_326 = Vertex(name = 'V_326',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_799,(0,1):C.GC_813})

V_327 = Vertex(name = 'V_327',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_795,(0,1):C.GC_805})

V_328 = Vertex(name = 'V_328',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_797,(0,1):C.GC_811})

V_329 = Vertex(name = 'V_329',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_801,(0,1):C.GC_807})

V_330 = Vertex(name = 'V_330',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_803,(0,1):C.GC_809})

V_331 = Vertex(name = 'V_331',
               particles = [ P.b__tilde__, P.c, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_745,(0,1):C.GC_731})

V_332 = Vertex(name = 'V_332',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_737,(0,1):C.GC_727})

V_333 = Vertex(name = 'V_333',
               particles = [ P.d__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_739,(0,1):C.GC_733})

V_334 = Vertex(name = 'V_334',
               particles = [ P.s__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_741,(0,1):C.GC_735})

V_335 = Vertex(name = 'V_335',
               particles = [ P.b__tilde__, P.u, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_743,(0,1):C.GC_729})

V_336 = Vertex(name = 'V_336',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,1):C.GC_664,(0,0):C.GC_665})

V_337 = Vertex(name = 'V_337',
               particles = [ P.d__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_764,(0,1):C.GC_769})

V_338 = Vertex(name = 'V_338',
               particles = [ P.s__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_766,(0,1):C.GC_771})

V_339 = Vertex(name = 'V_339',
               particles = [ P.b__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_768,(0,1):C.GC_765})

V_340 = Vertex(name = 'V_340',
               particles = [ P.b__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_770,(0,1):C.GC_767})

V_341 = Vertex(name = 'V_341',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_812,(0,1):C.GC_798})

V_342 = Vertex(name = 'V_342',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_804,(0,1):C.GC_794})

V_343 = Vertex(name = 'V_343',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_806,(0,1):C.GC_800})

V_344 = Vertex(name = 'V_344',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_808,(0,1):C.GC_802})

V_345 = Vertex(name = 'V_345',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_810,(0,1):C.GC_796})

