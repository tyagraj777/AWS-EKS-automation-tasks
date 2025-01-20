# This script checks for risky role bindings (e.g., bindings granting cluster-admin privileges).


from kubernetes import client, config

def audit_role_bindings():
    config.load_kube_config()
    rbac_api = client.RbacAuthorizationV1Api()
    
    role_bindings = rbac_api.list_role_binding_for_all_namespaces()
    cluster_role_bindings = rbac_api.list_cluster_role_binding()

    for rb in role_bindings.items + cluster_role_bindings.items:
        for subject in rb.subjects or []:
            if rb.role_ref.kind == "ClusterRole" and rb.role_ref.name == "cluster-admin":
                print(f"High-privilege role binding detected: {rb.metadata.name}, subject: {subject.name}")

if __name__ == "__main__":
    audit_role_bindings()


