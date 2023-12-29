library identifier: 'jenkins-shared-library@main', retriever: modernSCM(
  [$class: 'GitSCMSource',
   remote: 'https://github.com/UST-PACE/pace_jenkins_shared_library.git',
   credentialsId: 'scm-cred-id'])

kanikoPythonTest{
  gitCredentialsId = 'scm-cred-id'
  gitBranch = "main"
  codeRating = 8.0
	imageName = "python-image"
	//registryRepo = "test-python"
  techName = "python"
  containerRegistry = "682452625784.dkr.ecr.us-east-2.amazonaws.com"
  containerRegistryCredId = "aws-cred-id-workshop"
  awsRegion = "us-east-2"
}
