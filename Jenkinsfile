pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS = credentials('dockerhub-credentials')
    }
    stages {
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
                . ./venv/bin/activate
                pip install black
                black --check app.py
                '''
            }
        }
        stage('Build') {
            steps {
                sh 'echo $DOCKER_CREDENTIALS_PSW | docker login -u $DOCKER_CREDENTIALS_USR --password-stdin'
                sh 'docker build --network host -t Challagiri/flask-app:0.0.1 .'
                sh 'docker push <dockerhub-username>/<repo-name>:0.0.1'
            }
        }
    }
}
