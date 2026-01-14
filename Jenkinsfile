pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = credentials('dockerhub-credentials')
    }

    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('docker-login') {
            steps {
                sh '''
                echo $DOCKER_CREDENTIALS_PSW | docker login -u $DOCKER_CREDENTIALS_USR --password-stdin
                '''
            }
        }

        stage('docker-build') {
            steps {
                sh '''
                docker build -t challagiri/flask-app:latest .
                '''
            }
        }

        stage('docker-push') {
            steps {
                sh '''
                docker push challagiri/flask-app:latest
                '''
            }
        }
    }
}
