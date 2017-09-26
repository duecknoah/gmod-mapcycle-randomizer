# gmod-mapcycle-randomizer
A python script that randomizes the mapcycle for any Garry's Mod server
## Installation Simple (GUI)
- Click the 'Clone or download' button and download ZIP
- Open the downloaded ZIP file and drag gmod_mapcycle_rand.py into your Garry's Mod server folder
- Go to the link below and download the latest version of python 3: https://www.python.org/downloads/
- Make this the first line in your start_server.sh file for your server:
```
python3 gmod_mapcycle_rand.py
```

## Installation command-line
First clone the repo
```
git clone https://github.com/duecknoah/gmod-mapcycle-randomizer
```
Next move gmod_mapcycle_rand.py into the root directory of your server.
Then install python 3 using the following:
#### Linux
```
sudo apt-get install python3
```
#### Windows or Mac
Go to the link below and download the latest version of python 3
https://www.python.org/downloads/

## How to Use
Run this command in the home directory of your server, or put it as the first line in your startup script:
```
python3 gmod_mapcycle_rand.py
```

### Example
An example start_server.sh file using the randomizer could look like this:
```
python3 gmod_mapcycle_rand.py
./srcds_run -game garrysmod +maxplayers 12 +map gm_flatgrass +host_workshop_collection 844193892 -authkey 123456789101112131415 -mapcyclefile -port 27015
```
