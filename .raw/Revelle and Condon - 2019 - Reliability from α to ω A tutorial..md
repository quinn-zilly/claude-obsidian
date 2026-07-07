## Page 1

PsychologicalAssessment

©2019AmericanPsychologicalAssociation2019,Vol.31,No.12,1395–1411

ISSN:1040-3590http://dx.doi.org/10.1037/pas0000754

(cid:2)(cid:3)

ReliabilityFromto:ATutorial

WilliamRevelleDavidM.Condon

NorthwesternUniversityNorthwesternUniversityandUniversityofOregon

Reliabilityisafundamentalproblemformeasurementinallofscience.Althoughdefinedinmultiple

ways,andestimatedinevenmoreways,thebasicconceptsseemstraightforwardandneedtobe

understoodbypractitionersaswellasmethodologists.Reliabilitytheoryisnotjustforthepsychome-

tricianestimatinglatentvariables,itisforeveryonewhowantstomakeinferencesfrommeasuresof.

y

l

dindividualsorofgroups.Forthecaseofasingletestadministration,weconsidermultiplemeasuresof

.as

ro(cid:4)(cid:2)(cid:5)(cid:5)

reliability,rangingfromtheworst()toaverage(,)tobest()splithalfreliabilities,andconsiderer

h34b

s(cid:3)(cid:3)

whymodel-basedestimates(,)shouldbereported.Wealsoaddresstheutilityoftest–retestandid

lhte

b

tualternateformreliabilities.Theadvantagesofimmediateversusdelayedreteststodecomposeobserved

a

pn

idscorevarianceintospecific,state,andtraitscoresarediscussed.Butreliabilityisnotjustfortestscores,

m

e

ei

litisalsoimportantwhenevaluatingtheuseofratings.Estimatesthatmaybeappliedtocontinuousdatas

ls

a

i

dincludeasetofintraclasscorrelationswhilediscretecategoricaldataneedstotakeadvantageofthes

te

i

(cid:6)bfamilyofstatistics.Examplesofthesevariousreliabilityestimatesaregivenusingstateandtrait

f

o

o

temeasuresofanxietygivenwithdifferentdelaysandunderdifferentconditions.Anonlinesupplemental

nt

oo

materialsisprovidedwithmoredetailandelaboration.Theonlinesupplementalmaterialsisalsousedton

r

os

demonstrateapplicationsofopensourcesoftwaretoexamplesofrealdata,andcomparisonsaremadei

nd

on

betweenthemanytypesofreliability.i

at

a

ir

ce

os

us

s

Al

aPublicSignificanceStatement

u

ld

a

iAtutorialontheestimationofthereliabilityoftestscoresconsidersclassicalandmodelbasedc

vi

gi

doapproaches.Examplesusingopensourcesoftwareappliedtoseveralrealworlddatasetsare

nl

oi

provided.he

ch

yt

sf

Po

ne

as

Keywords:reliability,generalizability,classicaltesttheory,Rpackagescu

i

rl

ea

mn

oSupplementalmaterials:http://dx.doi.org/10.1037/pas0000754.suppA

s

r

ee

ph

t

e

yh

bt

rd

o

ef

theoryandmeasurementofreliabilityhavegonefarbeyondtheReliabilityisafundamentalproblemformeasurementinalloft

hy

gl

eisciencefor“(a)llmeasurementisbefuddledbyerror”(McNemar,earliercontributions,muchofthisliteratureismoretechnicalthan

rl

yo

ps

1946,p.294).Perhapsbecausepsychologicalmeasuresaremorereadableandisaimedforthespecialistratherthanthepractitioner.o

dc

e

dbefuddledthanthoseoftheothernaturalsciences,psychologists(Thisisnotanewproblem;e.g.,Anastasi,1967;Glass,1986,s

in

et

nhavelongstudiedtheproblemofreliability(Cronbach,1951;Feldtbemoanthistendency).Wehopetoremedythisissuesomewhat,t

ne

im

&Brennan,1989;Guttman,1945;Kuder&Richardson,1937;foranappreciationoftheproblemsandimportanceofreliabilityiss

ui

c

eo

Lord,1955;McDonald,1999;Spearman,1904b),anditremainscriticaltotheactivityofmeasurementacrossmanydisciplines.l

dc

i

tsanactivetopicofresearch(Bentler,2009;McNeish,2018;Revelle

rReliabilitytheoryisnotjustforthepsychometricianestimatingi

ah

Ts

&Zinbarg,2009;Sijtsma,2009;Wood,Harms,Lowman,&latentvariables,butalsoforthebaseballmanagertryingtopredicti

h

T

DeSimone,2017).Unfortunately,althoughrecentadvancesinthehowwellahighperformingplayerwillperformthenextyear,for

accuratelyestimatingagreementamongdoctorsinpatientdiagno-

ses,andinevaluationsoftheextenttowhichstockmarketadvisors

underperformthemarket.

ThisarticlewaspublishedOnlineFirstAugust5,2019.Issuesofreliabilityarefundamentaltounderstandinghowcor-

XWilliamRevelle,DepartmentofPsychology,NorthwesternUniver-relationsbetweenobservedvariablesare(attenuated)underesti-

sity;DavidM.Condon,DepartmentofMedicalSocialSciences,North-

matesoftherelationshipsbetweentheunderlyingconstructs,how

westernUniversity,andDepartmentofPsychology,UniversityofOregon.

observedestimatesofaperson’sscorearebiasedestimatesoftheir

PreparationofthisarticlewasfundedinpartbyGrantSMA-1419324

latentscore,andhowtoestimatetheconfidenceintervalsaround

fromtheNationalScienceFoundationtoWilliamRevelle.

anyparticularmeasurement.Understandingthemanywaysto

CorrespondenceconcerningthisarticleshouldbeaddressedtoWilliam

estimatereliabilityaswellasthewaystousetheseestimates

Revelle,DepartmentofPsychology,NorthwesternUniversity,SwiftHall,

allowsonetobetterassessindividualsandtoevaluateselection2029SheridanRoad,Evanston,IL60208.E-mail:revelle@northwestern

andpredictiontechniques.Thisisnotjustaproblemformeasure-.edu

1395

## Page 2

ment specialists but for all who want to make theoretical infer- r (cid:2) V X (cid:6)(cid:7)2 (cid:5)(cid:2)1(cid:6) (cid:7)2(cid:5) . (2)
encesfromobserveddata.SchmidtandHunter(1996)discuss26 xx V V
X X
waysthatnotcorrectingfortheeffectsofreliabilityandmeasure-
If the test is unidimensional the product of the observed score
ment error can hinder progress in many areas of psychological
variance and the reliability is an estimate of the variance of the
research. However, Borsboom and Mellenbergh (2002) take a
latentconstruct(sometimescalledthe“truescore”)1inatestthat
contrary position and suggest that using classical measures of
reliabilityforsuchcorrectionsisanerror. wewillsymbolize2as(cid:7) (cid:3) 2 (cid:2)V X (cid:6)(cid:7)2 (cid:5) (cid:2)r xx V X .Spearman(1904b)
developed reliability theory because he was interested in correct-
The fundamental question in reliability is to what extent do
ingtheobservedcorrelationbetweentwoabilitytestsfortheirlack
scoresmeasuredatonetimeandplacewithoneinstrumentpredict
ofreliability.Inmodernterminology,thisdisattenuatedcorrelation
scores at another time and/or place and perhaps measured with a
((cid:7) )representsthecorrelationbetweentwolatentvariables((cid:8)and
differentinstrument?Thatis,givenaperson’sscoreonTest1at (cid:8)(cid:9)
(cid:9)) estimated by the correlation of two observed tests (r ) cor-
Time1,whatscoreshouldbeexpectedatasecondmeasurement xy
rected for the reliability of the observed tests (r and r ; see
occasion? The naive belief is that if the tests measure the same xx yy
Figure1).
construct,thenpeoplewilldojustaswellonthesecondmeasure
astheydidonthefirst.Thismistakenbeliefcontributestoseveral r
errorsincludingthecommonviewthatpunishmentimprovesand (cid:8) (cid:3)(cid:9) (cid:2) (cid:2)r xy r . (3)
xx yy
rewardsdiminishsubsequentperformance(Kahneman&Tversky,
1973) and other popular phenomena like the “sophomore slump” Furthermore,givenanobservedscore,thevarianceoftheerror
and the “Sports Illustrated jinx” (Schall & Smith, 2000). More ofthatscore((cid:7)2 (cid:5))isjusttheobservedtestvariancetimesoneminus
formally,theexpectationforthesecondmeasureisjusttheregres- the reliability and thus the standard deviation of the error associ-
sion of observations at Time 2 on the observations at Time 1. If atedwiththatscore(thestandarderrorofmeasurement)is:
both the Time 1 and Time 2 measures are equally “befuddled by
error,” then the observed relationship is the reliability of the (cid:7) (cid:5) (cid:2)(cid:7) x (cid:2)1(cid:6)r xx . (4)
measure:theratioofthelatentscorevariancetotheobservedscore Although expressed as a correlation between observed scores,
variance. reliability is a ratio of reliable variance to total variance. In
addition, because the covariance of the latent score with the
observed score is just the reliable variance, the predicted latent
Reliability as a Variance Ratio score(cid:3)ˆ is
The basic concept of reliability seems to be very simple: ob-
(cid:3)ˆ(cid:2)r x (5)
servedscoresreflectanunknownmixtureofsignalandnoise.To xx
detect the signal, we need to reduce the noise. Reliability thus wherexistherawdeviationscore(x(cid:2)X(cid:6)X¯ ).FromEquation4,
defined is a function of the ratio of signal to noise. The signal we know the standard error of measurement and can give a
might be something as esoteric as a gravity wave produced by a confidence interval for our observed score and even for the esti-
collision of two black holes, or as prosaic as estimating the matedlatentscore(Charter&Feldt,2001):
expected batting average of a baseball player based upon the
performanceoftheprioryear.Thenoiseingravitywavedetectors (cid:3)ˆ i (cid:2)r xx x i (cid:10)t(cid:11)⁄2,df (cid:7) x (cid:2)r xx (1(cid:6)r xx ) (6)
include the seismic effects of cows wandering in fields near the
wheret representsStudent’stwithanappropriateprobability
detectoraswellaspassingicecreamtrucks.Thenoiseinbatting (cid:2)/2,df
level(e.g.,(cid:2)(cid:10).05).
averagesincludetheeffectofopposingpitchers,variationsinwind
Increasingreliabilityreducesthestandarderrorofmeasurement
direction,andtheeffectsofjetlagandsleepdeprivation.Wecan
(Equation4)andincreasestheobservedcorrelationwithexternal
enhance the signal/noise ratio by either increasing the signal or
variables (Equation 3). That is, if we knew the reliabilities, we
reducing the noise. Unfortunately, this classic statement of reli-
couldcorrecttheobservedcorrelationtofindthelatentcorrelation
abilityignorestheneedforunidimensionalityofourmeasuresand
and estimate the precision of our measurement. The problem for
equates expected scores with construct scores, a relationship that
Spearmanwas,andremainsforustoday,howtofindreliability?
needstobetestedratherthanassumed(Borsboom&Mellenbergh,
Equations 1–6 are intellectually interesting, but not very help-
2002).
ful, for they decompose an observed measure into the two unob-
WecancreditSpearman(1904b)fortheoriginalformalization
servablevariablesoflatentscoreandlatenterror.Tomakeiteven
of reliability. In the first of two landmark papers (the other,
more complicated, all tests are assumed to measure something
Spearman, 1904a, laid the basis for factor analysis and measure-
stableovertime(denotedasTfortraitlike),somethingthatvaries
ment of cognitive ability) he developed the ordinal correlation
over time (reflecting the current state and denoted as S), some
coefficient and the basic principles of reliability theory. Spear-
specificvariance(s)thatisstablebutdoesnotmeasureourtraitof
man’sfundamentalinsightwasthatanobservedtestscorecouldbe
interest,andsomeresidual,randomerror(E;Baltes,1987;Cattell,
decomposed into two unobservable constructs: a latent score of
interestandaresidualbutlatenterrorscore:
1AsdiscussedbyLordandNovick(1968)andBorsboomandMellen-
X(cid:2)(cid:3)(cid:4)(cid:5). (1) bergh(2002),classicaltesttheories“truescore”isjusttheexpectedvalue
andshouldnotbeconfusedwithPlatonicTruth.
Reliability was defined as the fraction of an observed score 2ObservedvariablesandcorrelationsareshowninconventionalRoman
variancethatwasnoterror: fonts,latentvariablesandlatentpathsinGreekfonts.
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
1396 REVELLEANDCONDON

## Page 3

1397RELIABILITY

Inallcases,weareinterestedinthescoresfortheindividuals

beingmeasured.Tomaketheproblemevenmorecomplicated,it

islikelythatourtraitorstatescoresreflectsomeaggregationof

itemresponsesoroftheratingsofjudges.Thus,wewanttoassess

thevarianceduetotraitsorstatesthatisindependentoftheeffects

ofitemsorjudges,howmuchvarianceisduetotheitemsor

judges,andfinallyhowmuchvarianceisduetotheinteractionsof

4items/judgeswiththetrait/statemeasures.Tobeconsistentwith

muchoftheliterature,wewilltreattraitandstateasbothlatent

sourcesofvariancefortheobservedscoreXandrefertotraitasa

stableacrosstimeandstateasvaryingacrosstime.Werecognize,

ofcoursethattraitsdochangeoverlongerperiodsoftimebutwill

usethisstable/unstabledistinctionforrelativelyshorttemporal

.y

l(cid:7)2

d)durations.Althoughsomeprefertothinkofspecificvariance(

.as

s

ro

e(cid:7)2r

)ashopelesslyconfounded,weprefertoanderrorvariance(hb

es

id

lseparatethemfortherearesomedesigns(e.g.,test–retestvs.e

b

tu

a

pnparallelforms)thatallowustodistinguishthem.

id

mFigure1.Thebasicconceptofreliabilityandcorrectingforattenuation.

e

eReliabilityasdefinedinEquations7and8isnotjustafunctioni

ls

rrrAdjustingobservedcorrelations()byreliabilities(,)estimatesls

axyxxyy==

iofthetest,butalsoofwhoisbeingtested,wheretheyaretested,

d(cid:7)s

underlyinglatentcorrelations(;seeEquation3).Observedvariablest

(cid:8)(cid:9)ei

bandwhentheyaretested.Becauseitisavarianceratio,increasingf

andcorrelationsareshowninconventionalRomanfonts,latentvariableso

o

tebetween-personvariancewithoutincreasingtheerrorvariancewill

andlatentpathsinGreekfonts.n

t

oo

n

increasethereliability.Similarly,decreasingbetween-personvari-r

os

i

nancewilldecreasereliability.Generalizabiltytheory(Cronbach,d

on

ia

t

Rajaratnam,&Gleser,1963;Gleser,Cronbach,&Rajaratnam,a

1966b;Hamaker,Schuurman,&Zijlmans,2017;Kenny&Zautra,ir

ce

os1965)isonewaytoestimatetheindividualvariancecomponents

u1995).s

