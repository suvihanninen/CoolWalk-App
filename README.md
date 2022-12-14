# CoolWalk

## Setting up code enviroment
After cloning the depository, run two command in the terminal:
git submodel init
git submodel update

### Conda yml
1. conda env create -f environment.yml
2. conda env list
3. conda activate geo_env

### Manual procedure
-Create new enviroment manually
1. conda create --name myenv
2. conda activate myenv
If it doesn't work here are our versions of the different packages:
osmnx 1.2.2       
networkx 2.8.7  
geopandas 0.11.1
flask  2.2.2
Python 3.10.6
conda 22.9.0

### Andorid studio
1. Install android studio
2. Change emulator by pressing where the blue box is
![android studio](https://github.itu.dk/storage/user/3592/files/dc20d384-10b1-4d46-9397-4eafaf5a4493)
4. 4. Press device manager
5. Create device
6. Choose pixel 2 
7. Choose R 30 x86 and then finish



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
