pipeline {
  agent { dockerfile true }
  stages {
    stage('Test') {
      steps {
        sh '''
          python --version
        '''
        
        // Write cloud.properties file
        script {
          def cloudProperties = """
            [cloud]
            url=${env.CT_URL}
            accessKey=${CT_ACCESS_KEY}
          """
          writeFile file: 'cloud.properties', text: cloudProperties
        }
      }
    }
  }
}