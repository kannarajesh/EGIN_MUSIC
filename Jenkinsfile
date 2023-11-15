pipeline {
 environment {
    dockerimagename = "kannarajesh064/eginmusic:002"
    dockerImage = ""
   }
 agent any
 stages {

    stage('Checkout Source') {
      steps {
        git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/kannarajesh/EGIN_MUSIC.git'
      }
    }

    stage('Build image') {
      steps{
        script {
          dockerImage = docker.build dockerimagename
        }
      }
    }

    stage('Pushing Image') {
      environment {
               registryCredential = 'dockerhub-credentials'
           }
      steps{
        script {
          docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
            dockerImage.push("latest")
          }
        }
      }
    }
    stage('Deploying egin_music container to Kubernetes') {
      steps {
        script {
          kubernetes Deploy(configs: "eginmusic-deployment.yaml", "egin-svc.yaml")
        }
      }
    }

  }
}