s

Al

aratherthantheirratio.AnotherapproachisItemResponseTheory

Althoughultimatelyinterestedintheprecisionofascoreforu

ld

a

ic(e.g.,Embretson,1996;Lord&Novick,1968;Lumsden,1976;eachindividual,reliabilityisexpressedasaratioofvariances

vi

gi

do

3nMellenbergh,1996;Rasch,1966;Reise&Waller,2009),whichrbetweenindividuals:ThereliabilityofX(-)isjustthepercent

l

oixx

he

Vageoftotalvariability()thatisnoterror.Unlesswehaveaddressesthisproblembyattemptingtogetameasureofprecisionch

yXt

sf

repeatedmeasures,errorisanunknownmixtureofvariabilityduePforaperson’sestimatethatisindependentofthevarianceoftheo

ne(cid:11)

todifferencesinitemmeans,thePersonIteminteraction,andaspopulationanddependsuponjusttheprobabilityofaparticular

cu

i

rlsomeunmodeledresidual.Thereliablebetweenpersonvarianceis

epersonansweringparticularitems.a

mn

oamixtureofTrait,State,andspecificvariance.(Forinstance,anA

s

r

ee

itemsuchas“Ienjoyalivelyparty”isanunknownmixtureoftraitph

t

eConsistency,ReliabilityandtheDataBox

yextraversion,statepositiveaffect,andthespecificwordingoftheh

bt

rd

item—howoneinterpretslivelyandparty.)Ifweareinterestedino

ef

databoxWhenCattell(1946)introducedtheitwasathree-wayt

hy

thestabletraitscores,reliabilityistheratioof(unobservable)traitg

l

eiorganizationofmeasurestakenoverpeople,tests,andtime.In

rl(cid:7)(cid:12)2

2yoVvariance()to(observable)totaltestvariance().(Weuseto

psTx

typicalCattellianfashion,overtheyearsthissimpleideagrewtoo

drepresentunobservablevariances,Vtorepresentobservablevari-c

e

dsasmanyas10dimensions(Cattell,1966a;Cattell&Tsujioka,

inance.)Thatis,

et

nt1964).However,thethreeprimarydistinctionsarestilluseful

ne

im

(cid:7)(cid:7)22s

today(Nesselroade&Molenaar,2016;Revelle&Wilt,2016).ui

TT(cid:2)(cid:2)c

r.(7)e

ott

l(cid:7)(cid:4)(cid:7)(cid:4)(cid:7)(cid:4)(cid:7)V2222Usingthesedimensions,Cattell(1964)distinguishedbetweend

c

XiTSse

ts

ri

threewaysthattestscanbeconsistent:acrossoccasions(reliabil-ah

THowever,ifweareinterestedinhowwellwearemeasuringas

i

ity),acrossitems(homogeneity),andacrosspeople(transferabilityh

Tparticularfluctuatingstate(e.g.,anemotion)wewanttoknow

orhardiness).Weconsiderthefirsttwooftheseconceptsandleave

(cid:7)(cid:7)22thelattertoadiscussionofvalidity.Thesevarioustypesof

SS(cid:2)(cid:2)

r.(8)

ssreliabilitymaybesummarizedgraphicallyintermsoflatenttraits,(cid:7)(cid:4)(cid:7)(cid:4)(cid:7)(cid:4)(cid:7)V2222

XTSse

paths,observedvariables,andcorrelations(seeFigure2).

(cid:7)(cid:7)22orandhowtoseparateTheproblembecomeshowtofind

TS

theireffects.Althoughtraitscoresarethoughttobestableover

time,statescores,whilefluctuating,showsome(unknown)short-

termtemporalstability.Considerameasureofdepression.Partof

anindividual’sdepressionscorewillreflectlong-termtraitneu-

3Wecanalsofindwithin-subjectreliabilityacrosstime.Thiswillbe

roticismandsomeofitreflectscurrentnegativeemotionalstate.

discussedlaterandintheonlinesupplementalmaterials.

Twomeasurestakenafewhoursapartshouldproducesimilartrait

4Unfortunately,someprefertouseStatetoreflectthemeasureata

andstatevalues,althoughmeasurestakenayearapartshould

particulartimepointandtodecomposethis“State”intoTraitandOccasion

reflectjustthetrait.components(Coleetal.,2005).

## Page 4

1398REVELLEANDCONDON

.y

l

d

.as

ro

er

hb

s

id

le

b

tu

a

pn

id

m

e

ei

ls

ls

a

i

dFigure2.internalconsistencyReliabilityhasmanyforms.Itemswithinthesametestprovideestimatesof.s

te

i

balternateformsrrObservedcorrelationbetweenorparalleltestsgivenatthesametime(,)estimateparallelf

(cid:2)(cid:2)oxxxx

o1122

trrtestreliability.Testsgivenat(almost)thesametime(Times1and2;e.g.,,)providemeasuresofe

(cid:2)(cid:2)nxxxx

t1212

oo

dependabiltyrr,whilemeasurestakenoveralongerperiod(Times2and3;e.g.,,)aremeasuresofn

xxxxr

1323os

stability.ThesemeasuresdifferintheamountofTraitandStateandspecificvarianceinthemeasures.Observedi

nd

on

variablesandcorrelationsareshowninconventionalRomanfonts,latentvariablesandlatentpathsinGreeki

at

a

irfonts.

ce

os

us

s

Al

a

u

ld

a

ic

vi

gi

dthisrestriction(Sackett&Yang,2000),thecorrelationwasAlternativeEstimatesofReliabilityo

nl

oi

hfoundtobe.73.e

ch

yt

sButtheScottishLongitudinalStudyisunusuallylong,andisitf

PTest–RetestofTotalScoreso

nemorecommontotaketest–retestsovermuchshorterperiodsof

as

cu

iPerhapsthemostobviousmeasureofreliabilityisthecorrela-

time.Inmostcasesitisimportantthatwedonotassumethattherl

ea

mn

tionoftestwiththesametestsometimelater.ForGuttman(1945),ostateeffectis0(Chmielewski&Watson,2009).Itismoretypical

A

s

r

ettethiswasreliability.Ifwehaveonlytwotimepoints(and),this

tofindapatternofcorrelationsdiminishingasafunctionoftheph

12

t

ecorrelationisanunknownmixtureoftrait,state,andspecific

ytimelagbutnotasymptoticallyapproachingzero(Cole,Martin,&h

bt

varianceand,additionally,afunctionofthelengthoftimebetweenrd

Steiger,2005;Damian,Spengler,Sutu,&Roberts,2018).Thiso

ef

t

hthetwomeasures:y

patternistakentorepresentamixtureofstabletraitvarianceandg

l

ei

rl

yodiminishingstateeffectssuchthatthetest–retestreliabilityacross

p(cid:6)s(cid:4)(cid:12)(cid:7)(cid:4)(cid:7)(cid:7)tt222

21o

dTSs(cid:2)c

twotimeperiodsasshowninEquation9willbecomesmallerther(9)e

ttd(cid:7)(cid:4)(cid:7)(cid:4)(cid:7)(cid:4)(cid:7)s2222

12in

TSsegreaterthetimelag.Unfortunately,withonlytwotimepointswe

et

nt

ne

(cid:13)icannotdistinguishbetweenthetraitandstateeffects.However,mwhere(theauto-correlationduetoshorttermstateconsis-

su

i(cid:6)

(cid:12)(cid:7)ctt2ttttwiththreeormoretimepoints(,,,...,),wecandecomposetency)islessthan1andthusthestateeffect()will

e21o

n123Sld

c

irrrtheresultingcorrelations(,,,...),intotraitandstatebecomesmallerthegreaterthetimelag.Iftheinterveningtime

ts

rxxxxxxi

a121323h

TcomponentsusingStructuralEquationModeling(SEM)proce-islongenoughthatthestateeffectisminimal,wewillstillhaves

i

h

Tspecificvariance,andthecorrelationofatestwiththesametestdures(Hamakeretal.,2017)orsimplepathtracingrules

lateris(Chmielewski&Watson,2009)andtheresolutioncontinuesto

improvewithfourormoretimepoints(Coleetal.,2005;Kenny&

(cid:4)(cid:7)(cid:4)(cid:7)(cid:7)(cid:7)2222

Zautra,1995).(SeeFigureS1intheonlinesupplementalmateri-TsTs(cid:2)(cid:2)

r.(10)

xx(cid:7)(cid:4)(cid:7)(cid:4)(cid:7)(cid:4)(cid:7)V2222

xals).TSse

Alargetest–retestcorrelationoveralongperiodoftime

Animpressiveexampleofacorrelationofthesamemeasure

stabilityindicatestemporal(Boyle,Stankov,&Cattell,1995;

overtimeisthecorrelationof.66ofabilityasmeasuredby

Cattell,1964;Chmielewski&Watson,2009).ThisshouldbetheMorayHouseExamatage11withthesametestgiventothe

expectedifweareassessingsomethingtrait-like(suchascog-sameparticipants69yearslaterwhentheywere80yearsofage

nitiveabilityorperhapsemotionalstabilityorextraversion)but(Deary,Whiteman,Starr,Whalley,&Fox,2004).Thiscorre-

notifweareassessingsomethingthoughttorepresentanlationwaspartiallyattenuatedduetorestrictionofrangeforthe

emotionalstate(e.g.,alertnessorarousal).Becauseweare80-year-oldparticipants.(Thelessable11yearoldswereless

likelytoappearinthe80-year-oldsample.)Whencorrectingfortalkingaboutcorrelations,meanlevelscanincreaseordecrease

## Page 5

over time with no change in the correlation.5 Measures of trait anytemporaleffectsofafirstorsecondadministration,andallthe
stability are a mixture of immediate test–retest dependability possibleinteractionsbetweentheseterms:
and longer-term trait effects (Cattell, 1964; Chmielewski &
X (cid:2)(cid:13)(cid:4)P (cid:4)I (cid:4)T (cid:4)PI (cid:4)PT (cid:4)IT (cid:4)PIT (cid:4)(cid:5).
Watson, 2009). For Boyle et al. (1995) and Cattell (1964), ijk i j k i j i k j k i j k
dependability was the immediate test–retest correlation; for (11)
Chmielewski and Watson (2009) the time lag of 2 weeks is
With complete data, we can find these components using con-
considered an index of dependability. To Wood et al. (2017),
ventionalrepeatedmeasuresanalysisofvarianceofthedata(i.e.,
dependability is assessed by repeating the same items later in
aovincoreR)orusingmultilevelfunctionssuchaslmerinthe
one testing session.
lme4 package (Bates, Maechler, Bolker, & Walker, 2015) for R.
All of these indicators of dependability and stability are in
Asanexampleofsuchavariancedecompositionconsiderthe10
contradictiontothelong-heldbeliefthataproblemwithtest–retest
overlapping mood items discussed in the online supplemental
reliability is that it introduces memory effects of learning and
materials (see Table S1). Nineteen percent of the variance of the
practice(Kuder&Richardson,1937).Asevidenceforthememory
anxietyscoreswasduetobetween-personvariability,25%tothe effect,Woodetal.(2017)reportsthattheaverageresponsetimes
veryshortperiodoftime,19%totheinteractionofpersonbytime, tothesecondadministrationofidenticalitemsinthesamesession
andsoforth;and13%wasresidual(unexplained)variance.
isabout80%ofthetimeofthefirstadministration.
Multilevel modeling approaches are particularly appropriate if
Intheonlinesupplementalmaterials(seeTableS1)wecompare
repeatingthesamemeasuremultipletimes(e.g.,inanexperience
multiple estimates of reliability for three different example data
sampling study: Bolger & Laurenceau, 2013; Fisher, 2015; Mehl
setsavailableinthepsychToolspackage(Revelle,2019b)intheR
& Conner, 2012; Mehl & Robbins, 2012; Wilt, Funkhouser, &
open-sourcestatisticalsystem(RCoreTeam,2019).Wedescribe
Revelle, 2011; Wilt, Bleidorn, & Revelle, 2016, 2017). We can
thesedatasetsinsomedetailastheyareusefuldemonstrationsof
derive multiple measures of reliability, across subjects, across
traitandstatevariations.Wecompareimmediateretesttoshort(45
time,acrossitemsandthevariousPerson(cid:11)Time,Person(cid:11)Items,
min) and then longer delay (1 to 7 days) on 10 mood items and
Time (cid:11) Item interactions (Cranford et al., 2006; Shrout & Lane,
9–24itemtraitscalesfor1to4weeks.
2012). This is implemented in the multilevel.reliability
To compare the effects of an immediate retest versus a short
function and discussed in more detail in a tutorial for analyzing
delay versus a somewhat longer delay, consider the msqR, sai,
dynamic data (Revelle & Wilt, 2019) as well as in the online
and tai example data sets6; the analyses discussed below are
supplementalmaterials.Althoughthesevariancecomponentscan
demonstrated in the online supplemental materials. We will use
befoundusingtraditionalrepeatedmeasuresanalysisofvariance,
some of these items in the subsequent examples evaluating and
itismoreappropriatetousemultileveltechniques,particularlyin
comparingtheimmediatedependabilityandthe45minandmul-
thecaseofmissingdata.
tidaystabilitycoefficientsofthesemeasures.10itemsweregiven
Stabilityneedstobeadjustedfordependability,andthusthe
as part of the STAI and then immediately given again (with a
.36 stability over 2 days of the SAI (online supplemental
slightly different wording) as part of the MSQ. Five of the items
materialsTableS1)shouldbeadjustedfortheimmediatedepend-
werescoredinapositive(anxious)direction,fiveinthenegative
abilityof.85tosuggesta2-daystabilityofanxiousmoodof.42,
(nonanxious)direction.
whichisnotablysimilartothatofthestate–traitcorrelationof.43.
Whenmeasuringmood,weneedtodisentangletheepisodicmem-
Components of Variance Estimated by
ory components of the state measure from the semantic memory
Test–Retest Measures
Apowerfuladvantageofrepeatingitemsisthatitallowsforan 5Forexample,participantsintheScottishLongitudinalStudyperformed
assessmentofsubjectconsistencyacrosstime(thecorrelationfor better in adulthood than they did as 11 year olds but the correlations
eachsubjectoftheirpatternofresponsesacrossthetwoadminis- showedremarkablestability.
6Thedata(N(cid:14)4,000)werecollectedaspartofalong-termseriesof
trations) as well as the consistency of the items (the correlation
studiesoftheinterrelationshipsbetweenthestablepersonalitydimensions
acrosssubjectsofresponsestoeachitem;DeSimone,2015;Wood
of extraversion, neuroticism, and impulsivity (e.g., Eysenck & Eysenck,
et al., 2017). This allows for identification of unstable items and 1964;Revelle,Humphreys,Simon,&Gilliland,1980),situationalstressors
inconsistent responders. In addition, by using multilevel anal- (caffeine, time of day, movie-induced affect, e.g., Anderson & Revelle,
yses7 it is possible to estimate the variance components due to 1983,1994;Rafaeli,Rogers,&Revelle,2007;Rafaeli&Revelle,2006),
people, items, the Person (cid:11) Item interaction, time, the Person (cid:11) momentary affective and motivational state (e.g., energetic and tense
arousal,Thayer,1978,1989;stateanxiety,Spielberger,Gorsuch,&Lush-
Time interaction, and the residual (error) variance (DeSimone, ene,1970),andcognitiveperformance(Humphreys&Revelle,1984).The
2015; Revelle & Wilt, 2019; Shrout & Lane, 2012). This is Motivational State Questionnaire (MSQ, Revelle & Anderson, 1998) in-
implementedforexampleastheTest–Retestfunctioninthepsych cluded75itemstakenfromanumberofmoodquestionnaires(e.g.,Larsen
&Diener,1992;Thayer,1978;Watson,Clark,&Tellegen,1988)andhad
package. The responses to any particular item can be thought to
10anxietyitemsthatoverlappedwiththestateversionoftheStateTrait
representmultiplesourcesofvariance,andthereliabilityofatest
AnxietyInventory(Spielbergeretal.,1970).SeeTable1andtheonline
madeupofitemsisthusafunctionofthoseindividualsourcesof supplementalmaterialsformoredetails.
variance.IfweletP representthei person,I thej item,T the 7Analyticstrategiesforanalyzingsuchmultileveldatahavebeengiven
i th j th k
firstorsecondadministrationoftheitem,thentheresponsetoany different names in a variety of fields and are known by a number of
differenttermssuchastherandomeffectsorrandomcoefficientmodelsof
item(e.g.,ofananxietyinventory)isafunctionofthemeanlevel
economics, multilevel models of sociology and psychology, hierarchical
ofalloftheitemsinthetest,thetraitlevelofthepersontakingthe linearmodelsofeducationormoregenerally,mixedeffectsmodels(Fox,
item,thedifficultyoraverageendorsementfrequencyoftheitem, 2016).
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
RELIABILITY 1399

