#This script will add Success Metrics for the current year to include metrics up to 'last week'
from datetime import *
import requests
import json
import pandas

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

#Now we need to loop for each week
for counter in range(1,cur_week+2):
    print("\nSuccess Metrics for Week "+ str(counter) + ":" + "\n")
    #set the time period
    time_period = cur_year + '-W' + str(counter)
    r_body = '{"timePeriod": "WEEK","firstTimePeriod": "'+ time_period + '","lastTimePeriod": "' + time_period + '"}'
    #print r_body
    resp = requests.post(iq_url, auth=(iq_user, iq_password) ,data=r_body, headers={'Content-Type':'application/json', 'Accept':'application/json'})
    raw_data = resp.json()
    with open("raw_data.json",'w') as f:
        json.dump(raw_data,f)

    df = pandas.read_json(resp.text)
    df.to_csv("raw_data.csv")
    
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
        
        
        
       # print (iq_app['applicationName'] + ', For week ' + str(counter) + ' there are ' + str(iq_app['aggregations'][0]['openCountsAtTimePeriodEnd']['SECURITY']['CRITICAL']) + ' open security critical violations')
    
