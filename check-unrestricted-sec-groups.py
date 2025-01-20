# This script checks for security groups in your EKS cluster with overly permissive ingress rules.

import boto3

def check_security_groups():
    ec2 = boto3.client('ec2')
    response = ec2.describe_security_groups()
    for sg in response['SecurityGroups']:
        for rule in sg.get('IpPermissions', []):
            for ip_range in rule.get('IpRanges', []):
                if ip_range.get('CidrIp') == '0.0.0.0/0':
                    print(f"Security Group {sg['GroupId']} allows unrestricted access.")
                    
if __name__ == "__main__":
    check_security_groups()
