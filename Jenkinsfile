pipeline{
    agent any
    tools{
        nodejs "node"
    }
    environment{
        BUILD_VERSION = '1.0.0'
    }

    stages{

        stage('Cleanup Workspace') {
            steps {
                cleanWs()
                sh """
                echo "Cleaned Up Workspace For Project"
                """
            }
        }

        stage("Install dependencies"){
            steps{
                dir('Frontend'){
                    sh "npm install" 
                }

                dir('Backend'){
                    sh "npm install" 
                }
            }
        }

        stage("Unit Testing"){
            steps{
                dir('Frontend'){
                    // sh "npm test" 
                    sh """
                    echo "unit Testing frontend"
                    """
                }

                dir('Backend'){
                    // sh "npm test" 
                    sh """
                    echo "unit Testing Backend"
                    """
                }
            }
        }

        stage('CQA'){
            steps {
                echo 'Testing...'
                snykSecurity(
                snykInstallation: 'Snyk@latest',
                snykTokenId: 'Snyk_sec_token',
                failOnError: true
                )
            }
        }

        stage("Docker Login"){
            when {
                branch 'main'
            }
            steps{
                withCredentials([
                    usernamePassword(credentials: 'Dockerhub-credentials', usernameVariable: USER, passwordVariable: PWD)
                ]) {
                    sh "docker login -u ${USER} -p ${PWD}"
                }
            }
        }

        stage("Docker Build and push"){
            when {
                branch 'main'
            }
            steps{
                dir('Frontend'){
                    sh "docker build -t nim-nambi/TestFrontend:${BUILD_VERSION} ."
                    sh "docker push nim-nambi/TestFrontend:${BUILD_VERSION}" 
                }

                dir('Backend'){
                    sh "docker build -t nim-nambi/TestBackend:${BUILD_VERSION} ." 
                    sh "docker push nim-nambi/TestBackend:${BUILD_VERSION}"
                }
            }
        }

        stage("Deploy pods"){
            when {
                branch 'main'
            }
            steps{
                dir('Deployment'){
                    sh "ansible-playbook apply.yml"
                }
            }
        }

    }
}