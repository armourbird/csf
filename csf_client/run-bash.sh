#!/bin/sh

while true
do
    #Output log file details
    mkdir -p logs
    dt=`date '+%d-%m-%Y_%H-%M-%S'`
    logger='logs/output_'$dt'.log'

    #Load all tests. It will not execute the tests as they are inside the functions
    for test in tests/*.sh; do
      . ./"$test"
    done

    #Load all tests functions from this script
    . ./functions_lib.sh

    #Load all dependency functions for outputing data
    . ./output_lib.sh

    #Dependency functions from helper_lib.sh
    . ./helper_lib.sh

    #Executing all tests under cis() within functions_lib.sh
    printf '{"tests":[' | tee -a "$logger.json" 2>/dev/null 1>&2
    cis
    printf "]}" | tee -a "$logger.json" 2>/dev/null 1>&2

    #Sending data to CDN. Need to set CSF_CDN and CSF_API_KEY env variables
    #export ENV_VAR=value
    cdn=$CSF_CDN
    api_key=$CSF_API_KEY
    cdn_url=$cdn
    base64_logfile=`base64  $logger.json`
    base64_logfile=$(echo $base64_logfile|tr -d '\n' | tr -d ' ')
    curl --request POST $cdn_url --data "data=$base64_logfile"
    echo
    echo "JSON log posted on CDN"
    time_unit=m
    sleep_time=$CSF_INTERVAL
    echo "Sleeping for: $sleep_time$time_unit"
    sleep $sleep_time$time_unit
done
