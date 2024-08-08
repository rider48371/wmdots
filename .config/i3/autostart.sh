
# Autostart applications

# bar start
~/.config/i3/polybar-i3 &

# wallpaper
feh --bg-fill --randomize ~/.config/backgrounds/* &

# compositor and notifications
picom  &
numlockx on &
dunst &
blueman-applet &
lxsession &
~/Documents/onedrive &

# sxhkd
sxhkd -c ~/.config/i3/sxhkdrc &
