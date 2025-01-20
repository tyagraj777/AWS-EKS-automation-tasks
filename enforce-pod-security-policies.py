# This script ensures that a Pod Security Policy (PSP) exists and denies privileged containers.

from kubernetes import client, config

def enforce_psp():
    config.load_kube_config()
    v1 = client.PolicyV1beta1Api()
    psp = client.V1beta1PodSecurityPolicy(
        metadata=client.V1ObjectMeta(name="deny-privileged"),
        spec=client.V1beta1PodSecurityPolicySpec(
            privileged=False,
            allowed_capabilities=[],
            se_linux=client.V1beta1SELinuxStrategyOptions(rule="RunAsAny"),
            run_as_user=client.V1beta1RunAsUserStrategyOptions(rule="MustRunAsNonRoot"),
            fs_group=client.V1beta1FSGroupStrategyOptions(rule="MustRunAs"),
            supplemental_groups=client.V1beta1SupplementalGroupsStrategyOptions(rule="MustRunAs"),
        ),
    )
    v1.create_pod_security_policy(body=psp)
    print("Pod Security Policy created: deny-privileged")

if __name__ == "__main__":
    enforce_psp()
