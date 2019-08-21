#This script will add Success Metrics for the current year to include metrics up to 'last week'
from datetime import *
import requests
import json
import pandas as pd

#Let's get the current year and week - These will be needed to query IQ server for success metrics
#start by figuring out today
today = datetime.today()
cur_year = today.strftime("%Y")
cur_week = int(today.strftime("%U"))
#print(cur_week)

#Let's define some variables for connecting to IQ Server
iq_user = 'admin'
iq_password = 'qgrrDd6b'
iq_url = 'http://localhost:8070/api/v2/reports/metrics'


#First we generate the JSON and CSV files for each week YTD
for counter in range(1,cur_week+2): #DO NOT FORGET TO SET WEEK+2 BACK TO WEEK+1
    #print("\nSuccess Metrics for Week "+ str(counter) + ":" + "\n")
    #set the time period
    time_period = cur_year + '-W' + str(counter)
    r_body = '{"timePeriod": "WEEK","firstTimePeriod": "'+ time_period + '","lastTimePeriod": "' + time_period + '"}'
    #print r_body
    resp = requests.post(iq_url, auth=(iq_user, iq_password) ,data=r_body, headers={'Content-Type':'application/json', 'Accept':'application/json'})
    raw_data = resp.json()
    with open("raw_data_wk"+str(counter)+".json",'w') as f:
        json.dump(raw_data,f)

    df = pd.read_json(resp.text)
    df.to_csv("raw_data_wk"+str(counter)+".csv")

    #print(df.head(10))


#Then we read each one of the weekly JSON files and aggregate the data for all the apps to calculate the metrics

DisSecLow = 0
DisSecLowWk = 0
DisSecMod = 0
DisSecModWk = 0
DisSecSev = 0
DisSecSevWk = 0
DisSecCri = 0
DisSecCriWk = 0

DisLicLow = 0
DisLicLowWk = 0
DisLicMod = 0
DisLicModWk = 0
DisLicSev = 0
DisLicSevWk = 0
DisLicCri = 0
DisLicCriWk = 0

DisQuaLow = 0
DisQuaLowWk = 0
DisQuaMod = 0
DisQuaModWk = 0
DisQuaSev = 0
DisQuaSevWk = 0
DisQuaCri = 0
DisQuaCriWk = 0

DisOthLow = 0
DisOthLowWk = 0
DisOthMod = 0
DisOthModWk = 0
DisOthSev = 0
DisOthSevWk = 0
DisOthCri = 0
DisOthCriWk = 0



FixSecLow = 0
FixSecLowWk = 0
FixSecMod = 0
FixSecModWk = 0
FixSecSev = 0
FixSecSevWk = 0
FixSecCri = 0
FixSecCriWk = 0

FixLicLow = 0
FixLicLowWk = 0
FixLicMod = 0
FixLicModWk = 0
FixLicSev = 0
FixLicSevWk = 0
FixLicCri = 0
FixLicCriWk = 0

FixQuaLow = 0
FixQuaLowWk = 0
FixQuaMod = 0
FixQuaModWk = 0
FixQuaSev = 0
FixQuaSevWk = 0
FixQuaCri = 0
FixQuaCriWk = 0

FixOthLow = 0
FixOthLowWk = 0
FixOthMod = 0
FixOthModWk = 0
FixOthSev = 0
FixOthSevWk = 0
FixOthCri = 0
FixOthCriWk = 0



WaiSecLow = 0
WaiSecLowWk = 0
WaiSecMod = 0
WaiSecModWk = 0
WaiSecSev = 0
WaiSecSevWk = 0
WaiSecCri = 0
WaiSecCriWk = 0

WaiLicLow = 0
WaiLicLowWk = 0
WaiLicMod = 0
WaiLicModWk = 0
WaiLicSev = 0
WaiLicSevWk = 0
WaiLicCri = 0
WaiLicCriWk = 0

WaiQuaLow = 0
WaiQuaLowWk = 0
WaiQuaMod = 0
WaiQuaModWk = 0
WaiQuaSev = 0
WaiQuaSevWk = 0
WaiQuaCri = 0
WaiQuaCriWk = 0

WaiOthLow = 0
WaiOthLowWk = 0
WaiOthMod = 0
WaiOthModWk = 0
WaiOthSev = 0
WaiOthSevWk = 0
WaiOthCri = 0
WaiOthCriWk = 0



OpeSecLow = 0
OpeSecLowWk = 0
OpeSecMod = 0
OpeSecModWk = 0
OpeSecSev = 0
OpeSecSevWk = 0
OpeSecCri = 0
OpeSecCriWk = 0

OpeLicLow = 0
OpeLicLowWk = 0
OpeLicMod = 0
OpeLicModWk = 0
OpeLicSev = 0
OpeLicSevWk = 0
OpeLicCri = 0
OpeLicCriWk = 0

OpeQuaLow = 0
OpeQuaLowWk = 0
OpeQuaMod = 0
OpeQuaModWk = 0
OpeQuaSev = 0
OpeQuaSevWk = 0
OpeQuaCri = 0
OpeQuaCriWk = 0

OpeOthLow = 0
OpeOthLowWk = 0
OpeOthMod = 0
OpeOthModWk = 0
OpeOthSev = 0
OpeOthSevWk = 0
OpeOthCri = 0
OpeOthCriWk = 0

MttrLow = 0
MttrLowWk = 0
MttrMod = 0
MttrModWk = 0
MttrSev = 0
MttrSevWk = 0
MttrCri = 0
MttrCriWk = 0

EvalCount = 0
EvalCountWk = 0


