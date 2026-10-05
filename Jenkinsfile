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
      stage('SonarQube Scan') {
    steps {
        script {
            def scannerHome = tool 'SonarQube-scanner'

            withSonarQubeEnv('Sonarqube-cloud') {
                sh """
                    ${scannerHome}/bin/sonar-scanner \
                    -Dsonar.organization=graceprem \
                    -Dsonar.projectKey=GracePrem_shopping-app \
                    -Dsonar.sources=. \
                    -Dsonar.python.version=3
                """
            }
        }
    }

}
        stage('Docker Build') {
    steps {
        sh '''
        docker build -t shopping-app:${BUILD_NUMBER} .
        '''
    }
}

stage('Push to Artifact Registry') {
    steps {
        sh '''
        docker tag shopping-app:${BUILD_NUMBER} \
        asia-south1-docker.pkg.dev/project-7e0ae7e5-dbc5-4c45-bc3/ecommerce-repo/shopping-app:${BUILD_NUMBER}

        docker push \
        asia-south1-docker.pkg.dev/project-7e0ae7e5-dbc5-4c45-bc3/ecommerce-repo/shopping-app:${BUILD_NUMBER}
        '''
    }
}
        stage('Deploy to GKE') {
    steps {
        sh '''
            kubectl set image deployment/shopping-app \
            shopping-app=asia-south1-docker.pkg.dev/project-7e0ae7e5-dbc5-4c45-bc3/ecommerce-repo/shopping-app:${BUILD_NUMBER}

            kubectl rollout status deployment/shopping-app
        '''
    }
}
}
}
