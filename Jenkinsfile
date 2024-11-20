pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials'
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
                    docker.withRegistry('', DOCKERHUB_CREDENTIALS) {
                        def image = docker.build("kira002/flask-app-example:latest")
                        image.push()
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
