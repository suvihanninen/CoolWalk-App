# CoolWalk
*By Kris Otte, Fethi Sarihan and Suvi Hänninen*

## Table of contents
* [Setting up code enviroment](#setting)  
* [Conda yml](#yml)
* [Manual procedure](#manual)
* [Android Studio](#android)
* [To run the application](#app)

## Project description
This repository contains an implementation of a GIS application that was part of our Research Project during our MSc. Degree at IT University of Copenhagen. The purpose of the app is to find an optimal path which goes in shadow. It serves its purpose by being a mobile application developed in Android and it has a backend computing the optimal path which is written in Python by using NetworkX library. It is possible to run the application locally by cloning the repository to your local machine.In order to find the optimal path, the user needs to input a source and destination node to the phone interface which will query the optimal path and visualise it on the map.



<a name="setting"></a>
## Setting up code enviroment
Cloning the depository, run the two command in the terminal:
1. git submodel init
2. git submodel update

<a name="yml"></a>
### Conda yml
[Download ".yml"](enviroment.yml) 
1. conda env create -f environment.yml
2. conda env list
3. conda activate geo_env

<a name="manual"></a>
### Manual procedure
Create new enviroment manually
1. conda create --name myenv
2. conda activate myenv

<a name="android"></a>
Our current versions of the different packages:
- osmnx 1.2.2       
- networkx 2.8.7  
- geopandas 0.11.1
- flask  2.2.2
- Python 3.10.6
- conda 22.9.0

<a name="app"></a>
### Android studio
1. Install android studio
2. Change emulator by pressing where the blue box is
![android studio](https://github.itu.dk/storage/user/3592/files/dc20d384-10b1-4d46-9397-4eafaf5a4493)
4. Press device manager
5. Create device
6. Choose pixel 2 
7. Choose R 30 x86 and then finish


### To run the application 
- Open IDE and android studio
- Navigate to the backend.py folder in terminal. Then run the Flask server with the command `flask --app app run`.
- Press the run app button at the top in android studio. Red box in picture above 
- Enter two nodes in the emulator
- Press the send node button
- Press show line