for counter in range(1,cur_week+2):  #DO NOT FORGET TO SET WEEK+2 BACK TO WEEK+1
    df = pd.read_json("raw_data_wk"+str(counter)+".json",typ='dict')
    for app in df:
        EvalCountWk = app['aggregations'][0]['evaluationCount']
        

        MttrLowWk = app['aggregations'][0]['mttrLowThreat']
        if(isinstance(MttrLowWk,int)):
            MttrLowWk = round(MttrLowWk/86400000) #converting from ms to days
        else:
            MttrLowWk = 0
            
        MttrModWk = app['aggregations'][0]['mttrModerateThreat']
        if(isinstance(MttrModWk,int)):
            MttrModWk = round(MttrModWk/86400000) #converting from ms to days
        else:
            MttrModWk = 0

        MttrSevWk = app['aggregations'][0]['mttrSevereThreat']
        if(isinstance(MttrSevWk,int)):
            MttrSevWk = round(MttrSevWk/86400000) #converting from ms to days
        else:
            MttrSevWk = 0

        MttrCritWk = app['aggregations'][0]['mttrCriticalThreat']
        if(isinstance(MttrCritWk,int)):
            MttrCritWk = round(MttrCritWk/86400000) #converting from ms to days
        else:
            MttrCritWk = 0

        
        DisSecLowWk = app['aggregations'][0]['discoveredCounts']['SECURITY']['LOW']
        DisSecModWk = app['aggregations'][0]['discoveredCounts']['SECURITY']['MODERATE']
        DisSecSevWk = app['aggregations'][0]['discoveredCounts']['SECURITY']['SEVERE']
        DisSecCriWk = app['aggregations'][0]['discoveredCounts']['SECURITY']['CRITICAL']

        DisLicLowWk = app['aggregations'][0]['discoveredCounts']['LICENSE']['LOW']
        DisLicModWk = app['aggregations'][0]['discoveredCounts']['LICENSE']['MODERATE']
        DisLicSevWk = app['aggregations'][0]['discoveredCounts']['LICENSE']['SEVERE']
        DisLicCriWk = app['aggregations'][0]['discoveredCounts']['LICENSE']['CRITICAL']

        DisQuaLowWk = app['aggregations'][0]['discoveredCounts']['QUALITY']['LOW']
        DisQuaModWk = app['aggregations'][0]['discoveredCounts']['QUALITY']['MODERATE']
        DisQuaSevWk = app['aggregations'][0]['discoveredCounts']['QUALITY']['SEVERE']
        DisQuaCriWk = app['aggregations'][0]['discoveredCounts']['QUALITY']['CRITICAL']

        DisOthLowWk = app['aggregations'][0]['discoveredCounts']['OTHER']['LOW']
        DisOthModWk = app['aggregations'][0]['discoveredCounts']['OTHER']['MODERATE']
        DisOthSevWk = app['aggregations'][0]['discoveredCounts']['OTHER']['SEVERE']
        DisOthCriWk = app['aggregations'][0]['discoveredCounts']['OTHER']['CRITICAL']



        FixSecLowWk = app['aggregations'][0]['fixedCounts']['SECURITY']['LOW']
        FixSecModWk = app['aggregations'][0]['fixedCounts']['SECURITY']['MODERATE']
        FixSecSevWk = app['aggregations'][0]['fixedCounts']['SECURITY']['SEVERE']
        FixSecCriWk = app['aggregations'][0]['fixedCounts']['SECURITY']['CRITICAL']

        FixLicLowWk = app['aggregations'][0]['fixedCounts']['LICENSE']['LOW']
        FixLicModWk = app['aggregations'][0]['fixedCounts']['LICENSE']['MODERATE']
        FixLicSevWk = app['aggregations'][0]['fixedCounts']['LICENSE']['SEVERE']
        FixLicCriWk = app['aggregations'][0]['fixedCounts']['LICENSE']['CRITICAL']

        FixQuaLowWk = app['aggregations'][0]['fixedCounts']['QUALITY']['LOW']
        FixQuaModWk = app['aggregations'][0]['fixedCounts']['QUALITY']['MODERATE']
        FixQuaSevWk = app['aggregations'][0]['fixedCounts']['QUALITY']['SEVERE']
        FixQuaCriWk = app['aggregations'][0]['fixedCounts']['QUALITY']['CRITICAL']

        FixOthLowWk = app['aggregations'][0]['fixedCounts']['OTHER']['LOW']
        FixOthModWk = app['aggregations'][0]['fixedCounts']['OTHER']['MODERATE']
        FixOthSevWk = app['aggregations'][0]['fixedCounts']['OTHER']['SEVERE']
        FixOthCriWk = app['aggregations'][0]['fixedCounts']['OTHER']['CRITICAL']



        WaiSecLowWk = app['aggregations'][0]['waivedCounts']['SECURITY']['LOW']
        WaiSecModWk = app['aggregations'][0]['waivedCounts']['SECURITY']['MODERATE']
        WaiSecSevWk = app['aggregations'][0]['waivedCounts']['SECURITY']['SEVERE']
        WaiSecCriWk = app['aggregations'][0]['waivedCounts']['SECURITY']['CRITICAL']

        WaiLicLowWk = app['aggregations'][0]['waivedCounts']['LICENSE']['LOW']
        WaiLicModWk = app['aggregations'][0]['waivedCounts']['LICENSE']['MODERATE']
        WaiLicSevWk = app['aggregations'][0]['waivedCounts']['LICENSE']['SEVERE']
        WaiLicCriWk = app['aggregations'][0]['waivedCounts']['LICENSE']['CRITICAL']

        WaiQuaLowWk = app['aggregations'][0]['waivedCounts']['QUALITY']['LOW']
        WaiQuaModWk = app['aggregations'][0]['waivedCounts']['QUALITY']['MODERATE']
        WaiQuaSevWk = app['aggregations'][0]['waivedCounts']['QUALITY']['SEVERE']
        WaiQuaCriWk = app['aggregations'][0]['waivedCounts']['QUALITY']['CRITICAL']

        WaiOthLowWk = app['aggregations'][0]['waivedCounts']['OTHER']['LOW']
        WaiOthModWk = app['aggregations'][0]['waivedCounts']['OTHER']['MODERATE']
        WaiOthSevWk = app['aggregations'][0]['waivedCounts']['OTHER']['SEVERE']
        WaiOthCriWk = app['aggregations'][0]['waivedCounts']['OTHER']['CRITICAL']
        


        OpeSecLowWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['SECURITY']['LOW']
        OpeSecModWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['SECURITY']['MODERATE']
        OpeSecSevWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['SECURITY']['SEVERE']
        OpeSecCriWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['SECURITY']['CRITICAL']

        OpeLicLowWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['LICENSE']['LOW']
        OpeLicModWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['LICENSE']['MODERATE']
        OpeLicSevWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['LICENSE']['SEVERE']
        OpeLicCriWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['LICENSE']['CRITICAL']

        OpeQuaLowWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['QUALITY']['LOW']
        OpeQuaModWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['QUALITY']['MODERATE']
        OpeQuaSevWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['QUALITY']['SEVERE']
        OpeQuaCriWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['QUALITY']['CRITICAL']

        OpeOthLowWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['OTHER']['LOW']
        OpeOthModWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['OTHER']['MODERATE']
        OpeOthSevWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['OTHER']['SEVERE']
        OpeOthCriWk = app['aggregations'][0]['openCountsAtTimePeriodEnd']['OTHER']['CRITICAL']
        

    EvalCount += EvalCountWk

    

    MttrLow += MttrLowWk
    MttrMod += MttrModWk
    MttrSev += MttrSevWk
    MttrCri += MttrCriWk

    
        
    DisSecLow += DisSecLowWk
    DisSecMod += DisSecModWk
    DisSecSev += DisSecSevWk
    DisSecCri += DisSecCriWk

    DisLicLow += DisLicLowWk
    DisLicMod += DisLicModWk
    DisLicSev += DisLicSevWk
    DisLicCri += DisLicCriWk

    DisQuaLow += DisQuaLowWk
    DisQuaMod += DisQuaModWk
    DisQuaSev += DisQuaSevWk
    DisQuaCri += DisQuaCriWk

    DisOthLow += DisOthLowWk
    DisOthMod += DisOthModWk
    DisOthSev += DisOthSevWk
    DisOthCri += DisOthCriWk



    FixSecLow += FixSecLowWk
    FixSecMod += FixSecModWk
    FixSecSev += FixSecSevWk
    FixSecCri += FixSecCriWk

    FixLicLow += FixLicLowWk
    FixLicMod += FixLicModWk
    FixLicSev += FixLicSevWk
    FixLicCri += FixLicCriWk

    FixQuaLow += FixQuaLowWk
    FixQuaMod += FixQuaModWk
    FixQuaSev += FixQuaSevWk
    FixQuaCri += FixQuaCriWk

    FixOthLow += FixOthLowWk
    FixOthMod += FixOthModWk
    FixOthSev += FixOthSevWk
    FixOthCri += FixOthCriWk



    WaiSecLow += WaiSecLowWk
    WaiSecMod += WaiSecModWk
    WaiSecSev += WaiSecSevWk
    WaiSecCri += WaiSecCriWk

    WaiLicLow += WaiLicLowWk
    WaiLicMod += WaiLicModWk
    WaiLicSev += WaiLicSevWk
    WaiLicCri += WaiLicCriWk

    WaiQuaLow += WaiQuaLowWk
    WaiQuaMod += WaiQuaModWk
    WaiQuaSev += WaiQuaSevWk
    WaiQuaCri += WaiQuaCriWk

    WaiOthLow += WaiOthLowWk
    WaiOthMod += WaiOthModWk
    WaiOthSev += WaiOthSevWk
    WaiOthCri += WaiOthCriWk
    


    OpeSecLow += OpeSecLowWk
    OpeSecMod += OpeSecModWk
    OpeSecSev += OpeSecSevWk
    OpeSecCri += OpeSecCriWk

    OpeLicLow += OpeLicLowWk
    OpeLicMod += OpeLicModWk
    OpeLicSev += OpeLicSevWk
    OpeLicCri += OpeLicCriWk

    OpeQuaLow += OpeQuaLowWk
    OpeQuaMod += OpeQuaModWk
    OpeQuaSev += OpeQuaSevWk
    OpeQuaCri += OpeQuaCriWk

    OpeOthLow += OpeOthLowWk
    OpeOthMod += OpeOthModWk
    OpeOthSev += OpeOthSevWk
    OpeOthCri += OpeOthCriWk
    

