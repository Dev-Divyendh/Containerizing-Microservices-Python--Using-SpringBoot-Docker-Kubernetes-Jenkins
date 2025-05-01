pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'devdivyendh10/extra-student-survey'
        DOCKER_CREDENTIALS_ID = 'dockerhub-creds'  // Replace with your Jenkins Docker Hub credentials ID
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Dev-Divyendh/Containerizing-Microservices-Python--Using-SpringBoot-Docker-Kubernetes-Jenkins.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: "$DOCKER_CREDENTIALS_ID", passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $DOCKER_IMAGE
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes (k3s)') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}
