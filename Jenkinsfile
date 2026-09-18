pipeline {
  agent any
  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
  }
  stages {
    stage('Mohammad Musaab - Build Docker Image') {
      steps { sh 'docker build -t mohammadmusaab/jenkins-docker-project:latest .' }
    }
    stage('Mohammad Musaab - Login to Dockerhub') {
      steps { sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin' }
    }
    stage('Mohammad Musaab - Push image to Dockerhub') {
      steps { sh 'docker push mohammadmusaab/jenkins-docker-project:latest' }
    }
  }
}