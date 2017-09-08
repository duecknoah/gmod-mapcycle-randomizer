# gmod-mapcycle-randomizer
A python script that randomizes the mapcycle for any Garry's Mod server

## Installation
First check if python is already installed, make sure its python 3.5 or later
```
python -V
```
If that doesn't work or it gives an earlier version, try:
```
python3 -V
```
If that doesn't work, then install python using:
```
sudo apt-get install python3
```

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
