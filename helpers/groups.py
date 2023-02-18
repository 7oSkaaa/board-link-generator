import re
import sys

from helpers.colors import bcolors


def getGroupData():
    groups = []
    with open("data/groups.txt") as groups_file:
        for line in groups_file:
            groups.append(line.strip())
    return groups


def getGroups():
    print("\nParsing groups..")

    try:
        groups = getGroupData()
    except:
        sys.exit("File groups.txt is missing inside data folder!")
    
    groups_split = {}
    for group in groups:
        group_id = re.search("group\/\w+", group)[0].split('/')[1]
        contest_id = re.search("contest\/\d+", group)[0].split('/')[1]
        
        if group_id not in groups_split:
            groups_split
            groups_split[group_id] = []
        groups_split[group_id].append(contest_id)
        
    result = []
    for group in groups_split:
        result.append({'id': group, 'contests': groups_split[group]})
    
    print(f"{bcolors.OKGREEN}ACCEPTED!{bcolors.ENDC}")
    return result
