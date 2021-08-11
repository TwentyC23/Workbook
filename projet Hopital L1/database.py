from classe import *
M1=medecin("DR JEAN ANDRE","Pédiatre",1,11)
M2=medecin("DR ANNE SINCLAIR","Radiologue",2,21)
M3=medecin("DR MAMADOU NIANG","Urgentiste Généraliste",3,31)
M4=medecin("DR PHILLIPE LEGVILLE","Urgentiste Généraliste",3,32)
M5=medecin("DR SEONG HYO HOK","Urgentiste Généraliste",3,33)
M6=medecin("DR VLADIMIR POPOV","Gastro-entérologue",1,12)
M7=medecin("DR ALEJANDRO LOPES","Pédiatre",1,13)
M8=medecin("DR MARCUS RAGEFORE","Chirurgien",2,22)
M9=medecin("DR MOUAMAD HENNI","Chirurgien",2,23)
M10=medecin("DR SANDRINE GRUDAT","Obstétricienne",1,14)
M11=medecin("DR MARIN PASCAL","Phsychologue",2,24)
LV1=urgence(1,"Le pronostic vital du patient est en danger"," immédiatement")
LV2=urgence(2,"Le patient a besoin de soin immediat pour éviter tout traumatisme"," d'ici 10min")
LV3=urgence(3,"Le patient a besoin de soin rapidement mais ne risque pas de traumatisme"," d'ici 30min")
LV4=urgence(4,"Le patient a besoin de soin mais qui peuvent attendre", "d'ici 1H")
s1=symptome("Fracture et torsion")
s2=symptome("Perte des eaux")
s3=symptome("Fièvre intense")
s4=symptome("Coupure grave, saignement abondant")
s5=symptome("Brulure")
s6=symptome("Douleur abdominal intense")
s7=symptome("Difficulté respiratoire")
s8=symptome("Evanouissement malaise")
s9=symptome("Vomissement/Diahrée sévère ou persistant")
s10=symptome("Problème phsychologique")
s11=symptome("Enfant malade")
s12=fracture("Fracture ouverte/crannienne",LV2,M2)
s13=fracture("Fracture membre/torse",LV3,M2)
s14=fracture("Fracture légère",LV4,M2)
s15=fracture("Torsion forte",LV3,M2)
s16=fracture("Torsion légère",LV4,M2)
s21=perte_des_eaux("Perte des eaux",LV3,M10)
s31=fièvre("+de41°",LV1,M3)
s32=fièvre("40°",LV2,M3)
s33=fièvre("39°",LV3,M3)
s34=fièvre("38°",LV4,M3)
s41=coupure("Blessure par balle",LV1,M8)
s42=coupure("Entaille profonde organe potentiellement blessé",LV1,M8)
s43=coupure("Entaille profonce organe non touché",LV2,M4)
s44=coupure("Entaille moyennement profonde",LV3,M4)
s45=coupure("Entaille peu profonde",LV4,M4)
s51=brulure("Brulure faciale",LV2,M5)
s52=brulure("Brulure sur large partie du corps",LV2,M5)
s53=brulure("Brulure forte mais peu étendue",LV3,M5)
s54=brulure("Brulure legère",LV4,M5)
s61=douleur_abdominal("Douleur après_blessure",LV3,M4)
s62=douleur_abdominal("Douleur gastrique",LV3,M6)
s63=douleur_abdominal("Douleur apendicite",LV2,M9)
s71=difficulté_respiratoire("Crise d'asthme",LV3,M4)
s72=difficulté_respiratoire("Trachée bouchée",LV2,M4)
s73=difficulté_respiratoire("Aucune raison apparente",LV2,M4)
s81=malaise("Arrêt du coeur",LV1,M5)
s82=malaise("Perte de connaissance",LV2,M5)
s83=malaise("Coma éthylique",LV2,M3)
s84=malaise("Malaise important",LV3,M3)
s85=malaise("Malaise léger",LV4,M3)
s91=vomi("Vomissement et/ou diahrée abondant(e)",LV2,M6)
s92=vomi("Sang dans les selles",LV2,M6)
s93=vomi("Vomissement/diahrée léger/légère",LV4,M6)
s101=phsyco("Envie suscidaire",LV1,M11)
s102=phsyco("Maladie mentale grave",LV2,M11)
s103=phsyco("Maladie mentale légère",LV3,M11)
s104=phsyco("Crise phsycologique",LV3,M11)
s111=enfant("Nourisson malade",LV1,M1)
s112=enfant("+3ans malade",LV1,M7)