## Page 6

Table1
CalculatingMultipleMeasuresofInternalConsistencyReliabilityDemonstratedon10ItemsFromtheMotivationalState
Questionnaire(msqRDataSet,N(cid:10)3,032)
10anxietyitemsfromthemsqRdataset
Variable anxis jttry nervs tense upset at.s- calm- cnfd- cntn- rlxd- g F1 F2 h2
anxious 1.00 .41 .60 .00 .53
jittery .47 1.00 .47 .41 .00 .39
nervous .54 .48 1.00 .43 .60 .00 .55
tense .57 .48 .57 1.00 .54 .58 .00 .63
upset .29 .16 .35 .45 1.00 .34 .32 .00 .22
at.ease- .23 .24 .29 .35 .30 1.00 .66 .00 .47 .66
calm- .28 .32 .31 .36 .23 .62 1.00 .69 .00 .31 .57
confident- (cid:16).01 (cid:16).02 .08 .07 .17 .44 .31 1.00 .11 .00 .77 .61
content- .07 .04 .13 .19 .29 .56 .45 .61 1.00 .31 .00 .74 .65
relaxed- .27 .34 .30 .40 .29 .60 .56 .34 .45 1.00 .68 .00 .33 .57
SMC .42 .37 .44 .52 .27 .55 .47 .40 .51 .47
r .73 .69 .70 .77 .76 .63 .65 .70 .73 .60
ii
Reliability
Formula Calculation measure
Totalvariance(cid:10)V (cid:2) (cid:3)(cid:4)R (cid:5) (cid:2) 39.60
X ij
Totalreliableitemvariance(cid:10)(cid:3)r (cid:2) 6.97 V (cid:6)tr(cid:4)R(cid:5)(cid:4)(cid:3)(cid:4)r (cid:5) 39.60(cid:6)10(cid:4)6.97 (cid:10).923
ii glb (cid:2) x V ii 39.60
x
rbestsplit(A(cid:10)1,2,5,6,8vsB(cid:10)3,4,7,9,10)(cid:10).81
(cid:5) 4 (cid:10)bestsplithalf(cid:10) 1
2
(cid:4)
r
a r b
2
1
(cid:14)
(cid:4)
.
.
8
8
1
1
(cid:10).895
ab
Totalcommonvariance(cid:10)(cid:3)h2 (cid:2) 5.37 V (cid:6)tr(cid:4)R(cid:5)(cid:4)(cid:3)h2 39.60(cid:6)10(cid:4)5.37 (cid:10).883
i (cid:15) t (cid:2) x V i 39.60
x
Totalsquaredmultiplecorrelation(cid:17)(SMC)(cid:10)4.43 V (cid:6)tr(cid:4)R(cid:5)(cid:4)(cid:3)(cid:4)SMC(cid:5) 39.60(cid:6)10(cid:4)4.43 (cid:10).859
(cid:16) (cid:2) x
6 V 39.60
x
Averagesquaredcorrelation(cid:10)r(cid:2)2 (cid:2) (cid:3) n R (cid:14) i 2 j (cid:6) (cid:4)n t (cid:6) r(cid:4)R 1 2 (cid:5) (cid:5) (cid:10).137 (cid:16) 2 (cid:2) V x (cid:6)tr(cid:4)R(cid:5)(cid:4)(cid:2) V r(cid:2)2(cid:14)n⁄(cid:4)n(cid:6)1(cid:5) 39.6(cid:6)10(cid:4) 39 .(cid:2) .60 .137(cid:14)10⁄9 (cid:10).841
x
(cid:11) (cid:2) n V x (cid:6)tr(cid:4)R(cid:5) 1039.60(cid:6)10 (cid:10).831
n(cid:6)1 V 9 39.60
x
Averagecorrelation(cid:10)r(cid:2) (cid:2) n V X (cid:14) (cid:6) (cid:4)n tr (cid:6) (cid:4)V 1 X (cid:5) (cid:5) (cid:2) 0.329 (cid:11) (cid:2) 1(cid:4)(cid:4) n n r(cid:2) (cid:6)1(cid:5)r(cid:2) 1 1 (cid:4) 0 9 (cid:14) (cid:14) .3 . 2 3 9 29 (cid:10).831
rworstsplit(A(cid:10)1–5vs.B(cid:10)6–10)(cid:10).385
(cid:4)(cid:10)worstsplithalf(cid:10) 1
2
(cid:4)
r
a r b
2
1
(cid:14)
(cid:4)
.
.
3
3
8
8
5
5
(cid:10).556
ab
Sumofgloadings(cid:10)4.65(bifactor) (cid:4)(cid:3)g(cid:5)2 4.652 (cid:10).545
(cid:15) (cid:2) i
g V 39.60
X
Sumofgloadings(cid:10)4.09(Schmid-Leiman) (cid:4)(cid:3)g(cid:5)2 4.092 (cid:10).422
(cid:15) (cid:2) i
h V 39.60
X
Note. Therownamesfortheitemshavebeenabbreviatedforclarity.Negativesignsfollowingtheitemimplytheitemshouldbenegativelyscored.The
10itemsmaybethoughtofasmeasuresofstateanxiety.Fivearepositivelyscored,fivenegatively.Generalfactorloadings(g)andgroupfactorloadings
were found from the omegaSem function, which applies a bifactor solution. The hierarchical solution from omega applies the Schmid-Leiman
transformation and has slightly lower general factor loadings. Split half calculations were done by finding all possible splits of the test. Although the
statisticsshownaredonebyhand,theyarealldoneautomaticallyinvariouspsychfunctions(seeTable2).
involved when answering trait like questions (Cattell, 1964; creating another test (an alternate form) that has conceptually
Chmielewski&Watson,2009).Statemeasuresofaffectivityprob- similar but semantically different items. If measuring the same
ably involve episodic memory whereas trait measures of similar construct (e.g., arithmetic performance) we can subtly duplicate
constructs (e.g., trait anxiety or neuroticism) likely tap semantic itemsoneachformandevenmatchforpossibledifficultyoforder
memory (Klein, Cosmides, Tooby, & Chance, 2002). With only effects(a1:whatis6(cid:15)3?anda2:whatis4(cid:15)5?vs.b1:whatis
twomeasuresofstateanxietyandoneoftraitanxiety,wecannot 3 (cid:15) 6? and b2: what is 5 (cid:15) 4?). Cattell (1964) discusses “Her-
disentangle how much of the trait measure is state (Equation 9),
ringbone”consistency,whichareessentiallyparallelforms:Each
butifwehadmoremeasuresoverlongerperiodsoftimewewould
half of the test is made up of half of the items of multiple
beabletodoso.
constructs,andeachisduplicatedintheotherhalf(math,English,
social studies). Although creating alternate forms by hand is te-
Alternate Forms
dious,ithasbecomepossibleforabilityitemstogeneratealternate
Ifwedonotwanttowaitforalongtimeandwedonotwantto formsusingcomputerAutomaticItemGenerationtechniques(Em-
exactly repeat the same items, we can estimate reliability by bretson,1999;Leon&Revelle,1985;Loe&Rust,2017).
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
1400 REVELLEANDCONDON

## Page 7

1401RELIABILITY

(cid:14)rAlternateformsgivenatthesametimeeliminatetheeffectof2

xx

(cid:2)12r.(12)

thespecificitemvariancebutdonotremoveanymotivationalstate(cid:4)xx

r1

xx

12effect:Sometimesalternateformscanbedevelopedwhenalonger

Itisimportanttonotethecorrelationbetweenthetwopartstestissplitintomultipleshortertests.Asanexampleofthis,

r()isnotthesplithalfreliability,butisusedtofindthesplithalfsaiconsiderthedatasetdiscussedintheonlinesupplemental

xx

12

rreliability()foundbythe“Spearman-Brownprophecyformula”materials,whichincludes20items,10ofwhichoverlappedwith

xx

(Equation12)msqRthedatasetandwereusedforourexamplesoftest–retest

nGiventhatwehavewrittenitemsandformedthemintotwoandrepeatedmeasurereliability.Theother10canbethoughtofas

nsplitsoflength/2,whatifweformedadifferentsplit?Howanalternateformoftheanxietymeasureandindeedcorrelate.74

saimsqRwiththetargetitemsfromtheand.Thesecorrelationsshouldwesplittheitemsintotwogroups?Odd/even,firsthalf/last

arelessthanwhenweactuallyrepeatthesameitemsbycorrelatinghalf,randomly?Thisisacombinatoriallydifficultproblem,inthat

!nsaimsqRtheoverlappingitemsoftheand(.85);arealmost

uniquewaystosplitatestintotwoequalparts.thereare

(cid:4)(cid:5)(cid:4)(cid:5)nn2⁄2!⁄2!

identicalwhenweconsidertheirshorttermdependability(.76);Whilethereareonly126possiblesplitsforthe10anxietyitems

.(cid:2)y

butlessthanestimatesofinternalconsistencysuchasorthediscussedabove,thisbecomes6,435fora16-itemabilitytest,

l

d

.(cid:16)as

averagesplithalfreliability(.83.87).1,352,078forthe24-itemEPIExtraversionScale(Eysenck&

ro

er

hb

Eysenck,1964),andover4.5billionfora36-itemtest.Thes

id

le

b

tsplit-Halffunctionwilltryallpossiblesplitsfortestsof16itemsu

a

pSplitHalf(AdjustedforTestLength)n

iorless,andthensample10,000splitsfortestslongerthanthat.Thed

m

e

ei

lsdistributionofallpossiblesplitsforthe10stateanxietyitems

lIfwehavegonetothetroubleofdevelopingtwoalternateformss

a

i

ds

discussedearliershowthatgreatestsplit-halfreliabilityis.92,theforaconceptandthenadministeredbothformstoasampleoft

ei

bf

oaverageis.87,andthelowestis.66(Figure3panelA).Thisisinparticipants,itislogicaltoaskwhatisthereliabilityofthe

o

te

ntcontrasttoallthepossiblesplitsof16abilityitemstakenfromthecompositeformedfrombothofthesetests.Thatis,ifwehavethe

oo

n

rInternationalCognitiveAbilityResource(ICAR;Condon&Rev-correlationbetweentwo5-itemtests,whatwouldbethereliability

os

i

nd

elle,2014)collectedaspartoftheSAPAproject(Revelle,Wilt,&ofthecomposite10-itemtest?Withabitofalgebra,wecanpredicto

n

ia

t

aRosenthal,2010;Revelleetal.,2016),wherethegreatestsplit-half

itusingaformuladevelopedbySpearman(1910)andBrownir

ce

os

