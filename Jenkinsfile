pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials' // Nome ID delle credenziali su Jenkins
        DOCKERHUB_USER = 'kira002'  // Sostituisci con il tuo username DockerHub
        REPO_NAME = 'marco-flask-app'       // Nome della tua repository su DockerHub
        IMAGE_TAG = 'latest'                    // Tag predefinito dell'immagine Docker
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm // Clona la repository Git
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKERHUB_USER}/${REPO_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKERHUB_CREDENTIALS) {
                        docker.image("${DOCKERHUB_USER}/${REPO_NAME}:${IMAGE_TAG}").push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline completata con successo!"
        }
        failure {
            echo "Errore durante l'esecuzione della pipeline."
        }
    }
}
