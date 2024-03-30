pipeline {
    environment {
        registryCredential = 'git'
        IMAGE_NAME = 'ayeshaahmed123/mlops_assignment1'
        TAG = 'latest' 
    }
    agent any
    stages {
        stage('Cloning Git Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/ayeshaAhmed123/MLA1.git'
            }
        }
        stage('Building our image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }
        stage('Deploy our image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        docker.image("${IMAGE_NAME}:${TAG}").push()
                    }
                }
            }
        }
    }
    post {
    success {
        emailext(
            to: 'ahmedayesha2402@gmail.com',
            subject: 'Build Successful',
            body: 'The docker image successfully pushed to Dockerhub!',
        )
    }
}

}
