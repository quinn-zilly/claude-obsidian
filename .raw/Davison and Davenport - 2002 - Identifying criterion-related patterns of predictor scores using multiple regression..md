## Page 1

PsychologicalMethods Copyright2002bytheAmericanPsychologicalAssociation,Inc.
2002,Vol.7,No.4,468–484 1082-989X/02/$5.00 DOI:10.1037//1082-989X.7.4.468
Identifying Criterion-Related Patterns of Predictor Scores Using
Multiple Regression
MarkL.Davison and ErnestC.Davenport Jr.
UniversityofMinnesota
Alongwithexamplesinvolvingvocationalinterestsandmathematicsachievement,
theauthorsdescribeamultipleregressionbased,patternrecognitionprocedurethat
canbeusedtoidentifyapatternofpredictorscoresassociatedwithhighscoreson
acriterionvariable.Thispatterniscalledthecriterionpattern.Afterthecriterion
patternhasbeenidentified,asecondregressionprocedurecanbeusedtoestimate
theproportionofvariationattributabletothecriterionpattern.Cross-validationcan
thenbeusedtoestimatethevariationattributabletoacriterionpatternderivedfrom
regressionweightsestimatedinanothersample.Finally,issuesofcriterionpattern
invarianceandinterpretationarediscussed.
According to Meehl (1950), pattern is one of the est,considerthehypotheticaldatainTable1,loosely
most important words in the clinician’s vocabulary. patterned after a study by Goldberg (1970). For 6
He questioned whether predictor score patterns can clinical patients, the top portion of Table 1 shows
improve criterion score prediction. In this article, we scores on four scales of a hypothetical personality
do not attempt to answer Meehl’s question as to the inventory, the Inventory of Personality and Mood
predictivepowerofscorepatterns,butwedodescribe Manifestations (IPMM). The scales are Anxiety (A),
regressionmethodsbywhichresearcherscanaddress Hypochondriasis (H), Schizophrenia (S), and Bipolar
the question. Disorder (B). The table also contains a dichotomous
Insomeresearch,theinvestigatormaybeinterested criterion variable, N-P, that indicates whether the pa-
in determining whether there is a pattern of predictor tient was diagnosed as neurotic (N-P (cid:1) 1) or psy-
scoresassociatedwithhighscoresonacriterionvari- chotic(N-P(cid:1)0).Visuallyinspectingthisdatashows
ableand,ifso,indetermininghowmuchvariationin thattheneuroticandpsychoticpatientshavedifferent
criterion scores can be attributed to that pattern. For scorepatterns.Ineachneuroticpatient’srowofdata, the moment, we define a profile pattern as the ar-
Clients1–3,theAandHscorestendtobehigherthan
rangementofthescoresinasinglerespondent’svec- theSandBscores.Ineachpsychoticpatient’srowof
tor of predictor scores. If there is a predictor-score
data, Clients 4–6, the A and H scores are lower than
arrangement associated with high scores on the crite- the S and B scores.
rion, we call this arrangement the criterion pattern.
InthesmallsampleatthetopofTable1,thepattern
Tobetterunderstandtheresearchquestionofinter-
associated with the neurotic diagnosis can readily be
discernedvisually.Inalargersample,however,visual
identificationofthepatterncanbemoredifficult,and
Mark L. Davison and Ernest C. Davenport Jr., Depart-
mentofEducationalPsychology,UniversityofMinnesota. some formal analysis may be needed to find the pat-
ThisresearchwassupportedbyNationalCenteronEdu- ternassociatedwithhighscoresonthecriterionvari-
cationStatisticsGrantR999B40010andMinnesotaDepart- able. This article describes how multiple regression
ment of Children, Families, and Learning Contract 38709. can be used to identify such a pattern and how mul-
OurthankstoMichaelHarwellforhelpfulcommentsona tiple regression can be used to quantify the variation
draft and to Rex Blake, Rene Dawis, Sharon Sackett, and
accountedforbythatpattern.Thatis,wefirstdescribe
DavidJ.Weiss,whocollecteddatausedinouranalyses.
a multiple regression procedure for identification of
Correspondence concerning this article should be ad-
thecriterionpattern.Thenwedescribecorrelationand
dressed to Mark L. Davison, Department of Educational
regression procedures that can be applied after the
Psychology, University of Minnesota, 178 Pillsbury Drive
Southeast, Minneapolis, Minnesota 55455. E-mail: criterion pattern has been identified to estimate the
mld@umn.edu variation accounted for by that pattern.
468
.srehsilbup
deilla
sti
fo
eno
ro
noitaicossA
lacigolohcysP
naciremA
eht yb
dethgirypoc
si
tnemucod
sihT
.yldaorb
detanimessid
eb
ot
ton
si
dna
resu
laudividni
eht
fo
esu
lanosrep
eht
rof
ylelos
dednetni
si
elcitra
sihT
.devreser
era
,seigolonhcet
ralimis
dna
,gniniart
IA
,gninim
atad
dna txet
rof
gnidulcni
,sthgir
llA

## Page 2

CRITERION-RELATEDPATTERNS 469
Table1
InventoryofPersonalityandMoodManifestation(IPMM)Profilesof6Normaland6ClinicalRespondentsDiagnosedas
EitherNeuroticorPsychotic
IPMMpredictorscaleandvariables
Clientandvector A H S B N-P X Cov C-N
p. pc
Clinicalsample
1 75 60 50 50 1 58.75 115.4 1
2 60 75 45 55 1 58.75 150.0 1
3 60 60 55 45 1 55.00 98.1 1
4 50 50 75 60 0 58.75 −115.4 1
5 45 55 60 75 0 58.75 −150.0 1
6 55 45 60 60 0 55.00 −98.1 1
Normalsample
7 25 40 50 50 41.25 0
8 40 25 55 45 41.25 0
9 40 40 45 55 45.00 0
10 50 50 25 40 41.25 0
11 55 45 40 25 41.25 0
12 45 55 40 40 45.00 0
Regressionweightsandcriterion-patternvectors
b 0.00923 0.02308 −0.00923 −0.02308 v
b −b 0.00923 0.02308 −0.00923 −0.02308
v .
x :k(cid:1)500 4.62 11.54 −4.62 −11.54
c x :k(cid:1)1,000 9.23 23.08 −9.23 −23.08 c
x :k(cid:1)2,000 18.46 46.16 −18.46 −46.16
c
Note. A(cid:1)Anxiety;H(cid:1)Hypochondriasis;S(cid:1)Schizophrenia;B(cid:1)BipolarDisorder;N-P(cid:1)neuroticversuspsychoticcriterionvariable;
X (cid:1)theprofilelevelofpersonp;Cov (cid:1)thecovariancebetweenthescoreprofileofpersonpandthecriterion-patternvector;C-N(cid:1) p. pc
clinicalversusnormalsample(1(cid:1)clinical,0(cid:1)normal).
The literature contains a variety of methods for terns exist but whether the patterns have any theoret-
studying the patterns that appear in profiles (Games, icalorappliedvalidity(Davison,2000).OrasMeehl
1990;Moskowitz&Hershberger,2002;Nesselroade, (1950)phrasedthequestion,Dothepatternshaveany
2001), for example, cluster analysis (Glutting, Mc- predictive efficiency? A two-step procedure for ad-
Grath, Kamphaus, & McDermott, 1992; Gore, 2000; dressing this question involves first identifying fre-
Lorr,1994),configuralfrequencyanalysis(Stanton& quent or prominent patterns using an internal proce-
Reynolds, 2000; von Eye, 1990; von Eye, Spiel, & dure described above and then investigating the
Wood, 1996), modal profile analysis (Moses & patterns’ validity in a second step. Nothing in an in-
Pritchard, 1995; Skinner, 1979), and multidimen- ternal procedure would guarantee that identified pat-
sionalscaling(Davison,Gasser,&Ding,1996;Davi- terns have associations with external criterion vari-
son, Kuang, & Kim, 1999). Such methods typically ables. A more efficient, one-step procedure would
presume a data matrix containing V variables and P involve identifying profile patterns on the basis of
observations on each variable. Each row of the data their associations with external criteria or diagnostic
matrix,X ,...,X (p(cid:1)1,...,P;v(cid:1)1,...,V), categories. Any pattern identified in this fashion
p1 pV
constitutes a profile of scores for person p. would have associations with at least one external
Cluster analysis, modal profile analysis, and mul- variable.
tidimensional scaling are internal analyses in the Given discrete predictor and criterion variables,
sensethattheanalysisreliessolelyontheVvariables configural frequency analysis (Stanton & Reynolds,
within each profile. No external criterion or diagnos- 2000; von Eye, 1990; von Eye et al., 1996) can be
ticcategoryvariableisusedtoidentifytheprominent usedtostudytherelationshipbetweenconfigurations
profile types. of scores on predictor variables and a criterion vari-
In clinical practice and applied research, the fun- able. That is, configural frequency analysis can be
damentalquestionoftenisnotwhetherprominentpat- used to determine whether certain predictor-response
.srehsilbup
deilla
sti
fo
eno
ro
noitaicossA
lacigolohcysP
naciremA
eht
yb
dethgirypoc
si
tnemucod
sihT
.yldaorb
detanimessid
eb
ot
ton
si dna
resu
laudividni
eht
fo
esu
lanosrep
eht
rof
ylelos
dednetni
si
elcitra
sihT
.devreser
era
,seigolonhcet
ralimis
dna
,gniniart
IA
,gninim
atad
dna
txet
rof
gnidulcni
,sthgir
llA

## Page 3

