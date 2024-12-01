# Jenkins Pipeline con Helm e Kubernetes

Questo progetto configura una pipeline Jenkins per installare Helm e `kubectl`, e consente l'uso di Helm per distribuire applicazioni su un cluster Kubernetes creato con Minikube.

## Creazione del cluster di Kubernetes su MAC.

Per la creazione del cluster su MAC abbiamo bisogno dei seguenti strumenti: minikube e hyperkit che si possono installare con i seguenti comandi:  
     `brew install minikube`
  
     `brew install hyperkit`

## Setup per far interaggire jenkins con il cluster.

1. **Avvio del cluster con Hyperkit**:  
   ```bash
   minikube start --listen-address=0.0.0.0 --ports=8443:8443 --driver=hyperkit
 ora abbiamo bisogno anche di avere installato helm e kubectl sul container jenkins che esegue la pipeline e che il contaioner jenkins possa raggiungiere il cluster di Kubernetes per fare cio bisogna installare kubectl com il comando curl poi bisogna fare il comando chmod -x cosi che possa essere eseguito e con il comando mv ./kubectl /usr/bin/local/kubectl cosi che ogni volta che si riavvia il container possiamo eseguire il comando senza problemi in seguito bisogna copiare il config di Kubernetes del mac all interno del container per fare cio creiamo la cartella .kube nella home del container e ci inseriamo il config con l ip del cluster che otteniamo facendop minikube ip dal nostro mac inseguito bisogna togliere il percorso del certificato e inserire la seguente stringa 'ciao' poi bisogna copiare i certificati riguardo il client all interno del container e inserire all interno del config il path corretto all interno del container, 
