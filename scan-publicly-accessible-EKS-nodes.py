# This script identifies EKS nodes with public IP addresses, which could pose a security risk.

import boto3

def check_public_eks_nodes():
    ec2 = boto3.client('ec2')
    eks = boto3.client('eks')

    # List clusters
    clusters = eks.list_clusters()['clusters']
    for cluster in clusters:
        print(f"Checking cluster: {cluster}")
        response = eks.describe_cluster(name=cluster)
        vpc_config = response['cluster']['resourcesVpcConfig']
        
        if vpc_config.get('endpointPublicAccess', False):
            print(f"Cluster {cluster} allows public access. Consider restricting access.")
        else:
            print(f"Cluster {cluster} has public access disabled.")

if __name__ == "__main__":
    check_public_eks_nodes()
