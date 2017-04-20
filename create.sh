#! /bin/bash -x
#############################################
# bash script wrapper for taiga issue creation script
#############################################
declare -a ARGUMENTS
for ((i=0;i<${COG_ARGC};i++)); do
    var="COG_ARGV_${i}"
    ARGUMENTS[$i]=${!var}
done

output=$(python ./create-issue.py --user $TAIGA_USER --project 'antweiss-fluxomate' --passwd $TAIGA_PASSWORD --message "${ARGUMENTS[*]}")

echo $output
