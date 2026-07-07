## Page 1

PsychologicalMethods

©2020AmericanPsychologicalAssociation2021,Vol.26,No.2,186-209

ISSN:1082-989Xhttp://dx.doi.org/10.1037/met0000305

Meta-AnalyticCriterionProfileAnalysis

BrentonM.WiernikMichaelP.Wilmot

UniversityofSouthFloridaUniversityofArkansas

MarkL.DavisonandDenizS.Ones

UniversityofMinnesota

Abstract

.y

lIntraindividualpatternsorconfigurationsareintuitiveexplanationsforphenomena,andpopularinbothlay

d

.as

roandresearchcontexts.Criterionprofileanalysis(CPA;Davison&Davenport,2002)isawell-established,

er

hb

sregression-basedpatternmatchingprocedurethatidentifiesapatternofpredictorsthatoptimallyrelatetoa

id

le

b

criterionofinterestandquantifiesthestrengthofthatassociation.ExistingCPAmethodsrequireindividual-tu

a

pn

leveldata,limitingopportunitiesforreanalysisofpublishedwork,includingresearchsynthesisviameta-id

m

e

eianalysisandassociatedcorrectionsforpsychometricartifacts.Inthisarticle,wedevelopmethodsfor

ls

ls

a

imeta-analyticcriterionprofileanalysis(MACPA),includingnewmethodsforestimatingcross-validityand

ds

te

i

fungibilityofcriterionpatterns.WealsoreviewkeymethodologicalconsiderationsforapplyingMACPA,b

f

o

o

includinghomogeneityofstudiesinmeta-analyses,correctionsforstatisticalartifacts,andsecond-orderte

nt

oosamplingerror.Finally,wepresentexampleapplicationsofMACPAtopublishedmeta-analysesfrom

n

r

osRorganizational,educational,personality,andclinicalpsychologicalliteratures.codeimplementingthese

i

nd

(cid:2)oconfiguralmethodsisprovidedinthepackage,availableathttps://cran.r-project.org/packageconfiguraland

n

ia

t

a

athttps://doi.org/10.17605/osf.io/aqmpc.ir

ce

os

us

TranslationalAbstracts

Al

a

uPatternsorconfigurationsofpredictorsarepopularwaysforresearchersandscienceconsumersto

ld

a

ic

vunderstandphenomena.Criterionprofileanalysis(CPA;Davison&Davenport,2002)isaregression-i

gi

do

nbasedpatternmatchingprocedurethatidentifiespatternsofpredictorsthataremaximallyrelatedtoal

oi

he

criterionofinterest.Thistechniqueallowsresearcherstoconsideranewperspectiveontherelationshipc

h

yt

sbetweenasetofpredictorsandacriterion—thatthecriterionisassociatedmostwithaspecificpatternf

Po

norconfigurationofpredictors.ExistingCPAmethodsrequireindividual-leveldata,limitingopportunitiese

as

cu

forresearchsynthesisviameta-analysisorreanalysisofpublishedresearch.Inthisarticle,wedevelopi

rl

ea

mnmethodsformeta-analyticcriterionprofileanalysis(MACPA),includingnewmethodsforestimating

oA

s

cross-validationperformanceandsensitivityanalyses.Wealsoreviewmethodologicalconsiderationsandr

ee

ph

caveatsforMACPA,includinghomogeneityofstudiesinmeta-analyses,correctionforstatisticalt

e

yh

artifacts,andsecond-ordersamplingerror.Finally,wepresentexampleapplicationsofMACPAtobt

rd

opublishedmeta-analysesfromorganizational,educational,personality,andclinicalpsychologicalliter-

ef

t

hy

Ratures.codeimplementingthesemethodsisprovided.ApplicationofMACPAinbothnewmeta-gl

ei

rl

yoanalysesandreanalysisofexistingcorrelationalresearchcanopennewavenuesofinquiryintothe

ps

o

dpotentialmechanismsdrivingimportantoutcomesinpsychologicalresearch.c

e

ds

in

et

nt

Keywords:criterionprofileanalysis,meta-analysis,configural,patternanalysis,fungibleregressionne

im

sweightsu

i

c

eo

ld

c

iSupplementalmaterials:http://dx.doi.org/10.1037/met0000305.supp

ts

ri

ah

Ts

i

h

T

Manyresearchersandpractitionersareinterestedindeterminingspecificpatternofsymptomsthatismostindicativeofadisorder;

ifaspecificconfigurationorpatternofcharacteristicsrelatestohumanresourcesmanagersseektoknowtheconfigurationof

highscoresonacriterionvariable.Cliniciansareinterestedinthecompetenciesthatismostpredictiveofjobperformance;and

ThisarticlewaspublishedOnlineFirstJuly30,2020.Themethodsdescribedinthisarticlehavebeenimplementedinthe

(cid:2)configuralRBrentonM.Wiernik,DepartmentofPsychology,UniversityofSouthXpackagefor,availableathttps://cran.r-project.org/package

Florida;MichaelP.Wilmot,DepartmentofManagement,Universityofconfiguralandhttps://doi.org/10.17605/osf.io/aqmpc.

Arkansas;XMarkL.Davison,DepartmentofEducationalPsychology,CorrespondenceconcerningthisarticleshouldbeaddressedtoBrenton

UniversityofMinnesota;XDenizS.Ones,DepartmentofPsychology,M.Wiernik,DepartmentofPsychology,UniversityofSouthFlorida,4202

UniversityofMinnesota.EastFowlerAvenue,Tampa,FL33620.E-mail:brenton@wiernik.org

186

## Page 2

communitypsychologistsaimtofindtheparticularcombinationof Objectives and Contributions of the Current Article
design factors that makes the most effective intervention (cf.
Inthisarticle,wedescribeproceduresformeta-analyticcriterion
Davison&Kuang,2000;Kulas,2013;Meehl,1950).Inallthese
profile analysis. First, we distinguish between types of pattern
applications,thequestionisnotwhetherprominentpatternsexist,
relationships before reviewing the logic and procedures of CPA.
but rather if a specific pattern of given predictors explains key
Next, we show how the key statistics of CPA can be computed
outcomes and how much variation is accounted for by such a
from summary data and present methods to limit overfitting and
pattern.
sensitivity analyses that aid in interpreting the shape of criterion
To address these important questions, Davison and Davenport
patterns. Third, we describe methods to integrate CPA with psy-
(2002) developed a procedure called criterion profile analysis
chometricmeta-analysis,includingcorrectingforbiasingeffectsof
(CPA;cf.Culpepper,2008).CPAisatwo-stageprocedurebuilton
statisticalartifacts.Finally,weprovideexamplesofMACPAusing
multipleregression.Inthefirststage,apatternofpredictorscores
meta-analyses from organizational, educational, personality, and
is identified that optimally relates to a criterion variable. This
clinical psychological literatures. We close by discussing the
pattern is called the criterion pattern. In the second stage, the
unique considerations for combining CPA and meta-analysis and strength of the association between the pattern and the criterion
highlightingpromisingareasforfutureresearch.Rcodetoimple- variable is quantified. In doing so, each person’s profile of pre-
mentallanalysesisavailableintheconfiguralpackageathttps://
dictor scores is reexpressed in terms of (a) their overall profile
cran.r-project.org/package(cid:2)configural and at https://doi.org/10
elevation and (b) the similarity of their individual pattern to the
.17605/osf.io/aqmpc.
optimalcriterionpattern.Levelandpatternscoresarethenusedin
Taken together, this article makes several contributions. First,
anewregressionmodeltoestimatetheamountofvariationdueto
we show how CPA pattern and level effects can be estimated
predictor configurations (pattern effect) and the overall profile
withoutaccesstoindividual-leveldata,openingavenuesforusing
level (level effect). By decomposing prediction from a set of
published data and interpreting meta-analyses from a configural
variablesintoconfiguralversussimpleaccumulationeffects,CPA
patternperspective.Second,weprovidemethodsforconstructing
helps explicate their theoretical relationships to a criterion and
confidenceintervalsandstatisticaltestsforparameters,including
informsassessmentbyindicatingwhetherattentiontoorinterpre-
in meta-analysis, allowing for consideration of sampling uncer-
tation of predictor configurations is warranted (Davison, Daven-
tainty when interpreting CPA and MACPA results. Third, we
port, Chang, Vue, & Su, 2015). CPA has been applied in work
present statistical methods to adjust the pattern effects to reduce
psychology(e.g.,identifyingpatternsoftraitsandbehaviorsasso-
overfitting and provide unbiased estimates of the population pat-
ciated with career interests; Dilchert, 2007; Wiernik, 2016; Wi-
tern effect or expected cross-validity in new samples. Fourth, we
ernik, Dilchert, & Ones, 2016; individual and team performance;
address challenges associated with integrating CPA with psycho-
Caughlin,2011;Grand,Pearce,&Kozlowski,2013;Kulas,2013;
metric meta-analysis, including correcting for statistical artifacts,
Shen, 2011; and career success; Booth, Murray, Overduin, Mat-
estimatinguncertainty,andhandlingnonpositivedefinitematrices
thews, & Furnham, 2016), educational psychology (e.g., patterns
and effect size heterogeneity. Fifth, to assess the sensitivity of
of abilities and experiences predictive of educational success;
results, we present procedures for fungible profile analysis
Chan, 2006; and college major choice; Culpepper, Davenport, &
(Waller, 2008), which help researchers to determine whether re-
Davison,2008;Davison,Jew,&Davenport,2014),socialpsychol-
sultsarerobusttominorperturbationsofagiveninputcorrelation
ogy(e.g.,patternsofsocialidentityvariableslinkedtowell-being;
matrix.Weconcludebypresentingseveralexampleapplicationsof
Lyons, 2015; Perry, 2008; Swinburne Romine, 2011), and the
MACPA to address substantive and applied questions from the
wider sciences (e.g., tooth wear patterns that distinguish monkey
literature.
taxa;Morse,Daegling,McGraw,&Pampush,2013).
Despite promising applications of CPA, existing procedures
are limited because they require primary individual-level data Types of Pattern Relationships Among Variables
asinputtocomputeindividualpatternandlevelscores;thatis,
Psychologicalresearchersareinterestedinavarietyoftypesof
current procedures preclude using CPA with summary (i.e.,
pattern relationships (also called configural relationships) among
secondary or meta-analytic) data. This limitation is consider-
variables(Cronbach&Gleser,1953;Hoffman,1960).Arelation-
able because it prevents reanalysis of published data to test
shipbetweentwovariables,X andX ,issaidtobeconfigural“if
intraindividualpatterneffects.Likewise,CPAcannotbeusedin 1 2
theinterpretationofoneitemofinformation[X ]iscontingenton
combinationwithmeta-analysis.Bypoolingresultsacrossmul- 1
a second [X ]” (Hoffman, 1960, p. 122). As noted by Hoffman,
tiplesamples,meta-analysisreducesbiasingeffectsofsampling 2
configural relationships can take an infinite variety of mathemat-
error and can address biases from other statistical artifacts
icalforms,buthefocusedontwotypes:(a)interactive,whichare
(e.g., measurement error and selection effects, such as range
patterns that have a multiplicative form (e.g., X · X ); and (b)
restriction;Schmidt&Hunter,2015;Wiernik&Dahlke,2020; 1 2
contrastive,whicharerepresentedmathematicallybyadifference
cf. Davison, Chang, & Davenport, 2014). Thus, this limitation
between two or more variables (e.g., X (cid:3) X ). Ipsative pattern
constrainstheabilityofCPAtocontributetotheaccumulation 1 2
relationships are a special case of the contrastive relationship in
of scientific knowledge via research synthesis. In response,
whichtherearepvariables(j(cid:2)1,...,p)andtherelationshiphas
the purpose of this article is to extend CPA procedures to
the form X (cid:2) 1(cid:2) X. For an ipsative relationship, a person’s
summary data, and to show how, in combination with psycho- 1 p j j
metric meta-analysis, meta-analytic criterion profile analyses score on a variable, X , is interpreted relative to the mean of all
1
(MACPA) can be used to advance research by examining pat- variablesforthatperson.Suchrelationshipsgiverisetoquestions
tern effects as part of integrative research synthesis. of whether there is within-person variability in scores across
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
META-ANALYTICCRITERIONPROFILEANALYSIS 187

## Page 3

predictors and whether this variability relates to important out- Criterion Profile Analysis
comes.
Examining contrastive pattern relationships entails decompos-
Logic and Procedures of Criterion Profile Analysis
ingvarianceinscoresonmultiplemeasuresintobetween-persons
(i.e., differences in profile level or elevation) and within-persons
DavisonandDavenport’s(2002)CPAisatwo-stageprocedure.
(i.e., differences in relative patterns of higher and lower scores,
First,ordinaryleastsquares(OLS)regression3isusedtoidentify
irrespective of profile elevation) components, followed by exam-
theconfiguralpatternofpredictorscoresthatisoptimallyrelated
iningthesecomponents’relationshipstoothervariables(Davison,
toacriterion.DavisonandDavenport(2002,AppendixA)proved
Kim,&Close,2009).Forexample,Davison,Jew,andDavenport
this criterion pattern can be described as a vector of contrast
(2014) examined how between-person (level) and within-person coefficients(cid:2)(cid:2)(cid:2)(cid:2)(cid:3)1(cid:4)¯ (cid:2)[(cid:4) (cid:3)(cid:4)¯]=,where(cid:2)isacolumnvector
(pattern) components of SAT scores predicted university student ofregressioncoefficients,1isa j columnvectorof1s,and(cid:4)¯ isthe
major choice. They found that between-person differences in
mean regression coefficient. Second, for each person, two new
scorespredictedsomemajors(e.g.,higheroverallabilitypredicted
profilescoresarecomputed:(a)theirprofilelevelscore,which
choice of math/physics and engineering; lower overall ability
istheoverallelevationoftheirpredictorprofile;itiscomputed
predicted choice of education major). However, they found that
asthewithin-personmeanacrosstheppredictorsinthemodel:
within-person differences in score patterns had much stronger (cid:2)
x (cid:3) (cid:3)x ,x ,x ,...,x (cid:4)⁄p;and(b)theircriterionpattern
relationships with major choices (e.g., a within-person pattern of levi 1i 2i 3i pi
similarityscore,whichisthesimilarityofatheirprofilepattern
higher SAT Math vs. SAT Verbal predicted choice of business,
to the criterion pattern; it is computed as the covariance be-
math,orphysicalsciencemajors;awithin-personpatternofhigher
tween their predictor score vector and the criterion pattern:
S T A he T se V a e u r t b h a o l r v s s c . o S n A cl T ud M ed at t h h p at re w d i i t c h te in d -p c e h r o s i o c n eo co f n h f u i m gu a r n a i t t i i o e n s s m o a f j S o A rs T ). Cov(cid:4) i * (cid:3) (cid:2)p j x ij (cid:4)* j ⁄p. Profile level and pattern scores, in turn,
areusedtopredictthecriterioninanewregressionmodelthat
scoreswerethemoreimportantdriverofmajorchoice(cf.Wang,
examines the relative explanatory power of the two effects. The
Eccles,&Kenny,2013).Thus,contrastivepatternrelationscon-
predictivepowerofthecriterionpatternforthecriterionvariableis
cernthepredictiveutilityofwithin-personconfigurationsofaset
captured by the correlation between the criterion and the profile
ofpredictorscores(orsubscalescores).1
the B r y el c a o ti n o t n r s a h st i , p i b n e te tw ra e c e t n ive tw p o at v t a e r r i n ab r l e e l s at c i h o a n n sh g i e p s s a c s o a nc fu er n n ct w io h n e o th f e a r t s h im e i r l e a g ri r t e y ss s i c o o n re m s, o C de o l v , (cid:4) yˆ i * i . (cid:3) Da (cid:4) v p is at o C n o a v n (cid:4) i * d (cid:5) Da (cid:4) v l e ev np x l o ev r i t , ( h 2 a 0 s 0 t 2 h ) e s s h a o m w e ed R2 th a a s t
theOLSregressionmodel.Thus,theCPAregressionmodelcanbe
third variable. For example, is a personality trait a stronger pre-
understoodasthecombinedimpactoftheelevationofscoreprofiles
dictor of behavior when situational pressures are weak versus
andthesimilarityofprofilepatternstotheoptimalcriterionpattern.
strong(Judge&Zapata,2015),orisabilityastrongerpredictorof
Although these CPA procedures are straightforward, they are
performancewhenmotivationishighversuslow(VanIddekinge,
limitedbyrequiringindividual-leveldatatocomputekeystatistics.
Aguinis, Mackey, & DeOrtentiis, 2018)? Interactive pattern rela-
Accordingly,newmethodsareneededtoestimatetheCPAregres-
tionships are represented by multiplicative terms in polynomial
sionmodelusingsummarydata.Sufficientstatisticsforthemodel
regressionandfollow-upanalyses(Cohen,Cohen,West,&Aiken,
are correlations of the criterion variable with (a) profile level
2003; Shanock, Baran, Gentry, Pattison, & Heggestad, 2010). A
scores, r , and (b) criterion pattern similarity scores, r , as
key distinction between these two types of pattern relationships lev,y pat,y
well as (c) the correlation between profile level and criterion
among variables is that contrastive pattern relationships concern
patternsimilarityscores,r (Cohenetal.,2003,p.70).Below,
decomposing variance in a set of predictors into between-person lev,pat
weshowhowtocomputethesecorrelationsfromsummarydata.
and within-person components, whereas interactive pattern rela-
tionshipsconcernexpandingthesetofpredictorstoincludemul-
tiplicativecompositesoftwoormorevariables. Procedures for Extending Criterion Profile Analysis to
Contrastive and interactive represent two distinct types of pat- Summary Data
tern relationships. One, both, or neither, can be present when
describingrelationshipsofasetofpredictorstoacriterionvariable. The theory of composites (Nunnally, 1978, pp. 166, 177; see
For example, Van Iddekinge, Aguinis, Mackey, and DeOrtentiis also Ghiselli, Campbell, & Zedeck, 1981, p. 163) shows that
(2018) meta-analytically tested the hypothesis that ability and
motivationhaveaninteractivepatternrelationshiptoworkperfor-
1Arelatedquestiontocontrastivepatternrelationshipsiswhethersub-
mance.Theyfoundthatmultiplicativeability–motivationcompos- scoresofameasurehaveinterpretativemeaningoriftheirsolecontribution
ites had negligible incremental validity over linear ability and isaddingtoaperson’stotalscore(Davisonetal.,2015;Haberman,2008;
motivationterms,indicatinglittleevidenceforaninteractivepat- Ree,Earles,&Teachout,1994).Ifsubscoresincrementallypredictovera
totalscore,thisindicatesacontrastivepatternrelationshipispresent.For
tern relationship. However, if one reanalyzes their meta-analytic
any specific total score, people with the same total score, but different
correlationmatrixusingthemethoddetailedinthisarticle,thereis
within-personsubscorepatterns,willtendtohavedifferentexpectedcri-
evidence of a contrastive pattern relationship.2 In other words, terionscores.
thereisaconfiguralrelationshipintheVanIddekingeetal.(2018) 2Both the ability–motivation profile level (r (cid:2) .50, (cid:4) (cid:2) .50,
lev lev
data,butithasacontrastiveform,notaninteractiveformposited (cid:5)(cid:6)R2 (cid:2).50)andprofilepattern(r (cid:2).11,(cid:4) (cid:2).11,(cid:5)(cid:6)R2 (cid:2).11)
lev pat pat lev
bytheauthors.Asnotedearlier,weextendmethodsforanalyzing offer unique prediction. This result can be interpreted as indicating that,
althoughbothconstructspredict,otherfactorsbeingequal,employeeswho
configural pattern relationships of the contrastive pattern type by
arerelativelymorecapablethantheyaremotivatedtendtoperformbetter.
showinghowDavisonandDavenport’s(2002)CPAtechniquecan 3CPA can also be applied with weighted least squares or generalized
beappliedtometa-analyticdata. linearmodels(cf.Davison,Jew,&Davenport,2014).
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
188 WIERNIK,WILMOT,DAVISON,ANDONES

