# Configurazione Ingress per Accedere a una Pagina "Hello World"

Con l' helm install viene installato anche l' ingress controller.  
Successivamente, bisogna attivarlo con il seguente comando: `minikube addons enable ingress`.  
Bisogna anche andare a modificare il file: `/etc/hosts` associando al dominio formazionesou.local l indirizzo IP di minikube, che si ottiene con il segunete comnado `minikube ip`
una volta fatto questi passaggi possiamo andare sul browser e inserendo formazionesou.local ci viene restituita la pagina con "Hello World"