470 DAVISONANDDAVENPORT
patterns occur more frequently in some criterion cat- mean of the predictor scores for person p, X (cid:1)
p.
egories than in others. If the predictor (or criterion) (1/V)(cid:1) X . This mean quantifies the overall eleva-
v pv
variables are continuous, they must be artificially di- tion of the scores in person p’s profile. The pattern
vided into categories before a configural frequency component is the V-length vector containing the de-
analysiscanbeperformed(e.g.,Stanton&Reynolds, viationofeachpredictorscorefrompersonp’smean:
2000). This artificial categorization of predictor x (cid:1)[X −X ].Becausetheelementsofthepattern
p pv p.
scores leads to a loss of predictor information. vector are expressed as deviations about the person’s
Anotherapproachistoidentifyallpeopleinagiven own mean, they always sum to zero.
diagnostic category (or all people high on a criterion To illustrate the decomposition of a profile into
variable) and compute the mean predictor profile for level and pattern components, consider the data of
thepeopleinthatdiagnosticcategory.Thatmeanpro- Client 3 in Table 1 with the predictor profile vector
fileisinsomesensetypicalofthecategory,butitmay (60, 60, 55, 45). The mean of these four scores, the
not distinguish members of the category from mem- level component, equals 55. The pattern vector (5, 5,
bers of other categories. That is, the mean profile 0,−10)canbecomputedbysubtracting55fromeach
characteristic of people in the diagnostic category element in the respondent’s predictor-score vector.
may also characterize people in other categories as Whentherearefourpredictors,asintheexampleof
well. Table 1, the multiple regression equation for the ex-
The procedures described in this article rely on pectedcriterionscoreofpersonp,Y(cid:2) ,canbewritten
p multiple regression techniques that are applicable to asY(cid:2) (cid:1)b X +b X +b X +b X +a,whereb
p 1 p1 2 p2 3 p3 4 p4 v
continuous predictor and criterion variables. We be- istheregressionweightforpredictorvariablev,anda
gin by showing how multiple regression can be used istheinterceptconstant.Moregenerally,thisequation
to identify the criterion pattern, the pattern of predic- canbewrittenforanynumberofVpredictorvariables
torscoresassociatedwithhighscoresonthecriterion. as follows:
Afteridentificationofthecriterionpattern,correlation
Y(cid:2) (cid:1) (cid:1) b X + a. (1) and regression can be used to quantify the variation p v v pv
accounted for by the criterion pattern. Next, we de-
The regression weights in Equation 1 can be used to
scribe a cross-validation technique to estimate the identifyacriterionpatternspecifiedasasetofpattern
shrinkage in R2 that would result when the criterion
vectors. As we show below, these pattern vectors are
pattern is used to predict the criterion in a new
called criterion-pattern vectors, because the regres-
sample. Illustrative examples are presented in which
sion equation for predicting the criterion can be re-
correlationandregressionareusedtoidentifythecri-
written in terms of any pattern vector in that set. All
terion pattern and to determine the amount of varia- ofthevectorsinthatsethavethesamearrangementof
tionaccountedforbythatpattern.Finally,wediscuss scores and, in that sense, they all have the same pat-
several issues involving the invariance and the inter-
tern.
pretation of the criterion pattern.
Finding the CriterionPattern
Identifying the CriterionPattern
Before describing how to find a criterion pattern,
wemustfirstdefineitmoreprecisely.Todoso,letb*
In explaining the regression procedures below, we
be the V-length vector of least squares regression
used a dot notation to designate row means, column
weights in Equation 1, expressed as deviations about
means, and the grand mean. The mean of the row
the regression weight mean, b* (cid:1) [b* (cid:1) b − b ].
corresponding to person p is designated as X (cid:1) v v .
p. Here b is the mean regression weight, b (cid:1) (1/
(1/V)(cid:1) X . The mean of column v is designated as . .
v pv V)(cid:1) b . The vector b* is a member of the criterion-
X (cid:1) (1/P) (cid:1) X . Similarly, the grand mean is des- v v
.v p pv pattern vectors. The set of criterion-pattern vectors
ignated as X (cid:1) (1/PV)(cid:1) X . The dot notation is
.. pv pv canbespecifiedintermsofb*asfollows:Avectorof
also used to designate the mean of the multiple re-
scores, x , belongs to the set of criterion-pattern vec-
gression weights, b (cid:1) (1/V)(cid:1) b . c
. v v tors if there exists a scalar constant k > 0 such that
Themultipleregressionanalysisbelowisbasedon
a decomposition of each person’s profile of predictor x (cid:1) kb*. (2)
c
scoresintotwocomponents:alevelcomponentanda
patterncomponent.Thelevelcomponentissimplythe Because all members of the criterion pattern set are
.srehsilbup
deilla
sti
fo
eno
ro
noitaicossA
lacigolohcysP
naciremA
eht
yb
dethgirypoc
si
tnemucod
sihT
.yldaorb
detanimessid
eb
ot
ton
si
dna
resu
laudividni
eht
fo
esu
lanosrep
eht
rof
ylelos
dednetni
si
elcitra
sihT
.devreser
era
,seigolonhcet
ralimis
dna
,gniniart
IA
,gninim
atad
dna
txet
rof
gnidulcni
,sthgir
llA

## Page 4

471CRITERION-RELATEDPATTERNS

proportional,theyallsharethesamepattern.Thatis,rionvariable.Asanexample,considerthethreepat-

,shownatthebottomofTable1,alloftheyallhavethesamearrangementofhighesttolow-ternvectors,x

c

whicharemembersofthecriterionsetforthecrite-estscores.Ifapatternisdefinedasanarrangementof

rionvariableToderivethesethreescorevectors,scores,theneachvalueofspecifiesanexemplarofN-P.k

weregressedthefourpredictorsinTable1,thearrangement.Thepatternisthearrangementcom-A,H,S,

andontothecriterionvariable,toobtainthemontoallexemplars.B,N-P,

fourunstandardizedregressionweights,0.00923,Asshownbelow,theregressionequationcanbe

0.02308,−0.00923,and−0.02308,forpredictorsrewrittenintermsofanymemberofthecriterionA,

andrespectively.Ordinarily,onewouldhavepatternset.Insomecases,itsufficestospecifytheH,S,B,

(cid:1)

tosubtractthemeanregressionweightfromeachofequationintermsof*itself(i.e.,1).Inotherbk

(cid:2)

thesefourvaluestoobtaintheelementsof*.How-cases,valuesof1facilitategraphicalortabularbk

ever,themeanofthesefourregressionweightsequalspresentationofthepattern.Instillotherapplications,

.y

zero,andthereforetheregressionweightsthemselvestherewillbeseveralcriterionvariables,eachdelin-l

d.

sa

ro

earetheelementsof*.eatingadifferentsetofcriterion-patternvectors.Theb

rh.

bds

eid

Multiplyingtheelementsof*(thefourregressionresearchermaythenwishtocomparetheseveralpat-blv

be

rut

ea(cid:1)

pweights)by500gavethefirstmemberoftheternsintermsofthedegreetowhichtheycharacterizeksn

eid

rm

e

ecriterionsetshownatthebottomofTable1.Multi-thedataofagivenrespondent.Appropriatechoicesofie

lr

sla

as

(cid:1) i,

plyingby1,000gavethesecondmember,andcanfacilitatesuchcomparisons.Theissueofselect-kksds

te

iei

(cid:1)gf

bmultiplyingby2,000gavethethirdmember.Allingwillbediscussedfurtherbelow.kk

oo

o l

eot

n threescorevectorsinTable1havethesamearrange-Usingthedefinitionofthecriterion-patternvectorsn

to

oh

ncr

o ementofhighesttolowestscores.Thatis,inallthreeinEquation2,wecanusemultipleregressiontoiden-

s

tin

r

doa

ofthesescorevectors,Histhehighestscore,Aisthetifythesetofpatternvectorsassociatedwithacrite-ni

lt

iaa

m

ir

cie

sos

sud

s n

Al

aa

u l

,adg

cin

vi

igi

nd

oi

nal

ori

the

I

ch

Ay

t

s f

,Pog

nn

e

ias

n

uci

mi

lr

ae

nam

to

aAs

dr

ee

dp

hn

te

a

yh

tbt

x

red

ot

e f

rt

ohy

fgl

eig

lr

ony

sip

d

odu

cel

cds

nni

iet

nt,

sne

tim

h

sg

ui

i c

re

oll

cld

Ai

ts

r

ia

h

sT

i

h

T

(cid:1)(cid:1)Criterion-patternvectorforcriterionvariableinTable1.1,000;IPMMInventoryofPersonalityandFigure1.N-Pk

MoodManifestation.

## Page 5