u(1910):reliabilitywas.87,theaverageis.83,andthelowestis.73(Figures

s

Al

a

u

ld

a

ic

vi

gi

do

nl

oi

he

ch

yt

sf

Po

ne

as

cu

i

rl

ea

mn

oA

s

r

ee

ph

t

e

yh

bt

rd

o

ef

t

hy

gl

ei

rl

yo

ps

o

dc

e

ds

in

et

nt

ne

im

su

i

c

eo

ld

c

i

ts

ri

ah

Ts

i

h

T

Figure3.Thedistributionof126split-halfreliabilitiesforthe10stateanxietyitems(panelA)andthe

1,352,078splitsofthe24EPIExtraversionitems(panelC)suggeststhatthetestsarenotunivocalwhilethatof

the6,435splitsoftheICARabilityitems(panelB)andthe1,352,078splitsoftheEPINScale(panelD)

suggestsgreaterhomogeneity.

## Page 8

3 panel B). The 24 items of the EPI show strong evidence for Alphaand(cid:5) maybethoughtofasthecorrelationofatestwith
3
nonhomogeneity,withamaximumsplit-halfreliabilityof.81,an a nonexistent test just like it. That is, they are estimates of reli-
average of .73, and a minimum of .42 (Figure 3 part C). This ability based upon a fictitious parallel test. Alpha estimates the
supports the criticism that the EPI E Scale tends to measure the correlationbetweentheobservedtestanditshypotheticaltwinby
twobarelyrelatedconstructsofsociabilityandimpulsivity(Rock- assuming that the average covariance within the observed test is
lin&Revelle,1981).TheEPINScale,ontheotherhand,shows thesameastheaveragecovariancebetweenitemsoftheobserved
amaximumsplit-halfof.85,ameanof.80,andaminimumof.65, and with the hypothetical test. It is correct to the extent that the
providing strong evidence for a relatively homogeneous scale average interitem correlation correctly estimates the amount of
(Figure 3 part D). Examining these various splits is one way to domain score variance (an unknown mixture of trait and state
understand the homogeneity of the test, for if the various spits variance)ineachitem.Butthisisonlycorrectifalltheitemshave
differ a great deal (e.g., the EPI E Scale), this can be taken as a equal covariances and differ only in their observed variances. In
warningthatthetestisnotunidimensional. thiscasetheyaresaidtobe(cid:13)equivalent(Lord&Novick,1968),
whichisafancywayofsayingthattheyallhaveequalcovariances
Internal Consistency and Domain Sampling withthelatentscorerepresentedbythetestandhaveequalfactor
loadings on the single factor of the test. This is very unlikely in
Alloftheaboveproceduresarefindingthecorrelationbetween practiceanddeviationsfromthisassumptionwillleadto(cid:2)under-
twoformsoroccasionsofatest.Butwhatifthereisjustoneform
estimatingreliability(Teo&Fan,2013).
and one occasion? The approaches that consider just one test are In addition to (cid:5) , Guttman (1945) considered five alternative
collectively known as internal consistency procedures but also 3
waysofestimatingreliabilitybycorrectingfortheerrorvariance
borrow from the concepts of domain sampling and can use the
ofeachitem.Alloftheseequationsrecognizethatsomeoftheitem
variance decomposition techniques discussed earlier. Some of is reliable variance, the problem is how much? (cid:5) and (cid:2) assume
thesetechniques(e.g.,Cronbach,1951;Guttman,1945;Kuder& that the average item covariance is a good estima 3 te, (cid:5) uses the
Richardson, 1937) were developed before advances in computa- 6
SquaredMultipleCorrelation(smc)foreachitemasanestimateof
tionalspeedmadeittrivialtofindthefactorstructureoftests,and its reliable variance, while (cid:5) uses a function of the average
werebasedupontestanditemvariances.Theseprocedures((cid:2),(cid:5) 3 , squared item covariance. (cid:5) is 2 just the maximum split-half reli-
KR20) were essentially shortcuts for estimating reliability. The 4
ability.
variance decomposition procedures continued this approach but
Oneadvantageofusingthemeanitemcovarianceisthatitcan
expandedtobeknownasgeneralizabilitytheory(Cronbachetal.,
beidentifiedfromananalysisofvarianceperspectiveratherthan
1963; Gleser et al., 1965; Vispoel, Morris, & Kilinc, 2018) and
actually finding all the intercovariances. That is, just decompose
allowforthemanyreliabilityestimatesdiscussedbefore.
the total test variance into three components: the between person
There are a number of different approaches for estimating variance(cid:7)2,thebetweenitemvariance,(cid:7)2,andtheinteractionof
P I
reliabilitywhenthereisjustonetestandonetime.Theearliestwas Person(cid:11)Item,(cid:7)2.Thenreliabilityisjust1(cid:6) (cid:7) e 2 (Feldt,Woodruff,
to split the test into two random split halves and then adjust the e (cid:7)2
&Salih,1987;Hoyt,1941).ByexpressingitinPthismanner,Feldt
resultingcorrelationbetweenthesetwosplitsusingtheSpearman-
etal.(1987)wereabletoderiveanFdistributionfor(cid:2),andthus
Brownprophecyformula(Brown,1910;Spearman,1910).
a means for finding confidence intervals. This is implemented as
Unfortunately,asweshowedinFigure3,notallrandomsplits
thealpha.cifunctioninthepsychpackage.Alternativeproce-
produceequalestimates.Ifweconsideralloftheitemsinthetest
dures for the confidence interval for (cid:2) have been developed by
to be randomly sampled from some larger domain (e.g., trait-
DuhachekandIacobucci(2004).Perhapsthebiggestadvantageto
descriptive adjectives sampled from all words in the Oxford Un-
the variance approach to KR20, (cid:2), or (cid:5) was that in the 1930s–
abridged Dictionary or sociability items sampled from a poten- 3
1950s calculations were done with desk calculators rather than
tiallyinfinitenumberofwaysofbeingsociable),thenwecanthink
computersanditwasfarsimplertofindthenitemvariancesand
of the test as a sample of that domain. Because the item covari-
one total test variance than it was to find the n(cid:2)(n (cid:16) 1)/2 item
ancesshouldreflectjustshareddomainvariance,butitemvariance
covariances. In the modern era, such shortcuts are no longer
will be an unknown mixture of domain and specific and error
necessary.
variance,theamountofdomainvarianceinatestwouldvaryasthe
square of the number of items in the test times the average
Two Problems With (cid:2)
covarianceoftheitemsinthetest.Consideringitemsasmeasuring
ability, Kuder and Richardson (1937) proposed several estimates
Althougheasytocalculatefromjusttheitemstatisticsandthe
of the reliability of the average split half, with their most well- total score, (cid:2) and (cid:5) are routinely criticized as poor estimates of
knownbeingtheir20thequation(andthusknownasKR20). 3
reliability because they do not reflect the structure of the test
AmoregeneralformofKR20allowsitemstobenotjustright
(Bentler,2009;Cronbach&Shavelson,2004;Revelle&Zinbarg,
or wrong and thus corrects for the sum of the individual item
2009;S.Green&Yang,2009;Sijtsma,2009).Perhapsbecausethe
variances.Thisisknownascoefficient(cid:2)(Cronbach,1951)aswell
abilitytofind(cid:2)isavailableineasy-to-usesoftwarepackages,itis
as(cid:5) (Guttman,1945)
3 routinelyused.Thisisunfortunate;exceptforveryrareconditions,
(cid:11)(cid:2)(cid:16) 3 (cid:2) n(cid:6) n 1 V t (cid:6) V (cid:3) v i . (13) (cid:2) lac is k b o o f th (cid:13) a e n qu u i n v d a e la re n s c t y im ,B at e e n o tl f e t r h , e 20 re 0 l 9 ia , b 2 i 0 li 1 ty 7; o S f i a jt t s e m st a ( , b 2 e 0 c 0 au 9 s ) e a o n f d t a h n e
t overestimateofthefractionoftestvariancethatisassociatedwith
whereV isthetotaltestvariance,v isthevarianceforaparticular thegeneralvarianceinthetest(Revelle,1979;Revelle&Zinbarg,
t i
item,andtherearenitemsinthetest. 2009; Zinbarg, Revelle, Yovel, & Li, 2005). As we show in the
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
1402 REVELLEANDCONDON

## Page 9

online supplemental materials (see Table S2), (cid:2) provides no in- wherethetotaltestvariance(V )isthesumoftheelementsofall
x
formationabouttheconstancyorstabilityofthetest.Forourmood theitemvariancesandcovariancesand((cid:17)c)2isthesquaredsum
i
items, (cid:2) (.83(cid:16).87) exceeded the short term constancy estimates oftheloadingsonthegeneralfactor.
(.42(cid:16).76) and greatly exceeded the 2-day stability coefficients Normally, the specific item variance is confounded with the
(.36(cid:16).39).Forthetraitmeasures(particularlyofimpulsivity),the residualitem(error)variance,butifwehaveawayofestimating
low (cid:2) (.51) did not reflect the relatively high (.70) 2–4 week thespecificvariancebyexaminingthecorrelationswithitemsnot
stabilityofthemeasures.Thatistosay,knowing(cid:2)toldusnothing in the test, (e.g., repeated items, Wood et al., 2017) then we can
abouttest–retestconstancyorstability. includeitaspartofthereliablevariance(Bentler,2017):
Ifnotanestimateofreliability,does(cid:2)measureinternalconsis-
tency?No.Foritisjustafunctionofthenumberofitemsandthe (cid:15)
(cid:2)1(cid:2)cc(cid:2)1(cid:4)1(cid:2)AA(cid:2)1(cid:4)1(cid:2)DD(cid:2)1
t V
average correlation between the items. It is not a function of the X
u w n i i t d h im eq e u n a s l io (cid:2) na v l a it l y ue o s f t t h h a e t t r e e s f t l . ec It t i o s n e e as te y st to w c i o th ns h t o ru m c o t g e e x n a o m u p s le ite te m st s s , (cid:2) 1(cid:2)cc(cid:2) 1 1 (cid:2)c (cid:4) c(cid:2) 1 1 (cid:2)A (cid:4) A 1(cid:2) (cid:2)1 A (cid:4) A(cid:2) 1 1 (cid:2)D (cid:4) D 1(cid:2) (cid:2)1 D (cid:4) D(cid:2) 1 1 (cid:2)ee(cid:2)1 . (17)
two slightly related subtests, or even two unrelated subtests each Unfortunately, in his development of (cid:3), McDonald (1999) re-
withhomogeneousitems(see,e.g.,Revelle,1979;Revelle&Wilt, ferstotwoformulae(6.20aand6.20b)onefor(cid:3) andonefor(cid:3) ,
t g
2013). and calls them both (cid:3) (Zinbarg et al., 2005). These two coeffi-
cients are very different, for one is an estimate of the total reli-
abilityofthetest((cid:3)),thesecondisanestimateoftheamountof
Model-Based Estimates t
varianceinthetestduetosingle,generalfactor((cid:3) ).Thentomake
g
That“internalconsistency”estimatesdonotreflecttheinternal it even more complicated, there are two ways to find the general
structure of the test becomes apparent when we apply “model factor. One method uses a bifactor solution (Holzinger & Swin-
based”techniquestoexaminethefactorstructureofthetest.These eford, 1937; Reise, 2012; Rodriguez, Reise, & Haviland, 2016)
proceduresactuallyexaminethecorrelationsorcovariancesofthe usingstructuralequationmodelingsoftware(e.g.,lavaan,Rosseel,
itemsinthetest.Thankstoimprovementsincomputationalpower, 2012);theotherextractsahigherorderfactorfromthecorrelation
thetaskoffindingcorrelationsandthefactorstructureofa10-item matrix of lower level factors and then applies a transformation
testhasbeentransformedoverthepasttwogenerationsfrombeing developed by Schmid and Leiman (1957) to find the general
asummerresearchprojectforanadvancedgraduatestudenttoan loadingsontheoriginalitems.Thebifactorsolution((cid:3) )tendsto
g
afternoon homework assignment for undergraduates. Using the produce slightly larger estimates than the Schmid-Leiman proce-
latentvariablemodelingapproachoffactoranalysis,theseproce- dure((cid:3) )becauseitforcesallthecrossloadingsofthelowerlevel
h
duresdecomposethetestvarianceintothatwhichiscommontoall factorstobe0.FollowingZinbargetal.(2005),wedesignatethe
items (g, a general factor), that which is specific to some items Schmid-Leimansolutionas(cid:3) recognizingthehierarchicalnature
h
(orthogonalgroupfactors,f)andthatwhichisuniquetoeachitem of the solution. Both approaches are implemented in the psych
(typically confounding specific, s, and error variance, e). Many package.
researchers have discussed this approach in great detail (e.g., Animportantquestionwhenexaminingahierarchicalstructure
Bentler, 2017; McDonald, 1999; Revelle & Zinbarg, 2009; Zin- is how many group factors to specify when calculating (cid:3) ? The
h
barg et al., 2005) and we just summarize the main points here. Schmid-Leiman procedure is defined if there are three or more
Mostimportantlyforappliedresearchers,asweshowintheonline group factors, and with only two group factors the default is to
supplementalmaterials,model-basedtechniquesarejustaseasyto assumethattheyarebothequallyimportant(Zinbarg,Revelle,&
implement in modern software as are the more conventional ap- Yovel,2007).WhiletheSchmid-Leimanapproachisexploratory,
proaches. the bifactor approach is a confirmatory model that requires spec-
Theobservedscoreonatestitemmaybemodeledintermsof ifyingwhichvariablesloadoneachgroupfactor.
thesumoftheproductsoffactorscores(g,f,s,e)andloadings(c, How do these various approaches differ and what difference
A,D)onthesefactors: does it make? If we want to correct observed correlations for
attenuation by using Equation 3, then underestimating reliability
x(cid:2)cg(cid:4)Af(cid:4)Ds(cid:4)e (14)
will lead to serious overestimation of the true validity of a mea-
Becausethereliablevarianceofthetestisthatwhichisnoterror, sure. This is why there has been so much work on trying to
thereliabilityofatestwithstandardizeditemsshouldbe estimate the greatest lower bound of reliability (e.g., Bentler,
2017). In this case if (cid:2) underestimates reliability, it is a poor
(cid:15)
(cid:2)1(cid:2)cc(cid:2)1(cid:4)1(cid:2)AA(cid:2)1(cid:2)1(cid:6) (cid:3)(1(cid:6)h
i
2)
(cid:2)1(cid:6)
(cid:3)u
i
2
(15)
measuretousewhencorrectingforattenuation.Inaddition,many
t V V V oftheconventionalmeasuresdonotreflectthepercentageoftotal
x x x
variancethatisactuallycommontoalloftheitemsinthetest.For
where h i 2 is the item communality and u i 2 is the item uniqueness. factor analytic approaches, this is only done by (cid:3) and (cid:3) ; for
Thepercentageofthetotalvariancethatisduetothegeneralfactor g h
non-model-basedproceduresthisistheworstsplit-halfreliability
((cid:3) g ,McDonald,1999)is ((cid:4)).
(cid:15)
(cid:2)1(cid:2)cc(cid:2)1(cid:2) 1(cid:2)cc(cid:2)1 In order to show how these various approaches can give very
g V 1(cid:2)cc(cid:2)1(cid:4)1(cid:2)AA(cid:2)1(cid:4)1(cid:2)DD(cid:2)1(cid:4)1(cid:2)ee(cid:2)1 different values, we consider a real-life data set consisting of the
X
10 anxiety items discussed in the online supplemental materials.
(cid:2)1(cid:6)
((cid:3)c
i
)2
, (16) We show the correlation matrix as well as different reliability
V x estimates in Table S5 in the online supplemental materials. Even
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
RELIABILITY 1403

