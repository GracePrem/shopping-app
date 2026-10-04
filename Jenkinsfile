pipeline {
    agent any

    stages {
        stage('Checkout Test') {
            steps {
                echo 'GitHub code successfully loaded by Jenkins'
            }
        }

        stage('Verify Files') {
            steps {
                sh 'ls -la'
            }
        }
        stage('Build - Install Dependencies') {
    steps {
        sh '''
            python3 -m venv venv
            venv/bin/pip install -r requirements.txt
        '''
    }
}
        stage('Unit Test') {
    steps {
        sh '''
            . venv/bin/activate
            pytest -v test_app.py
        '''
    }
}
    }
}