FixLow = FixSecLow + FixLicLow + FixQuaLow + FixOthLow
FixMod = FixSecMod + FixLicMod + FixQuaMod + FixOthMod
FixSev = FixSecSev + FixLicSev + FixQuaSev + FixOthSev
FixCri = FixSecCri + FixLicCri + FixQuaCri + FixOthCri

WaiLow = WaiSecLow + WaiLicLow + WaiQuaLow + WaiOthLow
WaiMod = WaiSecMod + WaiLicMod + WaiQuaMod + WaiOthMod
WaiSev = WaiSecSev + WaiLicSev + WaiQuaSev + WaiOthSev
WaiCri = WaiSecCri + WaiLicCri + WaiQuaCri + WaiOthCri

OpeLow = OpeSecLow + OpeLicLow + OpeQuaLow + OpeOthLow
OpeMod = OpeSecMod + OpeLicMod + OpeQuaMod + OpeOthMod
OpeSev = OpeSecSev + OpeLicSev + OpeQuaSev + OpeOthSev
OpeCri = OpeSecCri + OpeLicCri + OpeQuaCri + OpeOthCri

FixAll = FixLow + FixMod + FixSev + FixCri
WaiAll =  WaiLow + WaiMod + WaiSev + WaiCri
OpeAll = OpeLow + OpeMod + OpeSev + OpeCri


if OpeAll !=0:
    DeaRateAll = (FixAll+WaiAll)/OpeAll*100
else:
    DeaRateAll = 0


if FixLow !=0:
    MttrLowAvg = MttrLow/FixLow
else:
    MttrLowAvg = 0

if FixMod !=0:
    MttrModAvg = MttrMod/FixMod
else:
    MttrModAvg = 0

if FixSev !=0:
    MttrSevAvg = MttrSev/FixSev
else:
    MttrSevAvg = 0

if FixCri !=0:
    MttrCriAvg = MttrCri/FixCri
else:
    MttrCriAvg = 0




if OpeLow !=0:
    DeaRateLow = (FixLow+WaiLow)/OpeLow*100
else:
    DeaRateLow = 0

if OpeMod !=0:
    DeaRateMod = (FixMod+WaiMod)/OpeMod*100
else:
    DeaRateMod = 0

if OpeSev !=0:
    DeaRateSev = (FixSev+WaiSev)/OpeSev*100
else:
    DeaRateSev = 0

if OpeCri !=0:
    DeaRateCri = (FixCri+WaiCri)/OpeCri*100
else:
    DeaRateCri = 0




if OpeSecLow != 0:
    FixRateSecLow = FixSecLow/OpeSecLow*100
    WaiRateSecLow = WaiSecLow/OpeSecLow*100
    DeaRateSecLow = (FixSecLow+WaiSecLow)/OpeSecLow*100
else:
    FixRateSecLow = 0
    WaiRateSecLow = 0
    DeaRateSecLow = 0

if OpeSecMod != 0:
    FixRateSecMod = FixSecMod/OpeSecMod*100
    WaiRateSecMod = WaiSecMod/OpeSecMod*100
    DeaRateSecMod = (FixSecMod+WaiSecMod)/OpeSecMod*100
else:
    FixRateSecMod = 0
    WaiRateSecMod = 0
    DeaRateSecMod = 0

if OpeSecSev != 0:
    FixRateSecSev = FixSecSev/OpeSecSev*100
    WaiRateSecSev = WaiSecSev/OpeSecSev*100
    DeaRateSecSev = (FixSecSev+WaiSecSev)/OpeSecSev*100
else:
    FixRateSecSev = 0
    WaiRateSecSev = 0
    DeaRateSecSev = 0

if OpeSecCri != 0:
    FixRateSecCri = FixSecCri/OpeSecCri*100
    WaiRateSecCri = WaiSecCri/OpeSecCri*100
    DeaRateSecCri = (FixSecCri+WaiSecCri)/OpeSecCri*100
else:
    FixRateSecCri = 0
    WaiRateSecCri = 0
    DeaRateSecCri = 0



if OpeLicLow != 0:
    FixRateLicLow = FixLicLow/OpeLicLow*100
    WaiRateLicLow = WaiLicLow/OpeLicLow*100
    DeaRateLicLow = (FixLicLow+WaiLicLow)/OpeLicLow*100
else:
    FixRateLicLow = 0
    WaiRateLicLow = 0
    DeaRateLicLow = 0

if OpeLicMod != 0:
    FixRateLicMod = FixLicMod/OpeLicMod*100
    WaiRateLicMod = WaiLicMod/OpeLicMod*100
    DeaRateLicMod = (FixLicMod+WaiLicMod)/OpeLicMod*100
else:
    FixRateLicMod = 0
    WaiRateLicMod = 0
    DeaRateLicMod = 0

if OpeLicSev != 0:
    FixRateLicSev = FixLicSev/OpeLicSev*100
    WaiRateLicSev = WaiLicSev/OpeLicSev*100
    DeaRateLicSev = (FixLicSev+WaiLicSev)/OpeLicSev*100