## Page 4

multipleregressioncanbeconceptualizedasacompositecorrela- correctingforstatisticalartifacts,suchassamplingerror,measure-
tionweightedbytheregressioncoefficients.Likewise,CPAlevel ment error, and selection biases (Schmidt, 1992; Schmidt &
andpatterneffectscanbeunderstoodasalternativesetsofweights Hunter, 1977). These artifacts are present in all studies and bias
for computing composite correlations. Thus, the correlation be- observedcorrelationsbetweenvariablesawayfromtrueconstruct
tweenpredictorprofilelevelandthecriterion,r ,isestimableas relationships.TheycanalsodistortCPAresults,leadingtoincor-
lev,y
aunit-weightedcompositecorrelation: rect conclusions about the shape and predictive validity of
(cid:2) (cid:2) criterion-related predictor configurations. To avoid these distor-
r (cid:3)(cid:3)1(cid:2)R 1(cid:4)(cid:2)1⁄21(cid:2)r (cid:3) j 1·r xjy (cid:3) j r xjy , tions, these artifacts can be corrected by combining CPA with
lev,y xx xy (cid:5)(cid:2) (cid:5)(cid:2) psychometric meta-analysis (Schmidt & Hunter, 2015), a proce-
1·1·r r
j,k xjxk j,k xjxk durewecallmeta-analyticcriterionprofileanalyses(MACPA).In
(1) the sections below, we discuss how statistical artifacts impact
MACPAanddescribeprocedurestocorrecttheireffects.
where r is the column vector of correlations between each
xy
predictor variable and the criterion, R is the correlation matrix
xx Sampling Error
amongthepredictors,and1isacolumnvectorof1s.
Similarly, the correlation between criterion pattern similarity
Random sampling error can distort observed correlations in a
and the criterion, r , is estimable as a composite correlation
pat,y singlesamplefromtheirtruepopulationvalues.Aswithmultiple
weightedby(cid:2)(cid:2),thecriterionpatternvector:
regression,samplesizerequirementsforCPAcanbegreat,espe-
(cid:2) ciallyifthenumberofpredictorsislarge(Cohenetal.,2003).If
(cid:4)*r
r (cid:3)((cid:2)*(cid:2)R (cid:2)*)(cid:2)1⁄2(cid:2)*(cid:2)r (cid:3) j j xjy (2) samplesizesaresmall,theshapeoftheobservedcriterionpattern
pat,y xx xy (cid:5)(cid:2)
(cid:4)*(cid:4)*r andthesizeofthelevelandpatterneffectscanvarywidelyacross
j,k j k xjxk
samples.Bypoolingresultsfrommanystudiesinameta-analytic
Finally, the correlation between profile level and criterion pat- correlation matrix, MACPA reduces sampling error, allowing for
ternsimilarity,r lev,pat ,canbecalculatedusingtheformulaforthe increased power and more precise estimation of CPA parameters
correlationbetweentwocomposites(Waller,2008,p.692): thanwouldbepossibleinasinglesample(Viswesvaran&Ones,
r (cid:3)(cid:3)(cid:2)*(cid:2)R (cid:2)*1(cid:2)R 1 (cid:4)(cid:2)1⁄2(cid:2)*(cid:2)R 1 1995).
lev,pat xx xx xx
Measurement Error
(cid:2)
1·(cid:4)*·r
(cid:3) j,k k xjxk Classical measurement error variance (i.e., unreliability) sys-
(cid:5)(cid:2) (cid:5)(cid:2)
1·1·r (cid:4)*(cid:4)*r tematicallybiasescorrelationstowardzero,leadingtoconclusions
j,k xjxk j,k j k xjxk
that constructs have weaker relationships than they really do
(Schmidt&Hunter,1996;Viswesvaran,Ones,Schmidt,Le,&Oh,
(cid:2) 2014). In CPA, measurement error has three effects. First, it
(cid:4)*·r
(cid:3) j,k k xjxk (3) flattens the amplitude of the criterion pattern, making the peaks
(cid:5)(cid:2) (cid:5)(cid:2)
r (cid:4)*(cid:4)*r andvalleysofpatternfeatureslesspronouncedandmoredifficult
j,k xjxk j,k j k xjxk
to detect. Second, it weakens the criterion correlations for both
ThesethreecorrelationscanthenbeusedtocalculatetheCPA profile level and criterion pattern similarity, resulting in more
regressioncoefficientsandthefull-modelR2(Cohenetal.,2003, pessimistic conclusions about the explanatory power of the pre-
p.70): dictorset.Third,itcausesrelativelymoreexplanatorypowertobe
(cid:6) r r (cid:2)r r r (cid:2)r (cid:7) (cid:2) attributed to the level effect rather than to the pattern effect,
(cid:2) (cid:3)(cid:3)(cid:4) (cid:4) (cid:4)(cid:2)(cid:3) lev,y lev,pat pat,y pat,y lev,pat lev,y producing inaccurate inferences about their relative influence.
CPA pat lev r2 (cid:2)1 r2 (cid:2)1
lev,pat lev,pat Thus, measurement error systematically obscures configural pat-
(4) terneffectsinempiricalrelationships.
Twomethodsareavailabletocorrectformeasurementerrorin
R2(cid:3)(cid:3) 2·r r r (cid:2)r2 (cid:2)r2 (cid:4) ⁄ (cid:3) r2 (cid:2)1 (cid:4) (5)
pat,y lev,y lev,pat pat,y lev,y lev,pat CPA. First, each correlation in the matrix can be individually
AppendixApresentsproofsfortheseequations,andAppendix corrected for unreliability. This is the approach taken for most
B provides methods for computing confidence intervals and sta- applicationsofmultivariatetechniquestometa-analyticcorrelation
tisticalhypothesistestsforCPAparameters.UsingEquations1–5, matrices (Viswesvaran & Ones, 1995). When contributing meta-
researchers can compute all key CPA results (i.e., full-model R2, analyses do not report information to correct for measurement
zero-ordercorrelations,regressioncoefficients,and(cid:5)R2forlevel error(e.g.,Example2below),estimatescanbedrawnfromother
and pattern effects) using only the correlation matrix.4 This ad- meta-analyses in the literature. Second, the reliability of individ-
vance opens the possibility of applying CPA in secondary data uals’ profile level and criterion pattern similarity scores can be
analysisandmeta-analysis.
4WepresentformulasforconductingCPAusingcorrelationmatrices,
Meta-Analytic Criterion Profile Analysis becausestandardizedcoefficientsaretheoutputofmostmeta-analyses.In
cases where variable scales are meaningful (e.g., econometric analyses),
Meta-analysis is a technique for reducing biases in research researchersmayconductCPAusingcovariancematrices(cf.Davison&
findings by statistically pooling results from multiple studies and Davenport,2002).AssociatedformulasarepresentedinAppendixA.
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
META-ANALYTICCRITERIONPROFILEANALYSIS 189

## Page 5

estimatedandusedtodirectlycorrectr ,r ,andr .Bulut, anddirectselectionareparticularlyflexibleandcanbeappliedin
lev,y pat,y lev,pat
Davison,andRodriguez(2017)presentmethodsforestimatingthe awidevarietyofsettings(Dahlke&Wiernik,2019).
reliability of profile level scores (labeled (cid:7)ˆ BB(cid:2)) and pattern simi-
larityscores(labeled(cid:7)ˆ WW(cid:2))usingeitherparallelformsorsplit-half
Other Artifacts
reliability. Though both methods of correction are viable, they
havedifferenteffects.WhenCPAisperformedusingacorrected OtherartifactscanalsobiasMACPAresults,includingartificial
correlation matrix, the amplitude of the criterion pattern and va- polytomization(Alf&Abrahams,1975;Hunter&Schmidt,1990)
lidity of profile level and pattern effects will all be correctly anduseofcoarsemeasurementscales(Aguinis,Pierce,&Culpep-
estimated without the attenuating bias of measurement error. By per,2009).Ifapplicable,thesecanbecorrectedpriortoMACPA
comparison, directly correcting r lev,y , r pat,y , and r lev,pat will yield toimprovetheaccuracyofinferences.
unbiasedestimatesofprofilelevelandpatterneffects,whereasthe
shape of the criterion pattern will remain attenuated, making
interpretationsofresultsmoredifficult.5 Correcting Pattern Effect r , (cid:2),
pat
and (cid:3)R2 for Overfitting
Selection Effects A limitation of multiple regression is its tendency to overfit
coefficients to idiosyncratic features of small samples, leading to
Selection effects (i.e., range restriction, range enhancement,
reduced cross-validity (or shrinkage) in new samples (Wainer,
attritioneffects,orcolliderbias;Elwert&Winship,2014;Sackett
1976).Correctingforoverfittingiscriticalwhenevaluatingmodel
&Yang,2000)andtherelatedphenomenonofbaseratesthatdo
fit,andcanbedoneusingcross-validationorstatisticalestimators
not adequately reflect the population of interest (McGrath &
(Shieh,2008).InthecontextofCPA,overfittingcausesthepattern
Meyer, 2006; R. P. Steel, Shane, & Griffeth, 1990) also induce
effecttobeoverestimated,resultinginapositivebiasinr .To
artifacts needing correction. For example, relationships among pat,y
addressthis,DavisonandDavenport(2002)recommendedatwo-
personnelassessmentsdifferamongjobapplicantsversusincum-
foldcross-validationprocedurethatinvolvesestimatingthecrite-
bent employees (Sackett, Lievens, Berry, & Landers, 2007), and
rionpatterninonesubsampleandthenusingittocomputepattern
correlations among psychopathology symptoms vary between
scores in the other subsample (and vice versa). However, this
general-populationversusmore-restrictedclinicalsamples(Neale
procedure requires individual-level data. Consequently, a statisti-
&Kendler,1995;Westreich,2012).Dependingonselectionmech-
cal shrunken-R2 estimator must be used for MACPA or when
anism,selectioneffectscanattenuate,inflate,orevenreversesigns
calculatingCPAfromsummarystatistics.6
ofcorrelations(Dawes,1975;Wiernik&Dahlke,2020).InCPA,
Several shrunken-R2 estimators are available to estimate the
strong selection effects can seriously distort the shape of the
populationorcross-validityR2foraregressionmodel(seeShieh,
criterionpatternandtherelativeinfluenceofthelevelandpattern
2008; and Cattin, 1980, for reviews) and can also be used to
effects,particularlyifselectioncausescorrelationsignstoflip.If
estimate the population or cross-validity r . First, rearrange
allvariablesaresubjecttothesameselectionmechanism(e.g.,job pat,y
Equation5toexpressr intermsofr ,r ,andfull-model
knowledge,interpersonalskill,anddependabilityallmakeacan- pat,y lev,y lev,pat
R2(aproofofthisresultisgiveninAppendixC):
didate more likely to be hired), then the general shape of the
criterion pattern (i.e., which variables are high and low) will
typicallybethesameforobservedcorrelationsversuscorrelations r pat,y (cid:3)r lev,y r lev,pat (cid:5)(cid:5)(cid:3) 1(cid:2)r l 2 ev,pat (cid:4)(cid:3) R2(cid:2)r l 2 ev,y (cid:4) (6)
correctedforselection.However,theamplitudeofthepattern,and The population or cross-validity correlation between criterion
therelativecontributionsoflevelandpatterneffectscanbequite patternsimilarityandthecriterioncanbeestimatedbysubstituting
different. More seriously, if the variables are under different se- R2withanappropriateestimateofthepopulationorcross-validity
lection pressures (e.g., people high on trait Openness but low on R2:
Emotional Stability tend to develop psychosis-related psychopa-
thology), then the criterion patterns can have entirely different rˆ (cid:3)r r (cid:5)(cid:5) max (cid:8)(cid:3) 1(cid:2)r2 (cid:4)(cid:3) R˜2(cid:2)r2 (cid:4) ,0 (cid:9)
shapes if estimated from observed versus corrected correlation pat,y lev,y lev,pat lev,pat lev,y
matrices. (7)
Thus, a critical step for accurate MACPA results is specifying
theappropriatepopulationforwhichinterferencesaretobedrawn.
5In addition to the classical disattenuation formula, other error-in-
Then,eachcorrelationinthemeta-analyticmatrixshouldbecor-
variablesregressionmodelsmightalsobeusedtocorrectformeasurement
rected to reflect the target population. Importantly, corrections error, especially for more complex error structures (Fuller, 1987;
appliedtoeachcorrelationinthematrixmaydifferifthestudies Schennach,2016).
contributing to each meta-analysis are based on samples from 6Thisapproachcorrectsforoverfittingbyadjustingtheestimatedcor-
relation between the OLS criterion pattern and the criterion variable
differentpopulations(e.g.,ifpredictorintercorrelationscomefrom
downward. This adjusted r provides a more accurate estimate of the
general-population samples, but predictor–criterion correlations pat,y
predictivevalidityofaperson’ssimilaritytotheOLScriterionpatternin
comefromselectedsamples).Dependingonavailabledata,several the population or new samples than the naïve unadjusted pattern effect
methods exist to correct for selection effects and to estimate the correlation.Analternativeapproachtoreduceoverfittingistoestimatea
correlations in the target population (Dahlke & Wiernik, 2019; criterion pattern from a non-OLS set of regression coefficients, such as
ridgeorLASSOregressioncoefficients(Hastie,Tibshirani,&Friedman,
Sackett&Yang,2000).Suchcorrectionscanbeappliedtodataat
2009). These regularization routines bias the coefficients for predictors
the individual-level, study-level, or even post hoc to uncorrected towardacommonvalue,directlylimitingoverfittingandoverestimationof
meta-analytic results. Correction formulas for bivariate indirect thepatterneffect.
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
190 WIERNIK,WILMOT,DAVISON,ANDONES

## Page 6

