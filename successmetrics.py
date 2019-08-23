
########################################################################################################################
#This script is property of Sonatype. Contact: cmorenoserrano@sonatype.com
#This script will collect Success Metrics counters using the IQ Server Success Metrics API v2 and process them into...
#...meaningful Outcome-based success metrics. Data is pulled YTD (from ISO week 1 to the last fully completed ISO week)
########################################################################################################################

from datetime import *
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF
import numpy as np

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


#First we generate the JSON and (optionally) CSV files for each week YTD
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

    #df = pd.read_json(resp.text)                       #Remove the hash to activate generation of CSV files
    #df.to_csv("raw_data_wk"+str(counter)+".csv")       #Remove the hash to activate generation of CSV files

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


FixRateAll = []
WaiRateAll = []
DealtRateAll = []
EvalsCount = []
weeks = []

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


    weeks.append(str(counter))  
    EvalsCount.append(round(EvalCountWk))

    FixAllWk = FixSecLowWk + FixSecModWk + FixSecSevWk + FixSecCriWk + FixLicLowWk + FixLicModWk + FixLicSevWk + FixLicCriWk + FixQuaLowWk + FixQuaModWk + FixQuaSevWk + FixQuaCriWk + FixOthLowWk + FixOthModWk + FixOthSevWk + FixOthCriWk
    WaiAllWk = WaiSecLowWk + WaiSecModWk + WaiSecSevWk + WaiSecCriWk + WaiLicLowWk + WaiLicModWk + WaiLicSevWk + WaiLicCriWk + WaiQuaLowWk + WaiQuaModWk + WaiQuaSevWk + WaiQuaCriWk + WaiOthLowWk + WaiOthModWk + WaiOthSevWk + WaiOthCriWk
    OpeAllWk = OpeSecLowWk + OpeSecModWk + OpeSecSevWk + OpeSecCriWk + OpeLicLowWk + OpeLicModWk + OpeLicSevWk + OpeLicCriWk + OpeQuaLowWk + OpeQuaModWk + OpeQuaSevWk + OpeQuaCriWk + OpeOthLowWk + OpeOthModWk + OpeOthSevWk + OpeOthCriWk

    if OpeAllWk != 0:
        FixRateAll.append(round(FixAllWk/OpeAllWk*100,2))
        WaiRateAll.append(round(WaiAllWk/OpeAllWk*100,2))
        DealtRateAll.append(round((FixAllWk+WaiAllWk)/OpeAllWk*100,2))
        
    else:
        FixRateAll.append(0)
        WaiRateAll.append(0)
        DealtRateAll.append(0)
            
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


#PLOTTING GRAPHS AND SAVING THEM INTO PDF REPORT

N = cur_week+1
ind = np.arange(N)
width = 0.35

#print(plt.gcf().canvas.get_supported_filetypes())
plt.figure(figsize=(9,5)) #9 and 5 in inches
p1 = plt.bar(ind,EvalsCount,width)
plt.xlabel('Week number')
plt.ylabel('Total Number of Evaluations/week')
plt.title("Total Number of Evaluations (scans/week) week-on-week")
plt.xticks(ind,weeks)
#plt.show() #if we show, we cannot save afterwards
plt.savefig('EvalCount.png',orientation='landscape')

plt.figure(figsize=(9,5)) #9 and 5 in inches
p1 = plt.bar(ind,FixRateAll,width)
plt.xlabel('Week number')
plt.ylabel('Average Fix Rate (%)')
plt.title("Average Fix Rate (%) week-on-week")
plt.xticks(ind,weeks)
#plt.show() #if we show, we cannot save afterwards
plt.savefig('FixRateAll.png',orientation='landscape')

plt.figure(figsize=(9,5)) #9 and 5 in inches
p1 = plt.bar(ind,WaiRateAll,width)
plt.xlabel('Week number')
plt.ylabel('Average Waive Rate (%)')
plt.title("Average Waive Rate (%) week-on-week")
plt.xticks(ind,weeks)
#plt.show() #if we show, we cannot save afterwards
plt.savefig('WaiRateAll.png',orientation='landscape')