472 DAVISONANDDAVENPORT
secondhighestscore,Sisthethirdhighestscore,and onthefourpredictorsisshowninthecolumnlabeled
B is the lowest score. Figure 1 shows the criterion- X .Withanymultipleregressionprogram,readerscan
p
pattern vector for k (cid:1) 1,000. In that score vector, A readily verify the relationship between Equations 1
and H are the highest scores, and S and B are the and 4 by showing that the same predicted value
lowestscores.Thisarrangementisconsistentwiththe (within rounding error) is obtained for every respon-
pattern observed in the patient’s data: Each neurotic denteitherby(a)regressingthecriterionN-Pontothe
patient had a higher score on A and H than on S four predictors A, H, S, and B, or (b) regressing the
and B. criterionvariableN-PontothetwopredictorsX and
p.
Cov . Furthermore, the same multiple correlation is
Reexpressing the Regression Equation in Terms pc
obtained from either of these two regressions.
of a Criterion-PatternVector
It remains to determine the degrees of freedom as-
As shown in Appendix A, the regression Equation sociated with the pattern effect and the level effect.
1 can be reexpressed as Given V predictors, there are V degrees of freedom
associatedwiththeregressionweights.Thesedegrees
Y(cid:2) =(cid:1) (cid:1)b −b(cid:2)(cid:1)X −X (cid:2)+(cid:1) bX +a. (3) p v v . pv p. v . p. offreedommustbedividedbetweenthepatterneffect
InEquation3,thefirstsumontherightsideisalinear and the level effect. The mean of the regression
combinationoftheelementsinpersonp’spatternvec- weights in Equation 1 consumes only one degree of
tor:(X −X ).Hereafter,thissumwillbecalledthe freedom.Themeanregressionweightistheparameter
pv p. patterneffect.Thesecondsumontherightisafunc- associated with the level effect in Equation 4. There-
tionofpersonp’sprofilelevelX .Therefore,thissum fore, there is only one degree of freedom associated
p.
will be called the level effect.1 withtheleveleffect.TheremainingV−1degreesof
As is further shown in Appendix A, for any crite- freedom are associated with the pattern effect. In
rion-patternvectorx ,Equation1(orEquation3)can computing any criterion-pattern vector, V parameters
c
be rewritten in the form2 (b v − b) are used, but these parameters are subject to
theconstraintthattheirsummustbezero.Hence,only
Y(cid:2) p (cid:1) (V/k)Cov pc + Vb . X p. + a, (4) V − 1 of these parameters are free. Consequently,
there are only V − 1 degrees of freedom associated where V is again defined as the number of variables,
Cov (cid:1) (1/V)(cid:1) (X − X )(X − X ) is the covari- with the pattern effect.
pc v pv p. cv c.
ance between the actual predictor scores of person p
andthescoresincriterion-patternvectorx ,X isthe Estimating the Variation Accounted for by the
c p.
mean of the predictor scores for person p, and X is Pattern and LevelEffects c.
the mean of the scores in x . c Once the criterion pattern has been identified, ad- In Equation 4, the term involving Cov is the pat-
pc ditional correlation and regression procedures can be tern effect. The term involving X is the level effect.
p. used to estimate the variation accounted for by the
Equation 4 shows how regression Equation 1 can be
profile pattern effect and the profile level effect. The
expressed in terms of any pattern vector in the crite-
predictors in these additional correlation and regres- rion set. More precisely, the regression equation can
sion procedures are the two predictors in Equation 4,
be rewritten in terms of the covariance between the
Cov and X , rather than the V variables in Equa-
scores in any criterion-pattern vector x and the pre- pc p.
c tion 1.
dictorscoresofpersonp.Foranygivenprofilelevel,
X , the predicted value Y(cid:2) increases as its match to After the V predictor weights have been estimated
p. p usingmultipleregression,anycriterion-patternvector
thecriterionpatternCov increases.Thus,thepattern
pc can be specified using Equation 2 and any desired
effect is conditional on profile level.
value of k. Given the specification of a criterion-
For purposes of illustration, Table 1 shows the co-
pattern vector, for each person one can calculate
varianceCov forthe6peopleatthetopofTable1.
pc Cov aswedidinTable1usingthecriterionpattern
Here, the criterion-pattern vector is that shown at the pc
bottom of Table 1 for k (cid:1) 1,000. Each of these six for which k (cid:1) 1,000. The correlation between Y and
quantities, Cov , is the covariance between the four
pc
predictorscoresofpersonpandthefourscoresinthe
criterion-patternvectorfork(cid:1)1,000.Foreachofthe 1Equation3isEquationA3inAppendixA.
6peopleatthetopofTable1,themeanoftheirscores 2Equation4isEquationA6inAppendixA.
.srehsilbup
deilla
sti
fo eno
ro
noitaicossA
lacigolohcysP
naciremA
eht
yb dethgirypoc
si
tnemucod
sihT
.yldaorb
detanimessid
eb ot
ton
si dna
resu
laudividni
eht
fo
esu
lanosrep
eht rof
ylelos
dednetni
si
elcitra
sihT
.devreser
era
,seigolonhcet
ralimis
dna
,gniniart
IA
,gninim
atad
dna
txet
rof
gnidulcni
,sthgir
llA

## Page 6

CRITERION-RELATEDPATTERNS 473
Cov canbecalculated.Thesquaredcorrelationwill multiplecorrelationforthemodelwithjustthepattern
pc
be the proportion of variation in Y that can be ac- effect. Because the model including just the pattern
counted for by the profile pattern effect alone. Be- effect is hierarchically nested within the model con-
cause Cov indexes the match between the actual tainingbothlevelandpatterneffects,onecanthentest
pc
profileofpersonpandthecriterion-patternvector,the thehypothesisH :R2(cid:1)R2usingtheusualFstatistic
0 F P
squaredcorrelationcanalsobeinterpretedasthepro- with 1 and N − V − 1 degrees of freedom, F (cid:1) [(R2
F
portion of variation in Y that is attributable to the − R2)(N − V − 1)] / [(1 − R2)]. For our example in
P F
match with the criterion profile pattern. Using the
Equation1,R2 (cid:1).96,R2 (cid:1).96,andF(1,1)(cid:1)0.00,
F P
criterionvariableN-PandthevaluesCov inTable1, p>.05.Thus,wewouldnotrejectthenullhypothesis,
wefoundthatthecorrelationwas.98.Int p h c isexample, H 0 : R F 2 (cid:1) R P 2, in favor of the alternative.
96%ofthevariationinthecriterionvariableN-Pcan Tosummarizetheresultsofthisexample,fromthe
be attributed to the pattern effect alone. regressionweightswewereabletoidentifythesetof
Similarly, one can compute each person’s profile criterion-pattern vectors, three of which are shown at
the bottom of Table 1 and one of which is plotted in
level,X ,andthecorrelationbetweenYandX .The
p. p.
Figure 1. As expected from our visual inspection of
squaredcorrelationwillbetheproportionofvariation
the data, the criterion-pattern vectors contain higher
inYpredictedfromprofilelevelalone.Intheexample
scores on the A and H scales than on the S and B
of Table 1, the correlation between level and the cri-
scales. Correlating the profile match statistic, Cov ,
terion variable N-P was .00. None of the variation in pc
led to the conclusion that the pattern effect alone ac-
N-Pcanbeattributedtoindividualdifferencesinpro-
countedfor96%ofthevariationinthecriterionN-P.
file level.
Correlating the level statistic, X , with the criterion
By performing a multiple regression to predict Y p.
variable led to the conclusion that the level effect
from the two predictors Cov and X , one can esti-
pc p. aloneaccountedfornovariationinN-P.Togetherthe
mate how much variation the pattern effect can pre-
pattern and level effects accounted for 96% of the dictoverandabovetheleveleffect,howmuchvaria-
criterion variation.
tion the level effect can predict over and above the
pattern effect, and the amount of variation accounted
A Second CriterionVariable for by the two combined. First, consider the question
of whether the pattern effect accounts for variation TobrieflyextendtheexampleinTable1,asecond
overandabovetheleveleffect.LetR2 bethesquared criterion variable has been added for the full sample
F
multiple correlation obtained when both the pattern composed of both the 6 clinical patients and the 6
andtheleveleffectsareincludedinthemodel.LetR2 normal respondents. This second criterion variable, L
bethesquaredmultiplecorrelationforthemodelwith C-N, distinguishes between the clinical respondents
just the level predictor. Because the model including (C-N (cid:1) 1) and the normal respondents (C-N (cid:1) 0).
justtheleveleffectishierarchicallynestedwithinthe The last column of Table 1 shows this second crite-
model containing both level and pattern effects, one rion variable. As can be seen by inspecting the level
can then test the null hypothesis about population variable, X in Table 1, the clinical sample tends to
p.
multiple correlations, H : R2 (cid:1) R2, using the usual have more elevated profiles than does the normal
0 F L
F statistic with V − 1 and N − V − 1 degrees of sample. Therefore, one would expect the level effect
freedom,F(cid:1)[(R2 −R2)(N−V−1)]/[(1−R2)(V− toaccountforasubstantialportionofthevariationin
F L F
1)]. For our example in Equation 1, R2 (cid:1) .96, R2 (cid:1) this second criterion variable.
F L
.00,andF(3,1)(cid:1)8.00,p>.05.Thus,inthisexample First,thecriterionvariableC-Nwasregressedonto
withalargenumberofpredictorsrelativetothenum- the four predictors A, H, S, and B. This yielded a
ber of respondents, we would not reject the null hy- squared multiple correlation of .96 and four unstand-
pothesis,H :R2(cid:1)R2,infavorofthealternativeeven ardized regression weights, 0.01844, 0.01341,
0 F L
though the pattern effect adds 96% to the variation 0.01844,and0.01341,forA,H,S,andB,respectively.
accounted for over and above level alone. Subtracting the mean, b (cid:1) .015925, from each of
.
Next, consider the question of whether the level theseweightsgivesthecriterion-patternvectorb*(cid:1)
effect accounts for variation over and above the pat- .002515, −.002515, .002515, and −.002515, respec-
terneffect.Again,letR2 bethesquaredmultiplecor- tively.Thecorrelationbetweenthecriterionandlevel
F
relation obtained when both the level and pattern ef- effect is .973, which is highly significant (because of
fectsareincludedinthemodel.LetR2 bethesquared the increased sample size, which is twice that of the
P
.srehsilbup
deilla
sti
fo
eno
ro
noitaicossA
lacigolohcysP
naciremA
eht
yb
dethgirypoc
si
tnemucod
sihT
.yldaorb
detanimessid
eb
ot
ton
si
dna
resu
laudividni
eht
fo
esu
lanosrep
eht
rof
ylelos
dednetni
si
elcitra
sihT
.devreser
era
,seigolonhcet
ralimis
dna
,gniniart
IA
,gninim
atad
dna
txet
rof
gnidulcni
,sthgir
llA

## Page 7

474 DAVISONANDDAVENPORT
firstexample),andthesquaredmultiplecorrelationis estimated in Sample 1, Cov . For each person in
pc
.95. In contrast, the correlation between the criterion Sample 2, we also computed the level of their pro-
and the pattern effect is exactly zero. Thus, our hy- file, X .
p.
pothetical clinical patients are distinguished from HavingcomputedCov andX foreachpersonin
pc p.
nonpatients by their high level of symptoms. In con- Sample 2, we then computed (a) the correlation be-
trast, clinical patients, neurotics, and psychotics, are tweenthecriterionvariableandX ,(b)thecorrelation
p.
distinguished from each other by their pattern of between the criterion variable and Cov , and (c) the
pc
symptoms (as shown in the first example). multiple correlation obtained by regressing the crite-
rionvariableontobothX andCov .Thisallowedus
p. pc
to estimate the proportion of variation accounted for
Cross-Validation
bytheleveleffectalone,thepatternaffectalone,and
the combination of the level effect and the pattern
As noted by Dawes (1979) and others, regression
effect when the profile-match parameter, Cov , is
weights are notoriously unstable from sample to pc
computed with respect to a criterion-pattern vector
sample. When regression weights are derived in one
based on regression weights from a previous sample
sample,oftentheregressionequationwillnotaccount
(Sample 1). In the cross-validation sample, there will
for as much variation in a second sample. Cross-
be only one degree of freedom associated with the
validation, jackknifing, bootstrapping, or Browne’s
pattern effect, the degree of freedom associated with
(1975a,1975b)procedurecanbeusedtoestimatethe
dropinR2tobeexpectedwhentheregressionweights the regression weight for the predictor Cov pc .
This process was then repeated reversing the roles
estimated in one sample are then applied in a new
of Samples 1 and 2. That is, Sample 2 was used to
sample.Asimilarissueariseswithrespecttoaprofile
estimatetheregressionweightsandanassociatedcri-
pattern derived in one sample, because the profile
terion-patternvector.Thiscriterion-patternvectores-
pattern is a function of the regression weights. When
timatedinSample2wasthenusedtocomputeCov a profile pattern is derived from the regression pc
for each person in Sample 1. This profile-match sta-
weightsestimatedinonesample,thatpatternmaynot
tistic, Cov , was then used to predict the criterion
account for as much variation in a second sample. pc
variableinSample1bothbyitselfandincombination Cross-validationisonewaytoestimatethedropinR2
with the level statistic X . This double-cross valida-
to be expected when a profile pattern derived in one p.
tion scheme provides two estimates of the variation
sample is then applied in a second sample.
accountedforinasecondsamplebyaprofilepattern
In the real data examples below, we first applied
estimated in a prior sample, one estimate based on
multiple regression to the full sample to identify the
Sample 1 serving as the cross-validation sample and criterion profile pattern and to estimate the variation
another based on Sample 2 serving as the cross- accountedforbythatpattern.Then,weappliedcross-
validation sample. validation to estimate the variation that would be ac-
counted for when a profile pattern derived from re-
gression weights in one sample is then applied to a Examples
secondsample.Inthissection,wedescribethecross-
validation procedure used in the real data examples Intheexamplesbelow,ourreportedresultsempha-
below. sizethepatterneffect.Thatis,wefirstshowthegraph
Fortheseanalyses,werandomlyassignedapproxi- of a criterion-pattern vector identified using the pre-
mately 50% of the people to Sample 1 and 50% to dictor weights from a multiple regression analysis
Sample 2. The full model was fitted in Sample 1 to basedonthefullsample.Thenweshowatablelisting
estimate the regression weights. From the regression the percentage of variation accounted for by the pat-
weights, we then estimated a criterion-pattern vector tern effect alone, the percentage of variation that the
using the definition in Equation 2. In estimating the pattern effect accounts for over and above the level
criterion-pattern vector, any value of k can be used, effect (called the pattern increment), and the total
becausetheamountofvariationaccountedforbythe amountofvariationaccountedforbybothpatternand
criterion-pattern vector will be the same irrespective level. These tables show results for the full sample
of k. For each person in Sample 2, we computed the and two cross-validation samples.
covariance between their actual predictor profile Inevaluatingeachcriterionpatternestimatedinthe
scores and the scores in the criterion-pattern vector full sample, we first used the significance test de-
.srehsilbup
deilla
sti
fo eno
ro
noitaicossA
lacigolohcysP
naciremA
eht
yb
dethgirypoc
si
tnemucod
sihT
.yldaorb
detanimessid
eb
ot
ton
si
dna
resu
laudividni
eht
fo
esu
lanosrep
eht
rof
ylelos
dednetni
si
elcitra
sihT
.devreser
era
,seigolonhcet
ralimis
dna
,gniniart
IA
,gninim
atad
dna
txet
rof
gnidulcni
,sthgir
llA

