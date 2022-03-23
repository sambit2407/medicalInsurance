
# Medical Insurance Premium Prediction App

I have built this App to predict Future expenses of Indivisual or any 3rd party can do bulk prediction  for number of people using several features of individual such as age, physical/family condition and location.

Youtube - Live Demo -[link](https://youtu.be/YzMiOWWwpCQ)


## FrontEnd

- HTML
- CSS

## BackEnd
- Python
- Flask
- MongoDB
- Machine Learning

## Deployment

- Docker , Docker-Compose
- AWS EC2

## Tools
- Pycharm IDE
- Jupyter Notebook
- Putty 
- winSCP 





## Screenshots
### URL

![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/Application/URL.png?raw=true)
- IP - AWS Public DNS
- Port - Port maping in Docker Compose file
### LogIn  

![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/Application/LoginPage.png?raw=true)

### SignUp  

![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/Application/signUp%20and%20LogIN.png?raw=true)

### Home Page 
-  Home Page - For IndivisualPrediction

![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/Application/IndivisualPrediction.png?raw=true)

- Home Page - For Prediction of IndivisualPrediction Part

![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/Application/IndivisualPrediction2.png?raw=true)

- Home Page - For Prediction of BulkPrediction Part

![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/Application/bulkPrediction.png?raw=true)

- Home Page - Files For BulkPrediction

![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/Application/demoBulkData.png?raw=true)

- Home Page - Attching file for BulkPrediction

![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/Application/attachingBulkFilke.png?raw=true)

- Home Page  - Downloaded BulkPrediction File

![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/Application/DownloadedBulkCSVPrediction.png?raw=true)

- Home Page   - Predicted BulkPrediction File

![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/Application/PredictedBulkData.png?raw=true)

### Application BackEnd Process
- Data cleaning - Outlier Treatment - Data Preprocessing - Model Selection -Model Prediction all tradition roadmap for building ML App has been done in Modularization method (**Classes** and **Objects**)
- EDA has been performed in Jupyter notebook.
- **RandomForest** is giving highest accuracy for this dataset.
### MongoDB Process
- I am storing User data i.e. Username and password(bcrypt fotmat) and User file name in database.
- User dataset is not stored in database or hard drive. But predicted bulk dataset is being stored in hard drive with specific Username folder.

#### User data on MongoDB
![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/mongoDB/UserData.png?raw=true)
#### User File Name
![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/mongoDB/userfile.png?raw=true)

#### Predicted Output data files stored in hard drive with specific Username
![App screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/mongoDB/outputfile.png?raw=true)

### Deployment

- Create AWS account .
- Set up any free tier EC2 instance . I have opted for Ubuntu system.
- While creating EC2 save **.pem** key for cloud connection from local system.

![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/puttyconnectivity/publicDNS.png?raw=true)

#### Cloud system connection from local

- Download [PuTTy](https://www.putty.org/) and [PuTTYygen](https://www.puttygen.com/)
- Download [winSCP](https://winscp.net/eng/downloads.php)

#### PuTTy connection
- Genrate **.ppk** in PuTTYygen from **.pem** key and save it in system.
- Connect PuTTy terminal with **EC2 Public DNS and .ppk** authentication.
##### Host Name                     
![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/puttyconnectivity/puttyHost.png?raw=true)

##### authentication
![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/puttyconnectivity/puttyPPK.png?raw=true)

#### Connected With AWS Cloud System 
![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/puttyconnectivity/AWS_Ubuntu.png?raw=true)

### All file uploadation from Local to AWS Ubuntu system

- We can do it using [winSCP](https://winscp.net/eng/downloads.php)

- Connection to EC2 from winSCP
- Putting Hostname and Username

![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/winSCP/winSCP_connection.png?raw=true)

- Attaching **.ppk** for authentication
![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/winSCP/winSCP_connection2.png?raw=true)

- Deploying Files to EC2 Ubuntu
![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/winSCP/Deploying_files_to_EC2.png?raw=true)

- All files sent from Local winSCP
![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/winSCP/Deploying_files_to_EC2_sent.png?raw=true)

-  Checking All Files in EC2 through puTTY
![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/winSCP/checking%20files%20in%20EC2.png?raw=true)

### Installing Docker and Docker-Compose in EC2
 

```bash
  sudo apt-get update
```
```bash
  sudo apt-get install docker.io
```
```bash
  sudo systemctl enable docker
```
```bash
  sudo apt install docker-compose
```
### Build and Run Docker-Compose on EC2
```bash
  sudo docker-compose build
```
```bash
  sudo docker-compose up
```
![App Screenshot](https://github.com/sambit2407/medicalInsurance/blob/master/screenshots/server%20up/server%20up.png?raw=true)