else:
    FixRateLicSev = 0
    WaiRateLicSev = 0
    DeaRateLicSev = 0

if OpeLicCri != 0:
    FixRateLicCri = FixLicCri/OpeLicCri*100
    WaiRateLicCri = WaiLicCri/OpeLicCri*100
    DeaRateLicCri = (FixLicCri+WaiLicCri)/OpeLicCri*100
else:
    FixRateLicCri = 0
    WaiRateLicCri = 0
    DeaRateLicCri = 0



if OpeQuaLow != 0:
    FixRateQuaLow = FixQuaLow/OpeQuaLow*100
    WaiRateQuaLow = WaiQuaLow/OpeQuaLow*100
    DeaRateQuaLow = (FixQuaLow+WaiQuaLow)/OpeQuaLow*100
else:
    FixRateQuaLow = 0
    WaiRateQuaLow = 0
    DeaRateQuaLow = 0

if OpeQuaMod != 0:
    FixRateQuaMod = FixQuaMod/OpeQuaMod*100
    WaiRateQuaMod = WaiQuaMod/OpeQuaMod*100
    DeaRateQuaMod = (FixQuaMod+WaiQuaMod)/OpeQuaMod*100
else:
    FixRateQuaMod = 0
    WaiRateQuaMod = 0
    DeaRateQuaMod = 0

if OpeQuaSev != 0:
    FixRateQuaSev = FixQuaSev/OpeQuaSev*100
    WaiRateQuaSev = WaiQuaSev/OpeQuaSev*100
    DeaRateQuaSev = (FixQuaSev+WaiQuaSev)/OpeQuaSev*100
else:
    FixRateQuaSev = 0
    WaiRateQuaSev = 0
    DeaRateQuaSev = 0

if OpeQuaCri != 0:
    FixRateQuaCri = FixQuaCri/OpeQuaCri*100
    WaiRateQuaCri = WaiQuaCri/OpeQuaCri*100
    DeaRateQuaCri = (FixQuaCri+WaiQuaCri)/OpeQuaCri*100
else:
    FixRateQuaCri = 0
    WaiRateQuaCri = 0
    DeaRateQuaCri = 0



if OpeOthLow != 0:
    FixRateOthLow = FixOthLow/OpeOthLow*100
    WaiRateOthLow = WaiOthLow/OpeOthLow*100
    DeaRateOthLow = (FixOthLow+WaiOthLow)/OpeOthLow*100
else:
    FixRateOthLow = 0
    WaiRateOthLow = 0
    DeaRateOthLow = 0

if OpeOthMod != 0:
    FixRateOthMod = FixOthMod/OpeOthMod*100
    WaiRateOthMod = WaiOthMod/OpeOthMod*100
    DeaRateOthMod = (FixOthMod+WaiOthMod)/OpeOthMod*100
else:
    FixRateOthMod = 0
    WaiRateOthMod = 0
    DeaRateOthMod = 0

if OpeOthSev != 0:
    FixRateOthSev = FixOthSev/OpeOthSev*100
    WaiRateOthSev = WaiOthSev/OpeOthSev*100
    DeaRateOthSev = (FixOthSev+WaiOthSev)/OpeOthSev*100
else:
    FixRateOthSev = 0
    WaiRateOthSev = 0
    DeaRateOthSev = 0

if OpeOthCri != 0:
    FixRateOthCri = FixOthCri/OpeOthCri*100
    WaiRateOthCri = WaiOthCri/OpeOthCri*100
    DeaRateOthCri = (FixOthCri+WaiOthCri)/OpeOthCri*100
else:
    FixRateOthCri = 0
    WaiRateOthCri = 0
    DeaRateOthCri = 0


print("--------------------------------------------------------------------------------------------------------------------------------------------------")

print("\nWeekly rolling average YTD Number of Evaluations (scans/week): "+str(round(EvalCount/counter,2))+ " scans/week\n")

print("--------------------------------------------------------------------------------------------------------------------------------------------------")

print("\nWeekly rolling average YTD MTTR Low Threat (in days): "+str(round(MttrLowAvg,2))+" days")
print("Weekly rolling average YTD MTTR Moderate Threat (in days): "+str(round(MttrModAvg,2))+" days")
print("Weekly rolling average YTD MTTR Severe Threat (in days): "+str(round(MttrSevAvg,2))+" days")
print("Weekly rolling average YTD MTTR Critical Threat (in days): "+str(round(MttrCriAvg,2))+" days\n")


print("--------------------------------------------------------------------------------------------------------------------------------------------------")

print("\nWeekly rolling average YTD discoveredCounts Security Low (per week): "+str(round(DisSecLow/counter,2))+" per week")
print("Weekly rolling average YTD discoveredCounts Security Moderate (per week): "+str(round(DisSecMod/counter,2))+" per week")
print("Weekly rolling average YTD discoveredCounts Security Severe (per week): "+str(round(DisSecSev/counter,2))+" per week")
print("Weekly rolling average YTD discoveredCounts Security Critical (per week): "+str(round(DisSecCri/counter,2))+" per week")

print("\nWeekly rolling average YTD discoveredCounts License Low (per week): "+str(round(DisLicLow/counter,2))+" per week")
print("Weekly rolling average YTD discoveredCounts License Moderate (per week): "+str(round(DisLicMod/counter,2))+" per week")
print("Weekly rolling average YTD discoveredCounts License Severe (per week): "+str(round(DisLicSev/counter,2))+" per week")
print("Weekly rolling average YTD discoveredCounts License Critical (per week): "+str(round(DisLicCri/counter,2))+" per week")

print("\nWeekly rolling average YTD discoveredCounts Quality Low (per week): "+str(round(DisQuaLow/counter,2))+" per week")
print("Weekly rolling average YTD discoveredCounts Quality Moderate (per week): "+str(round(DisQuaMod/counter,2))+" per week")
print("Weekly rolling average YTD discoveredCounts Quality Severe (per week): "+str(round(DisQuaSev/counter,2))+" per week")
print("Weekly rolling average YTD discoveredCounts Quality Critical (per week): "+str(round(DisQuaCri/counter,2))+" per week")

print("\nWeekly rolling average YTD discoveredCounts Other Low (per week): "+str(round(DisOthLow/counter,2))+" per week")
print("Weekly rolling average YTD discoveredCounts Other Moderate (per week): "+str(round(DisOthMod/counter,2))+" per week")
print("Weekly rolling average YTD discoveredCounts Other Severe (per week): "+str(round(DisOthSev/counter,2))+" per week")
print("Weekly rolling average YTD discoveredCounts Other Critical (per week): "+str(round(DisOthCri/counter,2))+" per week\n")

print("--------------------------------------------------------------------------------------------------------------------------------------------------")

print("\nWeekly rolling average YTD fixedCounts Security Low (per week): "+str(round(FixSecLow/counter,2))+" per week")
print("Weekly rolling average YTD fixedCounts Security Moderate (per week): "+str(round(FixSecMod/counter,2))+" per week")
print("Weekly rolling average YTD fixedCounts Security Severe (per week): "+str(round(FixSecSev/counter,2))+" per week")
print("Weekly rolling average YTD fixedCounts Security Critical (per week): "+str(round(FixSecCri/counter,2))+" per week")