plt.figure(figsize=(9,5)) #9 and 5 in inches
p1 = plt.bar(ind,FixRateAll,width)
plt.xlabel('Week number')
plt.ylabel('Average Dealt-with Rate (%)')
plt.title("Average Dealt-with Rate (%) week-on-week")
plt.xticks(ind,weeks)
#plt.show() #if we show, we cannot save afterwards
plt.savefig('DealtRateAll.png',orientation='landscape')


pdf = FPDF()
pdf.add_page('L')
pdf.set_xy(0,0)
pdf.set_font('arial','B',12)
pdf.image('EvalCount.png', x = None, y = None, w = 0, h = 0, type = '', link = '')

pdf.add_page('L')
pdf.set_xy(0,0)
pdf.image('FixRateAll.png', x = None, y = None, w = 0, h = 0, type = '', link = '')

pdf.add_page('L')
pdf.set_xy(0,0)
pdf.image('WaiRateAll.png', x = None, y = None, w = 0, h = 0, type = '', link = '')

pdf.add_page('L')
pdf.set_xy(0,0)
pdf.image('DealtRateAll.png', x = None, y = None, w = 0, h = 0, type = '', link = '')

pdf.output('successmetrics.pdf', 'F')



#----------------------------------------------------------------------




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
print("--------------------------------------------------------------------------------------------------------------------------------------------------\n")