## Page 10

thoughthegreatestreliabilityestimatesexceed.90,itisimportant Generalizability Theory
torememberthatthisdoesnotimplyanythingaboutthestability
Mostdiscussionsofreliabilityconsiderreliabilityasthecorre-
ofthemeasure,whichisjust.30after2days.(SeeTableS1inthe
lationofatestwithatestjustlikeit.Test–retestandalternateform
onlinesupplementalmaterials.)
The (cid:3) based value of .88 agrees closely with the greatest reliabilities are the most obvious examples. Internal consistency
t measuresarefunctionallyestimatingthecorrelationofatestwith
split-halfof.89ortheduplicateitemestimateof.92.Theseareall
an imaginary test just like it. These estimates are based upon the
estimatesofthetotalreliablevariance.Theworstspli-half.56and
(cid:3) values of .55 suggest that slightly less than 60% of the test patternsofcorrelationsoftheitemswithinthetest.Analternative
g approachmakesuseofAnalysisofVarianceprocedurestodecom-
reflectsonegeneralfactorofanxiety.Thedifferencebetweenthe
posethetotaltestvarianceintothatduetoindividuals,toitems,to
.9 and the .6 values suggest that roughly 30% of the total test
time,relevantinteractions,andtoresidual(Cronbachetal.,1963;
varianceisduetothepositivelywordedversusnegativelyworded
Gleseretal.,1965;Shavelson,Webb,&Rowley,1989;Vispoelet
group variance. That is, roughly 2/3 of the reliable test variance
al., 2018). We have already discussed this in the context of
represents one construct, and about 1/3 represents something not
sharedwiththetotaltest.Notethatthe(cid:2)of.83doesnotprovide test–retestreliability.Thistechniqueismostfrequentlyappliedto
thequestionofthereliabilityofjudgeswhoaremakingratingsof asmuchinformation.
targets,butthelogiccanbeappliedequallyeasilytoitemanalysis.
Tetrachoric, Polychoric, and Pearson Correlations
Reliability of Raters
Testscoresaretypicallythesumoraverageofasetofindivid-
Consider the case where we are rating numerous subjects with
ual items. Each item is thought to reflect some underlying latent
only a few judges. We might do a small study first to determine
trait. Because the items are not continuous but rather are dichot-
howmuchourjudgesagreewitheachother,anddependingupon
omous or polytomous, the normal Pearson interitem correlation
thisresult,decideuponhowmanyjudgestousegoingforward.As
willbeattenuatedfromwhatwouldbeobservedifitwerepossible
an example, examine the data from five judges (raters) who are
tocorrelatethelatentscoresassociatedwitheachitem.Thelatent
rating the anxiety of 10 subjects (Table S5 in the online supple-
correlation can be estimated using tetrachoric or polychoric cor-
mentalmaterials).Ifratersareexpensive,wemightwanttousethe
relations, which find what a (latent) continuous bivariate normal
ratingsofjustonejudgeratherthanallfive.Inthiscase,wewill
correlationwouldbegiventheobservedpairwisecellfrequencies.
wanttoknowhowratingsofanysinglejudgewillagreewiththose
Theuseofsuchcorrelationsisrecommendedwhenexaminingthe
fromtheotherjudges.Inthiscase,differencesinleniency(thejudges’
structure of a set of items using factor analysis, for a clearer
means)betweenjudgeswillmakeadifferenceintheirjudgments.In
structure will appear and artificial difficulty factors will not be
addition,differentjudgesmightusethescaledifferently,withsome
found. However, the temptation to use tetrachoric or polychoric
havingmorevariancethanothers.Wealsoneedtothinkabouthow
correlationswhenfindingthereliabilityofatestusinganyofthe
wewillusethejudges.Willweusetheirratingsasgiven,willweuse
formulas in Table S5 in the online supplemental materials (e.g.,
theirratingsasdeviationsfromtheirmean,orwillwepoolthejudges?
McNeish, 2018) should be resisted, for this will lead to overesti-
All of these choices lead to different estimates of generalizability.
mates of the amount of variance in the observed test made up of
Shrout and Fleiss (1979) provide a very clear exposition of three
theobserveditems(Revelle&Condon,2018).
different cases and the resulting equations for reliability (see Equa-
tions 17–19 in the online supplemental materials). Although they
Reliability and Test Length
express their treatment in terms of Mean Squares derived from an
With the exception of the worst split-half reliability ((cid:4)) and analysisofvariance(e.g.,theaovfunctioninR),itisequallyeasyto
hierarchical(cid:3)(estimatedeitherbyabifactorapproach,(cid:3) orthe do this with variance components estimated using a mixed effects
g
Schmid-Leiman procedure (cid:3) ) all of the reliability estimates in linearmodel(e.g.,lmerfromthelme4package[Batesetal.,2015]
h
onlineTableS5arefunctionsoftestlengthandwilltendasymp- inR).BothoftheseproceduresareimplementedintheICCfunction
toticallytoward1asthenumberofitemsincreases.Examiningthe inthepsychpackage.Thisisdiscussedinmoredetailintheonline
equations in online Table S5 makes this clear: each method re- supplementalmaterials.
places the diagonal of the test, tr(V ), with the sum of some The intraclass correlation is appropriate when ratings are nu-
x
estimatebasedontheitemreliability(r ii ,h2,theSMC,(cid:2)(cid:2) r2 ij ,orr(cid:2) ij ) m cli e n r i i c c a a l l, d b ia u g t no so si m s e o ti r m i e n s e r v a a t l i u n a g t s in a g re the c m ate e g s o i r n ic s a t l or ( i p e a s r ) t . ic T u h la is rly the i n n
and then compares this adjusted test variance to the total test
leadstomeasuresofagreementofnominalratings.Rediscovered
variance.Butasthenumberofitemsinthetestincreases,theeffect
multiple times and given different names (Conger, 1980; Scott,
ofthediagonalelementsbecomeslessasafractionofthetotaltest
variance.Thus,thelimitoftheglb,(cid:5) ,(cid:3),(cid:5) ,(cid:5) ,(cid:2)asnincreases 1955; Hubert, 1977; Zapf, Castell, Morawietz, & Karch, 2016),
to infinity is 1, (cid:3) does not have this 4 pro t ble 6 m 2 as it will increase perhapsthemoststandardcoefficientisknownasCohen’sKappa
toward the limit o h f (cid:15) (cid:2) 1(cid:2)cc(cid:2)1 (cid:2) 1(cid:2)cc(cid:2)1 . When com- (Cohen,1960,1968),whichadjustsobservedproportionsofagree-
g(cid:17) VX 1(cid:2)cc(cid:2)1(cid:4)1(cid:2)AA(cid:2)1(cid:4)1(cid:2)DD(cid:2)1 mentbytheexpectedproportion:
paringreliabilitiesbetweentestsofdifferentlengths,itisusefulto
include the reliability of each test as if they were just one item p (cid:6)p f (cid:6)f
each. In the case of (cid:2), (cid:11) 1 (cid:2) r(cid:2) ij , Other single item reliability (cid:18)(cid:2) 1 o (cid:6)p e e(cid:2) N o (cid:6)f e e (18)
measuresaretheaverageitemtestretest(glb (cid:2)r(cid:2) ),theaverage
communality ((cid:15) (cid:2) h (cid:2) 2), the average SMC ((cid:16) 1 (cid:2) ii (cid:2) SMC), or the where p (cid:2) f o is the observed proportion (p ) or frequency of
squarerootofth t e 1 aver i agesquaredcorrelation 6 ( 1 (cid:16) 21 (cid:2)(cid:2) i (cid:2) r2 ij ). agreemen o t(f o ) N betweentwoobservers,andp e (cid:2) o N fe istheexpected
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
1404 REVELLEANDCONDON

## Page 11

proportionorfrequencyofagreement(f ;Cohen,1960;seeTable When doing multilevel reliability, it is straightforward to find
e
S7intheonlinesupplementalmaterials).Becauserawagreements thereliabilityofeachindividualsubjectoveritemsandovertime.
willreflectthebaseratesofjudgments,(cid:6)correctsfortheexpected Peoplearenotthesameandtheoverallindicesdonotreflecthow
agreementontheassumptionofindependenceoftheraters.Thus, some subjects show a very different pattern of response. The
if two raters each use one category 60% of the time, we would multilevel.reliability function returns reliability esti-
expectthemtoagreebychance36%ofthetimeintheirpositive mates for each subject over time, as well as the six estimates
judgmentsand16%intheirnegativejudgments.Variousestimates shownintheonlinesupplementalmaterialsfor77subjectsonour
of correlations of nominal data have been proposed and differ 10anxietyitemsacrossfourtimepoints.
primarilyinthetreatmentofthecorrectionforchanceagreement
(Feng, 2015). Thus, (cid:6) adjusts for differences in the marginal Composite Scores
likelihood of judges, while Krippendorf’s (cid:2) does not (Krippen-
k
dorff,1970,2004).ToKrippendorff(2004)thisisastrengthof(cid:2) , The typical use of reliability coefficients is to estimate the
k
buttoFleissitisnot(Krippendorff&Fleiss,1978). reliabilityofrelativelyhomogeneoustests.Indeed,thedistinctions
Ifsomedisagreementsaremoreimportantthanothers,wehave madebetween(cid:3) h ,(cid:2),and(cid:3) t areminimizedifthetestiscompletely
weighted(cid:6),whichwithappropriateweightsisequaltotheintra- homogeneous.Butifthetestisintentionallymadeupofunrelated
classcorrelationbetweentheraters(Cohen,1968;Fleiss&Cohen, orpartlyunrelatedcontent,thenweneedtoconsiderthereliability
1973). For multiple raters, the average (cid:6) is known as Light’s (cid:6) of a composite score. A composite is sometimes referred to as a
(Conger,1980;Light,1971). stratifiedtest,wherethestratamaybedifficultyorcontentbased
Reallifeexamplesofarangeof(cid:6)valuesaregivenbyFreedman (Cronbach,Schönemann,&McKie,1965).Thestratifiedreliabil-
etal.(2013)inadiscussionoftherevisedDiagnosticandStatis- ity((cid:7) xxs )ofacompositetestisfoundbyreplacingthevarianceof
ticalManualofMentalDisorders,wherethe(cid:6)valuesforclinical each subtest in the total test with its reliable variance and then
diagnoses range from very good agreement ((cid:14).60) for major dividingtheresultingsumbythetotaltestvariance:
neurocognitivedisordersorposttraumaticstressdisorder,togood V (cid:6)(cid:3)v (cid:4)(cid:3)p v
(.40–.60) for bipolar II, or schizophrena, to questionable agree- (cid:8) (cid:2) t i xxi i (19)
ment(.2–4)forgeneralizedanxietyorobsessive–compulsivedis-
xxs V
t
order, to values that did not exceed the confidence values of 0. where(cid:7) isreliabilityofthesubtestandv isthevarianceofthe
xxi i
Whencomparingthepresenceorabsenceofeachoffivenarrative subtest(Rae,2007).Conceptually,thisapproachisverysimilarto
themes in a life story interview, Guo, Klevan, and McAdams (cid:3) (McDonald,1999).
t
(2016) report how two independent raters of each of 12 different A procedure for weighting the elements of the composite to
interview segments showed high reliability of judgments with (cid:6) maximizethereliabilityofcompositescoresisdiscussedbyCliff
values ranging from .61 (did the story report early advantage) to and Caruso (1998), who suggest this as a procedure for Reliable
.83(didthestorydiscussprosocialgoals). ComponentsAnalysis(RCA)whichtheyseeasanalternativetoa
EFAorPCA.
Multilevel Reliability
Reliability of a Difference Score
With the introduction of cell phones and various apps, it has
become much easier to collect data within subjects over multiple Logicallysimilartothereliabilityofacompositeisthereliabil-
occasions (e.g., A. S. Green, Rafaeli, Bolger, Shrout, & Reis, ity of a difference score (Equation 20). Sometimes researchers
2006;Bolger&Laurenceau,2013;Mehl&Conner,2012;Wiltet want to find the difference between two scores (e.g., verbal and
al.,2011,2017).Thishastakenusfromthedailydiarytomultiple spatial ability or anxiety and depression). Even though the two
mood measures taken multiple times per day. These techniques tests themselves are highly reliable ((cid:7) xx , (cid:7) yy ), if they also have a
leadtofascinatingdata,inthatwecanexaminepatternsofstability high correlation, (r xy ) the reliability of the difference will be
andchangewithinindividualsovertime.Theseintensivelongitu- substantially lower. Indeed, if the correlation between the two
dinalmethods(Walls&Schafer,2006)“captureslifeasitislived” scalesmatchestheirreliability,thereliabilityofthedifferencewill
(Bolger, Davis, & Rafaeli, 2003). They also lead to important be 0. Given this reduction in reliability, individual differences in
questions about reliability. How consistent is one person over changeorinpatternshouldbeinterpretedcautiously.Wegivean
time? How stable are the differences between people over time? example of this problem when comparing the difference of two
The same decomposition of variance techniques discussed for cognitive tests (i.e., verbal vs. spatial reasoning) in the online
ratersandforgeneralizabilitytheorycanbeappliedtoananalysis supplementalmaterials.
oftemporalpatternsofreliability(Revelle&Wilt,2019;Shrout& (cid:8) (cid:4)(cid:8) (cid:6)2r
Lane, 2012). That is to say, we decompose the responses into (cid:8) x(cid:6)y (cid:2) x 2 x (cid:14)(1 yy (cid:6)r ) xy (20)
variance components due to stable individual differences ((cid:7)2), to xy
p
differences due to time ((cid:7)2), to the interaction of person by time
t Beyond Classical Test Theory
effects ((cid:7)2 p(cid:14)t , and to residual error (cid:7)2 e ). Shrout and Lane (2012)
givetheSPSSandSASsyntaxtodothesecalculations.InRthis Reliability is a joint property of the test and the people being
merelyrequirescallingthemultilevel.reliabilityfunc- measuredbythetest(referbacktoEquation2).Forfixedamount
tioninpsych.Intheinterestofspace,werefertheinterestedreader oferror,reliabilityisafunctionofthevarianceofthepeoplebeing
to Shrout and Lane (2012); Revelle and Wilt (2019); and the assessed.Scoresfromatestofabilitywillbereliableifgiventoa
examplesintheonlinesupplementalmaterials. randomsampleof18–20yearolds,butmuchlessreliableifgiven
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
RELIABILITY 1405

