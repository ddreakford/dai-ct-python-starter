pipeline {
  agent { dockerfile true }
  stages {
    stage('Test') {
      steps {       
        script {
            withCredentials([string(credentialsId: 'CT_CLOUD_ACCESS_KEY_ID', variable: 'CT_ACCESS_KEY')]) {
                // Run the tests
                sh '''
                  python --version
                  python -m unittest
                '''
            }
        }
      }
    }
  }
}