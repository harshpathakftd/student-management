pipeline {
    agent any

    environment {
        APP_NAME = "student-management"
        AWS_REGION = "ap-south-1"
        AWS_ACCOUNT_ID = "123456789012"
        ECR_REPO = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${APP_NAME}"
        IMAGE_TAG = "${BUILD_NUMBER}"
        K8S_NAMESPACE = "student-management"
        EKS_CLUSTER_NAME = "student-management-eks"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${APP_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Push To ECR') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-jenkins-creds']]) {
                    sh """
                      aws ecr describe-repositories --repository-names ${APP_NAME} --region ${AWS_REGION} || \
                      aws ecr create-repository --repository-name ${APP_NAME} --region ${AWS_REGION}

                      aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
                      docker tag ${APP_NAME}:${IMAGE_TAG} ${ECR_REPO}:${IMAGE_TAG}
                      docker tag ${APP_NAME}:${IMAGE_TAG} ${ECR_REPO}:latest
                      docker push ${ECR_REPO}:${IMAGE_TAG}
                      docker push ${ECR_REPO}:latest
                    """
                }
            }
        }

        stage('Deploy To EKS') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-jenkins-creds']]) {
                    sh """
                      aws eks update-kubeconfig --region ${AWS_REGION} --name ${EKS_CLUSTER_NAME}

                      kubectl apply -f k8s/namespace.yaml
                      kubectl apply -f k8s/secret.yaml
                      kubectl apply -f k8s/deployment.yaml
                      kubectl apply -f k8s/service.yaml
                      kubectl apply -f k8s/ingress.yaml

                      kubectl -n ${K8S_NAMESPACE} set image deployment/${APP_NAME} web=${ECR_REPO}:${IMAGE_TAG}
                      kubectl -n ${K8S_NAMESPACE} rollout status deployment/${APP_NAME}
                    """
                }
            }
        }
    }

    post {
        always {
            sh "docker image prune -f || true"
        }
    }
}
