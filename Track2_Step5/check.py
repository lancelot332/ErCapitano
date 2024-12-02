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
        print(f"Errore nell' esportazoine del deployment: {e.stderr}")
        return None

def check_attributes(deployment_yaml):
    """
    Check if readinessProbe, livenessProbe, and resources are defined with limits and requests.
    """
    if not deployment_yaml:
        print("Nessun deployment disponibile.")
        return

    containers = deployment_yaml.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])
    for container in containers:
        print(f"Controllo container: {container.get('name', 'Unnamed')}")

        if "readinessProbe" in container:
            print("- readinessProbe: Definiti")
        else:
            print("- readinessProbe: Non definiti")

        if "livenessProbe" in container:
            print("- livenessProbe: Definiti")
        else:
            print("- livenessProbe: Non definiti")

        resources = container.get("resources", {})
        limits = resources.get("limits")
        requests = resources.get("requests")

        if limits:
            print("- Resources limits: Definiti")
        else:
            print("- Resources limits: Non definiti")

        if requests:
            print("- Resources requests: Definiti")
        else:
            print("- Resources requests: Non definiti")

def main():

    deployment_name = input("\nInserisci il nome del deployment: ")
    namespace = input("\nInserisci nome del namespace: ")

    print(f"Esportazione del deployment '{deployment_name}' nel namespace '{namespace}'...")
    deployment_yaml = export_deployment(deployment_name, namespace)

    print("\nControllo attributi del deployment...")
    check_attributes(deployment_yaml)

if __name__ == "__main__":
    main()
