#!/usr/bin/env bash 

lxsession &
picom &
~/.local/bin/onedrive &

### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
# xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set a random wallpaper on login
# find /usr/share/backgrounds/dtos-backgrounds/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
# nitrogen --restore &
# 4. Uncomment to set random wallpaper with feh
feh --bg-fill --randomize ~/.config/backgrounds/* &