print("\nWeekly rolling average YTD fixedCounts License Low (per week): "+str(round(FixLicLow/counter,2))+" per week")
print("Weekly rolling average YTD fixedCounts License Moderate (per week): "+str(round(FixLicMod/counter,2))+" per week")
print("Weekly rolling average YTD fixedCounts License Severe (per week): "+str(round(FixLicSev/counter,2))+" per week")
print("Weekly rolling average YTD fixedCounts License Critical (per week): "+str(round(FixLicCri/counter,2))+" per week")

print("\nWeekly rolling average YTD fixedCounts Quality Low (per week): "+str(round(FixQuaLow/counter,2))+" per week")
print("Weekly rolling average YTD fixedCounts Quality Moderate (per week): "+str(round(FixQuaMod/counter,2))+" per week")
print("Weekly rolling average YTD fixedCounts Quality Severe (per week): "+str(round(FixQuaSev/counter,2))+" per week")
print("Weekly rolling average YTD fixedCounts Quality Critical (per week): "+str(round(FixQuaCri/counter,2))+" per week")

print("\nWeekly rolling average YTD fixedCounts Other Low (per week): "+str(round(FixOthLow/counter,2))+" per week")
print("Weekly rolling average YTD fixedCounts Other Moderate (per week): "+str(round(FixOthMod/counter,2))+" per week")
print("Weekly rolling average YTD fixedCounts Other Severe (per week): "+str(round(FixOthSev/counter,2))+" per week")
print("Weekly rolling average YTD fixedCounts Other Critical (per week): "+str(round(FixOthCri/counter,2))+" per week\n")

print("--------------------------------------------------------------------------------------------------------------------------------------------------")

print("\nWeekly rolling average YTD waivedCounts Security Low (per week): "+str(round(WaiSecLow/counter,2))+" per week")
print("Weekly rolling average YTD waivedCounts Security Moderate (per week): "+str(round(WaiSecMod/counter,2))+" per week")
print("Weekly rolling average YTD waivedCounts Security Severe (per week): "+str(round(WaiSecSev/counter,2))+" per week")
print("Weekly rolling average YTD waivedCounts Security Critical (per week): "+str(round(WaiSecCri/counter,2))+" per week")

print("\nWeekly rolling average YTD waivedCounts License Low (per week): "+str(round(WaiLicLow/counter,2))+" per week")
print("Weekly rolling average YTD waivedCounts License Moderate (per week): "+str(round(WaiLicMod/counter,2))+" per week")
print("Weekly rolling average YTD waivedCounts License Severe (per week): "+str(round(WaiLicSev/counter,2))+" per week")
print("Weekly rolling average YTD waivedCounts License Critical (per week): "+str(round(WaiLicCri/counter,2))+" per week")

print("\nWeekly rolling average YTD waivedCounts Quality Low (per week): "+str(round(WaiQuaLow/counter,2))+" per week")
print("Weekly rolling average YTD waivedCounts Quality Moderate (per week): "+str(round(WaiQuaMod/counter,2))+" per week")
print("Weekly rolling average YTD waivedCounts Quality Severe (per week): "+str(round(WaiQuaSev/counter,2))+" per week")
print("Weekly rolling average YTD waivedCounts Quality Critical (per week): "+str(round(WaiQuaCri/counter,2))+" per week")

print("\nWeekly rolling average YTD waivedCounts Other Low (per week): "+str(round(WaiOthLow/counter,2))+" per week")
print("Weekly rolling average YTD waivedCounts Other Moderate (per week): "+str(round(WaiOthMod/counter,2))+" per week")
print("Weekly rolling average YTD waivedCounts Other Severe (per week): "+str(round(WaiOthSev/counter,2))+" per week")
print("Weekly rolling average YTD waivedCounts Other Critical (per week): "+str(round(WaiOthCri/counter,2))+" per week\n")

print("--------------------------------------------------------------------------------------------------------------------------------------------------")

print("\nWeekly rolling average YTD openCountsAtTimePeriodEnd Security Low (per week): "+str(round(OpeSecLow/counter,2))+" per week")
print("Weekly rolling average YTD openCountsAtTimePeriodEnd Security Moderate (per week): "+str(round(OpeSecMod/counter,2))+" per week")
print("Weekly rolling average YTD openCountsAtTimePeriodEnd Security Severe (per week): "+str(round(OpeSecSev/counter,2))+" per week")
print("Weekly rolling average YTD openCountsAtTimePeriodEnd Security Critical (per week): "+str(round(OpeSecCri/counter,2))+" per week")

print("\nWeekly rolling average YTD openCountsAtTimePeriodEnd License Low (per week): "+str(round(OpeLicLow/counter,2))+" per week")
print("Weekly rolling average YTD openCountsAtTimePeriodEnd License Moderate (per week): "+str(round(OpeLicMod/counter,2))+" per week")
print("Weekly rolling average YTD openCountsAtTimePeriodEnd License Severe (per week): "+str(round(OpeLicSev/counter,2))+" per week")
print("Weekly rolling average YTD openCountsAtTimePeriodEnd License Critical (per week): "+str(round(OpeLicCri/counter,2))+" per week")

print("\nWeekly rolling average YTD openCountsAtTimePeriodEnd Quality Low (per week): "+str(round(OpeQuaLow/counter,2))+" per week")
print("Weekly rolling average YTD openCountsAtTimePeriodEnd Quality Moderate (per week): "+str(round(OpeQuaMod/counter,2))+" per week")
print("Weekly rolling average YTD openCountsAtTimePeriodEnd Quality Severe (per week): "+str(round(OpeQuaSev/counter,2))+" per week")
print("Weekly rolling average YTD openCountsAtTimePeriodEnd Quality Critical (per week): "+str(round(OpeQuaCri/counter,2))+" per week")

print("\nWeekly rolling average YTD openCountsAtTimePeriodEnd Other Low (per week): "+str(round(OpeOthLow/counter,2))+" per week")
print("Weekly rolling average YTD openCountsAtTimePeriodEnd Other Moderate (per week): "+str(round(OpeOthMod/counter,2))+" per week")
print("Weekly rolling average YTD openCountsAtTimePeriodEnd Other Severe (per week): "+str(round(OpeOthSev/counter,2))+" per week")
print("Weekly rolling average YTD openCountsAtTimePeriodEnd Other Critical (per week): "+str(round(OpeOthCri/counter,2))+" per week\n")

print("--------------------------------------------------------------------------------------------------------------------------------------------------")

