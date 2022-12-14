# CoolWalk

## Setting up code enviroment
After cloning the depository, run two command in the terminal:
1. git submodel init
2. git submodel update

### Conda yml
1. conda env create -f environment.yml
2. conda env list
3. conda activate geo_env

### Manual procedure
-Create new enviroment manually
1. conda create --name myenv
2. conda activate myenv
Ours current versions of the different packages:
- osmnx 1.2.2       
- networkx 2.8.7  
- geopandas 0.11.1
- flask  2.2.2
- Python 3.10.6
- conda 22.9.0

### Andorid studio
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
- Press the run app button at the top in android studio 
<img width="78" alt="Skærmbillede 2022-12-14 kl  21 31 37" src="https://github.itu.dk/storage/user/3592/files/032350e1-82c9-4157-a919-a572bca385cd">

- Enter two nodes in the emulator
- Press the send node button
- Press show line

