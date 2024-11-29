import subprocess
import yaml

def export_deployment(deployment_name, namespace):
    """
    Export the deployment YAML using kubectl.
    """
    try:
        result = subprocess.run(
            ["kubectl", "get", "deployment", deployment_name, "-n", namespace, "-o", "yaml"],
            capture_output=True,
            text=True,
            check=True
        )
        return yaml.safe_load(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error while exporting deployment: {e.stderr}")
        return None

def check_attributes(deployment_yaml):
    """
    Check if readinessProbe, livenessProbe, and resources are defined with limits and requests.
    """
    if not deployment_yaml:
        print("No deployment data available.")
        return

    containers = deployment_yaml.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])
    for container in containers:
        print(f"Checking container: {container.get('name', 'Unnamed')}")

        if "readinessProbe" in container:
            print("- readinessProbe: Defined")
        else:
            print("- readinessProbe: Missing")

        if "livenessProbe" in container:
            print("- livenessProbe: Defined")
        else:
            print("- livenessProbe: Missing")

        resources = container.get("resources", {})
        limits = resources.get("limits")
        requests = resources.get("requests")

        if limits:
            print("- Resources limits: Defined")
        else:
            print("- Resources limits: Missing")

        if requests:
            print("- Resources requests: Defined")
        else:
            print("- Resources requests: Missing")

def main():

    deployment_name = input("\nInserisci il nome del deployment: ")
    namespace = input("\nInserisci nome del namespace: ")

    print(f"Exporting deployment '{deployment_name}' in namespace '{namespace}'...")
    deployment_yaml = export_deployment(deployment_name, namespace)

    print("\nChecking deployment attributes...")
    check_attributes(deployment_yaml)

if __name__ == "__main__":
    main()
