library identifier: 'jenkins-shared-library@main', retriever: modernSCM(
  [$class: 'GitSCMSource',
   remote: 'https://gitlab.ustpace.com/conveyor_workshop/pace_jenkins_shared_library.git',
   credentialsId: 'scm-cred-id'])

kanikoPythonTest{
  gitCredentialsId = 'scm-cred-id'
  gitBranch = "main"
	imageName = "python-image"
	registryRepo = "docker-sf"
  techName = "python"
}