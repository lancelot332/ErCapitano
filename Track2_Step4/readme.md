# Jenkins Pipeline con Helm e Kubernetes

Questo progetto configura una pipeline Jenkins per installare Helm e `kubectl`, e consente l'uso di Helm per distribuire applicazioni su un cluster Kubernetes creato con Minikube.

## Creazione del cluster di Kubernetes su MAC.

Per la creazione del cluster su MAC abbiamo bisogno dei seguenti strumenti: minikube e hyperkit che si possono installare con i seguenti comandi:  
`brew install minikube`
`brew install hyperkit`
una volta fatto ciò bisogna eseguire il seguente comando:
`minikube start --listen-address=0.0.0.0 --ports=8443:8443 --driver=hyperkit`  
questo comando crea un cluster di Kubernetes con minikube utilizzando tutte le interfaccie di rete presenti e utilizzando il driver hyperkit.

## Setup per far interaggire jenkins con il cluster ed installazione di helm.

ora abbiamo bisogno di avere installato helm e far interaggire il container jenkins al cluster. così che possiamo eseguire la nostra pipeline senza avere errori.  
comando curl poi bisogna fare il comando chmod -x cosi che possa essere eseguito e con il comando mv ./kubectl /usr/bin/local/kubectl cosi che ogni volta che si riavvia il container possiamo eseguire il comando senza problemi in seguito bisogna copiare il config di Kubernetes del mac all interno del container per fare cio creiamo la cartella .kube nella home del container e ci inseriamo il config con l ip del cluster che otteniamo facendop minikube ip dal nostro mac inseguito bisogna togliere il percorso del certificato e inserire la seguente stringa 'ciao' poi bisogna copiare i certificati riguardo il client all interno del container e inserire all interno del config il path corretto all interno del container, 
