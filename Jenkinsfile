pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = credentials('dockerhub-credentials')
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Lint') {
            steps {
                sh '''
                python3 -m venv venv
                . ./venv/bin/activate
                pip install flake8
                flake8 app.py
                '''
            }
        }

        stage('Format') {
            steps {
                sh '''
                python3 -m venv venv
                . ./venv/bin/activate
                pip install black
                black --check app.py
                '''
            }
        }

        stage('Build') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Docker Login') {
            steps {
                sh '''
                echo $DOCKER_CREDENTIALS_PSW | docker login -u $DOCKER_CREDENTIALS_USR --password-stdin
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                docker build -t challagiri/flask-app:latest .
                '''
            }
        }

        stage('Docker Push') {
            steps {
                sh '''
                docker push challagiri/flask-app:latest
                '''
            }
        }
    }
}