print("\nWeekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) Security Low (per week): "+str(round(FixRateSecLow,2))+"%")
print("Weekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) Security Moderate (per week): "+str(round(FixRateSecMod,2))+"%")
print("Weekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) Security Severe (per week): "+str(round(FixRateSecSev,2))+"%")
print("Weekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) Security Critical (per week): "+str(round(FixRateSecCri,2))+"%")
print("\nWeekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) License Low (per week): "+str(round(FixRateLicLow,2))+"%")
print("Weekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) License Moderate (per week): "+str(round(FixRateLicMod,2))+"%")
print("Weekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) License Severe (per week): "+str(round(FixRateLicSev,2))+"%")
print("Weekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) License Critical (per week): "+str(round(FixRateLicCri,2))+"%")
print("\nWeekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) Quality Low (per week): "+str(round(FixRateQuaLow,2))+"%")
print("Weekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) Quality Moderate (per week): "+str(round(FixRateQuaMod,2))+"%")
print("Weekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) Quality Severe (per week): "+str(round(FixRateQuaSev,2))+"%")
print("Weekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) Quality Critical (per week): "+str(round(FixRateQuaCri,2))+"%")
print("\nWeekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) Other Low (per week): "+str(round(FixRateOthLow,2))+"%")
print("Weekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) Other Moderate (per week): "+str(round(FixRateOthMod,2))+"%")
print("Weekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) Other Severe (per week): "+str(round(FixRateOthSev,2))+"%")
print("Weekly rolling average YTD Fix Rate (fixedCounts / openCountsAtTimePeriodEnd) Other Critical (per week): "+str(round(FixRateOthCri,2))+"%\n")

print("--------------------------------------------------------------------------------------------------------------------------------------------------")


print("\nWeekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) Security Low (per week): "+str(round(WaiRateSecLow,2))+"%")
print("Weekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) Security Moderate (per week): "+str(round(WaiRateSecMod,2))+"%")
print("Weekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) Security Severe (per week): "+str(round(WaiRateSecSev,2))+"%")
print("Weekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) Security Critical (per week): "+str(round(WaiRateSecCri,2))+"%")
print("\nWeekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) License Low (per week): "+str(round(WaiRateLicLow,2))+"%")
print("Weekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) License Moderate (per week): "+str(round(WaiRateLicMod,2))+"%")
print("Weekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) License Severe (per week): "+str(round(WaiRateLicSev,2))+"%")
print("Weekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) License Critical (per week): "+str(round(WaiRateLicCri,2))+"%")
print("\nWeekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) Quality Low (per week): "+str(round(WaiRateQuaLow,2))+"%")
print("Weekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) Quality Moderate (per week): "+str(round(WaiRateQuaMod,2))+"%")
print("Weekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) Quality Severe (per week): "+str(round(WaiRateQuaSev,2))+"%")
print("Weekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) Quality Critical (per week): "+str(round(WaiRateQuaCri,2))+"%")
print("\nWeekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) Other Low (per week): "+str(round(WaiRateOthLow,2))+"%")
print("Weekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) Other Moderate (per week): "+str(round(WaiRateOthMod,2))+"%")
print("Weekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) Other Severe (per week): "+str(round(WaiRateOthSev,2))+"%")
print("Weekly rolling average YTD Waive Rate (waivedCounts / openCountsAtTimePeriodEnd) Other Critical (per week): "+str(round(WaiRateOthCri,2))+"%\n")

print("--------------------------------------------------------------------------------------------------------------------------------------------------")


print("\nWeekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) Security Low (per week): "+str(round(DeaRateSecLow,2))+"%")
print("Weekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) Security Moderate (per week): "+str(round(DeaRateSecMod,2))+"%")
print("Weekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) Security Severe (per week): "+str(round(DeaRateSecSev,2))+"%")
print("Weekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) Security Critical (per week): "+str(round(DeaRateSecCri,2))+"%")
print("\nWeekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) License Low (per week): "+str(round(DeaRateLicLow,2))+"%")
print("Weekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) License Moderate (per week): "+str(round(DeaRateLicMod,2))+"%")
print("Weekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) License Severe (per week): "+str(round(DeaRateLicSev,2))+"%")
print("Weekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) License Critical (per week): "+str(round(DeaRateLicCri,2))+"%")
print("\nWeekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) Quality Low (per week): "+str(round(DeaRateQuaLow,2))+"%")
print("Weekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) Quality Moderate (per week): "+str(round(DeaRateQuaMod,2))+"%")
print("Weekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) Quality Severe (per week): "+str(round(DeaRateQuaSev,2))+"%")
print("Weekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) Quality Critical (per week): "+str(round(DeaRateQuaCri,2))+"%")
print("\nWeekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) Other Low (per week): "+str(round(DeaRateOthLow,2))+"%")
print("Weekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) Other Moderate (per week): "+str(round(DeaRateOthMod,2))+"%")
print("Weekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) Other Severe (per week): "+str(round(DeaRateOthSev,2))+"%")
print("Weekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) Other Critical (per week): "+str(round(DeaRateOthCri,2))+"%\n")

print("--------------------------------------------------------------------------------------------------------------------------------------------------")


print("\nWeekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) All Low (per week): "+str(round(DeaRateLow,2))+"%")
print("Weekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) All Moderate (per week): "+str(round(DeaRateMod,2))+"%")
print("Weekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) All Severe (per week): "+str(round(DeaRateSev,2))+"%")
print("Weekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) All Critical (per week): "+str(round(DeaRateCri,2))+"%\n")


