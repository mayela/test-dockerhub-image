pipeline {
  environment {
    imageName = "mayela/sre-tht"
    registryCredentialSet = 'docker-hub-mayela'
  }
  agent any
  stages {
    stage('Building image') {
      steps{
        script {
          dir("application"){
            docker.build imageName + ":$BUILD_NUMBER"
          }
        }
      }
    }
  }
}