## Page 12

tostudentsataparticularlyselectivecollegebecausetherewillbe Corrections for Attenuation
less between-person variance. The reliability of scores of emo-
Reliability theory was originally developed to adjust observed
tional stability will be higher if given to a mixture of psychiatric
correlations between related constructs for the error of the mea-
patients and their spouses than it will be if given just to the
surement in each construct (Spearman, 1904b). Such corrections
patients. That is, reliability is not a property of test scores inde-
forattenuationwereperhapstheprimarypurposebehindreliability
pendentofthepeopletakingit.ThisisthebasicconceptofItem
and are the reason that some recommend routinely correcting for
ResponseTheory(IRT),calledbysomethe“newpsychometrics”
reliability when doing meta-analyses (Schmidt & Hunter, 1999).
(Embretson, 1996, 1999; Embretson & Reise, 2000), and which
However such a correction is appropriate only if the measure is
models the individual’s patterns of response as a function of
seen as the expected value of a single underlying construct. Ex-
parameters(discrimination,difficulty)oftheitem.
amplesofwhentheexpectedscoreofatestisnotthesameasthe
By focusing on item difficulty (endorsement frequency) it is
theoreticalconstructthataccountsforthecorrelationsbetweenthe
possible to consider the range of application of our scores. Items
observedvariablesincludechickensexing(Lord&Novick,1968)
are most informative if they are equally likely to be passed or
orthediagnosisofAlzheimers(Borsboom&Mellenbergh,2002). failed(endorsedornotendorsed).Butthiscanonlybethecasefor
ModernsoftwareforStructuralEquationModeling(e.g.,Rosseel, a particular person taking the test and cannot be the case for a
2012) models the pattern of observed correlations in terms of a
personwithahigherorlowerlatentscore.Althoughtestscoresare
measurement (reliability) model as well as a structural (validity)
maximally reliable if all of the items are equally difficult, such
model.
scoreswillnotbeverydiscriminatingatanyotherthanatthatlevel
(Loevinger, 1954). Thus, we need to focus on spreading out the
itemsacrosstherangetobemeasured. Reversion to Mediocrity
TheessentialassumptionsofIRTisthatitemscandifferinhow
Givenaparticularobservedscore,whatdoweexpectthatscore
hard they are, as well as how well they measure the latent trait.
tobeifthemeasureisgivenagain?Thathighscoresdecreaseand
Although seemingly quite different from classical approaches,
low scores increase is just a function of the reliability of the test
thereisaone-to-onemappingbetweenthedifficultyanddiscrim-
(Equation 5) with larger drops and gains for extreme scores than
ination parameters of IRT and the factor loadings and item re-
for moderate scores. Although expected, these regression effects
sponse thresholds found by factor analysis of the polychoric cor-
can mislead those who do not understand reliability and lead to
relations of the items (Kamata & Bauer, 2008; Markon, 2013;
surprise when successful baseball players are less successful the
McDonald, 1999). The relationship of the IRT approach to clas-
nextyear(Schall&Smith,2000)orwhenpoorlyperformingpilots
sicalreliabilitytheoryisgivenaveryclearexplicationbyMarkon
improve but better performing pilots get worse (Kahneman &
(2013),whoexamineshowtestinformation(andthusthereliabil-
Tversky, 1973). That superior performance is partly due to good
ity)variesbysubjectvarianceaswellastraitlevel.Atestcanbe
luck is hard for high performers to accept and that poor perfor-
developedtobereliableforcertaindiscriminations(e.g.,between
manceispartlyduetobadluckleadstofalsebeliefsaboutthelack
psychiatric patients) and less reliable for discriminating between
ofeffectforrewardsandthestrongeffectofpunishment(Kahne-
members of a control group. The particular strength of IRT ap-
man&Tversky,1973).
proachesistheuseintailoredoradaptivetestingwherethefocus
is on the reliability for a particular person at a particular level of
the latent trait. (See the discussion of IRT in the online supple- Confidence Intervals, Expected Scores, and the
mental materials, particularly Figure S3, which shows how reli- Standard Error
abilitydiffersasafunctionoflatentscore).
Notonlydoesreliabilityaffecttheregressiontowardthemean,
italsoaffectstheprecisionofmeasurement.Thestandarderrorof
The Several Uses of Reliability
measurement is a function of sample variability as well as the
Reliability is measured for at least three different purposes: reliability (Equation 4). Confidence intervals for expected scores
correctingforattenuation,estimatingexpectedscores,andprovid- aresymmetricaroundtheexpectedscore(Equation5),andthere-
ingconfidenceintervalsaroundtheseestimates.Whencomparing fore are not symmetric around the observed score. Combining
test reliabilities, it is useful to remember that reliability has non- these two equations and taking into account the variance of the
linearrelationswiththestandarderroraswellaswiththesignal/ expectedscoreweseethattheconfidenceintervalforanexpected
noise ratio (Cronbach et al., 1965). That is, seemingly small scorebaseduponanobservedscore,X,withasamplevarianceof
differencesinreliabilitybetweentestscanreflectlargedifferences Vx,meanofX¯ (andthusdeviationscore,xandestimatedreliability
intheratioofreliablesignaltounreliablenoiseorthesizeofthe of(cid:7) is
xx
standarderrorofmeasurement.Considerthesignal-to-noiseratio
oftestswithreliabilityof.7,.8,.9,and.95. (cid:8) xx (x)(cid:6)(cid:2)(cid:8) xx V x (1(cid:6)(cid:8) xx )(cid:19)(cid:8) xx (x)(cid:19)(cid:8) xx (x)(cid:4)(cid:2)(cid:8) xx V x (1(cid:6)(cid:8) xx ).
(21)
Signal (cid:8)
Noise (cid:2) 1(cid:6) xx (cid:8) .
xx
Thus an improvement in reliability from .7 (cid:4).7 (cid:2) 2.33 (cid:5) to .8 Estimating and Reporting Reliability
(cid:4).8(cid:2)4 (cid:5)
isamuchsmallerchangeinsignaltonoi
.
s
3
ethanthatfrom Wehaveincludedmanyequationsandreferredtomanyseparate
.8 .2 to .9 (cid:4).9 (cid:2) 9 (cid:5) which in turn is much less than from .9 to .95 R functions. What follows is a brief summary with an accompa-
(cid:4).95 (cid:2)19 .1(cid:5) . nyingflowchartthatwepresentedearlier(seeTable2).
.05
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
1406 REVELLEANDCONDON

## Page 13

Table2
StepsTowardReliabilityAnalysis:ChoosingtheAppropriateRFunctiontoFindReliability
Steps Statistic Rfunction
Preliminaries
Hypothesisdevelopment
Datacollection
Datainput read.file
Datascreening
Descriptivestatistics (cid:18),(cid:12),range describe
Analysisofinternalstructure
Exploratoryfactoranalysis R(cid:3)F(cid:19)F=(cid:4)U2 fa
Hierarchicalstructure (cid:3),(cid:3) omega, omegaSem
h t
Confirmatoryfactoranalysis lavaan::cfa
Estimationofvariousreliabilities
Items(dichotomous,polytomousorcontinuous)
Oneoccasion
Generalfactorsaturation (cid:3) omega
h
Totalcommonvariance (cid:3) omega
t
Averageinteritemr r(cid:2) omega, alpha
ij
Medianinteritemr omega, alpha
Meantestretest(tauequivalent) (cid:2),(cid:5) omega, alpha
3
Smallestsplithalfreliability (cid:4) splitHalf, iclust
Greatestsplithalfreliability (cid:5) splitHalf, guttman
4
Twooccasions
Test–retestcorrelation r cor
Variancecomponents (cid:12)2,(cid:12)2,(cid:12)2 testRetest
p i t
Multipleoccasions
Withinsubjectreliability (cid:2) multilevel.reliability
Variancecomponents (cid:12)2,(cid:12)2,(cid:12)2 multilevel.reliability
p i t
Ratings(Ordinalorinterval)
Singleraterreliability ICC 1 ICC
1..3
Multipleraterreliability ICC k ICC
1..3
Ratings(Categorical)
Tworaters (cid:6) cohen.kappa
Note. Allfunctionsexceptforthecfaandcorfunctionareinthepsychpackage.
Preliminary Steps examining the structure of the correlations should be done to
confirmthefactorstructureisasexpected.Aunidimensionalscale
The most important question to ask should be done before
would be expected to have just one large factor. More typical
collectingthedata:whatarewetryingtomeasureandhowarewe
scales will probably have some subgroups that can be explored
tryingtomeasureit?Doesthemeasuretobeanalyzedrepresenta
usinghierarchicalorbifactormodels.Ifthedataaredichotomous
single construct or is the factor structure more complicated? The
orpolytomous,usingthelatentvariablecorrelationsestimatedby
nextquestionis:whoarethesubjectsofinterest?Thereliabilityof
tetrachoricorpolychoriccorrelationswillshowthestructuremore
testscoresisnotapropertyofthetest,butajointfunctionofthe
clearly. However, when estimating the reliability of the resulting
people taking the test and of the test itself. Thus specifying the
scores,thestatisticsshouldbebaseduponthePearsoncorrelations.
latent construct and the population of interest is essential before
collectingandanalyzingdata.
Once one has decided what to measure, the test items must be Which Reliability to Estimate
giventowilling(andonecanhopeinterested)participants.Steps
Aswehavediscussedbefore,thereisnoonereliabilityestimate.If
should be taken to ensure participant involvement. Measures to
giving just one test on one occasion we need to rely on internal
take include the classic issues of data screening. Subjects who
consistency measures: (cid:3) , (cid:4) and the worst split-half reliability are
respond too rapidly or carelessly will not provide reliable infor- h
estimatesoftheamountofgeneralfactorvarianceinthetestscores.
mation (Wood et al., 2017). If response times are available, it is
Simulationssuggestthatforverylowlevelsofgeneralfactorsatura-
possible to screen for implausibly fast responses. If items are
tionthattheEFAbased(cid:3) ispositivelybiasedandthataCFAbased
repeated in the same session, it is also possible to screen for h
estimate((cid:3) )ismoreaccurate.(cid:3) isamodelbasedestimateofthe
temporalconsistency(DeSimone,2015;Woodetal.,2017). g t
GreatestLowerBoundofthetotalreliabilityofatestasisthebest
split-halfreliability((cid:5) ).Iftheitemsarerepeatedwithinoneform,the
Type of Measurement and Tests for Unidimensionality 4
glbcanbefoundbasedupontheitemtest–retestvalues.
Isthetestgivenmorethanonce?Isitgivenmanytimes?Arethe Iftestsaregiventwice,thentest–retestmeasuresdependability
data based upon item responses or ratings? Are the data categor- over the short term or stability over a longer term. Variance
ical,dichotomous,polytomous,orcontinuous?Forthelatterthree, decomposition techniques can be used to estimate how much
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
RELIABILITY 1407

## Page 14

variance is due to individuals, to the items, and to changes over awareness of what generalizations one wants to make is required
time. beforechoosingbetweenthesixpossibleindices.
If tests are given many times, then multiple measures of reli-
ability are relevant, each implying a different generalization: is
References
timetreatedasfixedorrandomeffect,areitemsseenasfixedor
random.Apowerfuladditiontothisdesignisthatreliabilityover Anastasi,A.(1967).Psychology,psychologistsandpsychologicaltesting.
time can be found for each subject as well as all of the subjects. AmericanPsychologist,22,297–306.
The scores of some subjects may be much more reliable than Anderson,K.J.,&Revelle,W.(1983).Theinteractiveeffectsofcaffeine,
others. impulsivityandtaskdemandsonavisualsearchtask.Personalityand
Ifthemeasuresarenotitems,butratherraters,andwewantto Individual Differences, 4, 127–134. http://dx.doi.org/10.1016/0191-
8869(83)90011-9
knowthelimitsofgeneralizabilityoftheraterstodifferentraters,
Anderson,K.J.,&Revelle,W.(1994).Impulsivityandtimeofday:Israte
orforpooledraters,wecanfindestimatesoftheintraclasscorre-
ofchangeinarousalafunctionofimpulsivity?JournalofPersonality
lations. There are several of these; all can be estimated the same
and Social Psychology, 67, 334–344. http://dx.doi.org/10.1037/0022-
way.
3514.67.2.334
Thesemanyformsofreliabilitycoefficients(seeTable2)may Baltes,P.B.(1987).Theoreticalpropositionsoflife-spandevelopmental
all be found in the psych package (Revelle, 2019a) for the open psychology: On the dynamics between growth and decline. Develop-
sourcestatisticsenvironment,R(RCoreTeam,2019).psychwas mental Psychology, 23, 611–626. http://dx.doi.org/10.1037/0012-1649
specially developed for personality-oriented psychologists to be .23.5.611
both thorough and easy to use. Although some of these statistics Bates,D.,Maechler,M.,Bolker,B.,&Walker,S.(2015).Fittinglinear
mixed-effects models using lme4. Journal of Statistical Software, 67,
areavailableincommercialsoftwarepackages,thepsychpackage
1–48.http://dx.doi.org/10.18637/jss.v067.i01
provides them all in one integrated set of functions. See Rstudio
Bentler, P. M. (2009). Alpha, dimension-free, and model-based internal
(RStudio Team, 2016) for a convenient interface. We show the
consistencyreliability.Psychometrika,74,137–143.http://dx.doi.org/10
specific commands to use to find all of these coefficients in the
.1007/s11336-008-9100-1
onlinesupplementmaterialstothisarticle. Bentler, P. M. (2017). Specificity-enhanced reliability coefficients. Psy-
chological Methods, 22, 527–540. http://dx.doi.org/10.1037/
met0000092
Conclusions Bolger,N.,Davis,A.,&Rafaeli,E.(2003).Diarymethods:Capturinglife
asitislived.AnnualReviewofPsychology,54,579–616.http://dx.doi
Althoughwehaveusedmanyequationstodiscussitandmany
.org/10.1146/annurev.psych.54.101601.145030
ways to estimate it, at its essence, reliability is a very simple
Bolger,N.,&Laurenceau,J.(2013).Intensivelongitudinalmethods.New
concept: Reliability is a property of the test scores and is the York,NY:GuilfordPress.
correlation of a test with a test just like it, or alternatively, the Borsboom,D.,&Mellenbergh,G.J.(2002).Truescores,latentvariables
fraction of the test score variance which is not due to error. and constructs: A comment on Schmidt and Hunter. Intelligence, 30,
Unfortunately, there is not just one reliability that needs to be 505–514.http://dx.doi.org/10.1016/S0160-2896(02)00082-X
reported,butratheravarietyofcoefficients,eachofwhichismost Boyle, G. J., Stankov, L., & Cattell, R. B. (1995). Measurement and
statisticalmodelsinthestudyofpersonalityandintelligence.InD.H.
appropriateforcertainpurposes.Arewetryingtogeneralizeover
Saklofske&M.Zeidner(Eds.),Internationalhandbookofpersonality
items, over time, over raters? Are we estimating unidimensional-
andintelligence(pp.417–446).Boston,MA:Springer.http://dx.doi.org/
ity, general factor saturation, or total reliable variance? Each of
10.1007/978-1-4757-5571-8_20
thesequestionsleadstoadifferentestimate(seeTable2).Sorather
Brown,W.(1910).Someexperimentalresultsinthecorrelationofmental
thanask,Whatisthereliability?,weshouldask,Whichreliability abilities. British Journal of Psychology, 3, 296–322. http://dx.doi.org/
andreliabilityforwhat? 10.1111/j.2044-8295.1910.tb00207.x
The initial appeal of (cid:2) or KR20 reliability estimates were that Cattell,R.B.(1946).Personalitystructureandmeasurement.I.Theoper-
theyweresimpletocalculateintheprecomputerera.Butthishas ationaldeterminationoftraitunities.BritishJournalofPsychology,36,
notbeenthecaseforthepast60years.Thecontinuedoveruseof 88–102.http://dx.doi.org/10.1111/j.2044-8295.1946.tb01110.x
(cid:2)isprobablyduetotheeaseofcalculationincommoncommercial Cattell,R.B.(1964).Validityandreliability:Aproposedmorebasicsetof
concepts. Journal of Educational Psychology, 55, 1–22. http://dx.doi
software.Butwithmodern,opensourcesoftwaresuchasR,thisis
.org/10.1037/h0046462
no longer necessary. Alpha, (cid:3) , (cid:3), minimum ((cid:4)) and maximum
h t Cattell,R.B.(Ed.).(1966a).Thedatabox:Itsorderingoftotalresources
((cid:5) )splithalfs,sixICCs,andsixrepeatedmeasurereliabilitiesare
4 in terms of possible relational systems. Handbook of multivariate ex-
all available with one or two simple commands. (See the online perimentalpsychology(pp.67–128).Chicago,IL:Rand-McNally.
supplemental materials for a guided tour.) It should no longer be Cattell,R.B.(Ed.).(1966b).Patternsofchange:Measurementinrelation
acceptabletoreportonecoefficientthatisonlycorrectifallitems to state dimension, trait change, lability, and process concepts. Hand-
are exactly equally good measures of a construct. Readers are bookofmultivariateexperimentalpsychology(pp.355–402).Chicago,
encouragedtoreportatleasttwocoefficients(e.g.,(cid:3) and(cid:3))and IL:Rand-McNally.
h t Cattell, R. B., & Tsujioka, B. (1964). The importance of factor-trueness
thendiscusswhyeachisappropriatefortheinferencethatisbeing
made.Theyarediscouragedfromreportingjust(cid:2)unlesstheycan andvalidity,versushomogeneityandorthogonality,intestscales.Ed-
ucationalandPsychologicalMeasurement,24,3–30.http://dx.doi.org/
justifytheassumptionsimplicitinusingit(i.e.,(cid:13)equivalenceand
10.1177/001316446402400101
unidimensionality). When reporting the reliability of raters, it is
Charter,R.A.,&Feldt,L.S.(2001).Confidenceintervalsfortruescores:
useful to report all six ICCs and then explain why one is most Isthereacorrectapproach?JournalofPsychoeducationalAssessment,
appropriate. Similarly, when reporting multilevel reliabilities, an 19,350–364.http://dx.doi.org/10.1177/073428290101900404
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
1408 REVELLEANDCONDON

## Page 15

Chmielewski,M.,&Watson,D.(2009).Whatisbeingassessedandwhy Eysenck,H.J.,&Eysenck,S.B.G.(1964).EysenckPersonalityInventory.
it matters: The impact of transient error on trait research. Journal of SanDiego,CA:EdITS.
Personality and Social Psychology, 97, 186–202. http://dx.doi.org/10 Feldt, L. S., & Brennan, R. L. (1989). Reliability. In R. L. Linn (Ed.),
.1037/a0015618 Educational measurement (3rd ed., pp. 105–146). New York, NY:
Cliff, N., & Caruso, J. C. (1998). Reliable component analysis through Macmillan.
maximizingcompositereliability.PsychologicalMethods,3,291–308. Feldt,L.S.,Woodruff,D.J.,&Salih,F.A.(1987).Statisticalinferencefor
http://dx.doi.org/10.1037/1082-989X.3.3.291 coefficient alpha. Applied Psychological Measurement, 11, 93–103.
Cohen,J.(1960).Acoefficientofagreementfornominalscales.Educa- http://dx.doi.org/10.1177/014662168701100107
tionalandPsychologicalMeasurement,20,37–46.http://dx.doi.org/10 Feng,G.C.(2015).Mistakesandhowtoavoidmistakesinusingintercoder
.1177/001316446002000104 reliability indices. Methodology, 11, 13–22. http://dx.doi.org/10.1027/
Cohen,J.(1968).Weightedkappa:Nominalscaleagreementprovisionfor 1614-2241/a000086
scaleddisagreementorpartialcredit.PsychologicalBulletin,70,213– Fisher, A. J. (2015). Toward a dynamic model of psychological assess-
220.http://dx.doi.org/10.1037/h0026256 ment: Implications for personalized care. Journal of Consulting and
Cole, D. A., Martin, N. C., & Steiger, J. H. (2005). Empirical and Clinical Psychology, 83, 825–836. http://dx.doi.org/10.1037/
conceptualproblemswithlongitudinaltrait-statemodels:Introducinga ccp0000026
trait-state-occasion model. Psychological Methods, 10, 3–20. http://dx Fleiss,J.L.,&Cohen,J.(1973).Theequivalenceofweightedkappaand
.doi.org/10.1037/1082-989X.10.1.3 theintraclasscorrelationcoefficientasmeasuresofreliability.Educa-
Condon,D.M.,&Revelle,W.(2014).TheInternationalCognitiveAbility tionalandPsychologicalMeasurement,33,613–619.http://dx.doi.org/
Resource:Developmentandinitialvalidationofapublic-domainmea-
10.1177/001316447303300309
sure. Intelligence, 43, 52–64. http://dx.doi.org/10.1016/j.intell.2014.01
Fox,J.(2016).Appliedregressionanalysisandgeneralizedlinearmodels
.004
(3rded.).ThousandOaks,CA:Sage.
Conger,A.J.(1980).Integrationandgeneralizationofkappasformultiple
Freedman, R., Lewis, D. A., Michels, R., Pine, D. S., Schultz, S. K.,
raters. Psychological Bulletin, 88, 322–328. http://dx.doi.org/10.1037/
Tamminga,C.A.,...Yager,J.(2013).TheinitialfieldtrialsofDSM–5:
0033-2909.88.2.322
Newbloomsandoldthorns.AmericanJournalofPsychiatry,170,1–5.
Cranford,J.A.,Shrout,P.E.,Iida,M.,Rafaeli,E.,Yip,T.,&Bolger,N.
http://dx.doi.org/10.1176/appi.ajp.2012.12091189
(2006).Aprocedureforevaluatingsensitivitytowithin-personchange:
Glass,G.V.(1986).Testingold,testingnew:Schoolboypsychologyand
Canmoodmeasuresindiarystudiesdetectchangereliably?Personality
theallocationofintellectualresources.InB.S.Plake&J.C.Witt(Eds.),
andSocialPsychologyBulletin,32,917–929.http://dx.doi.org/10.1177/
Thefutureoftesting(pp.9–27).Hillsdale,NJ:Erlbaum.
0146167206287721
Gleser,G.C.,Cronbach,L.J.,&Rajaratnam,N.(1965).Generalizability
Cronbach,L.J.(1951).Coefficientalphaandtheinternalstructureoftests.
ofscoresinfluencedbymultiplesourcesofvariance.Psychometrika,30,
Psychometrika,16,297–334.http://dx.doi.org/10.1007/BF02310555
395–418.http://dx.doi.org/10.1007/BF02289531
Cronbach, L. J., Rajaratnam, N., & Gleser, G. C. (1963). Theory of
Green,A.S.,Rafaeli,E.,Bolger,N.,Shrout,P.E.,&Reis,H.T.(2006).
generalizability:Aliberalizationofreliabilitytheory.BritishJournalof
Paper or plastic? Data equivalence in paper and electronic diaries.
Statistical Psychology, 41, 137–163. http://dx.doi.org/10.1111/j.2044-
Psychological Methods, 11, 87–105. http://dx.doi.org/10.1037/1082-
8317.1963.tb00206.x
989X.11.1.87
Cronbach,L.J.,Schönemann,P.,&McKie,D.(1965).Alphacoefficients
Green, S., & Yang, Y. (2009). Commentary on coefficient alpha: A
for stratified-parallel tests. Educational and Psychological Measure-
cautionarytale.Psychometrika,74,121–135.http://dx.doi.org/10.1007/
ment,25,291–312.http://dx.doi.org/10.1177/001316446502500201
s11336-008-9098-4
Cronbach, L. J., & Shavelson, R. J. (2004). My current thoughts on
Guo, J., Klevan, M., & McAdams, D. P. (2016). Personality traits, ego
coefficientalphaandsuccessorprocedures.EducationalandPsycholog-
development,andtheredemptiveself.PersonalityandSocialPsychol-
ical Measurement, 64, 391–418. http://dx.doi.org/10.1177/00131644
ogy Bulletin, 42, 1551–1563. http://dx.doi.org/10.1177/0146167216
04266386
665093
Damian,R.I.,Spengler,M.,Sutu,A.,&Roberts,B.W.(2018).Sixteen
Guttman, L. (1945). A basis for analyzing test–retest reliability. Psy-
going on sixty-six: A longitudinal study of personality stability and
chometrika,10,255–282.http://dx.doi.org/10.1007/BF02288892
changeacross50years.JournalofPersonalityandSocialPsychology.
Advanceonlinepublication.http://dx.doi.org/10.1037/pspp0000210 Hamaker,E.L.,Schuurman,N.K.,&Zijlmans,E.A.O.(2017).Usinga
Deary,I.J.,Whiteman,M.,Starr,J.,Whalley,L.,&Fox,H.(2004).The few snapshots to distinguish mountains from waves: Weak factorial
impactofchildhoodintelligenceonlaterlife:FollowinguptheScottish invarianceinthecontextoftrait–stateresearch.MultivariateBehavioral
mental surveys of 1932 and 1947. Journal of Personality and Social Research, 52, 47–60. http://dx.doi.org/10.1080/00273171.2016
Psychology, 86, 130–147. http://dx.doi.org/10.1037/0022-3514.86.1 .1251299
.130 Holzinger, K., & Swineford, F. (1937). The bifactor method. Psy-
DeSimone,J.A.(2015).Newtechniquesforevaluatingtemporalconsis- chometrika,2,41–54.http://dx.doi.org/10.1007/BF02287965
tency. Organizational Research Methods, 18, 133–152. http://dx.doi Hoyt, C. (1941). Test reliability estimated by analysis of variance. Psy-
.org/10.1177/1094428114553061 chometrika,6,153–160.http://dx.doi.org/10.1007/BF02289270
Duhachek,A.,&Iacobucci,D.(2004).Alpha’sstandarderror(ase):An Hubert,L.(1977).Kapparevisited.PsychologicalBulletin,84,289–297.
accurate and precise confidence interval estimate. Journal of Applied http://dx.doi.org/10.1037/0033-2909.84.2.289
Psychology,89,792–808. Humphreys, M. S., & Revelle, W. (1984). Personality, motivation, and
Embretson, S. E. (1996). The new rules of measurement. Psychological performance:Atheoryoftherelationshipbetweenindividualdifferences
Assessment,8,341–349.http://dx.doi.org/10.1037/1040-3590.8.4.341 andinformationprocessing.PsychologicalReview,91,153–184.http://
Embretson, S. E. (1999). Generating items during testing: Psychometric dx.doi.org/10.1037/0033-295X.91.2.153
issues and models. Psychometrika, 64, 407–433. http://dx.doi.org/10 Kahneman, D., & Tversky, A. (1973). On the psychology of prediction.
.1007/BF02294564 PsychologicalReview,80,237–251.http://dx.doi.org/10.1037/h0034747
Embretson,S.E.,&Reise,S.P.(2000).Itemresponsetheoryforpsychol- Kamata,A.,&Bauer,D.J.(2008).Anoteontherelationbetweenfactor
ogists.Mahwah,NJ:Erlbaum. analyticanditemresponsetheorymodels.StructuralEquationModel-
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
RELIABILITY 1409

## Page 16

ing: A Multidisciplinary Journal, 15, 136–153. http://dx.doi.org/10 search, 51, 396–412. http://dx.doi.org/10.1080/00273171.2015
.1080/10705510701758406 .1050481
Kenny,D.A.,&Zautra,A.(1995).Thetrait-state-errormodelformulti- Rae,G.(2007).Anoteonusingstratifiedalphatoestimatethecomposite
wavedata.JournalofConsultingandClinicalPsychology,63,52–59. reliability of a test composed of interrelated nonhomogeneous items.
http://dx.doi.org/10.1037/0022-006X.63.1.52 Psychological Methods, 12, 177–184. http://dx.doi.org/10.1037/1082-
Klein,S.B.,Cosmides,L.,Tooby,J.,&Chance,S.(2002).Decisionsand 989X.12.2.177
theevolutionofmemory:Multiplesystems,multiplefunctions.Psycho- Rafaeli,E.,&Revelle,W.(2006).Aprematureconsensus:Arehappiness
logical Review, 109, 306–329. http://dx.doi.org/10.1037/0033-295X andsadnesstrulyoppositeaffects?MotivationandEmotion,30,1–12.
.109.2.306 http://dx.doi.org/10.1007/s11031-006-9004-2
Krippendorff,K.(1970).Bivariateagreementcoefficientsforreliabilityof Rafaeli, E., Rogers, G. M., & Revelle, W. (2007). Affective synchrony:
data.SociologicalMethodology,2,139–150.http://dx.doi.org/10.2307/ Individualdifferencesinmixedemotions.PersonalityandSocialPsy-
270787 chology Bulletin, 33, 915–932. http://dx.doi.org/10.1177/014616720
Krippendorff,K.(2004).Reliabilityincontentanalysis.HumanCommu- 7301009
nicationResearch,30,411–433.http://dx.doi.org/10.1111/j.1468-2958 Rasch,G.(1966).Anitemanalysiswhichtakesindividualdifferencesinto
.2004.tb00738.x account.BritishJournalofMathematicalandStatisticalPsychology,19,
Krippendorff,K.,&Fleiss,J.L.(1978).Reliabilityofbinaryattributedata. 49–57.http://dx.doi.org/10.1111/j.2044-8317.1966.tb00354.x
Biometrics,34,142–144. R Core Team. (2019). R: A language and environment for statistical
Kuder,G.,&Richardson,M.(1937).Thetheoryoftheestimationoftest computing [Computer software]. Vienna, Austria: R Foundation for
reliability. Psychometrika, 2, 151–160. http://dx.doi.org/10.1007/ StatisticalComputing.Retrievedfromhttps://www.R-project.org/
BF02288391
Reise, S. P. (2012). The rediscovery of bifactor measurement models.
Larsen, R. J., & Diener, E. (1992). Promises and problems with the
Multivariate Behavioral Research, 47, 667–696. http://dx.doi.org/10
circumplex model of emotion. In M. S. Clark (Ed.), Emotion (pp.
.1080/00273171.2012.715555
25–59).ThousandOaks,CA:Sage.
Reise, S. P., & Waller, N. G. (2009). Item response theory and clinical
Leon, M. R., & Revelle, W. (1985). Effects of anxiety on analogical
measurement.AnnualReviewofClinicalPsychology,5,27–48.
reasoning:Atestofthreetheoreticalmodels.JournalofPersonalityand
Revelle,W.(1979).Hierarchicalcluster-analysisandtheinternalstructure
Social Psychology, 49, 1302–1315. http://dx.doi.org/10.1037//0022-
oftests.MultivariateBehavioralResearch,14,57–74.http://dx.doi.org/
3514.49.5.1302
10.1207/s15327906mbr1401_4
Light,R.J.(1971).Measuresofresponseagreementforqualitativedata:
Revelle,W.(2019a).psych:Proceduresforpersonalityandpsychological
Somegeneralizationsandalternatives.PsychologicalBulletin,76,365–
research (Version 1.9.6) [Computer software]. Retrieved from https://
377.http://dx.doi.org/10.1037/h0031643
CRAN.R-project.org/package(cid:10)psych
Loe,B.S.,&Rust,J.(2017).Theperceptualmazetestrevisited:Evalu-
Revelle,W.(2019b).psychtools:Toolstoaccompanythepsychpackage
atingthedifficultyofautomaticallygeneratedmazes.Assessment.Ad-
for psychological research (Version 1.9.6) [Computer software]. Re-
vanceonlinepublication.http://dx.doi.org/10.1177/1073191117746501
trievedfromhttps://CRAN.R-project.org/package(cid:10)psychTools
Loevinger,J.(1954).Theattenuationparadoxintesttheory.Psychological
Revelle,W.,&Anderson,K.J.(1998).Personality,motivationandcog-
Bulletin,51,493–504.http://dx.doi.org/10.1037/h0058543
nitive performance: Final report to the Army Research Institute on
Lord, F. M. (1955). Estimating test reliability. Educational and Psycho-
contractMDA903–93-K-0008(Tech.Rep.).Evanston,IL:Northwest-
logical Measurement, 15, 325–336. http://dx.doi.org/10.1177/
ernUniversity.
001316445501500401
Revelle,W.,&Condon,D.M.(2018).Reliability.InP.Irwing,T.Booth,
Lord, F. M., & Novick, M. R. (1968). Statistical theories of mental test
&D.J.Hughes(Eds.),TheWileyhandbookofpsychometrictesting:A
scores.Reading,MA:AddisonWesley.
multidisciplinaryreferenceonsurvey,scaleandtestdevelopment(pp.
Lumsden,J.(1976).Testtheory.AnnualReviewofPsychology,27,251–
709–749).London,UK:JohnWily&Sons.
280.http://dx.doi.org/10.1146/annurev.ps.27.020176.001343
Revelle,W.,Condon,D.M.,Wilt,J.,French,J.A.,Brown,A.,&Elleman,
Markon, K. E. (2013). Information utility: Quantifying the total psycho-
L. G. (2016). Web and phone based data collection using planned
metricinformationprovidedbyameasure.PsychologicalMethods,18,
missingdesigns.InN.G.Fielding,R.M.Lee,&G.Blank(Eds.),SAGE
15–35.http://dx.doi.org/10.1037/a0030638
McDonald,R.P.(1999).Testtheory:Aunifiedtreatment.Mahwah,NJ: handbookofonlineresearchmethods(2nded.,pp.578–595).Thousand
Erlbaum. Oaks,CA:Sage.
McNeish, D. (2018). Thanks coefficient alpha, we’ll take it from here. Revelle,W.,Humphreys,M.S.,Simon,L.,&Gilliland,K.(1980).Inter-
Psychological Methods, 23, 412–433. http://dx.doi.org/10.1037/ active effect of personality, time of day, and caffeine: A test of the
met0000144 arousalmodel.JournalofExperimentalPsychologyGeneral,109,1–31.
McNemar, Q. (1946). Opinion-attitude methodology. Psychological Bul- http://dx.doi.org/10.1037/0096-3445.109.1.1
letin,43,289–374.http://dx.doi.org/10.1037/h0060985 Revelle,W.,&Wilt,J.(2013).Thegeneralfactorofpersonality:Ageneral
Mehl,M.R.,&Conner,T.S.(2012).Handbookofresearchmethodsfor critique.JournalofResearchinPersonality,47,493–504.http://dx.doi
studyingdailylife.NewYork,NY:GuilfordPress. .org/10.1016/j.jrp.2013.04.012
Mehl,M.R.,&Robbins,M.L.(2012).Naturalisticobservationsampling: Revelle,W.,&Wilt,J.(2016).Thedataboxandwithinsubjectanalyses:
The electronically activated recorder (ear). In M. R. Mehl & T. S. A comment on Nesselroade and Molenaar. Multivariate Behavioral
Conner(Eds.),Handbookofresearchmethodsforstudyingdailylife(pp. Research, 51, 419–421. http://dx.doi.org/10.1080/00273171.2015
176–192).NewYork,NY:GuilfordPress. .1086955
Mellenbergh,G.J.(1996).Measurementprecisionintestscoreanditem Revelle, W., & Wilt, J. A. (2019). Analyzing dynamic data: A tutorial.
responsemodels.PsychologicalMethods,1,293–299.http://dx.doi.org/ PersonalityandIndividualDifferences,136,38–51.http://dx.doi.org/10
10.1037/1082-989X.1.3.293 .1016/j.paid.2017.08.020
Nesselroade,J.R.,&Molenaar,P.C.M.(2016).Somebehavioralscience Revelle, W., Wilt, J., & Rosenthal, A. (2010). Individual differences in
measurement concerns and proposals. Multivariate Behavioral Re- cognition:Newmethodsforexaminingthepersonality–cognitionlink.
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
1410 REVELLEANDCONDON

## Page 17

In A. Gruszka, G. Matthews, & B. Szymura (Eds.), Handbook of Spearman, C. (1910). Correlation calculated from faulty data. British
individual differences in cognition: Attention, memory and executive Journal of Psychology, 3, 271–295. http://dx.doi.org/10.1111/j.2044-
control(pp.27–49).NewYork,NY:Springer. 8295.1910.tb00206.x
Revelle,W.,&Zinbarg,R.E.(2009).Coefficientsalpha,beta,omegaand Spielberger,C.D.,Gorsuch,R.L.,&Lushene,R.E.(1970).Manualfor
the glb: Comments on Sijtsma. Psychometrika, 74, 145–154. http://dx theState-TraitAnxietyInventory.PaloAlto,CA:ConsultingPsycholo-
.doi.org/10.1007/s11336-008-9102-z gistsPress.
Rocklin,T.,&Revelle,W.(1981).Themeasurementofextraversion:A Teo, T., & Fan, X. (2013). Coefficient alpha and beyond: Issues and
comparison of the Eysenck Personality Inventory and the Eysenck alternatives for educational research. The Asia-Pacific Education Re-
Personality Questionnaire. British Journal of Social Psychology, 20, searcher,22,209–213.http://dx.doi.org/10.1007/s40299-013-0075-z
279–284.http://dx.doi.org/10.1111/j.2044-8309.1981.tb00498.x Thayer,R.E.(1978).Towardapsychologicaltheoryofmultidimensional
Rodriguez,A.,Reise,S.P.,&Haviland,M.G.(2016).Evaluatingbifactor activation(arousal).MotivationandEmotion,2,1–34.http://dx.doi.org/
models: Calculating and interpreting statistical indices. Psychological 10.1007/BF00992729
Methods,21,137–150.http://dx.doi.org/10.1037/met0000045 Thayer,R.E.(1989).Thebiopsychologyofmoodandarousal.NewYork,
Rosseel,Y.(2012).lavaan:AnRpackageforstructuralequationmodeling. NY:OxfordUniversityPress.
JournalofStatisticalSoftware,48,1–36.http://dx.doi.org/10.18637/jss Vispoel, W. P., Morris, C. A., & Kilinc, M. (2018). Applications of
.v048.i02 generalizability theory and their relations to classical test theory and
RStudioTeam.(2016).Rstudio:IntegrateddevelopmentenvironmentforR structuralequationmodeling.PsychologicalMethods,23,1–26.http://
[Computersoftware].Boston,MA:Author.Retrievedfromhttp://www dx.doi.org/10.1037/met0000107
.rstudio.com/ Walls, T. A., & Schafer, J. L. (2006). Models for intensive longitudinal
Sackett, P. R., & Yang, H. (2000). Correction for range restriction: An data.NewYork,NY:OxfordUniversityPress.
expandedtypology.JournalofAppliedPsychology,85,112–118.http:// Watson,D.,Clark,L.A.,&Tellegen,A.(1988).Developmentandvali-
dx.doi.org/10.1037/0021-9010.85.1.112 dation of brief measures of positive and negative affect: The PANAS
Schall, T., & Smith, G. (2000). Do baseball players regress toward the Scales.JournalofPersonalityandSocialPsychology,54,1063–1070.
mean? The American Statistician, 54, 231–235. http://dx.doi.org/10 http://dx.doi.org/10.1037/0022-3514.54.6.1063
.1080/00031305.2000.10474553 Wilt,J.,Bleidorn,W.,&Revelle,W.(2016).Findingalifeworthliving:
Schmid,J.J.,&Leiman,J.M.(1957).Thedevelopmentofhierarchical Meaning in life and graduation from college. European Journal of
factor solutions. Psychometrika, 22, 83–90. http://dx.doi.org/10.1007/ Personality,30,158–167.http://dx.doi.org/10.1002/per.2046
BF02289209 Wilt,J.,Bleidorn,W.,&Revelle,W.(2017).Velocityexplainsthelinks
Schmidt,F.L.,&Hunter,J.(1996).Measurementerrorinpsychological betweenpersonalitystatesandaffect.JournalofResearchinPersonal-
research:Lessonsfrom26researchscenarios.PsychologicalMethods,1, ity,69,86–95.http://dx.doi.org/10.1016/j.jrp.2016.06.008
199–223.http://dx.doi.org/10.1037/1082-989X.1.2.199 Wilt,J.,Funkhouser,K.,&Revelle,W.(2011).Thedynamicrelationships
Schmidt,F.L.,&Hunter,J.E.(1999).Theorytestingandmeasurement ofaffectivesynchronytoperceptionsofsituations.JournalofResearch
error. Intelligence, 27, 183–198. http://dx.doi.org/10.1016/S0160- inPersonality,45,309–321.http://dx.doi.org/10.1016/j.jrp.2011.03.005
2896(99)00024-0 Wood, D., Harms, P. D., Lowman, G. H., & DeSimone, J. A. (2017).
Scott,W.A.(1955).Reliabilityofcontentanalysis:Thecaseofnominal Response speed and response consistency as mutually validating indi-
scalecoding.ThePublicOpinionQuarterly,19,321–325.http://dx.doi cators of data quality in online samples. Social Psychological and
.org/10.1086/266577 Personality Science, 8, 454–464. http://dx.doi.org/10.1177/19485
Shavelson,R.J.,Webb,N.M.,&Rowley,G.L.(1989).Generalizability 50617703168
theory.AmericanPsychologist,44,922–932.http://dx.doi.org/10.1037/ Zapf, A., Castell, S., Morawietz, L., & Karch, A. (2016). Measuring
0003-066X.44.6.922 inter-rater reliability for nominal data: Which coefficients and confi-
Shrout, P. E., & Fleiss, J. L. (1979). Intraclass correlations: Uses in denceintervalsareappropriate?BMCMedicalResearchMethodology,
assessingraterreliability.PsychologicalBulletin,86,420–428.http:// 16,93.http://dx.doi.org/10.1186/s12874-016-0200-9
dx.doi.org/10.1037/0033-2909.86.2.420 Zinbarg,R.E.,Revelle,W.,&Yovel,I.(2007).Estimating(cid:3) forstruc-
h
Shrout, P. E., & Lane, S. P. (2012). Psychometrics. In Handbook of turescontainingtwogroupfactors:Perilsandprospects.AppliedPsy-
researchmethodsforstudyingdailylife(pp.302–320).NewYork,NY: chological Measurement, 31, 135–157. http://dx.doi.org/10.1177/
GuilfordPress. 0146621605278814
Sijtsma,K.(2009).Ontheuse,themisuse,andtheverylimitedusefulness Zinbarg, R. E., Revelle, W., Yovel, I., & Li, W. (2005). Cronbach’s (cid:2),
ofCronbach’salpha.Psychometrika,74,107–120.http://dx.doi.org/10 Revelle’s(cid:4),andMcDonald’s(cid:3) :Theirrelationswitheachotherand
H
.1007/s11336-008-9101-0 two alternative conceptualizations of reliability. Psychometrika, 70,
Spearman,C.(1904a).“Generalintelligence,”objectivelydeterminedand 123–133.http://dx.doi.org/10.1007/s11336-003-0974-7
measured.TheAmericanJournalofPsychology,15,201–292.http://dx
.doi.org/10.2307/1412107
Spearman,C.(1904b).Theproofandmeasurementofassociationbetween ReceivedMay15,2018
twothings.TheAmericanJournalofPsychology,15,72–101.http://dx RevisionreceivedJune11,2019
.doi.org/10.2307/1412159 AcceptedJune12,2019 (cid:3)
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
RELIABILITY 1411