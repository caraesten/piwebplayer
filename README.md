# A media player for Raspberry Pi
## How to use it
 - Set up your pi for the type of video output you want
 - Clone this git repository to your Raspberry Pi
 - Use pip to install `watchdog` and `flask` (`pip install watchdog flask`) on your Pi
 - Go to your home directory on your Pi, and `mkdir media`
 - Add the following lines to your `.bashrc`:
 ```
    python3 filescanner.py -d $HOME/media &
    python3 webserver.py -d $HOME/media &
 ```
 - Restart the pi

 ## Coming soon
 ...an easier way to run this!