print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print("\nWeekly rolling average YTD Dealt-with Rate ((fixedCounts + waivedCounts) / openCountsAtTimePeriodEnd) Aggregated All: "+str(round(DeaRateAll,2))+"%\n")
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------------------------------------")







    
'''    
    #print(resp.content)
    for iq_app in resp.json():
        date_start = str(iq_app['aggregations'][0]['timePeriodStart'])
        iq_app_id = iq_app['applicationId']
        iq_app_public_id = iq_app['applicationPublicId']
        iq_app_name = iq_app['applicationName']
        iq_org_id = iq_app['organizationId']
        iq_org_name = iq_app['organizationName']

        
        
        print("date_start: ",date_start)
        print("iq_app_id: ",iq_app_id)
        print("iq_app_public_id: ",iq_app_public_id)
        print("iq_app_name: ",iq_app_name)
        print("iq_org_id: ",iq_org_id)
        print("iq_org_name: ",iq_org_name)
        

        #MTTR LOW THREAT

        mttrLowThreat = str(iq_app['aggregations'][0]['mttrLowThreat'])
        metric = iq_app['aggregations'][0]['mttrLowThreat']
        print("MTTR LOW THREAT (in milliseconds): "+str(metric)+ " ms")

        if(isinstance(metric, int)):
            print("MTTR LOW THREAT (in days): "+ str(round(metric/86400000)) + " days")
        else:
            print("MTTR LOW THREAT (in days): None")

        #MTTR MODERATE THREAT

        mttrModerateThreat = str(iq_app['aggregations'][0]['mttrModerateThreat'])
        metric = iq_app['aggregations'][0]['mttrModerateThreat']
        print("MTTR MODERATE THREAT (in milliseconds): "+str(metric)+" ms")

        if(isinstance(metric, int)):
            print("MTTR MODERATE THREAT (in days): "+str(round(metric/86400000))+ " days")
        else:
            print("MTTR MODERATE THREAT (in days): None")

        #MTTR SEVERE THREAT

        mttrSevereThreat = str(iq_app['aggregations'][0]['mttrSevereThreat'])
        metric = iq_app['aggregations'][0]['mttrSevereThreat']
        print("MTTR SEVERE THREAT (in milliseconds): "+str(metric)+" ms")

        if(isinstance(metric, int)):
            print("MTTR SEVERE THREAT (in days): "+str(round(metric/86400000))+" days")
        else:
            print("MTTR SEVERE THREAT (in days): None")

        #MTTR CRITICAL THREAT

        mttrCriticalThreat = str(iq_app['aggregations'][0]['mttrCriticalThreat'])
        metric = iq_app['aggregations'][0]['mttrCriticalThreat']
        print("MTTR CRITICAL THREAT (in milliseconds): "+str(metric)+ " ms")

        if(isinstance(metric, int)):
            print("MTTR LOW THREAT (in days): "+str(round(metric/86400000))+ " days")
        else:
            print("MTTR LOW THREAT (in days): None")

        #discoveredCounts SECURITY LOW

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['SECURITY']['LOW'])
        print("discoveredCounts SECURITY LOW: ",metric)
        
        #discoveredCounts SECURITY MODERATE

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['SECURITY']['MODERATE'])
        print("discoveredCounts SECURITY MODERATE: ",metric)
        
        #discoveredCounts SECURITY SEVERE

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['SECURITY']['SEVERE'])
        print("discoveredCounts SECURITY SEVERE: ",metric)
        
        #discoveredCounts SECURITY CRITICAL

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['SECURITY']['CRITICAL'])
        print("discoveredCounts SECURITY CRITICAL: ",metric)
        
        #discoveredCounts LICENSE LOW

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['LICENSE']['LOW'])
        print("discoveredCounts LICENSE LOW: ",metric)
        
        #discoveredCounts LICENSE MODERATE

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['LICENSE']['MODERATE'])
        print("discoveredCounts LICENSE MODERATE: ",metric)
        
        #discoveredCounts LICENSE SEVERE

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['LICENSE']['SEVERE'])
        print("discoveredCounts LICENSE SEVERE: ",metric)
        
        #discoveredCounts LICENSE CRITICAL

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['LICENSE']['CRITICAL'])
        print("discoveredCounts LICENSE CRITICAL: ",metric)
         				
        #discoveredCounts QUALITY LOW

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['QUALITY']['LOW'])
        print("discoveredCounts QUALITY LOW: ",metric)
        
        #discoveredCounts QUALITY MODERATE

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['QUALITY']['MODERATE'])
        print("discoveredCounts QUALITY MODERATE: ",metric)
        
        #discoveredCounts QUALITY SEVERE

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['QUALITY']['SEVERE'])
        print("discoveredCounts QUALITY SEVERE: ",metric)
        
        #discoveredCounts QUALITY CRITICAL

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['QUALITY']['CRITICAL'])
        print("discoveredCounts QUALITY CRITICAL: ",metric)
        

        #discoveredCounts OTHER LOW

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['OTHER']['LOW'])
        print("discoveredCounts OTHER LOW: ",metric)
        

        #discoveredCounts OTHER MODERATE

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['OTHER']['MODERATE'])
        print("discoveredCounts OTHER MODERATE: ",metric)
        
        #discoveredCounts OTHER SEVERE

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['OTHER']['SEVERE'])
        print("discoveredCounts OTHER SEVERE: ",metric)
        

        #discoveredCounts OTHER CRITICAL

        metric = str(iq_app['aggregations'][0]['discoveredCounts']['OTHER']['CRITICAL'])
        print("discoveredCounts OTHER CRITICAL: ",metric)
        

        #fixedCounts

        #fixedCounts SECURITY LOW

        metric = str(iq_app['aggregations'][0]['fixedCounts']['SECURITY']['LOW'])
        print("fixedCounts SECURITY LOW: ",metric)
        

        #fixedCounts SECURITY MODERATE

        metric = str(iq_app['aggregations'][0]['fixedCounts']['SECURITY']['MODERATE'])
        print("fixedCounts SECURITY MODERATE: ",metric)
        

        #fixedCounts SECURITY SEVERE

        metric = str(iq_app['aggregations'][0]['fixedCounts']['SECURITY']['SEVERE'])
        print("fixedCounts SECURITY SEVERE: ",metric)
        

        #fixedCounts SECURITY CRITICAL

        metric = str(iq_app['aggregations'][0]['fixedCounts']['SECURITY']['CRITICAL'])
        print("fixedCounts SECURITY CRITICAL: ",metric)
        
        #fixedCounts LICENSE LOW

        metric = str(iq_app['aggregations'][0]['fixedCounts']['LICENSE']['LOW'])
        print("fixedCounts LICENSE LOW: ",metric)
        
        #fixedCounts LICENSE MODERATE

        metric = str(iq_app['aggregations'][0]['fixedCounts']['LICENSE']['MODERATE'])
        print("fixedCounts LICENSE MODERATE: ",metric)
        
        #fixedCounts LICENSE SEVERE

        metric = str(iq_app['aggregations'][0]['fixedCounts']['LICENSE']['SEVERE'])
        print("fixedCounts LICENSE SEVERE: ",metric)
        

        #fixedCounts LICENSE CRITICAL

        metric = str(iq_app['aggregations'][0]['fixedCounts']['LICENSE']['SEVERE'])
        print("fixedCounts LICENSE CRITICAL: ",metric)
        
					
        #fixedCounts QUALITY LOW

        metric = str(iq_app['aggregations'][0]['fixedCounts']['QUALITY']['LOW'])
        print("fixedCounts QUALITY LOW: ",metric)
        
        #fixedCounts QUALITY MODERATE

        metric = str(iq_app['aggregations'][0]['fixedCounts']['QUALITY']['MODERATE'])
        print("fixedCounts QUALITY MODERATE: ",metric)
        
        #fixedCounts QUALITY SEVERE

        metric = str(iq_app['aggregations'][0]['fixedCounts']['QUALITY']['SEVERE'])
        print("fixedCounts QUALITY SEVERE: ",metric)
        
        #fixedCounts QUALITY CRITICAL

        metric = str(iq_app['aggregations'][0]['fixedCounts']['QUALITY']['CRITICAL'])
        print("fixedCounts QUALITY CRITICAL: ",metric)
        
        #fixedCounts OTHER LOW

        metric = str(iq_app['aggregations'][0]['fixedCounts']['OTHER']['LOW'])
        print("fixedCounts OTHER LOW: ",metric)
        
        #fixedCounts OTHER MODERATE

        metric = str(iq_app['aggregations'][0]['fixedCounts']['OTHER']['MODERATE'])
        print("fixedCounts OTHER MODERATE: ",metric)
        
        #fixedCounts OTHER SEVERE

        metric = str(iq_app['aggregations'][0]['fixedCounts']['OTHER']['SEVERE'])
        print("fixedCounts OTHER SEVERE: ",metric)
        
        #fixedCounts OTHER CRITICAL

        metric = str(iq_app['aggregations'][0]['fixedCounts']['OTHER']['SEVERE'])
        print("fixedCounts OTHER CRITICAL: ",metric)
        

        #waivedCounts

        #waivedCounts SECURITY LOW

        metric = str(iq_app['aggregations'][0]['waivedCounts']['SECURITY']['LOW'])
        print("waivedCounts SECURITY LOW: ",metric)
        
        #waivedCounts SECURITY MODERATE

        metric = str(iq_app['aggregations'][0]['waivedCounts']['SECURITY']['MODERATE'])
        print("waivedCounts SECURITY MODERATE: ",metric)
        

        #waivedCounts SECURITY SEVERE

        metric = str(iq_app['aggregations'][0]['waivedCounts']['SECURITY']['SEVERE'])
        print("waivedCounts SECURITY SEVERE: ",metric)
        

        #waivedCounts SECURITY CRITICAL

        metric = str(iq_app['aggregations'][0]['waivedCounts']['SECURITY']['CRITICAL'])
        print("waivedCounts SECURITY CRITICAL: ",metric)
        

        #waivedCounts LICENSE LOW

        metric = str(iq_app['aggregations'][0]['waivedCounts']['LICENSE']['LOW'])
        print("waivedCounts LICENSE LOW: ",metric)
        

        #waivedCounts LICENSE MODERATE

        metric = str(iq_app['aggregations'][0]['waivedCounts']['LICENSE']['MODERATE'])
        print("waivedCounts LICENSE MODERATE: ",metric)
        
        #waivedCounts LICENSE SEVERE

        metric = str(iq_app['aggregations'][0]['waivedCounts']['LICENSE']['SEVERE'])
        print("waivedCounts LICENSE SEVERE: ",metric)
        
        #waivedCounts LICENSE CRITICAL

        metric = str(iq_app['aggregations'][0]['waivedCounts']['LICENSE']['SEVERE'])
        print("waivedCounts LICENSE CRITICAL: ",metric)
         				
        #waivedCounts QUALITY LOW

        metric = str(iq_app['aggregations'][0]['waivedCounts']['QUALITY']['LOW'])
        print("waivedCounts QUALITY LOW: ",metric)
        
        #waivedCounts QUALITY MODERATE

        metric = str(iq_app['aggregations'][0]['waivedCounts']['QUALITY']['MODERATE'])
        print("waivedCounts QUALITY MODERATE: ",metric)
        
        #waivedCounts QUALITY SEVERE

        metric = str(iq_app['aggregations'][0]['waivedCounts']['QUALITY']['SEVERE'])
        print("waivedCounts QUALITY SEVERE: ",metric)
        
        #waivedCounts QUALITY CRITICAL

        metric = str(iq_app['aggregations'][0]['waivedCounts']['QUALITY']['CRITICAL'])
        print("waivedCounts QUALITY CRITICAL: ",metric)
        
        #waivedCounts OTHER LOW

        metric = str(iq_app['aggregations'][0]['waivedCounts']['OTHER']['LOW'])
        print("waivedCounts OTHER LOW: ",metric)
        
        #waivedCounts OTHER MODERATE

        metric = str(iq_app['aggregations'][0]['waivedCounts']['OTHER']['MODERATE'])
        print("waivedCounts OTHER MODERATE: ",metric)
        
        #waivedCounts OTHER SEVERE

        metric = str(iq_app['aggregations'][0]['waivedCounts']['OTHER']['SEVERE'])
        print("waivedCounts OTHER SEVERE: ",metric)
        
        #waivedCounts OTHER CRITICAL

        metric = str(iq_app['aggregations'][0]['waivedCounts']['OTHER']['SEVERE'])
        print("waivedCounts OTHER CRITICAL: ",metric)
        

        #openCountsAtTimePeriodEnd


        #openCountsAtTimePeriodEnd SECURITY LOW

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['SECURITY']['LOW'])
        print("openCountsAtTimePeriodEnd SECURITY LOW: ",metric)
        
        #openCountsAtTimePeriodEnd SECURITY MODERATE

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['SECURITY']['MODERATE'])
        print("openCountsAtTimePeriodEnd SECURITY MODERATE: ",metric)
        

        #openCountsAtTimePeriodEnd SECURITY SEVERE

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['SECURITY']['SEVERE'])
        print("openCountsAtTimePeriodEnd SECURITY SEVERE: ",metric)
        

        #openCountsAtTimePeriodEnd SECURITY CRITICAL

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['SECURITY']['CRITICAL'])
        print("openCountsAtTimePeriodEnd SECURITY CRITICAL: ",metric)
        

        #openCountsAtTimePeriodEnd LICENSE LOW

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['LICENSE']['LOW'])
        print("openCountsAtTimePeriodEnd LICENSE LOW: ",metric)
        

        #openCountsAtTimePeriodEnd LICENSE MODERATE

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['LICENSE']['MODERATE'])
        print("openCountsAtTimePeriodEnd LICENSE MODERATE: ",metric)
        
        #openCountsAtTimePeriodEnd LICENSE SEVERE

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['LICENSE']['SEVERE'])
        print("openCountsAtTimePeriodEnd LICENSE SEVERE: ",metric)
        
        #openCountsAtTimePeriodEnd LICENSE CRITICAL

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['LICENSE']['SEVERE'])
        print("openCountsAtTimePeriodEnd LICENSE CRITICAL: ",metric)
         				
        #openCountsAtTimePeriodEnd QUALITY LOW

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['QUALITY']['LOW'])
        print("openCountsAtTimePeriodEnd QUALITY LOW: ",metric)
        
        #openCountsAtTimePeriodEnd QUALITY MODERATE

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['QUALITY']['MODERATE'])
        print("openCountsAtTimePeriodEnd QUALITY LOW: ",metric)
        
        #openCountsAtTimePeriodEnd QUALITY SEVERE

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['QUALITY']['SEVERE'])
        print("openCountsAtTimePeriodEnd QUALITY SEVERE: ",metric)
        
        #openCountsAtTimePeriodEnd QUALITY CRITICAL

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['QUALITY']['CRITICAL'])
        print("openCountsAtTimePeriodEnd QUALITY CRITICAL: ",metric)
        
        #openCountsAtTimePeriodEnd OTHER LOW

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['OTHER']['LOW'])
        print("openCountsAtTimePeriodEnd OTHER LOW: ",metric)
        
        #openCountsAtTimePeriodEnd OTHER MODERATE

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['OTHER']['MODERATE'])
        print("openCountsAtTimePeriodEnd OTHER MODERATE: ",metric)
        
        #openCountsAtTimePeriodEnd OTHER SEVERE

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['OTHER']['SEVERE'])
        print("openCountsAtTimePeriodEnd OTHER SEVERE: ",metric)
        
        #openCountsAtTimePeriodEnd OTHER CRITICAL

        metric = str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['OTHER']['SEVERE'])
        print("openCountsAtTimePeriodEnd OTHER CRITICAL: ",metric)
        
        #evaluationCount

        metric = str(iq_app['aggregations'][0]['evaluationCount'])
        print("evaluationCount: ",metric)


        #SUCCESS METRICS DERIVED FROM RAW DATA

        #Reduce OSS Vulnerabilities / License Risk
        
        
        
'''    
