pipeline {
  agent { dockerfile true }
  stages {
    stage('Test') {
      steps {       

        // Write cloud.properties file
        script {
            withCredentials([string(credentialsId: 'CT_CLOUD_ACCESS_KEY_ID', variable: 'CT_ACCESS_KEY')]) {
                def cloudProperties = """
                    [cloud]
                    url=${env.CT_URL}
                    accessKey=${env.CT_ACCESS_KEY}
                """
                writeFile file: 'cloud.properties', text: cloudProperties
            }
        }

        // Run the tests
        sh '''
          python --version
          python -m unittest
        '''
      }
    }
  }
}