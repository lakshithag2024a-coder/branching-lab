Step 1: Initialize the Project Repository
mkdir patient_records
cd patient_records
git init
git checkout -b main

Step 2: Create the Source Code Files
touch app.py requirements.txt Dockerfile Jenkinsfile
mkdir k8s
touch k8s/deploy.yaml

Step 3: Stage and Push to GitHub
git add .
git commit -m "Initial pipeline structural setup"
git remote add origin https://github.com
git push -u origin main


Step 4: Configure Jenkins Security Framework

1. Navigate to http://localhost:8080/manage/credentials/store/system/domain/_/newCredentials
2. Select Username with password from the Kind dropdown list.
3. Input your Docker Hub username into the Username field.
4. Input your Docker Hub personal access token into the Password field.
5. Set the ID field to exactly dockerhub-creds and click Save.


Step 5: Initialize the Automated Pipeline Job

1. Access http://localhost:8080/view/all/newJob
2. Input patient-pipeline-job into the item name framework configuration text box.
3. Select the Pipeline option item and click OK.
4. Navigate down to the Pipeline Definition section category box.
5. Switch the Definition selector to Pipeline script from SCM.
6. Set SCM to Git and paste https://github.com into the Repository URL box.
7. Change the Branch Specifier field to click matching lines to */main and click Save

Step 6: Test Local Platform Configurations
kubectl cluster-info
kubectl get nodes

Step 7: Clear Stale System Architectures
docker system prune -f
docker rmi $(docker images -f "dangling=true" -q)



