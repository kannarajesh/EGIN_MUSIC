pipeline {
 environment {
BUILD_NUMBER = env.BUILD_NUMBER ?: '1'    
dockerimagename = "kannarajesh064/eginmusic:00${BUILD_NUMBER}"
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
            dockerImage.push("00${BUILD_NUMBER}")
          }
        }
      }
    }
    stage('Deploying egin_music container to Kubernetes') {
      steps {
	script {
          sh "kubectl --kubeconfig=/var/lib/jenkins/admin.conf get pods"
          sh "sed s/GIVEMEBUILD__NUMBER/00${BUILD_NUMBER}/g -i eginmusic-deployment.yaml"
          sh "kubectl --kubeconfig=/var/lib/jenkins/admin.conf apply -f eginmusic-deployment.yaml"
          sh "kubectl --kubeconfig=/var/lib/jenkins/admin.conf apply -f egin-svc.yaml"
          sh "kubectl --kubeconfig=/var/lib/jenkins/admin.conf get pods"
        }
      }
    }

  }
}
