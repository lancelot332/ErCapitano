pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm // Clona la repository Git
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t kira002/flask-app-example:latest ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    script {
                        // Login su Docker
                        sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                        sh "docker push kira002/flask-app-example:latest"
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
