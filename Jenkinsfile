pipeline {
    agent any
    environment {
        IMAGE = "mohammadmusaab/jenkins-docker-project" 
    }
    stages {
        stage('Mohammad Musaab - Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE}:build-${BUILD_NUMBER} -t ${IMAGE}:latest .'
            }
        }
        stage('Mohammad Musaab - Login to Dockerhub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }
        stage('Mohammad Musaab - Push image to Dockerhub') {
            steps {
                sh 'docker push ${IMAGE}:build-${BUILD_NUMBER}'
                sh 'docker push ${IMAGE}:latest'
            }
        }
    }
}