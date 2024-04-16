# Facial Attendance

This is a Full Stack Facial Recognition Attendance Application, that automates Attendance Marking. 
The application uses Flask for the Backend and Angular Js for Frontend

## Overview

*Facial Attendance is a free and open-source service based on OPENCV that can be easily integrated into any system without prior machine learning skills. This System provides REST API for face recognition and is easily deployed with docker*

## Table of Contents

 - Features 
 - Technologies Used
 - Requirements
 - Installation
 - Usage
 - Screenshots

## 	Features

The system can accurately identify people with a very few datasets with the help of CNN.
Facial Attendance can have many advantages such as:

 - It is Open Source and self-hosted
 - It can be deployed on cloud or On-premises
 - Can be set-up without Machine Learning Knowledge
 - Starts quickly with one Docker Command

### Technologies Used
|  SDK|Version  |
|--|--|
|  nodejs|20  |
|python| 3.11|
|face_recognition| latest|
|opencv| latest|
|cmake| latest|
|angular| 17|
|yarn| latest|


### Requirements

1. Docker and Docker compose ( for linux )
2. Python 3.11 
3. NodeJs 18+ 
4. Cmake

## Installation
### For Linux 
1. Install python and node js 

	```bash
    sudo apt install python3 python3-pip nodejs
    ```

2.	 Install docker 

    sudo apt install docker docker-compose
3. Clone this repository

      ```bash
      git clone https://github.com/architmadankar/facial-attendance-JTP.git
      ```
4. Change the directory

    ```bash
    cd facial-attendance-JTP
    ```

5.  Open the terminal in this folder and run this command: 
 ```bash
 docker-compose up -d
 ```


6.  Open the service in your browser:  [http://localhost:4200/](http://localhost:4200/)


### For Windows | Non-Containerized

#### Prerequisite

+ [Cmake](https://github.com/Kitware/CMake/releases/download/v3.29.2/cmake-3.29.2-windows-x86_64.msi) 
+ [Visual Studio C++ Development Environments](https://visualstudio.microsoft.com/downloads/)

#### Installation

1. Install Python and Nodejs from their official websites
> [Python](https://www.python.org/downloads/) 

> [NodeJs](https://nodejs.org/en/download)


2. Clone this repository
>you can directly download from the github repository or use git cli 

      git clone https://github.com/architmadankar/facial-attendance-JTP.git
3. Change the directory

    ```bash
    cd facial-attendance-JTP
    ```

5.  Open the terminal in this folder and run this command  
```bash
docker-compose up -d
```

6.  Open the service in your browser:  [http://localhost:4200/login](http://localhost:4200/)



- Note: Since Webcam support is not avilable with docker deskop (windows), there's no way to run this application inside a docker container in windows


## Usage
- Create admin account http://localhost:4200/register
- Login http://localhost:4200/login
- In the Dashboard navigate to Users to Add New Users 
 >make sure to be in well lit environment
- add the name of user and click its pictures for dataset
- navigate to Video Feeds and click on Add Camera Name and Camera ID
> Camera ID is usually 0 you can try 1 if you have multiple cameras
- On the controls Tab select Start and it will start marking attendances
- Navigate to Check Attendance Tab to check the Marked Attendance

### Step-by-step Procedure


## Screenshots

![Add User](https://github.com/architmadankar/facial-attendance-JTP/blob/90e7a2ce5c84b12eb849293942e85112ebb2e740/screenshots/addUser.png) 

![Login](https://github.com/architmadankar/facial-attendance-JTP/blob/90e7a2ce5c84b12eb849293942e85112ebb2e740/screenshots/login.png)

![Register](https://github.com/architmadankar/facial-attendance-JTP/blob/90e7a2ce5c84b12eb849293942e85112ebb2e740/screenshots/register.png)


## References 
* facial recognition pre-trained classifier from official opencv github repo

> https://github.com/opencv/opencv/tree/master/data/haarcascades

* Image File Helper from isLinXu

> using https://github.com/isLinXu/CVProcessLib/blob/master/utils/ImgFileHelper.py

> from https://github.com/isLinXu/CVProcessLib

> in /modules/lib/image_helper.py for file uploads in Flask

* for camera-initialization, frame-capturing, and client sync using 

> https://kizniche.github.io/Mycodo/