## Page 8

475CRITERION-RELATEDPATTERNS

.y

l

d.

sa

ro

e

rh.

bds

eid

lv

be

rut

ea

psn

eid

rm

e

eie

lr

sla

as

i,

sds

te

iei

gf

b

oo

o l

eot

n n

to

oh

ncr

o e

s

tin

r

doa

nil

tia

am

ir

cie

sos

sud

s n

Al

aa

u l

,adg

cin

vi

igi

nd

oi

nal

ori

the

I

ch

Ay

t

(cid:1)s f

Criterion-patternvectorfortheSocialClosenesscriterionofExample1.100.Figure2.k,P

og

nn

e

ias

n

uci

mi

lr

ae

1985).ThecriterionvariablewasapersonalityscalescribedinAppendixBtodeterminewhichregressionnam

to

aAs

dfromTellegen’s(1982)MultidimensionalPersonalityweightsweresignificantlyabovethemeanregressionr

ee

dp

hn

(cid:1) t

Questionnaire,theSocialClosenessscale.There-:weight.Thatis,wetestedthehypothesisbHea

yh 0v

tbt

x(cid:3)

spondentswere328clientsoftheMinnesotaVoca-()foreachvalueofIneffect,weconcludedthatbv.red

ot

.e f

rt

3ohytionalAssessmentClinic.,couldbeconsideredtoTheresearcherwantedtoiftheregressionweight,b

fgl

v e

ig

lr

ondiffersignificantlyfromthemeanoftheregressionknowwhetherthepersonalitytrait,socialcloseness,isy

sip

d

odu

weights,thenthecorrespondingelementinthecrite-associatedwithapatternofvocationalpreferencescel

cds

nni

i,couldbeconsideredtodifferrion-patternvector,reflectedinthesixvocationalinterestscales.Xet

nt,

cvsn

et

imhsignificantlyfromthemeanscoreinthecriterion-Wefirstestimatedunstand-

Full-sampleresults.

sg

ui

i c

re

patternvector.Interpretationofthecriterion-patternardizedregressionweightsinthefullsample.Then ol

lc

ld

Ai

ts

rvectorwasbasedprimarilyonvariablesforwhichtheweconvertedeachregressionweighttoadeviation

ia

h

sT

(cid:1)(cid:3)i

:()couldberejectedatthe.05hypothesisaboutthemeanregressionweight.Thecriterion-bbHh

T0v.

(cid:1)

level.Resultsofthesignificancetestwereemployedpatternvectorfor100isplottedinFigure2.Thek

(cid:1)(cid:3)

:(),couldberejectedfortoidentifymarkervariablesusedtolabelorinterpretnullhypothesis,bbH

0v.

onlytwovocationalinterestscales,theSocialscalethepatternbutnottodeterminewhichvariablesto

andtheRealisticscale.Thus,thecriterion-patternretainintheregressionequation.

vectorinFigure2ismarkedbyasignificantlyhigh

Example1:PredictingaPersonalityScale

scoreontheSocialscaleandasignificantlylowscore

FromaVocationalInterestProfile

Inthisexample,thepredictorvariableswerethesix

Holland(1973)BasicThemescalesfromtheStrong–3OurthankstoReneDawis,DavidJ.Weiss,RexBlake,

