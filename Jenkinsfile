pipeline {
    agent any
    
    tools {
        // Optional: Add if you have Git plugin configured
    }
    
    environment {
        // Set Python path (adjust if using virtual environment)
        PYTHON_PATH = 'python'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', 
                    url: 'https://github.com/YOUR_USERNAME/jenkins_ml.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat 'pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('Train Model') {
            steps {
                echo 'Training ML model...'
                bat 'python train.py'
            }
            post {
                success {
                    echo 'Model training completed successfully'
                }
                failure {
                    echo 'Model training failed'
                    error('Training stage failed')
                }
            }
        }
        
        stage('Test Model') {
            steps {
                echo 'Testing ML model...'
                bat 'python test.py'
            }
            post {
                success {
                    echo 'Model testing passed'
                }
                failure {
                    echo 'Model testing failed'
                    error('Testing stage failed')
                }
            }
        }
        
        stage('Deploy Model') {
            steps {
                echo 'Deploying ML model...'
                // Kill any existing Flask app on port 5000
                bat 'for /f "tokens=5" %a in (\'netstat -aon ^| find ":5000" ^| find "LISTENING"\') do taskkill /f /pid %a || exit 0'
                // Start Flask app in background
                bat 'start /B python app.py'
                echo 'Model deployment initiated'
            }
            post {
                success {
                    echo 'Model deployed successfully'
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed'
            // Archive artifacts
            archiveArtifacts artifacts: 'model.pkl', fingerprint: true
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}