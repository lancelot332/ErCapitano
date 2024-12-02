# Jenkins Pipeline con Helm e Kubernetes

Questo progetto configura una pipeline Jenkins per installare Helm e `kubectl`, e consente l'uso di Helm per distribuire applicazioni su un cluster Kubernetes creato con Minikube.

## Creazione del cluster di Kubernetes su MAC.

Per creare il cluster su Mac, sono necessari i seguenti strumenti: **Minikube** e **HyperKit**, che possono essere installati con i comandi:  
`brew install minikube`  
`brew install hyperkit`  
Una volta installati, eseguire il comando:  
`minikube start --listen-address=0.0.0.0 --ports=8443:8443 --driver=hyperkit`  
Questo comando avvia un cluster Kubernetes con Minikube utilizzando tutte le interfacce di rete disponibili e configurando HyperKit come driver.

## Configurazione di Jenkins per interagire con il cluster ed installazione di Helm

Ho fatto alcune modifiche al playbook cosi che il container jenkins possa interagire con il cluster e possa utilizzare helm.
```yaml
    - name: Download Helm binary
      community.docker.docker_container_exec:
        container: jenkins_master
        user: root
        command: >
          curl -fsSL -o /var/jenkins_home/helm.tar.gz https://get.helm.sh/helm-v3.16.3-linux-amd64.tar.gz

    - name: Extract Helm binary
      community.docker.docker_container_exec:
        container: jenkins_master
        user: root
        command: >
          tar -xzf /var/jenkins_home/helm.tar.gz -C /var/jenkins_home --strip-components=1 linux-amd64/helm
```

 