CampbellInterestInventory(Campbell&Hansen,andSharonSackett,whocollectedandassembledthisdata.

## Page 9

476 DAVISONANDDAVENPORT
on the Realistic scale. Social occupations are gener- the predictable variation. The data support an asso-
allyhumanserviceprofessions.Realisticoccupations ciation between this personality characteristic and a
include jobs, such as mechanic or engineer that in- vocational interest pattern in which persons high on
volve making or repairing things. Someone with this Social Closeness tend to prefer social occupations
interest pattern would seem to prefer working with over realistic ones.
peopleoverworkingwiththings.Thecriterionpattern
Example 2: Predicting High School
inFigure2hasthesamemarkervariables,theSocial
Mathematics Achievement From High
and Realistic scales, as the People versus Things di-
SchoolCourse Work
mension in Prediger’s (1982) representation of Hol-
land’s (1973) hexagonal model for vocational inter- Oursecondexampledoesnotinvolveatest-battery
ests. This same People versus Things dimension profile. Rather, it involves predicting a high school
appearsinthemultidimensionalscalingstudies(Davi- student’s senior-year mathematics achievement score
son, 1994; Rounds, Davison, & Dawis, 1979) of cor- from the profile of the student’s high school math-
relations among vocational-interest scales. ematics course work as reported on his or her tran-
In this example, the correlation between interest script (Davenport et al., 1998). In this case, level re-
profile level and Social Closeness scores was only fers to the amount of course work taken in
.08.Thecorrelationwiththepatterneffectwassome- mathematics. Pattern refers to the distribution of the
what higher, .36, suggesting that the pattern effect course work over various course work categories.
alone accounted for 12.9% of the variation in Social Thisexamplewaschosenbecauseitillustrateshow
Closeness scores. The level effect and the pattern ef- theanalysisdescribedabovecanbeappliedtosetsof
fect were nearly uncorrelated, .04. predictorvariablesthat,takentogether,describeafre-
The pattern effect added a statistically significant quency distribution for each respondent. In such ap-
12.7% to the variation accounted for by the level ef- plications,eachpredictorvariable,X ,showsthefre-
pv
fect alone. Together, the level effect and the pattern quency with which responses falling in category v
effect accounted for only slightly more than 13% of occurred for person p. Using the analysis described
the variation in Social Closeness scores. above, multiple regression can be used to describe a
Cross-validation results. The cross-validation re- distributional pattern associated with high scores on
sults largely confirm the full-sample findings in the thecriterion,anditcanbeusedtoquantifytheamount
sense that, on cross-validation, the pattern effect, not of variation accounted for by that pattern.
level effect, accounted for most of the predictable ThedataforthisexampleweretakenfromtheNa-
variationinthecriterion.InSample1,levelaccounted tional Educational Longitudinal Study (NELS; Na-
for less than 1% of the variation in Social Closeness tional Center for Education Statistics–U.S. Depart-
scores.Thecriterion-patternvectoridentifiedfromre- ment of Education, 1990). The sample consists of
gression weights in Sample 2 accounted for 6.7% of 10,245 U.S. high school students who were 9th–12th
thecriterionvariationinSample1.Thatcriterionpat- gradersintheyears1988–1992.Thedatasetincludes
tern added an additional 6.4% to the variation ac- each student’s high school course transcript. In prior
countedforoverandabovelevel.Together,leveland research, mathematics courses were classified into
pattern accounted for 7.1% of the variation in the eight categories, including a miscellaneous category.
Social Closeness criterion variable. For purposes of this illustration, the miscellaneous
InSample2,levelagainaccountedforlessthan1% category was dropped. The remaining seven catego-
of the variation in Social Closeness scores. The cri- ries are listed along the horizontal axis in Figure 3.
terion-pattern vector identified from regression The categories are arrayed roughly in terms of com-
weights in Sample 1 accounted for 12.2% of the cri- plexity from functional courses (i.e., special educa-
terion variation in Sample 2. The criterion pattern tion)atoneextremetoadvancedcourses(e.g.,calcu-
found in Sample 2 added an additional 11.8% to the lus, pre-calculus, analysis) at the other.
variation accounted for over and above level. Severalofthecategoriesdeservesomeexplanation.
The results from the full-sample and the cross- Thebasicandgeneralmathematicscoursescovergen-
validationsamplesleadtosimilarconclusions.Scores eral arithmetic and its application. These courses
on the six vocational-interest scales account for only wouldusuallybetakenbystudentspriortoAlgebra1
a small portion of the variation in Social Closeness or by students who do not take Algebra 1. The cat-
scores.Profilepattern,notlevel,accountsformostof egory, Algebra, 2 Parts, refers to a 2-year course in
.srehsilbup
deilla
sti
fo
eno
ro
noitaicossA
lacigolohcysP
naciremA
eht
yb
dethgirypoc
si
tnemucod
sihT
.yldaorb
detanimessid
eb
ot
ton
si
dna
resu
laudividni
eht
fo
esu
lanosrep
eht
rof
ylelos
dednetni
si
elcitra
sihT
.devreser
era
,seigolonhcet
ralimis
dna
,gniniart
IA
,gninim
atad
dna
txet
rof
gnidulcni
,sthgir
llA

## Page 10

477CRITERION-RELATEDPATTERNS

.y

l

d.

sa

ro

e

rh.

bds

eid

lv

be

rut

ea

psn

eid

rm

e

eie

lr

sla

as

i,

sds

te

iei

gf

b

oo

o l

eot

n n

to

oh

ncr

o e

s

tin

r

doa

nil

tia

am

ir

cie

sos

sud

s n

Al

aa

u l

,adg

c(cid:1)in

Criterion-patternvectorfortheMathematicsAchievementcriterionofExample2.1.Figure3.kvi

igi

nd

oi

nal

ori

the

(cid:1)I

ch1wasplottedinFigure3.Thenullhypothesis,whichstudentsstudyAlgebra1overa2-yearperiod.k

Ay

t

s f

,P(cid:1)(cid:3)og

:(),wasrejectedforallbuttheAlgebra,SuchcoursesaredesignedforstudentswhoneedtobbH

nne

0v.i

asn

uc2Partscoursecategory.studyalgebraataslowerpace.Thecategorystandardi

mi

lr

ae

namThecorrelationbetweenprofilelevel(totalCUsreferstothestandardprecollegesequenceofAlgebra

to

aAs

dr

completed)andachievementscoreswas.45.Thecor-1,Algebra2,andGeometry.Thecategoryunified ee

dp

hn

te

a relationwithpattern(ordistributionofcourseworkconsistsofasequenceinwhichstudentsstudyalgebra

yh

tbt

x

red

overthecategories)was.76,indicatingthatthepat-andgeometryinamoreintegratedfashionthanintheot

e f

rt

ohy

terneffectaccountedfor57.4%ofthemathematics-sequence.Thecategorygenerallystandardadvancedfgl

eig

lr

ony

achievementvariation.Incontrasttoourearlierex-consistsofcoursesthatwouldbetakenaftercomplet-sip

d

odu

cel

amples(seeTables1and2),thecorrelationbetweeningtheorsequence.standardunified cd

s

nni

iet

levelandpatternwashigh,.61.Thatis,thereisaForeachstudent,wecomputedthenumberofCar-nt,

sne

tim

h

ssubstantialassociationbetweentheamountofcoursenegieUnits(CUs)completedbythestudentineachg

ui

i c

re

oll

category.ACUequalsroughlyayear’sworthofcl

d

Ai

ts

r

iastudyoritsequivalent.Formoststudentswhocom-

h

sTTable2

i

hpletehighschoolin4yearswithnosummerschool

T

VariationandIncrementalVariationAccountedforin

andtakeonlyonemathcourseatatime,thenumber

SocialClosenessbytheVocationalInterest

ofCUswillrangebetween0and4.Thus,eachstu-

Criterion-PatternVectorofFigure2:Fulland

dent’scourseworkprofileisasetofsevenscoresCross-ValidationSamples

eachshowingthenumberofCUscompletedinoneof

Cross-validation

PercentvariationFull

thesevencategories.

accountedforsampleSample1Sample2

Thecriterionvariable,math-Full-sampleresults.

ematicsachievement,wasregressedontotheseven-Patternalone12.9*6.7*12.2*

Patternincrement12.7*6.4*11.8*course-categoryvariables.Theunstandardizedregres-

Levelandpattern13.3*7.1*12.4*sionweightswereconvertedtodeviationsaboutthe

regressionweightmean.Thenthecriterionpatternfor*<.01.p

## Page 11

478 DAVISONANDDAVENPORT
work taken and the distribution of that course work graphed.However,therecanbemoresubstantialrea-
over the course categories. Students taking more sons for choosing k (cid:2) 1.0. In some of our work (not
course work tend to have taken advanced course reported here), we have had several criterion groups,
work. haveusedmultipleregressiontoidentifycriterionpat-
As shown in Table 3, the pattern effect added an terns associated with each group, and have then clas-
additional 36.8% to the variation accounted for by sifiedrespondentsintogroupsonthebasisofthecri-
level alone. In total, the pattern and level effects ac- terionpatternbestmatchedbyeachrespondent’sdata.
counted for 57.4% of the variation in mathematics Inthisresearch,wecomputedseveralcovariancepro-
achievement.Althoughlevelaccountedforasubstan- file-match statistics, Cov (c (cid:1) 1,..., C), for each
pc
tialamountoftheachievementvariation,21%,pattern person and then classified person p into the group
added substantially to that amount. corresponding to their highest profile match statistic.
Cross-validation results. Again, the cross- Before computing the profile-match statistics on
validationresultsinTable3confirmthefindingsfrom which classification is based, we standardized the
the full sample. In Sample 1, the pattern effect alone variabilitywithineachcriterionpatternbyselectinga
accounted for 58.1% of the variation in achievement. different value of k for each criterion pattern so that
The criterion-pattern vector identified in Sample 2 (1/V)(cid:1) x 2(cid:1)1.0foreachpattern.Thisstandardiza-
v cv
accounted for an additional 36.4% of the variation tiongivesprofile-matchstatisticsthatarecomparable
over and above level alone. Together, pattern and across the several criterion patterns. From our expe-
level accounted for 58.1% of the variation in math- rience, the choice of k seems most critical when the
ematics achievement. profilematchstatistic,Cov ,isusedtoclassifyindi-
pc
InSample2,thepatterneffectaccountedfor56.7% viduals by examining their match to one of several
of the variation in achievement. The criterion-pattern criterion patterns.
vector identified in Sample 1 accounted for an addi-
tional 37.2% of the variation over and above level Issues of Interpretation andInvariance
alone. Together, the level and pattern effects ac-
counted for a total of 56.8% of the variation. There are a number of issues involving either the
These data suggest that level, or amount of course interpretation of the multiple regression results, the
work taken, accounts for a substantial proportion of invariance of results, or both. Here we begin by con-
thevariationinmathematicsachievement,20%.How- sideringtheinterpretationoftheanalysiswithrespect
ever, the pattern, or distribution of course work over to the equal weighting issue in multiple regression.
the categories, more than doubles the variation ac- Then we turn to the interpretation and the invariance
counted for. There is a very substantial correlation of results with respect to various ways of scoring the between amount and content of course work, if con- predictor variables.
tent is taken to mean the distribution of the course
Unit Weighting of PredictorVariables work over our seven categories.
In drawing graphs of the criterion patterns in Fig-
There is an extensive literature comparing the
ures 1–2, we used values of k other than 1.0 for a
variation accounted for using optimal (least squares)
rathertrivialreason:togetridofnuisancezerostothe
predictor weights with the variation accounted for
right of the decimal place in the numbers being
when equal weights are used for all predictors (e.g.,
Dawes,1979;Dawes&Corrigan,1974;Green,1977;
Table3
Wainer, 1976). When all variables are rescored, if
VariationandIncrementalVariationAccountedforin
necessary, to be positively related to the criterion,
MathematicsAchievementbytheCourseWork
Criterion-PatternVectorofFigure3:Fulland equal weights often do as well on cross-validation as
Cross-ValidationSamples do the optimal weights, particularly if the optimal
weightshavebeenestimatedinasmallsample.Inthe
Cross-validation
Percentvariation Full analysis above, the model including only the level
accountedfor sample Sample1 Sample2
effectistheequalweightmodel.Themodelincluding
Patternalone 57.4* 58.1* 56.7* allofthepredictors(whichisalsothemodelincluding
Patternincrement 36.8* 36.4* 37.2* both pattern and level effects) is the optimal weight
Levelandpattern 57.4* 58.1* 56.8* model. The difference between R 2 and R 2 is the
F L
*p<.01. additional proportion of variation accounted for by
.srehsilbup
deilla
sti
fo
eno
ro
noitaicossA
lacigolohcysP
naciremA
eht
yb dethgirypoc
si
tnemucod
sihT
.yldaorb
detanimessid
eb
ot
ton
si
dna
resu
laudividni
eht
fo
esu
lanosrep
eht rof
ylelos
dednetni
si
elcitra
sihT
.devreser
era
,seigolonhcet
ralimis
dna
,gniniart
IA
,gninim
atad
dna
txet
rof
gnidulcni
,sthgir
llA

## Page 12

CRITERION-RELATEDPATTERNS 479
usingoptimalweightsinsteadofequalweights.Ifthe The major feature of the criterion-pattern vector in
null hypothesis H : R 2 (cid:1) R 2 is rejected, then the Figure1isthatithashigherscoresforscalesAandH
0 F L
equal weight model can be rejected in favor of the than for S and B. None of the respondents at the top
model that includes the optimal regression weights. of Table 4 has a higher score on A and H than on S
Therefore,theanalysisdescribedabovecanbeusedto andB.Respondent2’sdatasethasthehighestcovari-
investigate whether optimal weights can account for ance with the criterion pattern, and yet even that re-
more variation than equal regression weights. sponse vector does not have higher scores on A and
H. How can this paradox arise?
Scoring of PredictorVariables
Therawscoreofanyindividualcanbedividedinto
Three scoring issues can affect results and conclu- two components: X (cid:1) x + X . Here x is the
pv pv .v pv
sions reached with respect to profile patterns: stan- deviationscorex (cid:1)(X −X ),andX isthemean
pv pv .v .v
dardizing predictor means, standardizing predictor of variable v. As shown in Appendix C, the covari-
variances, and reverse scoring some predictors. ance between the actual profile of person p and any
Standardizing predictor means. Paradoxically, criterion-pattern vector depends on two factors: the
when the means of the predictor variables are differ- degree to which the pattern of person p’s deviation
ent for each variable, there can be no respondent scores matches the criterion-pattern vector and the
whosedatasetseemstoresemblethecriterionpattern, degree to which the pattern of the variable means
even if the criterion pattern accounts for most of the matchesthecriterionpattern.Individualdifferencesin
criterion variation. The top of Table 4 shows such a the profile-match statistic, Cov , are completely de-
pc
data set. If one regresses the four predictors, A, H, S, terminedbythefirstofthesetwofactors,becausethe
and B, onto the criterion variable N-P, the set of cri- second factor is a constant for all respondents (see
terion-pattern vectors identified on the basis of the Appendix C).
regressionweightsisexactlythesameasforthedata AtthetopofTable4,themeansofthevariablesA
at the top of Table 1. One of the criterion-pattern and H are so much lower than the means of S and B
vectors is plotted in Figure 1. The criterion-pattern thatnorespondenthashigherscoresonAandHthan
vectorinFigure1accountsfor96%ofthevariationin on S and B. The pattern of the means is masking the
the criterion variable N-P in Table 4. Yet no respon- fact that some respondents’ deviation scores are
dent’s data set looks like the pattern in Figure 1. higher on A and H than on S and B. As a result, the
Table4
RawScoreandDeviationScoreProfilesof6HypotheticalClientsDiagnosedasEither
NeuroticorPsychotic
IPMMscaleandvariable
Client A H S B N-P X Cov
p. pc
Rawscore
1 90 60 90 80 1 80.00 −115.4
2 75 75 85 85 1 80.00 −80.8
3 75 60 95 75 1 76.25 −132.7
4 65 50 115 90 0 80.00 −346.2
5 60 55 100 105 0 80.00 −380.8
6 70 45 100 90 0 76.25 −328.9
Deviationscore
1 17.50 2.50 −7.50 −7.50 1 1.25 115.4
2 2.50 17.50 −12.50 −2.50 1 1.25 150.0
3 2.50 2.50 −2.50 −12.50 1 −2.50 98.1
4 −7.50 −7.50 17.50 2.50 0 1.25 −115.4
5 −12.50 −2.50 2.50 17.50 0 1.25 −150.0
6 −2.50 −12.50 2.50 2.50 0 −2.50 −98.1
Note. IPMM (cid:1) Inventory of Personality and Mood Manifestations; A (cid:1) Anxiety; H (cid:1) Hypochon-
driasis;S(cid:1)Schizophrenia;B(cid:1)BipolarDisorder;N-P(cid:1)neuroticversuspsychoticcriterionvariable
(1(cid:1)neurotic,0(cid:1)psychotic);X (cid:1)theprofilelevelofpersonp;Cov (cid:1)thecovariancebetweenthe
p. pc
scoreprofileofpersonpandthecriterion-patternvector.
.srehsilbup
deilla
sti
fo
eno
ro
noitaicossA
lacigolohcysP
naciremA
eht
yb
dethgirypoc
si
tnemucod
sihT
.yldaorb
detanimessid
eb
ot
ton
si
dna
resu
laudividni
eht
fo
esu
lanosrep
eht
rof
ylelos
dednetni
si
elcitra
sihT
.devreser
era
,seigolonhcet
ralimis
dna
,gniniart
IA
,gninim
atad
dna
txet
rof
gnidulcni
,sthgir
llA

## Page 13

480 DAVISONANDDAVENPORT
covariance of every client is negative, indicating that standardized weights. Unstandardized weights serve
no client has a raw-score pattern closely resembling to identify a pattern of predictor-deviation scores as-
the criterion pattern. However, all of the neurotics sociated with high scores on the criterion variable.
have higher covariances than do the psychotics, and Standardizedpredictorweightsservetoidentifyapat-
therefore the profile-match statistic, Cov , is a good tern of z scores associated with high scores on the
pc
predictor of the criterion variable. criterion variable. That is, the standardized weights
If the variables at the top of Table 4 are converted refer to predictor variables that have been standard-
to deviation score form, one can readily see that the ized to have equal means and variances.
neurotics’deviationscoresdoresemblethepatternin Thesetofcriterion-patternvectorsidentifiedusing
Figure 1. The scores expressed in deviation-score unstandardizedweightsmaylookquitedifferentfrom
formaregivenatthebottomofTable4.Atthebottom the set of criterion-pattern vectors identified using
ofTable4,neuroticshavescorepatternssimilartothe standardized weights. That is, the arrangement of
criterionpatterninthatAandHarehigherthanSand highesttolowestscoresinthesetofcriterionvectors
B.ThetopofTable1showsthesamevariablesstan- computed from unstandardized regression weights
dardizedtohaveequalmeansof57.5.Whenthevari- maybequitedifferentfromthearrangementofhigh-
ables have equal means as at the top of Table 1, it is est to lowest scores in the set of criterion vectors
readilyseenthatAandHarehigherthanSandBfor computed from standardized regression weights. If
neurotics, whereas the psychotics have the mirror- the criterion-pattern vector is computed from stan-
image pattern. dardized regression weights, the predictor variables
In effect, multiple regression can discern the fact must first be standardized to have equal means and
that there is a criterion pattern such that people with variances before the covariance (Cov ) and the level pc
high criterion scores have predictor-deviation score (X .) variables are computed for each respondent.
p
patternsmorecloselyresemblingthatcriterionpattern Whenrawscoresareexpressedinmeaningfulunits
thandopeoplewithlowscoresonthecriterion.Mul- thatarecomparableacrossvariables(e.g.,highschool
tiple regression can do so even when the predictor CUs)ortheliteraturefocusesonpatternsexpressedin
variables are expressed in raw-score form with un- unstandardizedunits(e.g.,Butcher&Williams,2000;
equal means. Most human observers cannot. That is, McAllister, 1986), researchers will want to identify
when the predictor variables are expressed as raw patternsintheunstandardizedvariablesusingtheun-
scores with unequal means, human observers cannot standardized regression weights. In the discussion
always discern the deviation-score pattern associated above, variables are considered standardized only if
with high scores on the predictor variable simply by they have a mean of 0 and a variance of 1.0 in the
inspectingthedata.Humanobserverscannotidentify research sample. Variables that have been standard-
respondents whose deviation-score pattern looks like izedwithrespecttoanormgroup,butnottheresearch
thecriterionpattern.Becausetheimportantresultsare sample, are considered unstandardized.
unaffectedbystandardizingmeans,thereisnoreason Reverse-scoringpredictorvariables. Inthelitera-
tostandardizemeansforpurposesofstatisticalanaly- ture on unit weighting cited above, the researchers
sis. However, if researchers want to visually inspect conclude that unit weights often perform as well as
theirdatatoidentifyacriterionpattern,orifresearch- optimal weights on cross-validation if the predictor
erswanttovisuallycomparerespondentscorestothe variables are first scored so that all have a positive
criterion pattern, they should first convert the raw correlation with the criterion variable. In that litera-
scores to deviation-score form, as shown at the bot- ture, some predictors are reverse scored for purposes
tom of Table 4, or the researchers should standardize ofdevelopingaunitweightmodel.Instudyingprofile
the variables so all variables have equal means, as patterns, should some variables be reverse scored, if
shown at the top of Table 1. necessary, so as to be positively correlated with the
Standardizing predictor variances. Although a criterion variable?
human observer might be influenced by unequal The answer to this question is important to the
means,multipleregressionisnot.Multipleregression analyses described above, because reverse scoring
is, however, affected by unequal variances. Multiple some predictors can change the conclusions reached.
regression produces both standardized and unstand- For instance, in the data at the top of Table 1, the
ardized regression weights. In the examples above, multipleregressionanalysisledtotheconclusionthat
the criterion-pattern vectors have been based on un- profilelevelaccountedfornovariationinthecriterion
.srehsilbup
deilla
sti
fo
eno
ro
noitaicossA
lacigolohcysP
naciremA
eht
yb
dethgirypoc
si
tnemucod
sihT
.yldaorb
detanimessid
eb
ot
ton
si
dna
resu
laudividni
eht
fo
esu
lanosrep
eht
rof
ylelos
dednetni
si
elcitra
sihT
.devreser
era
,seigolonhcet
ralimis
dna
,gniniart
IA
,gninim
atad
dna
txet
rof
gnidulcni
,sthgir
llA

## Page 14

CRITERION-RELATEDPATTERNS 481
variable. Profile pattern accounted for 96% of the derived criterion pattern that subsequent clinicians
variation.Althoughwehavenotreportedtheanalysis can use as a guide in making diagnoses based on
here, after reverse scoring variables S and B so that IPMM information. Presumably, the empirically de-
they are positively correlated with the criterion vari- rived pattern should include predictor information
able, the total amount of variation accounted for re- scored in the same form that the information is com-
mains the same. However, profile level accounts for monlyreportedtoclinicians,evenifsomeofthepre-
most of the variation in the criterion variable. The dictorvariablesarethenscoredsoastobenegatively
variationaccountedforbythepatterneffectisgreatly related to the criterion. Reverse scoring some predic-
reduced. Because reverse scoring of some variables tors would yield a profile of no use to the clinician
can greatly change the conclusions reached, reverse because it would be based on variables scored in a
scoring is an important issue in research on profile manner other than the scoring used in clinical score
patterns. reports of actual clients. Reverse scoring some vari-
Ifthegoalofone’sresearchissimplytoproducea ablestomakethempositivelycorrelatedwiththecri-
terion variable would inhibit development of a score
linear regression equation that will perform well in
pattern useful to clinical practice.
other samples, then reverse scoring some predictor
In the absence of other considerations, researchers
variables may do no harm. In the type of research
may wish to rescore predictor variables so they have
described above, however, the goal is not mere pre-
positive correlations with the criterion variable. With
diction. Rather the goal is to develop an understand-
the possible exception of research on unit weighting,
ing of the predictor profile pattern associated with
however,therewillusuallybeotherconsiderations.In
highscoresonthecriterionvariable.Developingthat
some cases, one particular direction of scoring will
understanding requires a formal model expressed in
havebeenmostcommonlyusedinthepriorliterature,
terms of pattern and level effects. Consider two hy-
and therefore the researcher will want to adopt the
pothetical studies that might produce data similar to
common scoring so results of the new research are that at the top of Table 1.
more easily related to the prior literature. In other
Thefirstisastudyoftheclinicaljudgmentprocess
cases, theory assumes a particular direction of scor-
similar to research described by Goldberg (1970). In
ing. A theory about anxiety would seem to imply thishypotheticalresearchstudy,aclinicianisaskedto
variables scored so that high scores mean high levels
view the predictor scores of all 6 clients at the top of
of anxiety not a lack of anxiety. When the goal is
Table 1 and then to classify the client as either neu-
formalmodelingtoenhancetheory,commonresearch
roticorpsychotic.Thegoalistobuildalinearmodel
practice or the theory itself may imply a direction of
of the clinician’s judgment process. Presumably, the
scoring the variables. investigatorwouldpresenteachclient’sIPMMprofile
totheclinicianwithvariablesscoredinamannerwith
which the clinician is familiar, even if some of the Discussion
variables are then negatively correlated with the cri-
terion variable. Furthermore, the variables entered Interpreting profile patterns implicitly involves
into the model would be scored just as they were comparing scores across continuous variables. Such
scored in the information given to the clinician. To comparisonsarelegitimateonlyifthescoresfromthe
reverse score some variables in the model would not variables are, in some sense, comparable. In our
yield a model of the clinician’s judgment process, course-takingexampleabove,forinstance,thescores
becausetheinformationinthemodelwouldnotbethe for each category are all expressed as CUs, a unit
sameastheinformationgiventotheclinician.Asthis roughlyequivalenttoayear’sworthofstudy.Forour
exampleillustrates,itisnotalwayssensibletoreverse interest-inventory example, the scores were T scores
score the predictor information if the goal is to build scaled to have M (cid:1) 50 and SD (cid:1) 10 in the norm
a psychological model of human responses. group.Itisnotourintentiontodefendtheequivalence
Considerasecondpossiblestudyyieldinginforma- of CUs across high school course categories or the
tionsimilartothatinTable1.The6clientseachtake equivalenceofTscoresacrossdifferentpsychological
theIPMMonadmissiontotheclinician’scare.With- scales. Rather, we merely want to point out that in-
outseeingthepredictorvariables,theclinicianmakes terpreting profile patterns involves comparing vari-
anindependentdiagnosisofeachclientaseitherneu- ables. For such comparisons to be meaningful, the
rotic or psychotic. The goal is to find an empirically variables must be in comparable units.
.srehsilbup
deilla
sti
fo
eno
ro
noitaicossA
lacigolohcysP
naciremA
eht
yb
dethgirypoc
si
tnemucod
sihT
.yldaorb
detanimessid
eb
ot
ton
si
dna
resu
laudividni
eht
fo
esu
lanosrep
eht
rof
ylelos
dednetni
si
elcitra
sihT
.devreser
era
,seigolonhcet
ralimis
dna
,gniniart
IA
,gninim
atad
dna
txet
rof
gnidulcni
,sthgir
llA

## Page 15

482 DAVISONANDDAVENPORT
When the predictor variables are in comparable study of WAIS and GATB patterns. Psychological As-
units and the regression of the variables on the crite- sessment,8,26–31.
rion is linear, the regression weights sketch a set of Davison,M.L.,Kuang,H.,&Kim,S.K.(1999).Thestruc-
criterion-pattern vectors. All of the criterion-pattern ture of ability profile patterns: A multidimensional scal-
vectors are proportional to each other and, taken to- ingperspectiveonthestructureofintellect.InP.L.Ack-
gether,thissetconstitutesallofthevectorsdisplaying erman,P.C.Kyllonen,&R.D.Roberts(Eds.),Learning
a particular arrangement of the predictor variables. and individual differences: Process, trait, and content
For a given profile level, the expected criterion score determinants(pp.187–207).Washington,DC:American
increases as the match to any criterion-pattern vector PsychologicalAssociation.
increases when match is indexed as the covariance Dawes,R.M.(1979).Therobustbeautyofimproperlinear
between an observed-predictor score profile and the models.AmericanPsychologist,34,571–582.
criterion-pattern vector. The expected criterion score Dawes, R.M., & Corrigan, B. (1974). Linear models in
can be expressed as a function of just two predictor decisionmaking.PsychologicalBulletin,81,95–106.
profileeffects:profilelevelandmatchtothecriterion Games, P.A. (1990). Alternative analyses of repeated-
pattern.Asaconsequence,theaccountedforvariation measuredesignsbyANOVAandMANOVA.InA.von
in Y can be divided among two nonorthogonal Eye (Ed.), Statistical methods in longitudinal research:
sources,aprofile-leveleffectandaprofile-patternef- Vol. 1. Principles and structuring change (pp. 81–121).
fect. Multiple regression can be used both to identify NewYork:AcademicPress.
the criterion pattern and to determine the amount of Glutting, J.J., McGrath, E.A., Kamphaus, R.W., & Mc-
variation predictable from the match to the criterion Dermott,P.A.(1992).Taxonomyandvalidityofsubtest
pattern. profiles on the Kaufman Assessment Battery for Chil-
dren.TheJournalofSpecialEducation,26,85–115.
References Goldberg,L.(1970).Manversusmodelofman:Arationale,
plussomeevidence,foramethodofimprovingonclini-
Browne,M.W.(1975a).Acomparisonofsinglesampleand calinferences.PsychologicalBulletin,73,422–432.
cross-validationmethodsforestimatingthemeansquared Gore,P.A.,Jr.(2000).Clusteranalysis.InH.E.A.Tinsley
error of prediction in multiple linear regression. British &S.D.Brown(Eds.),Handbookofappliedmultivariate
JournalofMathematicalandStatisticalPsychology,28, statistics and mathematical modeling (pp. 298–318).
112–120. NewYork:AcademicPress.
Browne, M.W. (1975b). Predictive validity of a linear re- Green,B.F.,Jr.(1977).Parametersensitivityinmultivari-
gression equation. British Journal of Mathematical and ate methods. Multivariate Behavioral Research, 3, 263–
StatisticalPsychology,28,79–87. 287.
Butcher, J.N., & Williams, C.L. (2000). Essentials of Holland,J.L.(1973).Makingvocationalchoices:Atheory
MMPI-2andMMPI-Ainterpretation.Minneapolis:Uni- ofcareers.EnglewoodCliffs,NJ:PrenticeHall.
versityofMinnesotaPress. Lorr, M. (1994). Cluster analysis. In S. Strack & M. Lorr
Campbell, D.P., & Hansen, J. (1985). Strong–Campbell (Eds.),Differentiatingnormalandabnormalpersonality
InterestInventory.PaloAlto,CA:ConsultingPsycholo- (pp. 176–195). New York: Springer Publishing Com-
gistsPress. pany.
Davenport,E.C.,Jr.,Davison,M.L.,Kuang,H.,Ding,S., McAllister, L.W. (1986). A practical guide to CPI inter-
Kim,S.K.,&Kwak,N.(1998).Highschoolmathemat- pretation.PaloAlto,CA:ConsultingPsychologistsPress.
icscourse-takingbygenderandethnicity.AmericanEd- Meehl, P.E. (1950). Configural scoring. Journal of Con-
ucationalResearchJournal,35,497–514. sultingPsychology,14,165–171.
Davison,M.L.(1994).Multidimensionalscalingmodelsof Moses,J.A.,Jr.,&Pritchard,D.A.(1995).Modalprofiles
personality responding. In S. Strack & M. Lorr (Eds.), for the Wechsler Adult Intelligence Scale–Revised. Ar-
Differentiating normal and abnormal personality (pp. chivesofClinicalNeuropsychology,11,61–68.
196–215).NewYork:SpringerPublishingCompany. Moskowitz, D.S., & Hershberger, S.L. (Eds.). (2002).
Davison,M.L.(2000).Profilepatterns:Researchandpro- Modeling intraindividual variability with repeated mea-
fessional interpretation. School Psychology Quarterly, sures data: Methods and applications. Mahwah, NJ:
15,457–464. Erlbaum.
Davison,M.L.,Gasser,M.,&Ding,S.(1996).Identifying National Center for Education Statistics–U.S. Department
major profile patterns in a population: An exploratory ofEducation.(1990).User’sManual:NationalEducation
.srehsilbup
deilla
sti
fo
eno
ro
noitaicossA
lacigolohcysP
naciremA
eht
yb
dethgirypoc
si
tnemucod
sihT
.yldaorb
detanimessid
eb
ot
ton
si
dna
resu
laudividni
eht
fo
esu
lanosrep
eht
rof
ylelos
dednetni
si
elcitra
sihT
.devreser
era
,seigolonhcet
ralimis
dna
,gniniart
IA
,gninim
atad
dna
txet
rof
gnidulcni
,sthgir
llA

## Page 16

CRITERION-RELATEDPATTERNS 483
Longitudinal Study of 1988 Base Year: Student compo- proachtoclassification.AppliedPsychologicalMeasure-
nentdatafileuser’smanual.Washington,DC:U.S.Gov- ment,3,327–341.
ernmentPrintingOffice. Stanton, H.C., & Reynolds, C.R. (2000). Configural fre-
quency analysis as a method of determining Wechsler
Nesselroade, J.R. (2001). Intraindividual variability in de-
velopment within and between individuals. European
profiletypes.SchoolPsychologyQuarterly,15,434–448.
Psychologists,6,100–116. Tellegen, A.T. (1982). Brief manual for the Differential
Personality Questionnaire (MPQ). Minneapolis, MN:
Prediger, D.J. (1982). Dimensions underlying Holland’s
Author.
hexagon:Missinglinkbetweeninterestsandoccupations.
von Eye, A. (1990). Introduction to configural frequency
JournalofVocationalBehavior,21,268–277.
analysis.NewYork:CambridgeUniversityPress.
Rounds, J.B., Jr., Davison, M.L., & Dawis, R.V. (1979). von Eye, A., Spiel, C., & Wood, P.K. (1996). Configural
ThefitbetweenStrong–CampbellInterestInventorygen- frequencyanalysisinappliedpsychologicalresearch.Ap-
eral occupation themes and Holland’s hexagonal model. pliedPsychology:AnInternationalReview,45,301–352.
JournalofVocationalBehavior,15,303–315.
Wainer,H.(1976).Estimatingcoefficientsinlinearmodels.
Skinner,H.(1979).Dimensionsandclusters:Ahybridap- PsychologicalBulletin,83,312–317.
Appendix A
Expressing Regression Equations in Terms of Pattern and Level Effects
Thepurposeofthisappendixistoshowtheequivalence rion-pattern vector (Equation 2), (b − b) (cid:1) (1/k) (X −
v . cv
ofEquations1,3,and4.Letb (cid:1)(1/V)(cid:1) b andletX (cid:1) X ), where X is the vth element of the criterion-pattern
. v v p. c. cv
(1/V)(cid:1) X .Giventhesedefinitions,Equation1canbere- vector x , and X is the mean of the elements in the crite- v pv c c.
expressedintermsofb −b andX −X : rion-pattern vector. Using this equality, (b − b) (cid:1) (1/k)
v . pv p. v .
(X −X ),inEquationA4yields Y(cid:2) =(cid:1) b X +a (A1) cv c.
p v v pv
=(cid:1) v (cid:1)b v −b . +b . (cid:2)(cid:1)X pv −X p. +X p. (cid:2)+a (A2) Y(cid:2) p =(cid:1) v (cid:1)1(cid:3)k(cid:2)(cid:1)X cv −X c. (cid:2)(cid:1)X pv −X p. (cid:2)+Vb . X p. +a (A5)
=(cid:1)(cid:1)b −b(cid:2)(cid:1)X −X (cid:2)+(cid:1) bX +a (A3)
=(cid:1) v v (cid:1)b v v −b . . (cid:2)(cid:1)X p p v v −X p p . . (cid:2)+Vb v . X . p. p + . a. (A4) =(cid:1)V(cid:3)k(cid:2)Cov pc +Vb . X p. +a. (A6)
Equation A3 follows from A2 because (cid:1) (b − b) (cid:1) Equation A6 follows from the definition of the covariance
v v . (cid:1) (X −X )(cid:1)0.Because(cid:1) bX (cid:1)VbX ,EquationA4 Cov (cid:1)(1/V)(cid:1) (X −X )(X −X ).EquationsA1,A3,
v pv p. v . p. . p. pc v cv c. pv p.
follows from Equation A3. From the definition of a crite- andA6givethedesiredresult.
Appendix B
Statistical Test to Assist in Criterion PatternInterpretation
Toaidintheinterpretationofthecriterion-patternvectors weightb ,ands(b )isestimatedintheregressionanalysis.
v v
inExamples1and2,weperformedanapproximatetestof Because the population mean, (cid:3)(b), is unknown, we sub-
.
thenullhypothesisH :b (cid:1)(cid:3)(b)separatelyforeachvari- stituted the sample mean b in the computation of the test
0 v . .
able v, where (cid:3)(b) is the expected value of b over all statistic. If the regression weight b differed significantly
. . v
possiblerandomsamplesfromthispopulation.Ideally,the from the mean of the regression weights, then the corre-
teststatisticwouldbet(cid:1)[b −(cid:3)(b)]/s(b ),whichwouldbe spondingelementinthecriterion-patternvector,X ,would
v . v cv
distributedasStudent’stwith1and(N−V−1)degreesof differ significantly from the mean score in the criterion-
freedom. Here s(b ) is the standard error of the regression patternvectorbecauseelementsofthecriterion-patternvec-
v
.srehsilbup
deilla
sti
fo
eno
ro
noitaicossA
lacigolohcysP
naciremA
eht yb
dethgirypoc
si
tnemucod
sihT
.yldaorb
detanimessid
eb
ot
ton
si dna
resu
laudividni
eht
fo
esu
lanosrep
eht
rof
ylelos
dednetni
si
elcitra
sihT
.devreser
era
,seigolonhcet
ralimis
dna
,gniniart
IA
,gninim
atad
dna txet
rof
gnidulcni
,sthgir
llA

## Page 17

484DAVISONANDDAVENPORT

Hbsignificantcoefficientsforwhichthenullhypothesistorareproportionaltoregressionweightsexpressedasde-:

v0

(cid:1)(cid:3)bviationsabouttheirmean.Ourinterpretationofthecrite-()hasbeenrejected.

.

rion-patternvectorsinFigures2and3isbasedonthe

AppendixC

RawScoreandDeviationScoreProfile-MatchStatistics

=(cid:1)−+−−()(cid:2)(cid:2)(cid:2)(cid:1)(cid:1)(cid:1)(cid:3)Thepurposeofthisappendixistoshowthatthecovari-VXXxXxX1C5

vcvcpvvp.....

.y

pancebetweentheactualrawscoreprofileofpersonand

l

d.

sa

ranycriterion-patternvectordependsontwofactors:thede-o

e(cid:1)−−=(cid:2)(cid:2)(cid:2)(cid:1)(cid:1)(cid:1)(cid:3)VXXxx1

rh.

bvcvcpvp..ds

pgreetowhichthepatternofperson’sdeviationscores

ei+(cid:1)−−()(cid:2)(cid:2)(cid:2)(cid:1)(cid:1)(cid:1)(cid:3)d

VXXXX1C6lv

be

vcvcv....rut

matchesthecriterion-patternvectorandthedegreetowhichea

psn

eid

thepatternofthevariablemeansmatchesthecriterionpat-rm

e

ei+()=e

h,C7covlr

sltern.Individualdifferencesintheprofile-matchstatisticarea

pcas

i,

sds

tcompletelydeterminedbythefirstofthesetwofactors,e

iei

gf

b

oo(cid:1)(cid:1)

becausethesecondfactorisaconstantforallrespondents.hVXXXXhwhere(1/)(−)(−).Notethatisao

le

otvcvc.v...

n n

tCOVLetrefertothecovariancebetweentherawscoreso

oconstantforeveryperson.EquationC6showsthattheh

pcncr

o e

pc.sofpersonandthescoresincriterion-patternvectorLetCOVisafunctionoftwoterms,eachcorrespondingtoa

tin

pc,r

doa

covrefertothecovariancebetweenthedeviationscoresofnisumontheright-handside.Thefirsttermisequaltothel

tiapc

am

i(cid:1)(cid:1)r

pc.COVVXpersonandcriterionpatternThen(1/)(ccovariancebetweenthecriterion-patternvectorscoresandie

sopcvcvs

sud

sXXXX−)(−).Inthisexpression,thevariableisthep.thedeviationscoresofpersonThesecondisequaltothe n

Alc.pvp.p.

aa

u l

p,Xmeanrawscoreintheprofileofpersonandisthe,covariancebetweenthecriterion-patternvectorscoresand

adg

c.cin

vi

ixmeanscoreinthecriterion-patternvector.Ifweletbegthevectorofvariablemeans.EquationC7showsthatalli

nd

opvi

nal(cid:1)

oxXXXthedeviationscore,(−),whereisthemeanriCOVindividualdifferencesinareattributabletoindi-

thpvpv.vv.e

pcI

ch

Av,ofvariabletheny

vidualdifferencesinpredictordeviationscores,thatis,in-t

s f

,Pog

covhdividualdifferencesinbecauseisaconstantforall nn

e

ipc,=(cid:1)=(cid:1)+()as(cid:2)(cid:2)(cid:2)(cid:1)(cid:1)(cid:1)(cid:3)(cid:3)

nVXVxXX11C1

ucicov

people.Thematchparameterindexesthematchbe-pvpvvpvv..mi

lrpc

ae

namptweenthedeviationscoresofpersonandthecriterion

to(cid:1)+(cid:1)()=(cid:2)(cid:2)(cid:1)(cid:1)(cid:3)(cid:3)

VxVX11C2aA

sd

vpvvv.rprofilepatternvector.

ee

dp

hn

t+()=e

a Xx.C3

yh

tp...bt

x

red

ot

e f

rtXisthegrandmeanofrawscores.UsingtheresultinHere

ohy

..fgReceivedMarch20,2002l

eig

C3andthedefinitionofadeviationscore,lr

ony

RevisionreceivedJuly25,2002sip

d

odu

cel

=(cid:1)−−()(cid:1)(cid:2)(cid:2)(cid:2)(cid:1)(cid:1)(cid:1)(cid:3)AcceptedJuly25,2002 cCOVVXXXXd1C4

s

nnpcvcvcpvpi..

iet

nt,

sne

tim

h

sg

ui

i c

re

oll

cld

Ai

ts

r

ia

h

sT

i

h

T