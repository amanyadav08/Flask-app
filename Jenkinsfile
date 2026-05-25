pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-app"
        TAG = "latest"
    }

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/your-repo/flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$TAG .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop flask-container || true
                docker rm flask-container || true

                docker run -d \
                --name flask-container \
                -p 5000:5000 \
                flask-app:latest
                '''
            }
        }
    }
}