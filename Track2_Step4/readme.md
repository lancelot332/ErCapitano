# Jenkins Pipeline con Helm e Kubernetes

Questo progetto configura una pipeline Jenkins per installare Helm e `kubectl`, e consente l'uso di Helm per distribuire applicazioni su un cluster Kubernetes creato con Minikube.

## Creazione del cluster di Kubernetes su MAC.

Per creare il cluster su Mac, sono necessari i seguenti strumenti: **Minikube** e **HyperKit**, che possono essere installati con i comandi:
`brew install minikube`  
`brew install hyperkit`
Una volta installati, eseguire il comando:  
`minikube start --listen-address=0.0.0.0 --ports=8443:8443 --driver=hyperkit`  
Questo comando avvia un cluster Kubernetes con Minikube utilizzando tutte le interfacce di rete disponibili e configurando HyperKit come driver.

## Configurazione di Jenkins per interagire con il cluster e installazione di Helm

È necessario configurare il container Jenkins per interagire con il cluster Kubernetes ed installare Helm. così che possiamo eseguire la nostra pipeline senza avere errori.  
Per questo, dobbiamo installare kubectl e configurare l'accesso al cluster all'interno del container.  
Per installare kubectl, eseguire i seguenti comandi:
```bash
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl
mv ./kubectl /usr/local/bin/kubectl
```  
Questi comandi scaricano kubectl, ne configurano i permessi di esecuzione e lo spostano in una directory di sistema per renderlo disponibile globalmente.  
Ora dobbiamo copiare il file config creato dal cluster del MAC dentro il container, per fare cio creiamo la cartella .kube nella home del container e ci inseriamo il config, ora dobbiamo modificarlo inserendo l ip del cluster che lo otteniamo con il comando `minikube ip` 
inseguito bisogna togliere il percorso del certificato e inserire al di sotto la seguente stringa `insecure-skip-tls-verify: true` cosi che ignoriamo il certificato, ora dobbiamo invece copiare i certificati rigurado il client precisamente i seguenti `client.crt` e `client.key` all interno del container
poi dobbiamo inserire all interno del config il percorso giusto di dove li abbiamo copiati.  
Ora possiamo eseguire il comando `kubetcl get pods` per verificare se tutto funziona.  
Ora è necessario creare una directory .kube nella home del container e copiare al suo interno il file di configurazione (config) generato dal cluster Minikube sul Mac.
Una volta copiato il config bisogna modificarlo sostituendo l'indirizzo IP del cluster con quello ottenuto eseguendo il comando: `minikube ip`, aggiungere la seguente configurazione: `insecure-skip-tls-verify: true` questo passaggio consente di ignorare i problemi relativi ai certificati TLS.  
In seguito bisogna copiare i certificati del client (client.crt e client.key) all'interno del container. Modificare i percorsi dei certificati nel file config per puntare ai nuovi percorsi.  
Adesso possiamo verificare la configurazione eseguendo nel container il comando: `kubectl get pods`  

 
