pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'service-health-monitor-dashboard'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/AdityaAggarwal11/Service-Health-Dashboard-Monitoring.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
            }
        }

        stage('Deploy Container') {
            steps {
                sh 'docker rm -f service_health_monitor_dashboard || true'
                sh "docker run -d -p 5000:5000 --name service_health_monitor_dashboard ${DOCKER_IMAGE}:${DOCKER_TAG}"
            }
        }
    }
}

