#!/usr/bin/env bash

# background
feh --bg-fill --randomize ~/.config/backgrounds/* &

# compositor
picom &

# Notifications
dunst &

lxsession &
numlockx on &
~/.local/bin/onedrive &

