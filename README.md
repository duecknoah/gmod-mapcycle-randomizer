# gmod-mapcycle-randomizer
A Python script that randomizes the mapcycle for any Garry's Mod server.
## Setup Simple (GUI)
1. Click the 'Clone or download' button and download ZIP
2. Open the downloaded ZIP file and move gmod_mapcycle_rand.py into your Garry's Mod server folder
3. Go to the link below and download the latest version of python 3: https://www.python.org/downloads/
4. Make this the first line in your start_server.sh file for your server:
```
python3 gmod_mapcycle_rand.py
```

## Setup command-line
Clone the repo
```
git clone https://github.com/duecknoah/gmod-mapcycle-randomizer
```
Move __gmod_mapcycle_rand.py__ into your __server directory__.
Then install python 3 using the following:
```
sudo apt-get install python3
```
Or download the latest version of python 3 here:
https://www.python.org/downloads/

## Usage
Run this command in the __root directory of your server__, or put it as the first line in your __startup script__:
```
python3 gmod_mapcycle_rand.py path/to/mapcycle.txt
```

### Example
Example server startup script
```
python3 gmod_mapcycle_rand.py ./garrysmod/cfg/mapcycle.txt
./srcds_run -game garrysmod +maxplayers 12 +map gm_flatgrass +host_workshop_collection 844193892 -authkey 123456789101112131415 -mapcyclefile -port 27015
```
