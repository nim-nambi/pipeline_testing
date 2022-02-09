#use when Ansible is installed on aws since it will respond to api calls

import pprint
import boto3
import json

def getgrpofhosts(ec2):
    all_grps = {}

    for each_in in ec2.instances.filter(Filters[{'Name' : 'instance-state-name, 'Values' : ['running']}]):
        for tag in each_in.tags:
            hosts = all_grps.get(tag["Key"])
            hosts.append(each_in.public_ip_address)
            all_grps[tag["Key"]] = hosts
        else:
            hosts = [each_in.public_ip_address]
            all_grps[tag["Key"]] = hosts

        if tag["Value"] in all_grps:
            hosts = all_grps.get(tag["Value"])
            hosts.append(each_in.public_ip_address)
            all_grps[tag["Value"]] = hosts
        else:
            hosts = [each_in.public_ip_address]
            all_grps[tag["Value"]] = hosts

    return all_grps

def main():
    ec2 = boto3.resource("ec2")
    all_grps = getgrpofhosts(ec2)
    inventory = {}

    for key, value in all_grps.items():
        hostobj = {'hosts' : value}
        inventory[key] = hostobj

    print(json.json.dump(inventory))

if __name__ =="__main__":
        main()