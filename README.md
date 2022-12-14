# CoolWalk

## Setting up code enviroment
After cloning the depository, run two command in the terminal:
git submodel init
git submodel update

### Conda yml
conda env create -f environment.yml
conda env list
conda activate geo_env

### Manual procedure
-Create new enviroment
conda create --name myenv
conda activate myenv
If it doesn't work here are our versions of the different packages:
osmnx 1.2.2       
networkx 2.8.7  
geopandas 0.11.1
flask  2.2.2
Python 3.10.6
conda 22.9.0

### Andorid studio
Install android studio
Change emulator by pressing the top button
Press device manager
Create device
Choose pixel 2 
<img width="1440" alt="Screenshot 2022-12-08 at 21 02 53" src="https://github.itu.dk/storage/user/4415/files/c7431338-76f9-4e6a-97ca-5203a92bb840">

Choose R 30 x86 and then finish

### Start application 
- Open IDE and android studio
- Go to the backend folder in terminal. Then run the Flask server with the command python app.py.
- Press the run app button at the top in android studio 
- Enter two nodes in the emulator
- Press the send node button
- Press show line

To run the app: 
- In terminal go to backend folder ad run the Flask server with command `flask --app app run`
- Run the mobile app from android studio