#All Success Metrics are Weekly Rolling Average YTD
#Dump all of them into JSON dictionary
SuccessMetrics = {
    "EvaluationsPerWeek": round(EvalCount/counter,2),
    "MTTRLow_days": round(MttrLowAvg,2),
    "MTTRMod_days": round(MttrModAvg,2),
    "MTTRSev_days": round(MttrSevAvg,2),
    "MTTRCri_days": round(MttrCriAvg,2),
    "discoveredCountsSecurityLow": round(DisSecLow/counter,2),
    "discoveredCountsSecurityMod": round(DisSecMod/counter,2),
    "discoveredCountsSecuritySev": round(DisSecSev/counter,2),
    "discoveredCountsSecurityCri": round(DisSecCri/counter,2),
    "discoveredCountsLicenseLow": round(DisLicLow/counter,2),
    "discoveredCountsLicenseMod": round(DisLicMod/counter,2),
    "discoveredCountsLicenseSev": round(DisLicSev/counter,2),
    "discoveredCountsLicenseCri": round(DisLicCri/counter,2),
    "discoveredCountsQualityLow": round(DisQuaLow/counter,2),
    "discoveredCountsQualityMod": round(DisQuaMod/counter,2),
    "discoveredCountsQualitySev": round(DisQuaSev/counter,2),
    "discoveredCountsQualityCri": round(DisQuaCri/counter,2),
    "discoveredCountsOtherLow": round(DisOthLow/counter,2),
    "discoveredCountsOtherMod": round(DisOthMod/counter,2),
    "discoveredCountsOtherSev": round(DisOthSev/counter,2),
    "discoveredCountsOtherCri": round(DisOthCri/counter,2),
    "fixedCountsSecurityLow": round(FixSecLow/counter,2),
    "fixedCountsSecurityMod": round(FixSecMod/counter,2),
    "fixedCountsSecuritySev": round(FixSecSev/counter,2),
    "fixedCountsSecurityCri": round(FixSecCri/counter,2),
    "fixedCountsLicenseLow": round(FixLicLow/counter,2),
    "fixedCountsLicenseMod": round(FixLicMod/counter,2),
    "fixedCountsLicenseSev": round(FixLicSev/counter,2),
    "fixedCountsLicenseCri": round(FixLicCri/counter,2),
    "fixedCountsQualityLow": round(FixQuaLow/counter,2),
    "fixedCountsQualityMod": round(FixQuaMod/counter,2),
    "fixedCountsQualitySev": round(FixQuaSev/counter,2),
    "fixedCountsQualityCri": round(FixQuaCri/counter,2),
    "fixedCountsOtherLow": round(FixOthLow/counter,2),
    "fixedCountsOtherMod": round(FixOthMod/counter,2),
    "fixedCountsOtherSev": round(FixOthSev/counter,2),
    "fixedCountsOtherCri": round(FixOthCri/counter,2),
    "waivedCountsSecurityLow": round(WaiSecLow/counter,2),
    "waivedCountsSecurityMod": round(WaiSecMod/counter,2),
    "waivedCountsSecuritySev": round(WaiSecSev/counter,2),
    "waivedCountsSecurityCri": round(WaiSecCri/counter,2),
    "waivedCountsLicenseLow": round(WaiLicLow/counter,2),
    "waivedCountsLicenseMod": round(WaiLicMod/counter,2),
    "waivedCountsLicenseSev": round(WaiLicSev/counter,2),
    "waivedCountsLicenseCri": round(WaiLicCri/counter,2),
    "waivedCountsQualityLow": round(WaiQuaLow/counter,2),
    "waivedCountsQualityMod": round(WaiQuaMod/counter,2),
    "waivedCountsQualitySev": round(WaiQuaSev/counter,2),
    "waivedCountsQualityCri": round(WaiQuaCri/counter,2),
    "waivedCountsOtherLow": round(WaiOthLow/counter,2),
    "waivedCountsOtherMod": round(WaiOthMod/counter,2),
    "waivedCountsOtherSev": round(WaiOthSev/counter,2),
    "waivedCountsOtherCri": round(WaiOthCri/counter,2),
    "openCountsAtTimePeriodEndSecurityLow": round(OpeSecLow/counter,2),
    "openCountsAtTimePeriodEndSecurityMod": round(OpeSecMod/counter,2),
    "openCountsAtTimePeriodEndSecuritySev": round(OpeSecSev/counter,2),
    "openCountsAtTimePeriodEndSecurityCri": round(OpeSecCri/counter,2),
    "openCountsAtTimePeriodEndLicenseLow": round(OpeLicLow/counter,2),
    "openCountsAtTimePeriodEndLicenseMod": round(OpeLicMod/counter,2),
    "openCountsAtTimePeriodEndLicenseSev": round(OpeLicSev/counter,2),
    "openCountsAtTimePeriodEndLicenseCri": round(OpeLicCri/counter,2),
    "openCountsAtTimePeriodEndQualityLow": round(OpeQuaLow/counter,2),
    "openCountsAtTimePeriodEndQualityMod": round(OpeQuaMod/counter,2),
    "openCountsAtTimePeriodEndQualitySev": round(OpeQuaSev/counter,2),
    "openCountsAtTimePeriodEndQualityCri": round(OpeQuaCri/counter,2),
    "openCountsAtTimePeriodEndOtherLow": round(OpeOthLow/counter,2),
    "openCountsAtTimePeriodEndOtherMod": round(OpeOthMod/counter,2),
    "openCountsAtTimePeriodEndOtherSev": round(OpeOthSev/counter,2),
    "openCountsAtTimePeriodEndOtherCri": round(OpeOthCri/counter,2),
    "FixRateSecurityLow_%": round(FixRateSecLow/counter,2),
    "FixRateSecurityMod_%": round(FixRateSecMod/counter,2),
    "FixRateSecuritySev_%": round(FixRateSecSev/counter,2),
    "FixRateSecurityCri_%": round(FixRateSecCri/counter,2),
    "FixRateLicenseLow_%": round(FixRateLicLow/counter,2),
    "FixRateLicenseMod_%": round(FixRateLicMod/counter,2),
    "FixRateLicenseSev_%": round(FixRateLicSev/counter,2),
    "FixRateLicenseCri_%": round(FixRateLicCri/counter,2),
    "FixRateQualityLow_%": round(FixRateQuaLow/counter,2),
    "FixRateQualityMod_%": round(FixRateQuaMod/counter,2),
    "FixRateQualitySev_%": round(FixRateQuaSev/counter,2),
    "FixRateQualityCri_%": round(FixRateQuaCri/counter,2),
    "FixRateOtherLow_%": round(FixRateOthLow/counter,2),
    "FixRateOtherMod_%": round(FixRateOthMod/counter,2),
    "FixRateOtherSev_%": round(FixRateOthSev/counter,2),
    "FixRateOtherCri_%": round(FixRateOthCri/counter,2),
    "WaiveRateSecurityLow_%": round(WaiRateSecLow/counter,2),
    "WaiveRateSecurityMod_%": round(WaiRateSecMod/counter,2),
    "WaiveRateSecuritySev_%": round(WaiRateSecSev/counter,2),
    "WaiveRateSecurityCri_%": round(WaiRateSecCri/counter,2),
    "WaiveRateLicenseLow_%": round(WaiRateLicLow/counter,2),
    "WaiveRateLicenseMod_%": round(WaiRateLicMod/counter,2),
    "WaiveRateLicenseSev_%": round(WaiRateLicSev/counter,2),
    "WaiveRateLicenseCri_%": round(WaiRateLicCri/counter,2),
    "WaiveRateQualityLow_%": round(WaiRateQuaLow/counter,2),
    "WaiveRateQualityMod_%": round(WaiRateQuaMod/counter,2),
    "WaiveRateQualitySev_%": round(WaiRateQuaSev/counter,2),
    "WaiveRateQualityCri_%": round(WaiRateQuaCri/counter,2),
    "WaiveRateOtherLow_%": round(WaiRateOthLow/counter,2),
    "WaiveRateOtherMod_%": round(WaiRateOthMod/counter,2),
    "WaiveRateOtherSev_%": round(WaiRateOthSev/counter,2),
    "WaiveRateOtherCri_%": round(WaiRateOthCri/counter,2),
    "DealtRateSecurityLow_%": round(DeaRateSecLow/counter,2),
    "DealtRateSecurityMod_%": round(DeaRateSecMod/counter,2),
    "DealtRateSecuritySev_%": round(DeaRateSecSev/counter,2),
    "DealtRateSecurityCri_%": round(DeaRateSecCri/counter,2),
    "DealtRateLicenseLow_%": round(DeaRateLicLow/counter,2),
    "DealtRateLicenseMod_%": round(DeaRateLicMod/counter,2),
    "DealtRateLicenseSev_%": round(DeaRateLicSev/counter,2),
    "DealtRateLicenseCri_%": round(DeaRateLicCri/counter,2),
    "DealtRateQualityLow_%": round(DeaRateQuaLow/counter,2),
    "DealtRateQualityMod_%": round(DeaRateQuaMod/counter,2),
    "DealtRateQualitySev_%": round(DeaRateQuaSev/counter,2),
    "DealtRateQualityCri_%": round(DeaRateQuaCri/counter,2),
    "DealtRateOtherLow_%": round(DeaRateOthLow/counter,2),
    "DealtRateOtherMod_%": round(DeaRateOthMod/counter,2),
    "DealtRateOtherSev_%": round(DeaRateOthSev/counter,2),
    "DealtRateOtherCri_%": round(DeaRateOthCri/counter,2),
    "DealtRateLow_%": round(DeaRateLow/counter,2),
    "DealtRateMod_%": round(DeaRateMod/counter,2),
    "DealtRateSev_%": round(DeaRateSev/counter,2),
    "DealtRateCri_%": round(DeaRateCri/counter,2),
    "DealtRateAll_%": round(DeaRateAll,2)
    }

with open("successmetrics.json",'w') as f:
        json.dump(SuccessMetrics,f)

#print(json.dumps(SuccessMetrics))



    