Althoughthemostcommonestimatoristheadjustedr2 statis- regressioncoefficients(calledfungibleweights)withthismodelfit
adj
tic reported by most statistical packages, in a comprehensive thatismaximallydissimilarfromtheOLSregressionweights.This
simulation study, Shieh (2008) found that other estimators were algorithm can be adapted for CPA to identify an alternative con-
less biased without substantially increasing computational com- trastive pattern with a specified (cid:6)R2 that is maximally dissimilar
plexity.Basedontheseresults,thepopulationcorrelationbetween fromthecriterionpattern.Wecallthisprocedurefungibleprofile
criterionpatternsimilarityandthecriterionisbestestimatedusing analysis. First, select an amount of loss of model fit ((cid:6)R2) for
oneoftwomethods. computing fungible weights. Values should be small enough that
If the objective is to develop a model for how a profile of the loss of fit would not alter substantive conclusions.7 We rec-
predictors predicts a criterion in the population (i.e., descriptive ommend (cid:6)R2 (cid:2) (cid:3).005 and (cid:6)R2 (cid:2) (cid:3).010 to examine sensitivity
applicationsofCPA),estimatethepopulationcorrelationbysub- underrelativelysmallerandlargerdecrementsinmodelfit.Next,
stitutingR˜2with(cid:7)ˆ2(cid:5): foreachvalueof(cid:6)R2,usetheWallerandJones(2009)optimiza-
P
tion procedure to identify the alternative regression coefficients
(cid:7)ˆ P 2(cid:5)(cid:3)max (cid:8) 1(cid:2) (cid:3) N(cid:2) N(cid:2) p(cid:2) 3 1 (cid:4) (cid:3)1(cid:2)R2(cid:4) (cid:3) 1(cid:5) N 2 (cid:2) (cid:3)1 p (cid:2) (cid:2) R 2 2(cid:4) .3 (cid:4) ,0 (cid:9) t a h ) a . t F a i r n e al m ly a , x m im e a a l n l - y ce d n is te si r m a ila to r f c r o o m m p t u h t e e O a L p S at c te o r e n ff v ic e i c e t n o t r s , ( a la (cid:2) b , e a l n e d d
(8) compare a(cid:2) to the criterion pattern, (cid:2)(cid:2). If the shape of the maxi-
mally dissimilar pattern vector, a(cid:2), differs substantially from the
(cid:7)ˆ (cid:3)r r (cid:5)(cid:5) max (cid:8)(cid:3) 1(cid:2)r2 (cid:4)(cid:3)(cid:7)ˆ2(cid:5)(cid:2)r2 (cid:4) , 0 (cid:9) criterion pattern, (cid:2)(cid:2), with only a small loss in model fit, this
pat,y lev,y lev,pat lev,pat P lev,y
indicates that diverse predictor profiles can produce the same
(9)
criterionoutcomes.Examplesofsuchsubstantialdifferencescould
where p is the number of predictors contributing to the profile includeaprominentpeakinthecriterionprofilepatterndisappear-
pattern,andNisthesamplesize. inginthemaximallydissimilarfungiblepattern(e.g.,seeExample
If the objective is to estimate the performance of a criterion 3,below)ortherelativeorderofpredictorsinthecriterionprofile
patternforpredictingoutcomesinaspecificsample(i.e.,prescrip- pattern switching places in the maximally dissimilar fungible
tive applications of CPA; Davison, Chang, & Davenport, 2014), pattern.Inthesecases,researchersshouldbecautiousaboutinter-
estimatetheexpectedcross-validitycorrelationbysubstitutingR˜2 pretingthesubstantivemeaningoftheobservedcriterionpattern.
with(cid:7)ˆ2(cid:5) :
C.BR–P
(cid:10) (cid:11) Accuracy of Proposed Methods
(N(cid:2)p(cid:2)3)(cid:7)ˆ4(cid:5)(cid:5)(cid:7)ˆ2(cid:5)
(cid:7)ˆ C 2(cid:5) .BR–P (cid:3)max (N(cid:2)2p(cid:2)2) B (cid:7)ˆ2(cid:5)(cid:5) P p ,0 , (10) MACPAcombinesthreewell-establishedanalytictechniques—
P CPA, psychometric meta-analysis, and meta-analytic structural
2p(cid:3)1(cid:2)(cid:7)ˆ2(cid:5)(cid:4)2
equationmodeling(MASEM;Viswesvaran&Ones,1995)—each
where(cid:7)ˆ4(cid:5)(cid:3)(cid:7)ˆ4(cid:5)(cid:2) P
B P (cid:3)N(cid:2)1(cid:4)(cid:3)N(cid:2)p(cid:5)1(cid:4) ofwhichhasbeenthesubjectofextensiveresearchandsimulation
work. We summarize key findings below and highlight the rele-
(cid:7)ˆ (cid:3)r r (cid:5)(cid:5) max (cid:8)(cid:3) 1(cid:2)r2 (cid:4)(cid:3)(cid:7)ˆ2(cid:5) (cid:2)r2 (cid:4) , 0 (cid:9)
Cpat,y lev,y lev,pat lev,pat C.BR–P lev,y vanceandimplicationsofthesesimulationstudiesforMACPA.
Davison, Davenport, Chang, Vue, and Su (2015) conducted
(11)
simulations of CPA to test the incremental validity of profile
patterneffectsandleveleffectsforconditionsvaryingacrossfive
Assessing Criterion Pattern Sensitivity Using Fungible parameters: (a) sample size (N (cid:2) 100; 300); (b) total model R2
Weights Analysis value(R2(cid:2).20,.40,.60);(c)predictorintercorrelations(r(cid:2).00,
.35, .70); (d) relative sizes of pattern and level effects ((cid:4) (cid:7) 0,
CPA equations show that the configuration of regression coef- lev
(cid:4) (cid:2)0;(cid:4) (cid:2)0,(cid:4) (cid:7)0;(cid:4) (cid:2)2(cid:8)(cid:4) ;(cid:4) (cid:2)(cid:4) );and
ficients can be interpreted as an indicator of the optimal within- pat lev pat lev pat lev pat
(e) residual error distributions (Normal; (cid:9)2). When there was no
personconfigurationofpredictorsforthecriterion.However,even
if the CPA pattern effect is substantial, caution may still be
warrantedininterpretingthespecificshapeofthecriterionpattern. 7We recommend focusing on effect size magnitude when choosing a
Waller (2008) showed that the relative pattern of larger and value for (cid:6)R2. The loss in model fit ((cid:6)R2) should be chosen so that the
smallerregressioncoefficientscansometimeschangedramatically reduced value would not lead to meaningfully different theoretical or
withonlyasmalllossinmodelfit.Thatis,ifonereducesmodel practicalconclusions.Forexample,aresearcherwouldlikelyconcludethat
R2 by a very small amount (e.g., reduce R2 (cid:2) .005, a value R2 (cid:2) .09 or .08 (R (cid:2) .30 or .28; (cid:6)R2 (cid:2) .01) reflect similar levels of
predictive validity (cf. Anvari & Lakens, 2019; Calin-Jageman & Cum-
possiblywithinsamplingerrorandunlikelytochangesubstantive ming,2019;Kruschke,2018).Whatconstitutesameaningfultheoreticalor
interpretations), some sets of possible regression coefficients practicaldifferencewillofcoursedependonthespecificresearchareaor
yieldingthatreducedR2valuemaydiffergreatlyfromtheconfig- application in question. Another approach would be to adopt an equiva-
lencetestingframework(Tryon,2001)andtochoose(cid:6)R2tocorrespondto
urationofOLScoefficients.TheCPAcriterionpatterndependson
thelowerboundoftheconfidenceintervalforR2(e.g.,forR2(cid:2).09[.04,
the relative pattern of regression coefficients, so, when applying .19],(cid:6)R2(cid:2)(cid:3).05).Thiswouldreflectthelargestlossinmodelfitthatis
CPA,researchersshouldfirstevaluatethesensitivityofthecrite- statistically equivalent to (i.e., not significantly different from) the ob-
rion pattern before making substantive interpretations about its served R2. However, this approach will often result in (cid:6)R2 values that
shape. reflect practically different levels of predictive validity (e.g., many re-
searcherswouldinterpretR(cid:2).20[R2(cid:2).04]assubstantivelysmallerthan
WallerandJones(2009)presentedanalgorithmtoevaluatethe
R(cid:2).30[R2(cid:2).09];Wiernik,Kostal,Wilmot,Dilchert,&Ones,2017).
sensitivityofthepatternofregressioncoefficients.Foragivenloss Accordingly, this equivalence testing procedure will often identify (cid:6)R2
inmodelfit((cid:6)R2),theiralgorithmidentifiesthesetofalternative valuesthataretoolargeforuseinfungibleprofileanalysis.
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
META-ANALYTICCRITERIONPROFILEANALYSIS 191

## Page 7

pattern effect ((cid:4) (cid:2) 0), CPA had nominal Type I error rates deviation of population effects, especially when statistical cor-
pat
acrossconditions.Whenthepatterneffectfullyaccountedforall rections are incorporated. Accordingly, MACPA represents a
prediction((cid:4) (cid:2)0),CPAhadpowernear1.0acrossconditions. valid approach for examining contrastive pattern effects. We
lev
When pattern and level effects were equal, power to detect a also note that our recommended methods for correcting for
nonzeropatterneffectremained(cid:7).90foruncorrelatedpredictors. overfittingandsensitivityanalysesviafungibleprofileanalysis
By comparison, power diminished as predictor intercorrelation are based on results of extensive analytic and simulation work
increased,unlesstotalmodelR2wasalsolarge(R2(cid:2).40;.60),and by Shieh (2008) and Waller (2008; Waller & Jones, 2009),
thislosswasgreaterwhenthepatterneffectwasrelativelysmaller respectively.
thantheleveleffect((cid:4) (cid:2)2(cid:8)(cid:4) ).8Takentogether,theauthors
lev pat
concluded CPA can reliably differentiate pattern versus level ef- Worked Examples of Meta-Analytic Criterion
fects in a set of predictors when one of these effects account for
Profile Analysis
mostofthepredictivevariance.However,whenbothpatternand
level effects are present, and predictors are substantially corre- In this section, we apply MACPA to four published meta-
lated, CPA is less able to detect pattern effects unless R2 or N is analyses from multiple psychology subfields. Table 1 shows
large (Davison et al., 2015). Therefore, by combining samples to meta-analytic intercorrelation matrices, and Table 2 presents
increaseN,MACPAcanincreasepowertodetectsmall,nonzero MACPA summary statistics. Figure 1 shows criterion pattern
patterneffects,comparedwithtraditionalCPA. plots, and Figure 2 shows fungible pattern plots.
For MACPA to yield accurate CPA parameter estimates, the
correlation matrix submitted to MACPA must likewise contain Example 1: MACPA With Fully-Corrected
accurateestimates.Severalstudieshaveevaluatedtheaccuracy Correlation Matrices—Work Characteristics and Job
ofmethodsformeta-analysisofcorrelations.Althoughvarious Performance Ratings
methods for weighting correlations or Fisher z=-transformed
correlations yield similar results, sample size-weighted corre- First,weapplyMACPAtoameta-analyticcorrelationmatrix
lations typically yield the most accurate estimates of the mean thathasbeencorrectedforstatisticalartifacts.Humphrey,Nah-
andstandarddeviationofthepopulationeffectsizedistribution rgang,andMorgeson(2007)meta-analyzedrelationsof10task
(Brannick, Potter, Benitez, & Morris, 2019; Hafdahl, 2010; design and social work characteristics with supervisor-ratings
Schulze, 2004; cf. Bakbergenuly, Hoaglin, & Kulinskaya, ofemployeejobperformance.Humphreyetal.(2007)corrected
2019).9 Further, when measurement error, selection effects, or allvariablesformeasurementerror,butinsufficientinformation
other statistical artifacts are present, making corrections for was available to correct for range restriction. We chose this
them yields more accurate estimates of population construct meta-analysisbecauseitisplausiblethataworkdesignstrategy
intercorrelations (Beatty, Barratt, Berry, & Sackett, 2014; that emphasizes some features (e.g., feedback), but deempha-
Dahlke&Wiernik,2019;Hedges&Olkin,1985;Schmidtetal., sizes others (e.g., increasing autonomy), might be more effec-
2009). Because contrastive configural patterns are strongly tivethanalternativesforimprovingjobperformance.Thatis,a
influencedbypatternsofvariableintercorrelations,itispartic- specific configuration of characteristics may have incremental
ularly important to correct for selection effects (cf. Sackett et validity over simply higher overall levels of positive work
al., 2007). Dahlke and Wiernik (2019) reviewed available cor- features.
rection models for the common case of indirect (incidental) We tested this hypothesis by applying MACPA to the meta-
selectionimpactingbothvariablesinacorrelation.Theyfound analyticcorrelationmatrix.AsFigure1Adisplays,thecriterion
that their proposed procedures for individual-correction and pattern showed that performance was highest for employees
artifact-distribution meta-analyses yielded highly accurate re- whose jobs had higher levels of feedback from others, higher
sults, and that information to apply these corrections is more complexity, and less variety of skill demands, compared with
commonly available than most researchers realize. other work characteristics. Comparing predictive power for
Finally, considerable research has explored the accuracy of level and pattern effects, Table 2 shows both the level effect
results of multivariate analyses (e.g., multiple regression, path (r (cid:2) .31) and pattern effect (r (cid:2) .37) related strongly to
lev pat
analysis, structural equations modeling) when conducted using performance. Further, supporting our hypothesis, the pattern
meta-analytic correlation matrices (Becker, 1992; Jak, 2015; effect showed substantial incremental validity over the level
Viswesvaran & Ones, 1995). MASEM has become widespread effect( (cid:5)(cid:6)R2(cid:2).48).Accordingly,resultsindicatethatsimply
inpsychology(Landis,2013;Michel,Viswesvaran,&Thomas, providingmoreworkdesignfeaturesisnotalwaysoptimaland
2011; Sheng, Kong, Cortina, & Hou, 2016). Simulation study that attention should be paid to providing an optimal configu-
results show MASEM yields accurate parameter estimates
(Cheung & Cheung, 2016; Furlow & Beretvas, 2005; Hafdahl,
8However,itshouldbenotedthat,insuchcases,thetrueeffectsizefor
2008; Oort & Jak, 2016; Rosopa & Kim, 2017; Sheng et al.,
thepopulationpatterneffectwillbesmall,soinferencesthatsucheffects
2016),withincreasingaccuracyastotalsamplesizeandnumber
areclosetozerowouldnotnecessarilybeinaccurate.Muchlargersample
of studies included in a meta-analysis increases. sizes would be needed to yield narrow enough confidence intervals to
Based on the preceding evidence, MACPA builds on a firm consistentlydifferentiatesuchsmall(cid:5)R2 fromzero.
pat
foundation:CPAcanaccuratelydetectcontrastivepatternrela-
9Otherweightsthatarealsonotdependentonsample-specificestimates
of sampling error variance, such as inverse-variance weights calculated
tionships, especially when the total sample size is large. Meta-
using the mean correlation as a fixed effect size, also perform well and
analysis not only functions to increase total sample size N, but betterthansimplesample-sizeweightsinsomesituations(Bakbergenulyet
italsoyieldsmoreaccurateestimatesofthemeanandstandard al.,2019;Brannicketal.,2019).
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
192 WIERNIK,WILMOT,DAVISON,ANDONES

## Page 8

Table1
Meta-AnalyticMatricesUsedforCriterionProfileAnalyses
Variable 1 2 3 4 5 6 7 8 9 10
Example1.Workcharacteristicspredictingjobperformancea
1.Autonomy(AU)
2.Skillvariety(SV) .64
3.Taskvariety(TV) .46 .52
4.Tasksignificance(TS) .50 .62 .52
5.Taskidentification(TI) .55 .37 .39 .39
6.Feedbackfromthejob(FJ) .53 .50 .40 .56 .49
7.Jobcomplexity(JC) .43 .51 .62 .31 .22 .21
8.Interdependence(IN) .29 .61 .18 .50 .19 .41 .37
9.Feedbackfromothers(FO) .48 .37 .10 .36 .31 .57 .01 .33
10.Socialsupport(SS) .38 .36 .21 .39 .24 .27 .12 .46 .38
11.Supervisor-ratedjobperformance .23 .07 .23 .23 .17 .20 .37 .18 .28 .12
Example2.GREsubtestspredictinggraduatestudentGPAb
1.GREverbal(V)
2.GREquantitative(Q) .56
3.GREanalytical(A) .77 .73
4.GraduateschoolGPA .34 .32 .36
Example3.BigFivetraitspredictingtraitmindfulnessc
1.EmotionalStability(ES) .31 .33 .27 .09 .57
2.Agreeableness(A) .24 .41 .20 .19 .32
3.Conscientiousness(C) .27 .32 .19 .12 .41
4.Extraversion(Ex) .22 .16 .15 .33 .20
5.Openness(O) .07 .15 .09 .26 .19
6.Traitmindfulness .47 .26 .34 .17 .15
Example4.BigFivetraitspredictingpsychologicaldisordersd
1.EmotionalStability(ES)
2.Agreeableness(A) .31
3.Conscientiousness(C) .33 .41
4.Extraversion(Ex) .27 .20 .19
5.Openness(O) .09 .19 .12 .33
6.Majordepressivedisorder(MDD) (cid:3).47 (cid:3).06 (cid:3).36 (cid:3).25 (cid:3).08
7.Socialphobia(SP) (cid:3).41 .11 (cid:3).34 (cid:3).37 (cid:3).15
8.Substanceusedisorder(SUD) (cid:3).36 (cid:3).27 (cid:3).44 (cid:3).16 (cid:3).07
Note. GRE(cid:2)graduaterecordexamination;GPA(cid:2)gradepointaverage.
aCorrelations corrected for measurement error from Humphrey, Nahrgang, and Morgeson (2007); harmonic mean N (cid:2) 3,444; work characteristic
intercorrelationksrange2–111;workcharacteristic–performancecorrelationksrange2–42. bCorrelationscorrectedforcriterionmeasurementerrorand
predictorrangerestrictionfromKuncel,Hezlett,andOnes(2001);harmonicmeanN(cid:2)5,089;GREintercorrelationksrange2–7;GRE–GPAcorrelation
ks range 2–103. cObserved correlations below the diagonal, correlations corrected for measurement error above the diagonal; Big Five–mindfulness
correlations from Hanley and Garland (2017), Big Five intercorrelations from Davies, Connelly, Ones, and Birkland (2015); mindfulness reliability
estimatedas(cid:11)(cid:2).85(Giluk,2009);harmonicmeanN(cid:2)17,060;BigFiveintercorrelationksrange148–211;BigFive–mindfulnesscorrelationksrange
25–45. dCorrelations corrected for measurement error, Big Five–disorder correlations from Kotov, Gamez, Schmidt, and Watson (2010), Big Five
intercorrelationsfromDaviesetal.(2015);harmonicmeanNs(cid:2)49,409(MDD),25,283(SP),51,626(SUD);BigFiveintercorrelationksrange148–211;
BigFive–disordercorrelationksrange4–63.
ration of design features. These results support findings from work and clarity from feedback, without overwhelming em-
work design research that so-called “enriched jobs” can some- ployees with diverse skill demands, are the most effective for
times overwhelm employees and reduce motivation and, there- motivating high performance levels. In this example, both the
fore, job performance. profile level and pattern effects are important.
Because several job characteristics correlated strongly (e.g.,
autonomy and skill variety, (cid:10) (cid:2) .64), we applied fungible Example 2: MACPA Showing a Negligible Pattern
profile analysis with (cid:6)R2 values of (cid:3).005 and (cid:3).010 to exam- Effect—GRE Scores and Graduate School GPA
ine the sensitivity of the shape of the criterion pattern. Results
presented in Figure 2A show that feedback from others, job Second, we apply MACPA to another fully corrected meta-
complexity, and (low) skill variety were consistently the most analytic correlation matrix. Kuncel, Hezlett, and Ones (2001)
prominentpeaksandvalleysofthecriterionprofilepatternover examined the validity of graduate record examination (GRE)
minor losses of predictive power. Thus, fungible profile anal- subtest scores for predicting graduate school success criteria,
yses support the conclusion that jobs providing challenging including grade point average (GPA). Kuncel et al. (2001)
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
META-ANALYTICCRITERIONPROFILEANALYSIS 193

## Page 9

Table2
ResultsofMeta-AnalyticCriterionProfileAnalyses
Total Leveleffect Patterneffect
Inputmatrixandvariables R R2 r r2 (cid:5)(cid:6)R2 (cid:4) r r2 (cid:5)(cid:6)R2 (cid:4) r
lev,pat
1.Jobcharacteristicsand .57 .33 .31 .10 .43 .45 .37 .14 .48 .50 (cid:3).29
performance .42,.73 .15,.50 .26,.36 .07,.12 .24,.63 .26,.48 .08,.20 .26,.70 (cid:3).43,(cid:3).15
2.GREsubtestspredicting .38 .15 .38 .15 .15 .38 .02 .0004 .00 .00 .05
graduateGPA .34,.43 .11,.18 .34,.42 .11,.18 .11,.18 .00,.34 .00,.11 .00,.22 (cid:3)1.0,1.0
3.BigFivetraitsand
mindfulness
Observed .54 .29 .47 .22 .46 .46 .27 .07 .26 .26 .02
.50,.57 .25,.33 .43,.50 .18,.25 .41,.51 .22,.32 .05,.10 .19,.34 (cid:3).007,.04
Corrected .63 .40 .54 .29 .54 .54 .33 .11 .32 .32 .01
.58,.67 .34,.45 .50,.58 .24,.34 .47,.60 .27,.39 .07,.15 .24,.41 (cid:3).02,.04
4.BigFivetraitsand
psychologicaldisorders
Majordepressivedisorder .56 .31 (cid:3).39 .15 (cid:3).39 (cid:3).39 .40 .16 .40 .40 (cid:3).002
.50,.62 .24,.38 (cid:3).44,(cid:3).34 .11,.19 (cid:3).47,(cid:3).30 .32,.48 .09,.23 .31,.50 (cid:3).03,.03
Socialphobia .65 .42 (cid:3).37 .14 (cid:3).38 (cid:3).38 .52 .27 .53 .53 .02
.51,.79 .24,.60 (cid:3).45,(cid:3).29 .08,.20 (cid:3).61,(cid:3).15 .34,.71 .08,.46 .28,.78 (cid:3).01,.05
Substanceusedisorder .50 .25 (cid:3).41 .17 (cid:3).40 (cid:3).40 .30 .09 .28 .28 (cid:3).05
.42,.58 .17,.33 (cid:3).47,(cid:3).35 .12,.22 (cid:3).50,(cid:3).30 .21,.39 .04,.14 .14,.41 (cid:3).09,(cid:3).01
Note. GRE (cid:2) graduate record examination; GPA (cid:2) grade point average. Results based on estimated population R2 (Equation 9), adjusted using the
harmonicmeansamplesizeofcontributingmeta-analyses;R(cid:2)totalregressionmodelmultiplecorrelation;r(cid:2)zero-ordercorrelationbetweeneffectand
criterion; (cid:5)(cid:6)R2 (cid:2) signed square root of incremental R2 (i.e., semipartial correlation) for effect beyond the other effect; (cid:4) (cid:2) standardized regression
coefficientformodelincludingbothlevelandpatterneffects;r (cid:2)correlationbetweenlevelandpatterneffects;valuesinitalicsare95%deltamethod
lev,pat
confidenceintervals(AppendixD).
corrected criterion variables for measurement error and the combinedtheirresultswithameta-analyticcorrelationmatrixamong
GRE subscales for range restriction relative to the applicant theBigFive(Davies,Connelly,Ones,&Birkland,2015).Tocorrect
pool; however, they did not correct GRE scores for measure- formeasurementerror,weusedinternalconsistenciesfortheBigFive
menterror,asadmissionsdecisionsaremadebasedonobserved andtraitmindfulnessreportedbyDavies,Connelly,Ones,andBirk-
testscores.Wechosethismeta-analysisbecausedecisionmak- land(2015)andGiluk(2009),respectfully.Bothmeta-analyseswere
ersoftenwonderwhetherthereisvalueinattendingtospecific basedongeneralpopulationsamples,sowedidnotcorrectforrange
subtests or if only the GRE total composite is relevant. We restriction. Some scholars argue that compound personality traits,
examined this question for the three primary GRE subtests suchasmindfulness,shouldbeconceptualizedasaconfigurationof
(verbal, quantitative, and analytical).
highandlowlevelsacrossmultipletraits(Judge&Erez,2007;Ones
As Figure 1B shows, the criterion pattern was flat, with no
& Viswesvaran, 2001; Ones, Wiernik, Wilmot, & Kostal, 2016;
pronounced high or low predictors. Likewise, Table 2 shows
Stanek&Ones,2018).Thus,wechosethismeta-analysistoevaluate
thatallthepredictivepoweroftheGREsubscalesforgraduate
thishypothesisfortraitmindfulness.
GPAareattributabletotheprofilelevel(r (cid:2).38),nottothe
lev As Figure 1C shows, the criterion pattern was marked by ele-
within-person profile pattern (r (cid:2) .02, (cid:5)(cid:6)R2(cid:2) .00). These
pat vated Emotional Stability, as well as low levels of Extraversion
findings were consistent under fungible profile analysis (see
and Openness. Low Agreeableness initially appeared to be an
Figure2B).Thus,resultssuggestthatevaluationoftheGREfor
additional marker, but it was unstable in the fungible profile
predictinggraduateGPAshouldfocusonthetotalscore,notthe
analysis (see Figure 2C). Illustrating the importance of measure-
scores of its subtests. In this example, only the profile level
ment error correction, the criterion pattern was more pronounced
effect, not the pattern effect, is important for predicting the
and accounted for more variance when MACPA was conducted
criterion.
usingcorrectedcorrelations.
Comparinglevelandpatterneffects,Table2showstraitmind-
Example 3: Combining Results from Multiple
fulnessrelatessubstantiallytobothanindividual’soveralllevelof
Meta-Analyses and Applying Post-Hoc Reliability traits relevant to adaptation (r (cid:2) .54) and the degree to which
Corrections—Big Five Personality Traits lev
theirtraitconfigurationmatchestheprototypicalmindfulnesscri-
and Trait Mindfulness terionpattern(r (cid:2).33, (cid:5)(cid:6)R2(cid:2).32).Thus,thougheachofthe
pat
Third,wecombinedmeta-analyticcorrelationsfrommultiplepub- Big Five relates positively to trait mindfulness, mindfulness ten-
lished meta-analyses and corrected for artifacts, before applying dencies are strongest for those whose personality configurations
MACPA. Hanley and Garland (2017) meta-analyzed relationships are marked by higher emotional adjustment and relatively lower
between the Big Five personality traits and trait mindfulness. We needs for cognitive exploration and social stimulation, compared
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
194 WIERNIK,WILMOT,DAVISON,ANDONES

## Page 10

0.3
0.2
0.1
0.0
-0.1
-0.2
-0.3
V Q A
GRE Subtests
withtheirothertraits.Thus,inthisexample,onceagain,boththe ranged .30 to .52, (cid:5)(cid:6)R2 ranged .28 to .53). However, each
profilelevelandpatterneffectsareimportant. diagnosis had its own distinct criterion pattern (see Figure 1D).
MajordepressivedisorderwasmarkedbyhighAgreeablenessand
Example 4: Comparing MAPCA Profiles for lowEmotionalStabilityandConscientiousness.Socialphobiahad
Multiple Criteria—Personality Traits a similar configuration, with the addition of low Extraversion.
and Psychological Disorders Substance use disorder was marked with a configuration of low
Conscientiousness, as well as high levels of Extraversion and
Fourth, we compared MACPA criterion patterns across re-
Openness.Fungibleprofileanalyses(Figures2D–2F)showedthat
lated criterion variables. Kotov, Gamez, Schmidt, and Watson
the shapes of these criterion patterns were quite stable. Thus,
(2010) meta-analyzed relationships between personality traits
individualsaremostatriskforaspecificdisorderwhentheirtrait
and diagnoses for several psychological disorders. Kotov et al.
profile combines a high overall level of maladaptive traits along
(2010) corrected correlations for measurement error. We com-
withakeyconfigurationofhighandlowtendencies.Forexample,
bined results with the corrected Big Five matrix described in
depressionisassociatedwithatraitconfigurationwhereaperson’s
Example 3. We chose this meta-analysis to examine whether
trait configurations are risk factors for specific disorders or if needs for interdependence and empathy (high Agreeableness rel-
disorders reflect overall low levels of adaptive traits (cf. psy- ative to other traits) are out of step with their low capacity for
chopathology “P factor”; Markon, Krueger, & Watson, 2005), emotional or impulse control (low Emotional Stability and Con-
as well as whether different disorders are associated with sim- scientiousness).Incontrast,substanceuseisassociatedwithatrait
ilar or distinct trait patterns. configurationmarkedbypersonalweaknessesforimpulsecontrol
Results showed that all diagnoses related significantly to both (low Conscientiousness), as well as relatively elevated needs for
profile level (r ranged (cid:3).38 to (cid:3).40) and profile pattern (r stimulationandnovelty(highExtraversionandOpenness).Inthis
lev pat
*β
A B
C D
Figure 1. Criterion patterns for example methods for meta-analytic criterion profile analysis (MACPA)
analyses.Errorbarsare95%deltamethodconfidenceintervals.GRE(cid:2)graduaterecordexamination;GPA(cid:2)
gradepointaverage.Seetheonlinearticleforthecolorversionofthisfigure.
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
META-ANALYTICCRITERIONPROFILEANALYSIS 195

## Page 11

1.0
0.5
0.0
-0.5
-1.0
AU SV TV TS TI FJ JC IN FO SS
Job characteristics
example, both profile level and pattern effects are important for data.Theseexamplesfocusedoneffectsattheindividuallevel.
predicting the criterion, with the shape of the optimal pattern Althoughspaceprohibitsmoreexampleshere,itisimportantto
varyingacrossdisorders. note that MACPA can also be used to examine configural
effects at the group level and as part of meta-regression. Ex-
Supplemental Examples
amples of these applications from organizational psychology,
The above examples show the utility of MACPA for explor- human resource management, and social psychology are in-
ing previously unexamined configural effects in meta-analytic cluded in the online supplemental materials.
*β
Observed Pattern
Fungible Pattern [−.005]
Fungible Pattern [−.010]
0.50
0.25
0.00
-0.25
V Q A
GRE Subtests
*β
A
B C
Observed Pattern
Fungible Pattern [−.005]
Fungible Pattern [−.010]
Figure 2. Fungible patterns for example methods for meta-analytic criterion profile analysis (MACPA)
analyses. Error bars are 95% delta method confidence intervals for the observed criterion pattern elements.
GRE(cid:2)graduaterecordexamination;GPA(cid:2)gradepointaverage.Seetheonlinearticleforthecolorversion
ofthisfigure.(Figurecontinuesonnextpage.)
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
196 WIERNIK,WILMOT,DAVISON,ANDONES

## Page 12

0.2
0.0
-0.2
ES A C Ex O
Big Five Trait
Additional Considerations and Caveats Comparability of Included Correlations
A key potential application of MACPA is to examine profile ThemostcriticalconsiderationwhenconductingMACPAwith
levelandpatterneffectsforsetsofpredictorsthatmayhavenever syntheticcorrelationmatricesistoensurethatallcorrelationsare
been examined in any single study. Accordingly, researchers can comparableintermsofthepopulationstheyrepresent.Researchers
applyMACPAtoacorrelationmatrixcompiledusingresultsfrom shouldavoidconstructinga“franken-matrix”,whichcontainscor-
many individual bivariate meta-analyses. However, conducting relations from wildly different populations or contexts. Accord-
MACPAwithsuchsyntheticcorrelationmatricespresentsseveral ingly,researchersshouldverifythatallcontributingmeta-analyses
challenges that researchers must address to ensure accurate and had similar inclusion criteria for factors relevant for the research
meaningfulresults. questions at hand, such as age and type of participants (e.g.,
*β
D E
F
Observed Pattern
Fungible Pattern [−.005]
Fungible Pattern [−.010]
Figure2. (continued)
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
META-ANALYTICCRITERIONPROFILEANALYSIS 197

## Page 13

children, clinical patients, etc.) and study design features (e.g., Second-Order Sampling Error
cross-sectionalvs.longitudinal).Forexample,iftheobjectiveisto
Second-order sampling error is also a concern in applying
determine whether configurations of cognitive abilities predict
MACPA. If a contributing meta-analysis is based on a small
performancefordifferentuniversitymajors,itwouldbeimproper
number of samples (k), substantial uncertainty will remain in the
to use correlations from meta-analyses with elementary school
distribution, even if it is based on a large total N. The reason is
samples.Similarly,allcorrelationsshouldbecomparableinterms becausesmall-kmeta-analyseshavelittlepowertoestimateeffect
ofcorrectionsforstatisticalartifacts(i.e.,correctingformeasure- size heterogeneity between-studies (i.e., (cid:12) or SD ). Thus, if any
(cid:10)
ment error10 and selection effects to reflect the same target pop- contributing meta-analysis has small k, MACPA conclusions
ulation). shouldbeconsideredtentative.Usingdeltamethodestimators(see
Appendix D) to construct confidence intervals is a solution that
can better capture the impact of second-order sampling error,
Improper Matrices particularly if it is combined with a Bayesian estimate of SD
(cid:10)
(P.D.G.Steel,Kammeyer-Mueller,&Paterson,2015).
When correlations in a meta-analytic matrix are based on dif-
ferent samples, the resulting matrix can sometimes be improper
(i.e.,nonpositivedefinite).Thismeansthatthespecificcorrelation Heterogeneity
matrix used could not be observed with real data in a single
Most meta-analyses of psychological constructs report non-
sample. Improper matrices are a concern because they prohibit
negligible heterogeneity in effect sizes, which suggests the pres-
multivariate analyses using maximum likelihood estimation and
ence of unaccounted for moderators or artifacts. As a result,
can prevent computation of standard errors in generalized least
cautionisurgedwheninterpretingMACPAresultsinthepresence
squares methods (Yuan, 2016). Counterintuitively, improper ma-
ofsubstantialeffectsizeheterogeneity.Inthesecases,resultsmay
trices are more likely to occur when corrections for statistical
only apply to certain subpopulations or in limited contexts. Con-
artifactsareapplied.Thisdoesnotmeanthatmeta-analyticcorre-
sequently,whenanalyzingheterogeneousmatrices,wheneverpos-
lationmatricesorartifactcorrectionsareinvalid,butratherthata
sible, moderator analyses should be conducted first to identify
value from the credibility interval other than the mean must be subpopulations or contexts where effects are less variable. After-
usedforoneormorecorrelations.11Inthesecases,MACPAcanbe
ward,MACPAcanbeconductedonmorehomogeneousmatrices.
performedby“smoothing”thematrixtoobtainapositive-definite Ifsubstantialheterogeneityremains,sensitivityanalysesshouldbe
correlationmatrixthatisascloseaspossibletotheoriginal.12 runtoexaminehowresultschangeifvaluesfromvariouspointsin
meta-analyses’ credibility intervals are substituted for mean val-
ues. Yu, Downes, Carter, and O’Boyle (2016) present bootstrap
Choice of Sample Size
methods for constructing credibility intervals around model pa-
Individual cells of meta-analytic correlation matrices are often rameters in meta-analytic structural equations models (see also
basedondifferenttotalsamplesizes.Thisraisesthequestionasto Hedges, 2016). These methods can also be used to construct
credibilityintervalsforMACPAparameters.Ifcredibilityintervals
what sample size(s) is appropriate to use for MACPA. Sample
for MACPA parameters are wide, strong inferences about ob-
sizes are used in two ways in multivariate analyses: (a) to test
servedcriterionpatternsshouldbeavoided.
overall structural equations model fit and to compute fit indices,
and (b) to estimate uncertainty for model parameters. Because
MACPA, like OLS regression, uses a fully saturated structural Discussion
equationmodel,theoverallmodelfittestisperfectbyconstraint
((cid:9)2 (cid:2) 0, df (cid:2) 0). Consequently, MACPA sample sizes are only Criterion profile analysis (CPA) provides a unique alternative
perspective on the meaning of predictor–criterion relations. It
neededtoestimateconfidenceintervalsforMACPAparameters.A
showsthatOLSregressionmodelscanbeinterpretedasthejoint
commonsolutionistousethearithmeticorharmonicmeansample
influenceofprofileelevationandwithin-personconfigurationsof
sizeacrossthecontributingmeta-analyses(Landis,2013).Viswes-
scores on the criterion (Davison & Davenport, 2002). CPA iden-
varanandOnes(1995)recommendedtheharmonicmean(i.e.,the
reciprocal of the mean reciprocal sample size), which helps to
conservatively balance uncertainty associated with larger and 10If pattern and level scores will be used to inform decision making
smallersamplesizes.Analternative,moreaccurateapproachisto (e.g.,toselectemployeesordiagnosedisorders),theiroperationalvalidity
shouldbeestimatedbycorrectingformeasurementerrorinthecriterion
estimate uncertainty using the delta method (cf. Becker, 1992;
variableonly,asdecisionsinpracticemustbemadeusingobservedscores,
Olkin&Finn,1995).Here,variancesofMACPAparametersare ratherthanerror-freetruescores(Schmidt&Hunter,2015).Further,the
estimated as a weighted sum of the variances of each element of intercorrelationsamongthepredictorsusedintheMACPAshouldalsobe
the meta-analytic correlation matrix. This method incorporates valuesnotcorrectedformeasurementerror.
11Alternativepossibilitiesare(a)second-ordersamplingerrorperturbed
the uncertainty associated with each contributing meta-analysis
one or more correlations from their true values, (b) correlations in the
when determining the overall uncertainty in the MACPA results. matrixdonotallrepresentthesamepopulation,or(c)someartefactvalues
Delta method standard errors for each MACPA statistic are werepoorestimates.
12KrachtandWaller(2018a,2018b)comparedtheaccuracyofsmooth-
giveninAppendixD,andRcodeimplementingthesemethodsin
ingalgorithmsandfoundthatthemethodbyHigham(2002;implemented
the configural package, available at https://cran.r-project.org/
in R as the Matrix::nearPD() function) yields the most accurate
package(cid:2)configuralandathttps://doi.org/10.17605/osf.io/aqmpc. results.
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
198 WIERNIK,WILMOT,DAVISON,ANDONES

## Page 14

tifiestheconfigurationofpredictorscoresthatoptimallyrelatesto effectiveinterpretationandapplicationofassessmentinformation.
the criterion variable, but current methods are limited to primary Althoughoptimaldata-drivenselectiondecisionscanbemadeby
data.Themethodsdetailedinthisarticleexpandtheapplicability selecting top-down using regression-based composite scores, in
ofCPAtoawiderrangeofresearchcontexts,includingreanalysis applied practice, most decisions are made using some form of
of published studies from a pattern perspective and integrating holisticorsubjectivejudgments.Thiscanbeproblematicbecause
CPA into the research synthesis process through meta-analytic humanjudgmentisnotoriouslypooratreliablyintegratingmulti-
criterionprofileanalysis(MACPA). plepiecesofdatatomakepredictions(Kuncel,Klieger,Connelly,
& Ones, 2013). A major reason for the enduring popularity of
Contributions subjectivejudgmentsisjudges’interestinincorporatingconfigural
effectsintodecisions(cf.Kulas,2013).Accordingly,MACPAcan
Thisarticlemakesfourmethodologicalcontributions.First,we
provideanavenuetoimprovethevalidityofsubjectivejudgments
showed how CPA pattern and level effects can be estimated
by steering judges to focus on empirically defensible, criterion-
withoutaccesstoindividual-leveldata,whichopensthepossibility
validconfiguraleffects,ratherthanspuriousorirrelevantpredictor
ofreanalyzingpublisheddataandinterpretingmeta-analysesfrom
patterns.MACPAcanbeusedtoidentifythecriterionpatternfor
a pattern perspective. We presented methods for constructing a desired outcome, and then judges can be trained to identify
confidenceintervalsandstatisticaltestsforparameters,including
candidates that match this prototypical pattern (cf. Asendorpf,
in meta-analyses, allowing for consideration of sampling uncer-
2006). This can simplify subjective judgments involving many
tainty when interpreting results. Second, we presented statistical
predictorsbyreducingthemtoonlytwopiecesofinformation:(a)
methods to adjust the pattern effect (r ) to reduce overfitting
pat,y anoverallimpressionofquality(i.e.,profilelevel);and(b)simi-
andprovideunbiasedestimatesofthepopulationpatterneffect,or
larity to a prototype profile (i.e., criterion pattern similarity; cf.
expected cross-validity, in new samples. Procedures allow for
Davenport & Davison, 2012). Judgments based on these two
overfitting corrections in MACPA applications, but can also be
pieces of information are likely to be more reliable than those
more practical and accurate when applied to primary data than
basedontheoriginallargerpredictorset;thus,MACPAcanhelp
cross-validation(cf.Kromrey&Hines,1996).Third,weaddressed
toimproveholisticdecisionmakingineducation,personnelselec-
critical challenges associated with integrating CPA with psycho-
tion,clinicaldiagnosis,andothercontexts.
metric meta-analysis, including correcting for statistical artifacts,
Training judges to attend to criterion-relevant profile features
estimatinguncertainty,andhandlingnonpositivedefinitematrices
identifiedthroughMACPAcanalsoenhancetheaccessibilityand
and effect size heterogeneity. Fourth, to assess the sensitivity of
acceptabilityofquantitativeassessmentdatatodecision-makers.A
CPAresults,wepresentedproceduresforfungibleprofileanalysis
likelyreasonforthepersistenceofcategoricaltype-basedperson-
(Waller, 2008), which can help researchers to determine whether
ality assessments in lay and applied practice (e.g., Myers-Briggs
resultsarerobusttominorperturbationsofthecorrelationmatrix.
Type Indicator), despite contrary evidence (McCrae & Costa,
We recommend that researchers routinely apply these fungible
1989; Wilmot, Haslam, Tian, & Ones, 2018), is that typological
profile analyses before drawing conclusions about the shape and
systemsareeasierforuntraineduserstounderstandandinterpret
criterion-relatedvalidityofcriterionpatterns.
thanmulti-indicatorscoreprofiles—particularlywhenpresentedas
percentiles or other norm-referenced scores. By describing the pre-
Implications
dictivevalidityofanassessmentbatteryintermsofacharacteristic
ThepatternperspectiveenabledbyMACPAhasapplicationsfor successful “type,” decision-makers may be more willing to rely on
bothpsychologicaltheoryandassessmentpractice. informationderivedfromconstruct-andcriterion-valid,multidimen-
Implications for psychological research and theory. MACPA sional, quantitative measures versus easier-to-understand, but less
canbeuseddescriptivelytocharacterizethenatureofrelationships valid,categorical,orqualitativeassessments.
between predictor variables and a criterion. For example, a strong
pattern effect might suggest that configurations of risk factors
Future Directions
uniquely predispose individuals to psychological disorders, rather
thansimplecumulativeexposure(cf.Dohrenwend,2006).MACPA Several avenues exist for future methodological research to
couldalsobeusedtocomparecriterionpatternsacrossrelatedcon- expand and extend MACPA. One is to incorporate level and
structs (e.g., different disorders, compound personality traits) as a pattern effects for a set of predictors into a broader structural
methodforevaluatingconstructsimilarityordistinctiveness.Further, model for a criterion. For example, researchers interested in
MACPAcanilluminatewithin-personprocessesthroughwhichpre- personality–job performance relationships may wonder whether
dictorsinfluenceoutcomes.Forexample,Davison,Jew,andDaven- theeffectsofoptimaltraitconfigurationaremediatedbyspecific
port (2014) found that motivation to pursue a STEM major was goal pursuit strategies (cf. Barrick, Mount, & Li, 2013). This
highest among individuals who had stronger mathematics versus questioncanbeaddressedbyestimatingmediationmodelsincor-
verbalability,regardlessoftheiroverallgeneralabilitylevel.Simi- poratingoneormorelatentpersonalitycriterionpatternvariables
larly,Dilchert(2007)foundthatindividualswhoemphasizedExtra- (cf.Davison,Chang,&Davenport,2014).Asecondfuturedirec-
version,butdeemphasizedAgreeableness,atworktendedtobemost tionistofurtherdecomposecontrastivepatterneffectsintoeffects
interestedandeffectiveinleadershiproles.Finally,theintraindividual attributabletoprofileshape(i.e.,whichpredictorsareelevatedor
andconfiguralprocessessuggestedbyMACPAarefruitfulavenues depressed in the profile) and profile scatter (i.e., amplitude of
forlongitudinalstudy. profile peaks and valleys). Traditional methods for separating
Implicationsforpsychologicalassessmentpractice. Foras- these effects (e.g., Cronbach & Gleser, 1953) may not fully ac-
sessmentpractice,MACPAcanbeusedprescriptivelytofacilitate count for the relationships of these profile features with external
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
META-ANALYTICCRITERIONPROFILEANALYSIS 199

## Page 15

criteria.Futuredevelopmentsinthisareamayyieldmoreaccurate ysis. Multivariate Behavioral Research, 52, 86–104. http://dx.doi.org/
profile-based predictions and enhance configuration-based judg- 10.1080/00273171.2016.1253452
mentsintheoryandpractice.Futurestudiesmightalsoexplicitly Calin-Jageman,R.J.,&Cumming,G.(2019).Thenewstatisticsforbetter
examine random-effects heterogeneity in CPA effects by meta- science: Ask how much, how uncertain, and what else is known. The
analyzing the results of CPA conducted in primary studies (cf. AmericanStatistician,73,271–280.http://dx.doi.org/10.1080/00031305
.2018.1518266
Becker & Wu, 2007). Finally, the most important and promising
Cattin,P.(1980).Estimationofthepredictivepowerofaregressionmodel.
area for future research is applying the MACPA methods de-
JournalofAppliedPsychology,65,407–414.http://dx.doi.org/10.1037/
scribed here to existing literatures. Many areas of psychological
0021-9010.65.4.407
researchcanbenefitfromconsideringwhetherobservedpredictor–
Caughlin,D.E.(2011).Theimpactofpersonality,informalroles,andteam
criterionrelationshipsrepresentpatternorleveleffects.Weexpect
informal role configuration on team effectiveness (Master’s thesis).
applications of MACPA to reanalysis of existing correlational
Retrievedfromhttp://hdl.handle.net/1805/2469
research and new meta-analyses alike, to open new and exciting Chan,C.-K.(2006).Anexploratorystudyofpredictivevalidityanddiag-
avenues of inquiry into potential mechanisms driving important nostic utility of cognitive profile patterns on the Woodcock-Johnson
criteriaandoutcomes. Psychoeducational Battery-Revised (WJ-R) clinical database
(305305249) [Doctoral dissertation, University of Minnesota]. Pro-
Quest.http://search.proquest.com/docview/305305249
References
Cheung, M. W-L., & Cheung, S. F. (2016). Random-effects models for
Abadir,K.M.,&Magnus,J.R.(2005).Matrixalgebra.NewYork,NY:Cam- meta-analytic structural equation modeling: Review, issues, and illus-
bridgeUniversityPress.http://dx.doi.org/10.1017/CBO9780511810800 trations.ResearchSynthesisMethods,7,140–155.http://dx.doi.org/10
Aguinis,H.,Pierce,C.A.,&Culpepper,S.A.(2009).Scalecoarsenessas .1002/jrsm.1166
amethodologicalartifact:Correctingcorrelationcoefficientsattenuated Cohen,J.,Cohen,P.,West,S.G.,&Aiken,L.S.(2003).Appliedmultiple
fromusingcoarsescales.OrganizationalResearchMethods,12,623– regression/correlation analysis for the behavioral sciences (3rd ed.).
652.http://dx.doi.org/10.1177/1094428108318065 NewYork,NY:Routledge.http://dx.doi.org/10.4324/9780203774441
Alf,E.F.,Jr.,&Abrahams,N.M.(1975).Theuseofextremegroupsin Combs, J., Liu, Y., Hall, A., & Ketchen, D. (2006). How much do
assessing relationships. Psychometrika, 40, 563–572. http://dx.doi.org/ high-performance work practices matter? A meta-analysis of their ef-
10.1007/BF02291557 fects on organizational performance. Personnel Psychology, 59, 501–
Alf,E.F.,Jr.,&Graf,R.G.(1999).Asymptoticconfidencelimitsforthe 528.http://dx.doi.org/10.1111/j.1744-6570.2006.00045.x
difference between two squared multiple correlations: A simplified Cronbach, L. J., & Gleser, G. C. (1953). Assessing similarity between
approach.PsychologicalMethods,4,70–75.http://dx.doi.org/10.1037/ profiles. Psychological Bulletin, 50, 456–473. http://dx.doi.org/10
1082-989X.4.1.70 .1037/h0057173
Anvari,F.,&Lakens,D.(2019).Usinganchor-basedmethodstodetermine Culpepper,S.A.(2008).Conductingexternalprofileanalysiswithmultiple
thesmallesteffectsizeofinterest.PsyArXiv.http://dx.doi.org/10.31234/ regression.PracticalAssessment,Research&Evaluation,13,Article1.
osf.io/syp5a http://dx.doi.org/10.7275/xg59-sp16
Asendorpf, J. B. (2006). Typeness of personality profiles: A continuous Culpepper, S. A., Davenport, E. C., Jr., & Davison, M. L. (2008). A
person-centredapproachtopersonalitydata.EuropeanJournalofPer- method for choosing weights to predict college grades for admission
sonality,20,83–106.http://dx.doi.org/10.1002/per.575 decisionsandtoassesstheirfairnessbyrace/ethnicity.MultipleLinear
Bakbergenuly, I., Hoaglin, D. C., & Kulinskaya, E. (2019). Simulation RegressionViewpoints,34(2),4–14.Retrievedfromhttp://citeseerx.ist
studyofestimatingbetween-studyvarianceandoveralleffectinmeta- .psu.edu/viewdoc/summary?doi(cid:2)10.1.1.576.3616
analysis of standardized mean difference (1903.01362 [stat]). arXiv.
Dahlke, J. A., & Wiernik, B. M. (2019). Not restricted to selection
http://arxiv.org/abs/1903.01362
research: Accounting for indirect range restriction in organizational
Barrick,M.R.,Mount,M.K.,&Li,N.(2013).Thetheoryofpurposeful
research. Organizational Research Methods. Advance online publica-
work behavior: The role of personality, higher-order goals, and job
tion.http://dx.doi.org/10.1177/1094428119859398
characteristics.AcademyofManagementReview,38,132–153.http://dx
Davenport,E.C.,Jr.,&Davison,M.L.(2012).Quantificationofprofiles.
.doi.org/10.5465/amr.2010.0479
ProceedingsoftheFederalCommitteeonStatisticalMethodologyRe-
Beatty,A.S.,Barratt,C.L.,Berry,C.M.,&Sackett,P.R.(2014).Testing
search Conference. Retrieved from https://nces.ed.gov/FCSM/pdf/
thegeneralizabilityofindirectrangerestrictioncorrections.Journalof
Davenport_2012FCSM_V-D.pdf
AppliedPsychology,99,587–598.http://dx.doi.org/10.1037/a0036361
Davies,S.E.,Connelly,B.L.,Ones,D.S.,&Birkland,A.S.(2015).The
Becker, B. J. (1992). Using results from replicated studies to estimate
generalfactorofpersonality:The“BigOne,”aself-evaluativetrait,ora
linearmodels.JournalofEducationalStatistics,17,341–362.http://dx
methodological gnat that won’t go away? Personality and Individual
.doi.org/10.3102/10769986017004341
Differences,81,13–22.http://dx.doi.org/10.1016/j.paid.2015.01.006
Becker,B.J.,&Wu,M.-J.(2007).Thesynthesisofregressionslopesin
Davison,M.L.,Chang,Y.-F.,&Davenport,E.C.,Jr.(2014).Modeling
meta-analysis. Statistical Science, 22, 414–429. http://dx.doi.org/10
.1214/07-STS243 configural patterns in latent variable profiles: Association with an en-
Booth, T., Murray, A. L., Overduin, M., Matthews, M., & Furnham, A. dogenousvariable.StructuralEquationModeling,21,81–93.http://dx
(2016). Distinguishing CEOs from top level management: A profile .doi.org/10.1080/10705511.2014.859507
analysisofindividualdifferences,careerpathsanddemographics.Jour- Davison, M. L., & Davenport, E. C., Jr. (2002). Identifying criterion-
nalofBusinessandPsychology,31,205–216. related patterns of predictor scores using multiple regression. Psycho-
Brannick,M.T.,Potter,S.M.,Benitez,B.,&Morris,S.B.(2019).Bias logicalMethods,7,468–484.http://dx.doi.org/10.1037/1082-989X.7.4
andprecisionofalternateestimatorsinmeta-analysis:Benefitsofblend- .468
ingSchmidt–HunterandHedgesapproaches.OrganizationalResearch Davison, M. L., Davenport, E. C., Jr., Chang, Y.-F., Vue, K., & Su, S.
Methods,22,490–514.http://dx.doi.org/10.1177/1094428117741966 (2015). Criterion-related validity: Assessing the value of subscores.
Bulut, O., Davison, M. L., & Rodriguez, M. C. (2017). Estimating JournalofEducationalMeasurement,52,263–279.http://dx.doi.org/10
between-personandwithin-personsubscorereliabilitywithprofileanal- .1111/jedm.12081
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
200 WIERNIK,WILMOT,DAVISON,ANDONES

## Page 16

Davison,M.L.,Jew,G.B.,&Davenport,E.C.,Jr.(2014).PatternsofSAT Hedges,L.V.(2016).Applyingmeta-analysistostructuralequationmod-
scores,choiceofSTEMmajor,andgender.Measurement&Evaluation eling. Research Synthesis Methods, 7, 209–214. http://dx.doi.org/10
inCounseling&Development,47,118–126.http://dx.doi.org/10.1177/ .1002/jrsm.1214
0748175614522269 Hedges,L.V.,&Olkin,I.(1985).Statisticalmethodsformeta-analysis.
Davison,M.L.,Kim,S.-K.,&Close,C.(2009).Factoranalyticmodeling London,UK:AcademicPress.
of within person variation in score profiles. Multivariate Behavioral Helland, I. S. (1987). On the interpretation and use of R2 in regression
Research,44,668–687.http://dx.doi.org/10.1080/00273170903187665 analysis.Biometrics,43,61–69.http://dx.doi.org/10.2307/2531949
Davison, M. L., & Kuang, H. (2000). Profile patterns: Research and Higham,N.J.(2002).Computingthenearestcorrelationmatrix—Aprob-
professionalinterpretation.SchoolPsychologyQuarterly,15,457–464. lem from finance. IMA Journal of Numerical Analysis, 22, 329–343.
http://dx.doi.org/10.1093/imanum/22.3.329
http://dx.doi.org/10.1037/h0088801
Hoffman, P. J. (1960). The paramorphic representation of clinical judg-
Dawes, R. M. (1975). Graduate admission variables and future success.
ment. Psychological Bulletin, 57, 116–131. http://dx.doi.org/10.1037/
Science,187,721–723.http://dx.doi.org/10.1126/science.187.4178.721
h0047807
Dilchert, S. (2007). Peaks and valleys: Predicting interests in leadership
Humphrey,S.E.,Nahrgang,J.D.,&Morgeson,F.P.(2007).Integrating
andmanagerialpositionsfrompersonalityprofiles.InternationalJour-
motivational, social, and contextual work design features: A meta-
nalofSelectionandAssessment,15,317–334.http://dx.doi.org/10.1111/
analyticsummaryandtheoreticalextensionoftheworkdesignliterature.
j.1468-2389.2007.00391.x
Journal of Applied Psychology, 92, 1332–1356. http://dx.doi.org/10
Dohrenwend,B.P.(2006).Inventoryingstressfullifeeventsasriskfactors
.1037/0021-9010.92.5.1332
forpsychopathology:Towardresolutionoftheproblemofintracategory
Hunter, J. E., & Schmidt, F. L. (1990). Dichotomization of continuous
variability. Psychological Bulletin, 132, 477–495. http://dx.doi.org/10
variables:Theimplicationsformeta-analysis.JournalofAppliedPsy-
.1037/0033-2909.132.3.477
chology,75,334–349.http://dx.doi.org/10.1037/0021-9010.75.3.334
Elwert,F.,&Winship,C.(2014).Endogenousselectionbias:Theproblem
Jak,S.(2015).Meta-analyticstructuralequationmodelling.Cham,Swit-
ofconditioningonacollidervariable.AnnualReviewofSociology,40,
zerland: Springer International Publishing. http://dx.doi.org/10.1007/
31–53.http://dx.doi.org/10.1146/annurev-soc-071913-043455 978-3-319-27174-3
Fisher,R.A.(1921).Ontheprobableerrorofacoefficientofcorrelation Jones,J.A.,&Waller,N.G.(2013).Computingconfidenceintervalsfor
deduced from a small sample. Metron, 1, 3–32. https://hdl.handle.net/ standardized regression coefficients. Psychological Methods, 18, 435–
2440/15169 453.http://dx.doi.org/10.1037/a0033269
Fuller,W.A.(1987).Measurementerrormodels.NewYork,NY:Wiley. Jones,J.A.,&Waller,N.G.(2015).Thenormal-theoryandasymptotic
http://dx.doi.org/10.1002/9780470316665 distribution-free (ADF) covariance matrix of standardized regression
Furlow,C.F.,&Beretvas,S.N.(2005).Meta-analyticmethodsofpooling coefficients: Theoretical extensions and finite sample behavior. Psy-
correlation matrices for structural equation modeling under different chometrika,80,365–378.http://dx.doi.org/10.1007/s11336-013-9380-y
patternsofmissingdata.PsychologicalMethods,10,227–254.http://dx Judge,T.A.,&Erez,A.(2007).Interactionandintersection:Theconstel-
.doi.org/10.1037/1082-989X.10.2.227 lationofemotionalstabilityandextraversioninpredictingperformance.
Ghiselli,E.E.,Campbell,J.P.,&Zedeck,S.(1981).Measurementtheory Personnel Psychology, 60, 573–596. http://dx.doi.org/10.1111/j.1744-
forthebehavioralsciences.SanFrancisco,CA:W.H.Freeman. 6570.2007.00084.x
Giluk, T. L. (2009). Mindfulness, Big Five personality, and affect: A Judge,T.A.,&Zapata,C.P.(2015).Theperson-situationdebaterevisited:
meta-analysis. Personality and Individual Differences, 47, 805–811. EffectofsituationstrengthandtraitactivationonthevalidityoftheBig
http://dx.doi.org/10.1016/j.paid.2009.06.026 Fivepersonalitytraitsinpredictingjobperformance.AcademyofMan-
Grand,J.A.,Pearce,M.,&Kozlowski,S.W.J.(2013,August).Investi- agement Journal, 58, 1149–1179. http://dx.doi.org/10.5465/amj.2010
gating the episodic relationship between team processes and perfor- .0837
mance. Paper presented at the annual meeting of the Academy of Kotov,R.,Gamez,W.,Schmidt,F.,&Watson,D.(2010).Linking“big”
personalitytraitstoanxiety,depressive,andsubstanceusedisorders:A
Management,Orlando,FL.
meta-analysis.PsychologicalBulletin,136,768–821.http://dx.doi.org/
Guest,D.,Conway,N.,&Dewe,P.(2004).Usingsequentialtreeanalysis
10.1037/a0020327
tosearchfor‘bundles’ofHRpractices.HumanResourceManagement
Kracht,J.,&Waller,N.G.(2018a).Acomparisonofmatrixsmoothing
Journal, 14, 79–96. http://dx.doi.org/10.1111/j.1748-8583.2004
algorithms. Multivariate Behavioral Research, 53, 136–137. http://dx
.tb00113.x
.doi.org/10.1080/00273171.2017.1404899
Haberman, S. J. (2008). When can subscores have value? Journal of
Kracht, J., & Waller, N. G. (2018b). Smoothing non-positive definite
Educational and Behavioral Statistics, 33, 204–229. http://dx.doi.org/
correlationmatrices:Acomparisonof3methods.Manuscriptsubmitted
10.3102/1076998607302636
forpublication.
Hafdahl, A. R. (2008). Combining heterogeneous correlation matrices:
Kromrey, J. D., & Hines, C. V. (1996). Estimating the coefficient of
Simulation analysis of fixed-effects methods. Journal of Educational
cross-validity in multiple regression: A comparison of analytical and
and Behavioral Statistics, 33, 507–533. http://dx.doi.org/10.3102/
empirical methods. Journal of Experimental Education, 64, 240–266.
1076998607309472
http://dx.doi.org/10.1080/00220973.1996.9943806
Hafdahl, A. R. (2010). Random-effects meta-analysis of correlations:
Kruschke,J.K.(2018).RejectingoracceptingparametervaluesinBayes-
MonteCarloevaluationofmeanestimators.BritishJournalofMathe- ian estimation. Advances in Methods and Practices in Psychological
matical & Statistical Psychology, 63, 227–254. http://dx.doi.org/10 Science,1,270–280.http://dx.doi.org/10.1177/2515245918771304
.1348/000711009X431914 Kulas,J.T.(2013).Personality-basedprofilematchinginpersonnelselec-
Hanley, A. W., & Garland, E. L. (2017). The mindful personality: A tion: Estimates of method prevalence and criterion-related validity.
meta-analysis from a cybernetic perspective. Mindfulness, 8, 1456– Applied Psychology, 62, 519–542. http://dx.doi.org/10.1111/j.1464-
1470.http://dx.doi.org/10.1007/s12671-017-0736-8 0597.2012.00491.x
Hastie, T., Tibshirani, R., & Friedman, J. H. (2009). The elements of Kuncel, N. R., Hezlett, S. A., & Ones, D. S. (2001). A comprehensive
statistical learning: Data mining, inference, and prediction (2nd ed.). meta-analysisofthepredictivevalidityofthegraduaterecordexamina-
NewYork,NY:Springer.http://dx.doi.org/10.1007/978-0-387-84858-7 tions:Implicationsforgraduatestudentselectionandperformance.Psy-
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
META-ANALYTICCRITERIONPROFILEANALYSIS 201

## Page 17

chologicalBulletin,127,162–181.http://dx.doi.org/10.1037/0033-2909 Olkin,I.,&Finn,J.D.(1995).Correlationsredux.PsychologicalBulletin,
.127.1.162 118,155–164.http://dx.doi.org/10.1037/0033-2909.118.1.155
Kuncel, N. R., Klieger, D. M., Connelly, B. S., & Ones, D. S. (2013). Ones,D.S.,&Viswesvaran,C.(2001).IntegritytestsandotherCriterion-
Mechanicalversusclinicaldatacombinationinselectionandadmissions Focused Occupational Personality Scales (COPS) used in personnel
decisions:Ameta-analysis.JournalofAppliedPsychology,98,1060– selection.InternationalJournalofSelectionandAssessment,9,31–39.
1072.http://dx.doi.org/10.1037/a0034156 http://dx.doi.org/10.1111/1468-2389.00161
Landis,R.S.(2013).Successfullycombiningmeta-analysisandstructural Ones, D. S., Wiernik, B. M., Wilmot, M. P., & Kostal, J. W. (2016).
equationmodeling:Recommendationsandstrategies.JournalofBusi- Conceptualandmethodologicalcomplexityofnarrowtraitmeasuresin
ness and Psychology, 28, 251–261. http://dx.doi.org/10.1007/s10869- personality-outcome research: Better knowledge by partitioning vari-
013-9285-x ance from multiple latent traits and measurement artifacts. European
Laue, S., Mitterreiter, M., & Giesen, J. (2018). Computing higher order JournalofPersonality,30,319–321.
derivativesofmatrixandtensorexpressions.InS.Bengio,H.Wallach, Oort, F. J., & Jak, S. (2016). Maximum likelihood estimation in meta-
H. Larochelle, K. Grauman, N. Cesa-Bianchi, & R. Garnett (Eds.), analytic structural equation modeling. Research Synthesis Methods, 7,
Advancesinneuralinformationprocessingsystems31(NIPS;Vol.31, 156–167.http://dx.doi.org/10.1002/jrsm.1203
pp.2755–2764).Montréal,Canada:CurranAssociates.Retrievedfrom Perry, J. C. (2008). School engagement among urban youth of color:
https://papers.nips.cc/paper/7540-computing-higher-order-derivatives- Criterion pattern effects of vocational exploration and racial identity.
of-matrix-and-tensor-expressions JournalofCareerDevelopment,34,397–422.http://dx.doi.org/10.1177/
LePine,J.A.,Piccolo,R.F.,Jackson,C.L.,Mathieu,J.E.,&Saul,J.R. 0894845308316293
(2008).Ameta-analysisofteamworkprocesses:Testsofamultidimen-
Pettigrew,T.F.,&Tropp,L.R.(2006).Ameta-analytictestofintergroup
sionalmodelandrelationshipswithteameffectivenesscriteria.Person-
contacttheory.JournalofPersonalityandSocialPsychology,90,751–
nel Psychology, 61, 273–307. http://dx.doi.org/10.1111/j.1744-6570
783.http://dx.doi.org/10.1037/0022-3514.90.5.751
.2008.00114.x
Quintana, D. S. (2015). From pre-registration to publication: A non-
Lyons, J. (2015). Examining the influence of womanist identity attitudes
technical primer for conducting a meta-analysis to synthesize correla-
andconformitytogendernormsonthementalhealthofwomeninthe
tionaldata.FrontiersinPsychology,6,1549.http://dx.doi.org/10.3389/
U.S. (Doctoral dissertation, Columbia University). http://dx.doi.org/10
fpsyg.2015.01549
.7916/D86W98W7
Ree, M. J., Earles, J. A., & Teachout, M. S. (1994). Predicting job
Markon, K. E., Krueger, R. F., & Watson, D. (2005). Delineating the
performance:Notmuchmorethang.JournalofAppliedPsychology,79,
structureofnormalandabnormalpersonality:Anintegrativehierarchi-
518–524.http://dx.doi.org/10.1037/0021-9010.79.4.518
calapproach.JournalofPersonalityandSocialPsychology,88,139–
Rosopa,P.J.,&Kim,B.(2017).Robustnessofstatisticalinferencesusing
157.http://dx.doi.org/10.1037/0022-3514.88.1.139
linearmodelswithmeta-analyticcorrelationmatrices.HumanResource
McCrae,R.R.,&Costa,P.T.,Jr.(1989).ReinterpretingtheMyers-Briggs
Management Review, 27, 216–236. http://dx.doi.org/10.1016/j.hrmr
TypeIndicatorfromtheperspectiveofthefive-factormodelofperson-
.2016.09.012
ality. Journal of Personality, 57, 17–40. http://dx.doi.org/10.1111/j
Sackett, P. R., Lievens, F., Berry, C. M., & Landers, R. N. (2007). A
.1467-6494.1989.tb00759.x
cautionarynoteontheeffectsofrangerestrictiononpredictorintercor-
McGrath,R.E.,&Meyer,G.J.(2006).Wheneffectsizesdisagree:The
relations.JournalofAppliedPsychology,92,538–544.http://dx.doi.org/
caseofrandd.PsychologicalMethods,11,386–401.http://dx.doi.org/
10.1037/0021-9010.92.2.538
10.1037/1082-989X.11.4.386
Sackett, P. R., & Yang, H. (2000). Correction for range restriction: An
Meehl,P.E.(1950).Configuralscoring.JournalofConsultingPsychol-
expandedtypology.JournalofAppliedPsychology,85,112–118.http://
ogy,14,165–171.http://dx.doi.org/10.1037/h0058049
dx.doi.org/10.1037/0021-9010.85.1.112
Mendoza, J. L., & Stafford, K. L. (2001). Confidence intervals, power
Schennach, S. M. (2016). Recent advances in the measurement error
calculation,andsamplesizeestimationforthesquaredmultiplecorre-
literature. Annual Review of Economics, 8, 341–377. http://dx.doi.org/
lation coefficient under the fixed and random regression models: A
10.1146/annurev-economics-080315-015058
computerprogramandusefulstandardtables.EducationalandPsycho-
Schmidt,F.L.(1971).Therelativeefficiencyofregressionandsimpleunit
logical Measurement, 61, 650–667. http://dx.doi.org/10.1177/
predictor weights in applied differential psychology. Educational and
00131640121971419
Michel, J. S., Viswesvaran, C., & Thomas, J. (2011). Conclusions from Psychological Measurement, 31, 699–714. http://dx.doi.org/10.1177/
meta-analyticstructuralequationmodelsgenerallydonotchangedueto 001316447103100310
correctionsforstudyartifacts.ResearchSynthesisMethods,2,174–187. Schmidt, F. L. (1992). What do data really mean? Research findings,
http://dx.doi.org/10.1002/jrsm.47 meta-analysis,andcumulativeknowledgeinpsychology.AmericanPsy-
Morse,P.E.,Daegling,D.J.,McGraw,W.S.,&Pampush,J.D.(2013). chologist, 47, 1173–1181. http://dx.doi.org/10.1037/0003-066X.47.10
Dental wear among cercopithecid monkeys of the Taï forest, Côte .1173
d’Ivoire. American Journal of Physical Anthropology, 150, 655–665. Schmidt, F. L. (2017). Statistical and measurement pitfalls in the use of
http://dx.doi.org/10.1002/ajpa.22242 meta-regression in meta-analysis. Career Development International,
Neale,M.C.,&Kendler,K.S.(1995).Modelsofcomorbidityformulti- 22,469–476.http://dx.doi.org/10.1108/CDI-08-2017-0136
factorialdisorders.AmericanJournalofHumanGenetics,57,935–953. Schmidt,F.L.,&Hunter,J.E.(1977).Developmentofageneralsolution
https://europepmc.org/articles/PMC1801512/ totheproblemofvaliditygeneralization.JournalofAppliedPsychology,
Nel, D. G. (1980). On matrix differentiation in statistics. South African 62,529–540.http://dx.doi.org/10.1037/0021-9010.62.5.529
Statistical Journal, 14, 137–193. https://hdl.handle.net/10520/ Schmidt,F.L.,&Hunter,J.E.(1996).Measurementerrorinpsychological
AJA0038271X_668 research:Lessonsfrom26researchscenarios.PsychologicalMethods,1,
Nel,D.G.(1985).Amatrixderivationoftheasymptoticcovariancematrix 199–223.http://dx.doi.org/10.1037/1082-989X.1.2.199
ofsamplecorrelationcoefficients.LinearAlgebraandItsApplications, Schmidt, F. L., & Hunter, J. E. (2015). Methods of meta-analysis: Cor-
67,137–145.http://dx.doi.org/10.1016/0024-3795(85)90191-0 rectingerrorandbiasinresearchfindings(3rded.).ThousandOaks,
Nunnally, J. C. (1978). Psychometric theory (2nd ed.). New York, NY: CA:Sage.http://dx.doi.org/10.4135/9781483398105
McGraw-Hill. Schmidt, F. L., Le, H., & Oh, I.-S. (2009). Correcting for the distorting
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
202 WIERNIK,WILMOT,DAVISON,ANDONES

## Page 18

effectsofstudyartifactsinmeta-analysis.InH.Cooper,L.V.Hedges, chologie mit Zeitschrift fur Angewandte Psychologie, 215, 104–121.
& J. C. Valentine (Eds.), The handbook of research synthesis and http://dx.doi.org/10.1027/0044-3409.215.2.104
meta-analysis(pp.317–333).NewYork,NY:RussellSageFoundation. Viswesvaran,C.,&Ones,D.S.(1995).Theorytesting:Combiningpsy-
Schulze,R.(2004).Meta-analysis:Acomparisonofapproaches.Göttin- chometric meta-analysis and structural equations modeling. Personnel
gen,Germany:HogrefePublishing. Psychology, 48, 865–885. http://dx.doi.org/10.1111/j.1744-6570.1995
Shanock,L.R.,Baran,B.E.,Gentry,W.A.,Pattison,S.C.,&Heggestad, .tb01784.x
E.D.(2010).Polynomialregressionwithresponsesurfaceanalysis:A Viswesvaran,C.,Ones,D.S.,Schmidt,F.L.,Le,H.,&Oh,I.-S.(2014).
powerful approach for examining moderation and overcoming limita- Measurementerrorobfuscatesscientificknowledge:Pathtocumulative
tions of difference scores. Journal of Business and Psychology, 25, knowledgerequirescorrectionsforunreliabilityandpsychometricmeta-
543–554.http://dx.doi.org/10.1007/s10869-010-9183-4 analyses. Industrial and Organizational Psychology: Perspectives on
Shen, W. (2011). The application of a person-oriented criterion-related Science and Practice, 7, 507–518. http://dx.doi.org/10.1017/
configuralapproachtotherelationshipbetweenpersonalitytraitsand S1754942600006799
work behaviors (Doctoral dissertation). Retrieved from https://hdl Wainer,H.(1976).Estimatingcoefficientsinlinearmodels:Itdon’tmake
.handle.net/11299/113566 nonevermind.PsychologicalBulletin,83,213–217.http://dx.doi.org/10
Sheng,Z.,Kong,W.,Cortina,J.M.,&Hou,S.(2016).Analyzingmatrices .1037/0033-2909.83.2.213
of meta-analytic correlations: Current practices and recommendations. Waller, N. G. (2008). Fungible weights in multiple regression. Psy-
ResearchSynthesisMethods,7,187–208.http://dx.doi.org/10.1002/jrsm chometrika,73,691–703.http://dx.doi.org/10.1007/s11336-008-9066-z
.1206
Waller, N. G., & Jones, J. A. (2009). Locating the extrema of fungible
Shieh,G.(2006).Exactintervalestimation,powercalculation,andsample
regression weights. Psychometrika, 74, 589–602. http://dx.doi.org/10
size determination in normal correlation analysis. Psychometrika, 71,
.1007/s11336-008-9087-7
529–540.http://dx.doi.org/10.1007/s11336-04-1221-6
Wang, M.-T., Eccles, J. S., & Kenny, S. (2013). Not lack of ability but
Shieh, G. (2008). Improved shrinkage estimation of squared multiple
morechoice:Individualandgenderdifferencesinchoiceofcareersin
correlationcoefficientandsquaredcross-validitycoefficient.Organiza-
science,technology,engineering,andmathematics.PsychologicalSci-
tional Research Methods, 11, 387–407. http://dx.doi.org/10.1177/
ence,24,770–775.http://dx.doi.org/10.1177/0956797612458937
1094428106292901
Westreich,D.(2012).Berkson’sbias,selectionbias,andmissingdata.
Shieh, G. (2009). Exact analysis of squared cross-validity coefficient in
Epidemiology, 23, 159–164. http://dx.doi.org/10.1097/EDE
predictive regression models. Multivariate Behavioral Research, 44,
.0b013e31823b6296
82–105.http://dx.doi.org/10.1080/00273170802620097
Wiernik,B.M.(2016).Intraindividualpersonalityprofilesassociatedwith
Stanek, K. C., & Ones, D. S. (2018). Taxonomies and compendia of
Realisticinterests.JournalofCareerAssessment,24,460–480.http://
cognitiveabilityandpersonalitymeasuresrelevanttoindustrial,work,
dx.doi.org/10.1177/1069072715599378
andorganizationalpsychology.InD.S.Ones,N.Anderson,C.Viswes-
Wiernik, B. M., & Dahlke, J. A. (2020). Obtaining unbiased results in
varan,&H.K.Sinangil(Eds.),TheSAGEhandbookofindustrial,work
meta-analysis: The importance of correcting for statistical artifacts.
and organizational psychology: Vols. 1: Personnel psychology and
Advances in Methods and Practices in Psychological Science, 3, 94–
employee performance (2nd ed., pp. 366–407). Thousand Oaks, CA:
123.http://dx.doi.org/10.1177/2515245919885611
Sage.http://dx.doi.org/10.4135/9781473914940.n14
Wiernik,B.M.,Dilchert,S.,&Ones,D.S.(2016).Creativeinterestsand
Steel,P.D.G.,Kammeyer-Mueller,J.,&Paterson,T.A.(2015).Improv-
personality: Scientific versus artistic creativity. Zeitschrift für Arbeits-
ing the meta-analytic assessment of effect size variance with an in-
und Organisationspsychologie, 60, 65–78. http://dx.doi.org/10.1026/
formedBayesianprior.JournalofManagement,41,718–743.http://dx
0932-4089/a000211
.doi.org/10.1177/0149206314551964
Wiernik,B.M.,Kostal,J.W.,Wilmot,M.P.,Dilchert,S.,&Ones,D.S.
Steel,R.P.,Shane,G.S.,&Griffeth,R.W.(1990).Correctingturnover
statistics for comparative analysis. Academy of Management Journal, (2017).Empiricalbenchmarksforinterpretingeffectsizevariabilityin
33,179–187. meta-analysis.IndustrialandOrganizationalPsychology:Perspectives
SwinburneRomine,R.E.(2011).Interviewcodingsofattachmentstyle: on Science and Practice, 10, 472–479. http://dx.doi.org/10.1017/iop
Using profile analysis to understand the patterns involved (Doctoral .2017.44
dissertation).Retrievedfromhttps://hdl.handle.net/11299/101937 Wiernik,B.M.,Wilmot,M.P.,&Kostal,J.W.(2015).Howdataanalysis
Thompson,S.G.,&Higgins,J.P.T.(2002).Howshouldmeta-regression candominateinterpretationsofdominantgeneralfactors.Industrialand
analyses be undertaken and interpreted? Statistics in Medicine, 21, Organizational Psychology: Perspectives on Science and Practice, 8,
1559–1573.http://dx.doi.org/10.1002/sim.1187 438–445.http://dx.doi.org/10.1017/iop.2015.60
Tryon, W. W. (2001). Evaluating statistical difference, equivalence, and Wilmot, M. P., Haslam, N., Tian, J., & Ones, D. S. (2018). Direct and
indeterminacyusinginferentialconfidenceintervals:Anintegratedal- conceptualreplicationsofthetaxometricanalysisofTypeAbehavior.
ternativemethodofconductingnullhypothesisstatisticaltests.Psycho- JournalofPersonalityandSocialPsychology.Advanceonlinepublica-
logical Methods, 6, 371–386. http://dx.doi.org/10.1037/1082-989X.6.4 tion.http://dx.doi.org/10.1037/pspp0000195
.371 Yu, J. J., Downes, P. E., Carter, K. M., & O’Boyle, E. H. (2016). The
Van Iddekinge, C. H., Aguinis, H., Mackey, J. D., & DeOrtentiis, P. S. problemofeffectsizeheterogeneityinmeta-analyticstructuralequation
(2018).Ameta-analysisoftheinteractive,additive,andrelativeeffects modeling.JournalofAppliedPsychology,101,1457–1473.http://dx.doi
ofcognitiveabilityandmotivationonperformance.JournalofManage- .org/10.1037/apl0000141
ment,44,249–279.http://dx.doi.org/10.1177/0149206317702220 Yuan,K.-H.(2016).Metaanalyticalstructuralequationmodeling:Com-
Viechtbauer,W.(2007).Accountingforheterogeneityviarandom-effects mentsonissueswithcurrentmethodsandviablealternatives.Research
models and moderator analyses in meta-analysis. Zeitschrift fur Psy- SynthesisMethods,7,215–231.http://dx.doi.org/10.1002/jrsm.1213
(Appendicesfollow)
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
META-ANALYTICCRITERIONPROFILEANALYSIS 203

## Page 19

Appendix A
Derivations of Equations for Correlations With Profile Level and Criterion Pattern From Summary Data
ThisappendixprovidesproofsforEquations1–3. wherec isthecolumnvectorofcovariancesbetweenthepredic-
xy
tor variables and the criterion, C is the variance-covariance
xx
Level Effect matrixamongthexvariables,1isacolumnvectorof1s,andSD
y
isthestandarddeviationofthecriterionvariable.
Foreachpersoni,letX (cid:2)(x ,x ,x ,...,x )=beavectorof
i 1i 2i 3i pi
ppredictorscoresandybeascoreonacriterionvariable.Themost
Pattern Effect
commonformofdataformeta-analyticcriterionprofileanalysisis
amatrixofmeta-analyticmeancorrelations.Suchdatatreaty and Continuing from above, let X* (cid:3) (cid:3)x (cid:2) x ,x (cid:2) x ,
eachx asstandardscoreswithmean(cid:2)0andSD(cid:2)1.Form i ulas x (cid:2) x ,...,x (cid:2) x (cid:4)(cid:2) be each i person’s 1i profile l p ev a i tte 2 r i n (i.e., l t e h v e i
for un j s i tandardized variables are presented below. Let x (cid:3) v 3 e i ctor l o ev f i deviat p i i ons o le f vi each of the p predictor scores from the
(cid:2) levi
X ⁄pbeaperson’sprofilelevel,theiraveragescoreacrossthe person’s mean score). From Davison and Davenport (2002,
ppre i dictors.Followingfromthetheoryofcomposites(Ghiselliet Equation 2), (cid:2)(cid:2) (cid:2) [(cid:4) (cid:3) (cid:4)¯]= is the criterion pattern. Let
j
al.,1981,p.163),thecorrelationbetweenx lev andyis: Cov(cid:2) i * (cid:3) p 1(cid:2) j x* ji (cid:4)* j beeachperson’scriterionpatternsimilarity
score,whichisthecovariancebetweentheirprofilepatternand
r (cid:3) (cid:2) y ip 1 (cid:3)x 1i (cid:5)x 2i (cid:5)x 3i (cid:5) ...(cid:5)x pi (cid:4) t w h e e ig c h r t i s te (cid:4) ri * o ⁄ n p: pattern. Cov(cid:2) i * is a composite score of X i * with
lev,y
(cid:2) y 1 (cid:3)x (cid:5)
N·
x
SD
(cid:5)
y ·
x
SD
(cid:5)
xlev
...(cid:5)x (cid:4)
(A1-a) j
Cov(cid:2) i * (cid:3)1 p (cid:2) j x* ji (cid:4)* j (A3-a)
ip 1i 2i 3i pi
(cid:3) N·1· (cid:5)(cid:2) j,k 1 p · 1 p ·r xjxk (A1-b) (cid:3)1 p (cid:2) j (cid:3)x ji (cid:2)x levi (cid:4)(cid:4)* j (A3-b)
(cid:3)
(cid:2) y
i
(cid:3)x
1i
(cid:5)x
2i
(cid:5)x
3i
(cid:5) ...(cid:5)xpi (cid:4) (cid:3)1 p (cid:2) j (cid:3) x ji (cid:4)* j (cid:2)x levi (cid:4)* j (cid:4) (A3-c)
(cid:6)
N· (cid:5)(cid:2) j,k r xjxk
(cid:7)
(A1-c) (cid:3)1 p (cid:12)(cid:2) j x ji (cid:4)* j (cid:2) (cid:2) j x levi (cid:4)* j (cid:13) (A3-d)
(cid:3) (cid:2) y i N x 1i(cid:5) y i N x 2i(cid:5) y i N x 3i(cid:5) ...(cid:5) y i N xpi (cid:3)1 p (cid:12)(cid:2) j x ji (cid:4)* j (cid:2)x levi (cid:2) j (cid:4)* j (cid:13) (A3-e)
(cid:5)(cid:2) j,k r xjxk (A1-d) (cid:3)1 p (cid:12)(cid:2) j x ji (cid:4)* j (cid:2)x levi ·0 (cid:13) (A3-f)
WhichyieldstheresultinEquation(1): Cov(cid:2) i * (cid:3)1 p (cid:2) j x ji (cid:4)* j (A3-g)
(cid:2)
r (cid:3) r yix 1i (cid:5)r yix 2i (cid:5)r yix 3i (cid:5) ...(cid:5)r yixpi(cid:3) j r xjy Followingthesamelogicasfortheleveleffect,thecorrelation
lev,y (cid:5)(cid:2)
r
(cid:5)(cid:2)
r
betweenCov(cid:2)*andyis:
j,k xjxk j,k xjxk
(cid:2) y 1(cid:3) x (cid:4)*(cid:5)x (cid:4)*(cid:5)x (cid:4)*(cid:5) ...(cid:5)x (cid:4)*(cid:4)
The analogous formula for the unstandardized profile level ip 1i 1 2i 2 3i 3 pi p
r (cid:3)
effectis: pat,y N·SD y ·SD Cov(cid:4)* (A4-a)
(unstd)r
lev,y
(cid:3)
SD(cid:5)
c x (cid:2) y
1
1
(cid:2)C 1 (cid:3)
(cid:2) y ip 1(cid:3) x 1i (cid:4) 1 *(cid:5)
(cid:14)
x 2i (cid:4) 2 *(cid:5)x 3i (cid:4) 3 *(cid:5) ...(cid:5)x pi (cid:4)* p (cid:4)
y xx
(cid:2) (cid:4)* (cid:4)*
(cid:3)
(cid:2)
j
1·c
xjy
N·1· j,kp j · p k·r xjxk (A4-b)
SD y (cid:5)(cid:2) j,k 1·1·c xjxk (cid:3) (cid:2) y i (cid:3) x 1i (cid:4) 1 *
N
(cid:5)
· (cid:5)
x 2i (cid:4)
(cid:2)
2 *(cid:5)
j,k
x 3
(cid:4)
i (cid:4)
* j (cid:4)
3 *
* k
(cid:5)
r xj
.
xk
..(cid:5)x pi (cid:4)* p (cid:4)
(A4-c)
(cid:6) (cid:7)
(cid:3) SD y (cid:5) (cid:2) j (cid:2) c xj j, y k c xjxk , (A2) (cid:3) (cid:2) (cid:4) 1 * y i N x 1i(cid:5)(cid:4) (cid:5) 2 * y i N x (cid:2) 2i(cid:5) j,k (cid:4) (cid:4) 3 * * j y (cid:4) i N x * k r 3 x i j (cid:5) xk ...(cid:5)(cid:4)* p y i N x ( p A i 4-d)
(Appendicescontinue)
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
204 WIERNIK,WILMOT,DAVISON,ANDONES

## Page 20

WhichyieldstheresultinEquation(2): weighting schemes. Accordingly, following Ghiselli et al. (1981,
p.174),thecorrelationbetweenthesetwocompositesisgivenby
(cid:4)*r (cid:5)(cid:4)*r (cid:5)(cid:4)*r (cid:5) ...(cid:5)(cid:4)*r
r (cid:3) 1 yix 1i 2 yix 2i 3 yix 3i p yixpi Equation(3):
pat,y (cid:5)(cid:2)
(cid:4)*(cid:4)*r
(cid:2)
j,k j k xjxk
(cid:2)*(cid:2)R 1
(cid:4)*r r (cid:3) xx
(cid:3) j j xjy lev,pat (cid:5)(cid:2)*(cid:2)R (cid:2)*(cid:5)1(cid:2)R 1
(cid:5)(cid:2) xx xx
j,k (cid:4)* j (cid:4)* k r xjxk (cid:2)
(cid:4)*·r
Theanalogousformulafortheunstandardizedprofilepatterneffectis: (cid:3) j,k k xjxk
(cid:5)(cid:2) (cid:5)(cid:2)
(unstd)r pat,y (cid:3) SD (cid:5) c x (cid:2) b y * b (cid:2) * C b* (cid:3) SD (cid:5) (cid:2) (cid:2) j b* j c b xj * y b*c (A5) Theanalogousformula j f , o k r r x th jx e k correla j, t k io (cid:4) n * j b (cid:4) e * k t r w xj e x e k nunstandard-
y xx y j,k j k xjxk izedprofilelevelandcriterionpatternsimilarityis:
whereb*(cid:3)b(cid:2)(cid:2)
bistheunstandardizedcriterionpatterncomputed
by ipsatizing the unstandardized regression coefficients around
b*(cid:2)C 1
theirmean,andothervariablesaredefinedasinEquationA2. r (cid:3) xx
lev,pat (cid:5) b*(cid:2)C b*(cid:5)1(cid:2)C 1
xx xx
Level–Pattern Correlation (cid:2)
b*·c
(cid:3) j,k k xjxk (A6)
TheaboveequationsshowthatCPAprofileandleveleffectsare (cid:5)(cid:2)
c
(cid:5)(cid:2)
b*b*c
twoalternativecompositesofthepredictorvariableswithdifferent j,k xjxk j,k j k xjxk
Appendix B
Single-Sample CPA Confidence Intervals and Sampling Distributions
Forthefullmultipleregressionmodel, AnapproximateconfidenceintervalcanbeconstructedforR2as
F (cid:3) (cid:6) R2 (cid:7) · N(cid:2)p(cid:2)1 , (B1) R st 2 an (cid:10) da z r (cid:11) d ⁄2 n S o E rm R2 a , l w d h i e st r r e ib z u (cid:11) t / i 2 on is . t A h n e1 a 0 p 0 p ( r 1 ox (cid:3) im (cid:11) at / e 2) c th on p f e id rc e e n n c t e ile in o te f r t v h a e l
full 1(cid:2)R2 p forRcanbeconstructedas (cid:5) R2(cid:10)z(cid:11)⁄2 SE R2.Alternativeapprox-
imateandexactintervalmethodsarealsoavailable(Helland,1987;
where R2 is the full-model R2, N is the sample size, and p is the
Mendoza&Stafford,2001;Shieh,2006,2009).
number of predictors. F follows the noncentral F distribution
full The CPA level and pattern effects are a decomposition of the
(Shieh,2006):
full-model R2, so they have similar sampling distributions, vari-
F (cid:8)(cid:6) (cid:15)F(p, N(cid:2)p(cid:2)1,(cid:6) ) ances,andconfidenceintervalmethods.
full full full
(cid:6) (cid:7)
and(cid:6) (cid:15)
R2
·(cid:9)2(N(cid:2)1). (B2)
Level Effect
full 1(cid:2)R2
Forthecorrelationbetweenprofilelevelandthecriterion,r ,
Here,theteststatistic,F ,followsanFdistributionwithpand (cid:6) (cid:7) lev,y
N(cid:3)p(cid:3)1degreesoffree f d u o ll mandnoncentralityparameter,(cid:5) full . F (cid:3) r l 2 ev,y ·(N(cid:2)2), (B4)
The noncentrality parameter captures the degree to which the lev 1(cid:2)r2
lev,y
shapeoftheFdistributionisalteredwhenR2(cid:7)0.WhenR2(cid:2)0,
withF followingthenoncentralFdistribution:
(cid:5) alsoequals0,andthedistributionisreducedtotheordinary lev (cid:6) (cid:7)
full
centralFdistribution.Thenoncentralityparameter,(cid:5) full ,followsa F (cid:8)(cid:6) (cid:15)F(cid:3)1, N(cid:2)2,(cid:6) (cid:4)and(cid:6) (cid:15) r l 2 ev,y ·(cid:9)2(N(cid:2)1).
(cid:9)2distributionwithN(cid:3)1degreesoffreedom,multipliedbythe lev lev lev lev 1(cid:2)r2
lev,y
quantityR2/[1(cid:3)R2].
(B5)
ThesamplingerrorvarianceforR2iswell-approximated(Cohen
etal.,2003)by: Here,theteststatistic,F ,followsanFdistributionwith1and
lev
N(cid:3)2degreesoffreedomandnoncentralityparameter,(cid:5) .The
SE R 2 2 (cid:3) 4R2( ( 1 N (cid:2) 2(cid:2) R2 1 )( ) N (N (cid:2) (cid:5) p 3 (cid:2) ) 1)2 . (B3) n d o eg n r c e e e n s tr o a f lit f y re p e a d r o a m m , e m ter u , lt (cid:5) ip le l v i , ed fo b ll y ow th s e a q (cid:9) u 2 an d t i i s t t y rib r u 2 tio / n [1 wi (cid:3) th le r N v 2 (cid:3) ]. 1
lev,y lev,y
(Appendicescontinue)
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
META-ANALYTICCRITERIONPROFILEANALYSIS 205

## Page 21

As r is a unit-weighted composite correlation, its sampling same as for the OLS regression coefficient vector, (cid:2). However,
lev,y
errorvarianceiswell-knownasapproximately(Schmidt&Hunter, thisprocedureyieldsconfidenceintervalsfor(cid:2)(cid:2)thataretoowide;
2015): itdoesnotaccountforthesamplingerrorvariancetheelementsof
(cid:2)(cid:2) share because the same estimate of the mean regression coef-
SE r 2 lev,y (cid:3) (cid:3) 1(cid:2) N(cid:2) r l 2 e 1 v,y (cid:4)2 (B6) f c i o c n ie f n id t, en (cid:4)¯ c , e i i s nt s e u r b v t a r l a s c a te c d co f u r n o t m fo e r a t c h h es e h le a m re e d n v t a o r f ian (cid:2) c . e M of or (cid:4)¯ e u a s c in cu g r t a h t e e
4r2 (cid:3) 1(cid:2)r2 (cid:4)2 formula:
SE r 2 l 2 ev,y (cid:3) lev,y N(cid:2)1 lev,y . (B7) (cid:16) (cid:12)(cid:2)* (cid:12)(cid:2)* (cid:17) (cid:16) (cid:12)(cid:2)* (cid:12)(cid:2)* (cid:17) (cid:2)
Approximate confidence intervals for r
lev,y
can be computed (cid:4) (cid:2)* (cid:3)J(cid:2)* (cid:4) r J(cid:2) (cid:2) * (cid:3) (cid:12)r(cid:2)
xx
(cid:12)r
x
(cid:2)
y
(cid:4) r (cid:12)r(cid:2)
xx
(cid:12)r
x
(cid:2)
y
, (B11)
usingFisher’s(1921)r-to-z=transformation.13Thehypothesisthat
the level effect fully accounts for the variables’ predictive power
where(cid:4) (cid:2)*isthesamplingerrorvariance-covariancematrixforthe
canbetestedusingR2(cid:3)r2 (cid:13)F(p(cid:3)1,N(cid:3)p(cid:3)1).
elementsof(cid:2)(cid:2),J(cid:2)*istheJacobianmatrixofpartialderivativesof
lev,y (cid:2)(cid:2)withrespecttoeachuniqueelementofthevariablecorrelation
matrix,R,(cid:4) isthesamplingcovariancematrixamongtheunique
Pattern Effect r
elements of R, r is the column vector of correlations between
xy
For the correlation between criterion pattern similarity and the each predictor and the criterion, and r is the column vector of
xx
criterion,r , predictor intercorrelations (i.e., vecp(R ); Nel, 1985). Formulas
pat,y xx
(cid:6) (cid:7) for(cid:4) aregivenbyOlkinandFinn(1995)andNel(1985).
F pat (cid:3) 1(cid:2) r p 2 r at 2 ,y · N p(cid:2) (cid:2) 1 p , (B8) The r formulafor(cid:2)(cid:2)canbeexpressedinmatrixalgebraas:
pat,y (cid:2)*(cid:3)(cid:2)(cid:2)1p(cid:2)1(cid:2)(cid:2)(cid:3)(cid:3)I(cid:2)1p(cid:2)1(cid:2)(cid:4)(cid:2)(cid:3)Q(cid:2), (B12)
withF followingthenoncentralFdistribution:
pat where1isacolumnvector1soflengthp(thenumberofpredic-
F (cid:8)(cid:6) (cid:15)F(cid:3)p(cid:2)1, N(cid:2)p,(cid:6) (cid:4)
tors),p(cid:3)1isacolumnvectoroflengthpwitheachelementequal
pat pat pat (cid:6) (cid:7) to1/p,andIisap(cid:8)pidentitymatrix.Followingthechainrule
and(cid:6) (cid:15)
r
p
2
at,y ·(cid:9)2(N(cid:2)1). (B9)
for matrix differentiation (Nel, 1980), J(cid:2)* (cid:3) QJ(cid:2), indicating that
lev 1(cid:2)r
p
2
at,y
J(cid:2)*containsshrunkenvaluesofJ
(cid:2)
.
JonesandWaller(2013,2015)showedthatthestandardmethod
Here,theteststatistic,F pat ,followsanFdistributionwithp(cid:3)1 for calculating the standard errors of (cid:2) (Cohen et al., 2003) is
andN(cid:3)pdegreesoffreedomandnoncentralityparameter,(cid:5) .The
pat negativelybiasedbecauseitfailstoaccountfortheuncertaintyin
noncentrality parameter,(cid:5) , follows a(cid:9)2 distribution with N (cid:3) 1
pat thesamplestandarddeviationsusedtostandardizetheregression
degreesoffreedom,multipliedbythequantityr2 /[1(cid:3)r2 ].
pat,y pat,y coefficients. Jones and Waller (2013) presented a more accurate
The sampling error variance of r2 is well-approximated14
pat,y deltamethodestimatorofthesamplingvariance-covariancematrix
usingaformulalikethatforR2: of(cid:2):
(cid:16) (cid:17) (cid:16) (cid:17)
4r2 (1(cid:2)r2 )(N(cid:2)p(cid:2)1)2 (cid:12)(cid:2) (cid:12)(cid:2) (cid:12)(cid:2) (cid:12)(cid:2) (cid:2)
SE r 2 p 2 at,y (cid:3) pat,y (N2(cid:2) pa 1 t, ) y (N(cid:5)3) (B10) (cid:4) (cid:2) (cid:3)J(cid:2) (cid:4) r J(cid:2) (cid:2) (cid:3) (cid:12)r xx (cid:12)r xy (cid:4) r (cid:12)r xx (cid:12)r xy , (B13)
Anapproximateconfidenceintervalcanbeconstructedforr p 2 at,y J(cid:2) (cid:3)(cid:12)(cid:2)2 (cid:12) r x (cid:2) y R x (cid:2) x 1(cid:3)R x (cid:2) x 1(cid:13) K(cid:2) c R x (cid:2) x 1(cid:13) (B14)
p
as
erc
r
e
p 2 a
n
t,
t
y
il
(cid:10)
e o
z
f
1(cid:2)
th
(cid:11)
e
⁄2
s
S
t
E
an
r
d
p 2 a
a
t,
r
y
d
, w
no
h
r
e
m
r
a
e
ld
z 1
is
(cid:3)
tr
(cid:11)
ib
/
u
2
tio
is
n.
t
A
he
na
1
p
0
p
0
r
(
o
1
xim
(cid:3)
ate
(cid:11)
c
/
o
2
n
)
f
t
i
h
-
whereJ(cid:2)istheJacobianmatrixof(cid:2),RistheKroneckerproduct
(Abadir & Magnus, 2005, p. 274), and K is a transition matrix
d
E
e
x
n
a
c
c
e
ti
i
n
n
t
t
e
e
r
r
v
v
a
a
l
l
s
f
c
o
a
r
n
r
b
pa
e
t,y
co
c
n
a
s
n
tru
b
c
e
te
c
d
on
b
s
y
tr
a
u
d
c
a
te
p
d
tin
a
g
s
m
(cid:5)
eth
r
o
p 2
d
at
s
,y
f
(cid:10)
or
z
R
(cid:11)
2
⁄2 S
(S
E
h
r
i
p 2
e
at
h
,y .
,
(Nel,1985,p.143)thatextractsthelowertr c iangularelementsfrom
R .
2006, 2009). The hypothesis that the pattern effect fully accounts for xx
variables’ predictive power can be tested using R2 (cid:3) r2 (cid:13) F(1,
pat,y
N(cid:3)p(cid:3)1).
13Exact confidence intervals for r can be computed using
lev,y
t (cid:3) (cid:5)N(cid:2)2·r ⁄(cid:5)1(cid:2)r2 with t |(cid:14) (cid:13) t(N (cid:3) 2, (cid:14) ) and
Criterion Pattern Elements (cid:13) lev (cid:15)(cid:5)(cid:9)2(cid:3)N(cid:2)1 l (cid:4) ev · ,y r ⁄(cid:5)1 le (cid:2) v,y r2 . lev lev lev
lev lev,y lev,y
14Simulation results supporting this approximation are available from
Davison and Davenport (2002, Appendix B) suggested an ap-
thefirstauthor.
proximatehypothesistestfortheelementsofthecriterionpattern 15Unless stated otherwise, all vectors are column vectors. The prime
vector, (cid:2)(cid:2),15 by assuming that the sampling error for (cid:2)(cid:2) is the symbolindicatesthetransposeoperation.
(Appendicescontinue)
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
206 WIERNIK,WILMOT,DAVISON,ANDONES

## Page 22

SubstitutingtheresultsofEquationB14intoEquationB11yields: The sampling error for the mean regression coefficient, (cid:4)¯, is
computedas
(cid:4) (cid:2)* (cid:3)QJ(cid:2) (cid:4) r J(cid:2) (cid:2) Q, (B15)
w S th E h e E (cid:4) e * j a j r t e c (cid:3) h h t e (cid:5) le e m l d e i m e a n g e t (cid:3) n (cid:4) i o t s f (cid:2) 2 t * h o (cid:2) (cid:4) e j f . (cid:2) T 1 c 0 (cid:2) h a 0 e n (cid:2) ( 1 1 b 0 t e 0 (cid:3) h (cid:3) e e 1 n s (cid:11) t (cid:2) i / m 2 h (cid:11) ) a a t (cid:4) s t h e % d p a c e a o r s c n s e f (cid:4) t n i a d * j t n i e (cid:10) l d n e a c t r o e 1 d f (cid:2) in (cid:11) th t e ⁄ e 2 e r , r d r v o f t( a S r N l E f (cid:4) o o (cid:3) * j f r , with SE (cid:4) 2 ¯ (cid:3)J(cid:4)¯ (cid:4) r J(cid:4) (cid:2) ¯ , (B16)
p (cid:3) 1) 1 d (cid:3) is (cid:11) tr /2 i , b d u f tion. J(cid:4)¯ (cid:3)(cid:12)(cid:2)2p(cid:2)1(cid:2)(cid:12) r
x
(cid:2)
y
R
x
(cid:2)
x
1(cid:3)R
x
(cid:2)
x
1(cid:13) K
c
p(cid:2)1(cid:2)R
x
(cid:2)
x
1(cid:13) . (B17)
Appendix C
Derivation of Shrinkage-Adjusted and Cross-Validity Pattern Effects
The correlation between criterion pattern similarity and the criterion, r , can be expressed in terms of (a) the correlation between
pat,y
profile level and the criterion, r , (b) the correlation between profile level and criterion pattern similarity, r , and (c) the total
lev,y lev,pat
regressionmodelR2.
(cid:16) (cid:17) (cid:16) (cid:17)
R2(cid:3)r(cid:2) R(cid:2)1r (cid:3)(cid:12)r r (cid:13) 1 r lev,pat (cid:2)1 r pat,y
xy xy pat,y lev,y r 1 r (C1-a)
lev,pat lev,y
(cid:6) (cid:7) (cid:16) (cid:17)(cid:16) (cid:17)
R2(cid:3) 1 (cid:12)r r (cid:13) (cid:2)1 r lev,pat r pat,y
r l 2 ev,pat (cid:2)1 pat,y lev,y r lev,pat (cid:2)1 r lev,y (C1-b)
(cid:6) (cid:7)
R2(cid:3) 1 (cid:3) 2r r r (cid:2)r2 (cid:2)r2 (cid:4)
r2 (cid:2)1 pat,y lev,y lev,pat pat,y lev,y (C1-c)
lev,pat
R2· (cid:3) r2 (cid:2)1 (cid:4)(cid:3)2r r r (cid:2)r2 (cid:2)r2 (C1-d)
lev,pat pat,y lev,y lev,pat pat,y lev,y
r2 (cid:2)2r r r (cid:3)(cid:2)R2· (cid:3) r2 (cid:2)1 (cid:4)(cid:2)r2 (C1-e)
pat,y pat,y lev,y lev,pat lev,pat lev,y
r2 r2 (cid:5)r2 (cid:2)2r r r (cid:3)r2 r2 (cid:2)R2· (cid:3) r2 (cid:2)1 (cid:4)(cid:2)r2 (C1-f)
lev,y lev,pat pat,y pat,y lev,y lev,pat lev,y lev,pat lev,pat lev,y
(cid:3)r r (cid:2)r (cid:4)2(cid:3)r2 · (cid:3) r2 (cid:2)1 (cid:4)(cid:2)R2· (cid:3) r2 (cid:2)1 (cid:4) (C1-g)
lev,y lev,pat pat,y lev,y lev,pat lev,pat
(cid:3)r r (cid:2)r (cid:4)2(cid:3)(cid:3) r2 (cid:2)1 (cid:4)(cid:3) r2 (cid:2)R2(cid:4) (C1-h)
lev,y lev,pat pat,y lev,pat lev,y
(cid:3)r r (cid:2)r (cid:4)2(cid:3)(cid:3) 1(cid:2)r2 (cid:4)(cid:3) R2(cid:2)r2 (cid:4) (C1-i)
lev,y lev,pat pat,y lev,pat lev,y
r r (cid:2)r (cid:3) (cid:10)(cid:5)(cid:3) 1(cid:2)r2 (cid:4)(cid:3) R2(cid:2)r2 (cid:4) (C1-j)
lev,y lev,pat pat,y lev,pat lev,y
(cid:2)r (cid:3)(cid:2)r r (cid:10)(cid:5)(cid:3) 1(cid:2)r2 (cid:4)(cid:3) R2(cid:2)r2 (cid:4) (C1-k)
pat,y lev,y lev,pat lev,pat lev,y
r (cid:3)r r (cid:10)(cid:5)(cid:3) 1(cid:2)r2 (cid:4)(cid:3) R2(cid:2)r2 (cid:4) (C1-l)
pat,y lev,y lev,pat lev,pat lev,y
Itcanbeassumedthatthepatterneffectispositivelycorrelatedwiththecriterion,yieldingtheresultinEquation(6):
r (cid:3)r r (cid:5)(cid:5)(cid:3) 1(cid:2)r2 (cid:4)(cid:3) R2(cid:2)r2 (cid:4)
pat,y lev,y lev,pat lev,pat lev,y
(Appendicescontinue)
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
META-ANALYTICCRITERIONPROFILEANALYSIS 207

## Page 23

Appendix D
Delta Method Confidence Intervals for MACPA Parameters
Approximate confidence intervals for MACPA parameters can Level Effect, Pattern Effect, and Correlation Between
be computed using the following sampling error formulas and Profile Level and Criterion Pattern Similarity
criticalvaluesfromatorstandardnormaldistribution(cf.Alf&
Jacobianmatricesfortheleveleffect,patterneffect,andcorre-
Graf,1999;Cohenetal.,2003,p.88).Rcodeimplementingthese
lationbetweenprofilelevelandcriterionpatternsimilaritycanbe
methods is available in the configural package at https://cran.r-
project.org/package(cid:2)configural or at https://doi.org/10.17605/osf obtainedbydifferentiatingEquations1–3.
TheJacobianmatrixfortheleveleffect,J ,is:
.io/aqmpc. (cid:16) rlev,y (cid:17)
Eachsamplingerrorformulatakesthegeneralform: r¯(cid:2) 1 1
(cid:16) (cid:12)f (cid:12)f (cid:17) (cid:16) (cid:12)f (cid:12)f (cid:17) (cid:2) J rlev,y (cid:3) (cid:2) (cid:3) 1(cid:2)¯R x xx y 1 (cid:4)3⁄2 (cid:3)1(cid:2)(cid:3)1(cid:2)(cid:4)K(cid:2) c (cid:3) 1(cid:2)¯R xx 1 (cid:4)1⁄21(cid:2) .
SE2 f (cid:3)J f (cid:4) r¯ J(cid:2) f (cid:3) (cid:12)r¯ x (cid:2) x (cid:12)r¯ x (cid:2) y (cid:4) r¯ (cid:12)r¯ x (cid:2) x (cid:12)r¯ x (cid:2) y , (D1) (D6)
whereJ f istheJacobianmatrixofpartialderivativesoftheformula TheJacobia (cid:16) nma (cid:6) trixfor (cid:7) thesquaredlevel (cid:6) effect,J (cid:7)rl 2 ev,y(cid:17) ,is:
forthespecifiedMACPAparameterwithrespecttoeachelement
r¯(cid:2) 1 2 r¯(cid:2) 1
o m f e t t h a e -a v n e a c ly to ti r c o m f e m an et i a n - t a e n rc a o ly r t r i e c la m tio ea n n sa c m or o r n el g at t i h o e n p s r , e ¯r di ( c in to c r l s u , d r¯ ing ,a t n h d e J rl 2 ev,y (cid:3) (cid:2)2 1(cid:2)¯R xy 1 (1(cid:2)(cid:3)1(cid:2))K(cid:2) c 2 1(cid:2)¯R xy 1 1(cid:2) .
xx xx xx
themeta-analyticmeancriterioncorrelationforeachpredictor,r¯ )
xy (D7)
and(cid:4) isthesamplingcovariancematrixamongtheelementsof¯r
r¯
(Becker,1992). TheJacobianmatrixf
(cid:16)
orthepatterne
(cid:17)
ffect,J rpat,y ,s:
J (cid:3)
(cid:12)r
pat,y
(cid:12)rpat,y
, where (D8)
Criterion Pattern Vector rpat,y
(cid:16)
(cid:12)r¯
x
(cid:2)
x
(cid:12)r¯
x
(cid:2)
y
v
st
e
a
c
A
n
t
d
o
s
a
r
s
,
r
h
d
(cid:2)
o
e
w
(cid:2)
rr
n
h
o
a
r
i
s
v
n
e
o
A
f
s
p
t
t
h
a
p
n
e
e
d
n
s
a
d
ta
r
i
d
n
x
d
B
e
a
r
r
,
r
d
o
t
i
h
r
z
s
e
ed
t
e
h
l
O
e
a
m
t
LS
a
e
r
n
r
e
t
e
s
g
s
o
h
re
f
r
s
u
t
s
n
h
i
k
o
e
e
n
c
n
c
ri
o
v
te
e
a
r
f
l
i
f
u
o
ic
e
n
i
s
e
p
n
o
a
t
f
t
s
t
,
e
th
(cid:2)
rn
e
.
(cid:12)
(cid:12)
r
r¯
p
x
a
(cid:2)
x
t,y(cid:3) (cid:6)
(cid:2)*(cid:2)¯R
1
xx
(cid:2)*
(cid:7) 1⁄2 2((cid:2)(cid:2)(cid:3)r(cid:2)Q¯R
x
(cid:2)
x
1)
Thesamplingerrorvariance-covariancematrixfor(cid:2)(cid:2)inMACPA (cid:5) r¯ x (cid:2) y (cid:2)* (cid:3) ((cid:2)*(cid:2) (cid:3)(cid:2)*(cid:2))(cid:2)((cid:2)(cid:2)(cid:3)(cid:2)*(cid:2)¯R Q¯R(cid:2)1)
is: (cid:2)*(cid:2)¯R (cid:2)* xx xx
xx
(cid:17)
(cid:4) (cid:2)* (cid:3)QJ(cid:2) (cid:4) r¯ J(cid:2) (cid:2)Q, (D2) (cid:2)((cid:2)*(cid:2)¯R Q¯R(cid:2)1(cid:3)(cid:2)(cid:2)) (cid:4) K(cid:2), (D9)
xx xx c
w
nu
h
m
er
b
e
er
Q
o
(cid:2)
f p
(
r
I
ed
(cid:3) J
i
(cid:2)
c
1
t
(cid:3)
o
=p
r
(cid:12)
s
(cid:3) (cid:2)
),
1) 2
p
, (cid:12)
(cid:3)
1 r¯
1
x = (cid:2) y i ¯R
i
s
s
x (cid:2) a x
a
1 r (cid:3)
c
o
o
w ¯R
lu
x (cid:2) v
m
x 1 e (cid:13)
n
c K to (cid:2)
v
c r
ec
o
t
¯R f
o
x (cid:2)
r
1 x s 1
o
(cid:13) o
f
f
le
le
n
n
g
g
th
th
p
p (
w
( D t
i
h 3
th
e ) (cid:12) (cid:12) r r¯ pa
x
(cid:2) t
y
,y(cid:3) (cid:6) (cid:2)*(cid:2)¯R 1
xx
(cid:2)* (cid:7) 1⁄2 (cid:16) r¯ x (cid:2) y Q¯R x (cid:2) x 1(cid:5)(cid:2)*(cid:2)(cid:2) (cid:6) r¯ x (cid:2) y (cid:2) (cid:2) * * (cid:2) (cid:2)¯R *(cid:2)
x
R
x
(cid:2) Q * ¯R x (cid:2) x 1 (cid:7)(cid:17) .
each element equal to 1/p, I is p (cid:8) p identity matrix, R¯ is the (D10)
xx
m
th
e
e
ta
K
-
r
a
o
n
n
a
e
ly
c
t
k
i
e
c
r
m
p
e
ro
an
du
i
c
n
t
te
(
r
A
co
b
r
a
r
d
e
i
l
r
at
&
ion
M
m
ag
at
n
r
u
ix
s,
a
2
m
0
o
0
n
5
g
,p
p
.
re
2
d
7
i
4
ct
)
o
,
r
a
s
n
,
d
R
K
is TheJacobianmatrixf
(cid:16)
orthesquaredp
(cid:17)
atterneffect,J r2
pat,Y
,is:
i t s ria a ng tr u a l n a s r it e i l o e n m m en a t t s ri f x ro ( m Ne R¯ l, xx 1 . 9 T 8 h 5 e , s p t . an 1 d 4 a 3 r ) d t e h r a r t o e r x f t o r r ac e t a s ch th e e le l m ow en e c r t J rp 2 at,y (cid:3) (cid:16) (cid:12) (cid:12) r r¯ p 2 x a (cid:2) x t,y (cid:12) (cid:12) r r¯ p 2 a x (cid:2) t y ,y , where (D11)
of(cid:2)(cid:2)isSE(cid:4)* j (cid:3)(cid:5) diag(cid:3)(cid:4) (cid:2) 2 * (cid:4) j . (cid:12)r p 2 at,y(cid:3)(cid:2)2 r¯ x (cid:2) y (cid:2)* 2 (cid:3)(cid:2)(cid:2)(cid:3)r¯(cid:2) Q¯R(cid:2)1 (cid:4)
(cid:12)r¯
x
(cid:2)
x
(cid:2)*(cid:2)¯R
xx
(cid:2)* xy xx
Total Model R2 and R
The total model R2 in an OLS multiple regression is R2 (cid:3) r x (cid:2) y (cid:2).
(cid:5)
(cid:2)*
r¯
(cid:2)
x (cid:2)
¯R
y (cid:2)*
(cid:2)*
(cid:3)(cid:3)(cid:2)*(cid:2) (cid:3)(cid:2)*(cid:2)(cid:4)(cid:2)(cid:3)(cid:2)(cid:2)(cid:3)(cid:2)*(cid:2)¯R
xx
Q¯R
x
(cid:2)
x
1 (cid:4)
Applying principles of matrix differentiation (Laue, Mitterreiter, & xx (cid:17)
Giesen,2018;Nel,1980),theJacobianmatrixforR2,J R2is: (cid:2)(cid:3)(cid:2)*(cid:2)¯R Q¯R(cid:2)1(cid:3)(cid:2)(cid:2)(cid:4)(cid:4) K(cid:2), (D12)
xx xx c
J R2 (cid:3)(cid:12)(cid:2)2[(cid:2)(cid:2)(cid:3)(cid:2)(cid:2)]K(cid:2) c 2(cid:2)(cid:2)(cid:13). (D4) (cid:16) (cid:6) (cid:7)(cid:17)
TheJacobianmatrix
(cid:12)
fortotalmultiplecorre
(cid:13)
lation,J R ,is: (cid:12) (cid:12) r r¯ p 2 a
x
(cid:2) t
y
,y(cid:3) (cid:2) 2 *(cid:2) r¯ ¯R x (cid:2) y
x
(cid:2)
x
(cid:2) * * r¯ x (cid:2) y Q¯R x (cid:2) x 1(cid:5)(cid:2)*(cid:2)(cid:2) r¯ x (cid:2) y (cid:2) (cid:2) *(cid:2) *(cid:2) * ¯R (cid:2)¯R
xx
xx (cid:2) Q * ¯R(cid:2) xx 1 .
J R (cid:3) (cid:2) R 1 [(cid:2)(cid:2)(cid:3)(cid:2)(cid:2)]K(cid:2) c R 1(cid:2)(cid:2). (D5) (D13)
(Appendicescontinue)
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT .yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
208 WIERNIK,WILMOT,DAVISON,ANDONES

## Page 24

the
If
v
th
a
e
ri
p
an
at
c
t
e
ern
of
eff
r
ecti
.
sv
In
ery
th
s
i
m
s
a
c
ll
a
,
s
E
e
q
,
u
c
a
o
ti
n
o
s
n
tr
D
uc
8
ti
m
ng
ay
a
ov
c
e
o
r
n
e
f
s
i
t
d
im
en
a
c
t
e
e SE(cid:6) 2
Rl 2 ev
(cid:18)4R2S
(cid:16)
E
R
2(cid:5)4r
l
2
ev,y
SE
r
2
lev,y (cid:17)
intervalforr2 an p d at, t y akingthesquarerootsoftheboundswillbe r (cid:3) R6(cid:5)R4(cid:3) r2 (cid:2)3 (cid:4)(cid:5)R2(cid:3) 2(cid:2)r2 (cid:4)(cid:2)r2 (cid:4)
pat,y (cid:2) 8 lev,y lev,y lev,y lev,y
moreaccurate. 2R3(cid:3)1(cid:2)R2(cid:4)(cid:3) 1(cid:2)r2 (cid:4)
lev,y
TheJacobianmatrixfortheprofilelevel–criterionpatternsim-
(cid:14)SE SE Rr (D17)
ilaritycorrelation,J
rlev,p(cid:16)at
,is:
(cid:17)
R rlev,y lev,y
J (cid:3) (cid:12)r lev,pat (cid:12)rlev,pat , where (D14) SE(cid:6) 2 R2 pat (cid:18)4R2SE R 2(cid:5)4r p 2 at,y SE r 2 pat,y
(cid:6)
rlev,pat (cid:12)r¯
x
(cid:2)
x
(cid:12)r¯
x
(cid:2)
y
(cid:16) (cid:17)
(cid:12)r (cid:12) le r¯ v x (cid:2) , x pat(cid:3) (cid:3)(cid:2)*(cid:2)¯R x (cid:2) x * (cid:2) (cid:2) * ¯R 1 x (cid:2) x ¯R 1 xx 1 (cid:4)3⁄2 (cid:3) 1(cid:2)¯R xx 1 (cid:3)(cid:3)(cid:2)(cid:2)(cid:3)(cid:2)*(cid:2)¯R xx Q¯R x (cid:2) x 1 (cid:4) (cid:2)8 r pat,y (cid:3) R6(cid:5)R4 2 (cid:3) R r p 3 2 a (cid:3) t 1 ,y (cid:2) (cid:2) R 3 (cid:4) 2(cid:4) (cid:5) (cid:3) 1 R (cid:2) 2(cid:3) r 2 p 2 (cid:2) at,y r (cid:4) p 2 at,y (cid:4)(cid:2)r p 2 at,y (cid:4)
(cid:5)(cid:3)(cid:2)*(cid:2)¯R xx Q¯R x (cid:2) x 1(cid:3)(cid:2)(cid:2)(cid:4)(cid:2)(cid:3)(cid:2)*(cid:2) (cid:3)(cid:2)*(cid:2)(cid:4)(cid:4)(cid:2)(cid:2)*(cid:2)¯R xx (cid:2)*(1(cid:2)(cid:3)1(cid:2) (cid:7) ) (cid:4) (cid:14)SE R SE rpat,y Rr pat,y (D18)
The sampling error variances for the square roots of the these
(cid:5) (cid:3)(cid:2)*(cid:2)¯R (cid:2)* 2 1(cid:2)¯R 1 (cid:4)1⁄2 (cid:3)(cid:3)1(cid:2)(cid:3)(cid:2)*(cid:2)(cid:4)(cid:2)(cid:3) 1(cid:2)¯R xx Q¯R x (cid:2) x 1(cid:3)(cid:2)(cid:2)(cid:4)(cid:4) K(cid:2) c , values( (cid:5)(cid:6)R2;i.e.,thesemipartialcorrelationofprofileorcrite-
(cid:12)r
(cid:12) le r¯ v x (cid:2) , y pat(cid:3)
(cid:6) x
(cid:2)
x
*(cid:2)¯R xx (cid:2)
x
1
x
*1(cid:2)¯R xx 1
(cid:7)
1⁄2
(cid:16)
1(cid:2)¯R xx Q¯R x (cid:2) x 1 (cid:17)
(D15) m rio e n nt p a a l t R te 2 rn of s t i h m e il p a a
S
ri t
E
t t y e
(cid:5) 2
r w n
(cid:6)
i e t
R
f h
l 2
f
ev
e t
(cid:18)
c h t e o
S
c v
E
r e i
(cid:6) 2
t r e
Rl 2
r t
e
h i
v
o e
⁄
n l
(cid:3)
) e ,
4
v S
(cid:6)
e E
R
l 2 (cid:5) e
l 2 e
f
v
f
(cid:4)
(cid:6) e R c l 2 t e , v , S a E n 2 (cid:5) dt (cid:6) h R e 2 pa
(
i t n
D
, c a
1
r r
9
e e -
)
:
(cid:2) 1(cid:2)¯R xx (cid:2)*(cid:2)*(cid:2)¯R xx Q¯R x (cid:2) x 1 . (D16) SE(cid:5) 2 (cid:6)R2 pat (cid:18)SE(cid:6) 2 R2 pat ⁄ (cid:3) 4(cid:6)R2 pat (cid:4) (D20)
(cid:2)*(cid:2)¯R (cid:2)*
xx Ifthepatterneffectisverysmall,EquationD20mayoveresti-
mate the variance of
(cid:5)(cid:6)R2
. In this case, constructing a confi-
Incremental Validity ((cid:3)R2 and (cid:5)(cid:6)R2) of Level and denceintervalfor(cid:5)r2 and p t a a t kingthesquarerootsofthebounds
pat
Pattern Effects willbemoreaccurate.
FollowingAlfandGraf(1999),thesamplingerrorvariancesfor
the incremental R2 of the level effect over the pattern effect, ReceivedFebruary11,2019
e S f E fe (cid:6) 2 c R t l 2 e , v , S a E n (cid:6) 2 d Rp 2 t a h t , e a i r n e c : rementalR2ofthepatterneffectoverthelevel Revision A r c e c c e e p iv te e d d A A p p r r i i l l 2 2 9 7 , , 2 2 0 0 2 2 0 0 (cid:3)
.srehsilbupdeillastifoenoronoitaicossAlacigolohcysPnaciremAehtybdethgirypocsitnemucodsihT
.yldaorbdetanimessidebottonsidnaresulaudividniehtfoesulanosrepehtrofylelosdednetnisielcitrasihT
META-ANALYTICCRITERIONPROFILEANALYSIS 209
Call for Nominations
The Publications and Communications (P&C) Board of the American Psychological Association
has opened nominations for the editorships of Developmental Psychology, Journal of Consulting
and Clinical Psychology, and Journal of Experimental Psychology: General. Eric Dubow, PhD,
JoanneDavila,PhD,andNelsonCowan,PhDaretheincumbenteditors.
Candidates should be members of APA and should be available to start receiving manuscripts in
early 2022 to prepare for issues published in 2023. The APA Journals program values equity,
diversity,andinclusionandencouragestheapplicationofmembersofallgroups,includingwomen,
peopleofcolor,LGBTQpsychologists,andthosewithdisabilities,aswellascandidatesacrossall
stagesoftheircareers.Self-nominationsarealsoencouraged.
Searchchairshavebeenappointedasfollows:
● DevelopmentalPsychology,Chair:PamelaReid,PhD
● JournalofConsultingandClinicalPsychology,Chair:DannyWedding,PhD
● JournalofExperimentalPsychology:General,Co-Chairs:RichardPetty,PhDandMichael
Roberts,PhD
NominatecandidatesthroughAPA’sEditorSearchwebsite(https://editorsearch.apa.org).
Preparedstatementsofonepageorlessinsupportofanomineecanalsobesubmittedbye-mailto
JenChase,JournalServicesAssociate(jchase@apa.org).
DeadlineforacceptingnominationsisMonday,January11,2021,afterwhichphaseonevettingwill
begin.