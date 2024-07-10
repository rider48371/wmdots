# Copyright (c) 2024 JustAGuyLinux

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess

from libqtile import hook
import colors

@hook.subscribe.startup_once
def autostart():
   home = os.path.expanduser('~/.config/qtile/autostart.sh')
   subprocess.run([home])

mod = "mod4"
# terminal = "kitty"

colors, backgroundColor, foregroundColor, workspaceColor, chordColor = colors.monokai()

keys = [

# Add dedicated sxhkdrc to autostart.sh script

# CLOSE WINDOW, RELOAD AND QUIT QTILE
    Key([mod], "q", lazy.window.kill()),
# Qtile System Actions
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "q", lazy.shutdown()),
   #  Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

# CHANGE FOCUS USING VIM OR DIRECTIONAL KEYS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),


# MOVE WINDOWS UP OR DOWN,LEFT OR RIGHT USING VIM KEYS
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),

# MOVE WINDOWS UP OR DOWN,LEFT OR RIGHT USING DIRECTIONAL KEYS
    Key([mod, "shift"], "Left", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_down()),

# RESIZE UP, DOWN, LEFT, RIGHT USING DIRECTIONAL KEYS
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
     Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),

# QTILE LAYOUT KEYS
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
	Key([mod, "shift"], "z", lazy.layout.normalize(), desc="Reset all window sizes"),

    ]
# end of keys

#groups = [Group(i) for i in ["", "", "", "", "阮", "", "", "", ""]]
# groups = [Group(i) for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]
groups = [
	Group('1', label="1", layout="Columns"),
	Group('2', label="2", layout="Columns"),
	Group('3', label="3", layout="Columns"),	
	Group('4', label="4", layout="Columns"),
	Group('5', label="5", layout="MonadTall"),
	Group('6', label="6", layout="MonadTall"),
	Group('7', label="7", matches=[Match(wm_class='gimp')], layout="MonadTall"),
	Group('8', label="8", matches=[Match(wm_class='discord')], layout="MonadTall"),
	Group('9', label="9", matches=[Match(wm_class='obs')],layout="MonadTall"),
]


#groups = [Group(i) for i in ["www", "dev", "dir", "txt", "vid", "mus", "gfx", "dis", "obs"]]
# group_hotkeys = "123456789"

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# Define layouts and layout themes
layout_theme = {
        "margin":20,
        "border_width": 4,
        "border_focus": colors[3],
        "border_normal": colors[1]
    }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(**layout_theme,num_columns=3),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.Spiral(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]
widget_defaults = dict(
	font='Roboto Mono Nerd Font',
    background=colors[0],
    foreground=colors[2],
    fontsize=14,
    padding=6,
)
extension_defaults = widget_defaults.copy()
separator = widget.Sep(size_percent=50, foreground=colors[3], linewidth =1, padding =10)
spacer = widget.Sep(size_percent=50, foreground=colors[3], linewidth =0, padding =10)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    disable_drag=True,
                    use_mouse_wheel=False,
                    active = colors[4],
                    inactive = colors[5],
                    highlight_method='line',
                    this_current_screen_border=colors[10],
                    hide_unused = False,
                    rounded = False,
                    urgent_alert_method='line',
                    urgent_text=colors[9]
                ),
        widget.TaskList(
            icon_size = 0,
            foreground = colors[0],
            background = colors[2],
            borderwidth = 0,
            border = colors[6],
            margin_y = -5,
            padding = 8,
            highlight_method = "block",
            title_width_method = "uniform",
            urgent_alert_method = "border",
            urgent_border = colors[1],
            rounded = False,
            txt_floating = "🗗 ",
            txt_maximized = "🗖 ",
            txt_minimized = "🗕 ",
        ),

               widget.TextBox(text = "", foreground = colors[1]),
               widget.CPU(
					format="{load_percent:04}%",
					foreground=foregroundColor
			   ),
			   separator,
			   widget.TextBox(text = "󰻠", foreground = colors[1]),
               widget.Memory(
                format='{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                measure_mem='G',
                foreground=foregroundColor
               ),
               separator,
                widget.Clock(format=' %a, %b %-d',
					foreground=foregroundColor
				),
				widget.Clock(format='%-I:%M %p',
					foreground=foregroundColor
				),
				separator,
               widget.Volume(
					fmt="󰕾 {}",
					mute_command="amixer -D pulse set Master toggle",
					foreground=colors[4]
            ),
				separator,
				spacer,
				widget.CurrentLayoutIcon(
                    custom_icon_paths=["/home/drew/.config/qtile/icons/layouts"],
                    scale=0.5,
                    padding=0
                ),
                widget.Systray(
					padding = 6,
				),
				spacer,
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
border_width=4,
border_focus=colors[3],
border_normal=colors[1],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="qimgv"),  # q image viewer
        Match(wm_class="lxappearance"),  # lxappearance
        Match(wm_class="pavucontrol"),  # pavucontrol
        Match(wm_class="kitty"),  # kitty
        Match(wm_class="Galculator"),  # calculator
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
