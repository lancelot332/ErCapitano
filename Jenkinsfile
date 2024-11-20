pipeline {
    agent any
    def defaults = [
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials'
    ]

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.withRegistry('', DOCKERHUB_CREDENTIALS) {
                        def image = docker.build("kira002/flask-app-example:latest")
                        image.push()
                    }
                    sh "docker rmi --force kira002/flask-app-example:latest"
                }
            }
        }
    }
}
