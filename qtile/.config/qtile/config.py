# Import libraries
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
import json
import os


@hook.subscribe.client_new
def center_floating_window(window):
    if window.name in ["Bluetooth"]:
        window.floating = True
        window.set_size_floating(1200, 800)
        window.center()
        window.move_to_top()


def get_volume():
    try:
        vol = os.popen("pamixer --get-volume-human").read()

        if '%' not in vol:
            return " {:>3.0f}%".format(0)

        else:
            vol = int(vol.split('%')[0])
            return " {:>3.0f}%".format(vol)

    except BaseException:
        return "   ?%"


battery_icons = [['', '', '', '', ''], '']
network_icons = [['󰤟', '󰤢', '󰤥', '󰤨'], ['󰤡', '󰤤', '󰤧', '󰤪'], '󰤮', '󰤫', '']


def get_battery():
    try:
        bat = os.popen("upower -e | grep battery").read().strip("\n")

        bat_s = os.popen(
                "upower -i " + bat + " | " +
                "grep state | cut -d ':' -f2 | xargs").read().strip("\n")
        bat_p = os.popen(
                "upower -i " + bat + " | " +
                "grep percentage | grep -o '[0-9]*'").read().strip("\n")

        if bat_s == "discharging":
            i = int(round(int(bat_p)/25))
            return "{} {:>3.0f}%".format(battery_icons[0][i], int(bat_p))

        elif bat_s == "charging":
            return "{} {:>3.0f}%".format(battery_icons[1], int(bat_p))

        elif bat_s == "empty":
            return "{}   0%".format(battery_icons[0][0])

        elif bat_s == "fully-charged":
            return "{} {:>3.0f}%".format(battery_icons[1], int(bat_p))

        elif bat_s == "pending-charge" or bat_s == "pending-discharge":
            if bat_p[0] == '0':
                bat_p = '0'
            return "{} {:>3.0f}%".format(battery_icons[0][0], int(bat_p))

        else:
            return "{}   ?%".format(battery_icons[0][0])

    except BaseException:
        return "{}   ?%".format(battery_icons[0][0])


def get_network():
    try:
        out = os.popen(
                "nmcli -t -f NAME,DEVICE,STATE con show --active"
                ).read().split('\n')
        out = [x.split(':') for x in out if x != '']

        if "enp" in out[0][1]:
            return network_icons[4]

        elif "wlan0" in out[0][1]:
            quality = int(os.popen(
                "nmcli -t -f IN-USE,SIGNAL device wifi | " +
                "grep '*' | grep -o '[0-9]\\+'").read().split('\n')[0])

            if int(os.popen("nmcli con show --active | grep wireguard | wc -l")
                   .read()) >= 1:
                i = 1
            else:
                i = 0

            if quality >= 60:
                return network_icons[i][3]

            elif quality >= 40:
                return network_icons[i][2]

            elif quality >= 20:
                return network_icons[i][1]

            else:
                return network_icons[i][0]

        else:
            return network_icons[2]

    except BaseException:
        return network_icons[3]


def read_settings():
    try:
        with open("{}/.config/qtile/settings.json".format(
            os.getenv("HOME")), "r") as f:
            settings = json.load(f)

    except FileNotFoundError:
        with open("{}/.config/qtile/settings_default.json".format(
            os.getenv("HOME")), "r") as f:
            settings = json.load(f)

    f.close()
    return settings


# Initialise assigned keys and applications
mod = "mod4"
terminal = "kitty"
web_browser = "brave"
web_browser_2 = "qutebrowser"
file_manager = "nemo"
bluetooth_manager = "blueberry"
volume_mixer = "pavucontrol-qt"
system_monitor = "htop"
music_player = "spotify-launcher"
pdf_editor = "okular"
text_editor = "nvim"
network_manager = "nmtui"

# Initialise other device-specific variables
settings = read_settings()
qtile_bar_size = settings["qtile_bar_size"]
qtile_font_size = settings["qtile_font_size"]
rofi_dpi = str(settings["rofi_dpi"])

keys = [
    # [mod] + [key]
    # Move window focus
    Key([mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"
        ),
    Key([mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"
        ),
    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"
        ),
    Key([mod], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"
        ),
    # Toggle between layouts
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
        ),
    # Kill focused window
    Key([mod], "q",
        lazy.window.kill(),
        desc="Kill focused window"
        ),
    # Move screen focus
    Key([mod], "comma",
        lazy.prev_screen(),
        desc="Move focus to previous screen"
        ),
    Key([mod], "period",
        lazy.next_screen(),
        desc="Move focus to next screen"
        ),
    # Lock screen
    Key([mod], "escape",
        lazy.spawn("dm-tool lock"),
        desc="Switch to Lightdm greeter"
        ),
    # Launch applications
    Key([mod], "return",
        lazy.spawn(terminal),
        desc="Launch terminal"
        ),
    Key([mod], "b",
        lazy.spawn(bluetooth_manager),
        desc="Open the bluetooth manager"
        ),
    Key([mod], "d",
        lazy.spawn("rofi -show run -dpi " + rofi_dpi),
        desc="Run Rofi"
        ),
    Key([mod], "f",
        lazy.spawn(file_manager),
        desc="Open the file manager"
        ),
    Key([mod], "i",
        lazy.spawn(
            terminal + " --title=" + system_monitor + " -e " +
            system_monitor),
        desc="Open the system monitor"
        ),
    Key([mod], "m",
        lazy.spawn(music_player),
        desc="Open the music player"
        ),
    Key([mod], "n",
        lazy.spawn(
            terminal + " -e " +
            network_manager),
        desc="Open the network manager"
        ),
    Key([mod], "o",
        lazy.spawn(pdf_editor),
        desc="Open the PDF editor"
        ),
    Key([mod], "t",
        lazy.spawn(terminal),
        desc="Launch terminal"
        ),
    Key([mod], "v",
        lazy.spawn(volume_mixer),
        desc="Open the volume mixer"
        ),
    Key([mod], "w",
        lazy.spawn(web_browser),
        desc="Open the web browser"
        ),
    # [mod] + [ctl] + [key]
    # Change window size
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"
        ),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        desc="Grow window down"
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        desc="Grow window up"
        ),
    Key([mod, "control"], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"
        ),
    # Reload config
    Key([mod, "control"], "r",
        lazy.reload_config(),
        desc="Reload the config"
        ),
    # Shutdown
    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
        ),
    # Toggle fullscreen
    Key([mod, "control"], "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen"
        ),
    # [mod] + [sft] + [key]
    # Move window
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
        ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"
        ),
    # Toggle floating window and split sides
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc="Toggle floating"
        ),
    Key([mod, "shift"], "s",
        lazy.spawn("flameshot gui"),
        desc="Run flameshot"
        ),
    Key([mod, "shift"], "space",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"
        ),
    # Lauch alternative applications
    Key([mod, "shift"], "return",
        lazy.spawn(terminal),
        desc="Launch alternative terminal"
        ),
    Key([mod, "shift"], "w",
        lazy.spawn(web_browser_2),
        desc="Launch alternative web browser"
        ),
    # [mod] + [key] + [key] + [key]
    # Reboot or shutdown
    KeyChord([mod], "x", [
        KeyChord([], "u", [
            Key([], "r", lazy.spawn("systemctl reboot --no-wall")),
            Key([], "u", lazy.spawn("systemctl poweroff --no-wall"))
        ])
    ],
             mode=True,
             desc="Reboot or shutdown"
             )
]

groups = [Group(i) for i in "123456789"]

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
            # mod1 + shift + letter of group = switch to & move focused window
            # to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
                ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {"border_width": 3,
                "margin": 6,
                "border_focus": "#51afef",
                "border_normal": "#282c34"
                }

layouts = [
    layout.Columns(**layout_theme, border_on_single=True),
    layout.Max(**layout_theme),
    # layout.MonadTall(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.RatioTile(**layout_theme),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

colors = ["#000000", "#181a1f", "#ffffff", "#51afef"]

widget_defaults = dict(
    font="FiraCode Nerd Font, Sarasa Mono TC",
    fontsize=qtile_font_size,
    background=colors[1],
)


def set_widgets_screen():
    return [
            widget.Spacer(
                background=colors[1],
                length=3
                ),
            widget.GroupBox(
                active=colors[3],
                disable_drag=True,
                highlight_method="border",
                padding=3
                ),
            widget.Sep(
                padding=10
                ),
            widget.WindowName(
                foreground=colors[3],
                padding=10
                ),
            widget.Spacer(
                background=colors[1],
                length=10
                ),
            widget.GenPollText(
                background=colors[0],
                func=get_volume,
                padding=16,
                update_interval=0.1
                ),
            widget.Spacer(
                background=colors[1],
                length=10
                ),
            widget.CPU(
                background=colors[0],
                fmt=" {}",
                format="{load_percent:>3.0f}%",
                padding=16
                ),
            widget.Spacer(
                background=colors[1],
                length=10
                ),
            widget.Memory(
                background=colors[0],
                fmt=" {}",
                format="{MemPercent:>3.0f}%",
                padding=16
                ),
            widget.Spacer(
                background=colors[1],
                length=10
                ),
            widget.GenPollText(
                background=colors[0],
                func=get_network,
                update_interval=1
                ),
            widget.Spacer(
                background=colors[0],
                length=6
                ),
            widget.Spacer(
                background=colors[1],
                length=10
                ),
            widget.GenPollText(
                background=colors[0],
                func=get_battery,
                padding=16,
                update_interval=1
                ),
            widget.Spacer(
                background=colors[1],
                length=10
                ),
            widget.Spacer(
                background=colors[0],
                length=0
                ),
            widget.TextBox(
                background=colors[0],
                fmt="󰃰",
                padding=16
                ),
            widget.Clock(
                background=colors[0],
                format="%d-%m-%Y %H:%M:%S",
                padding=2
                ),
            widget.Spacer(
                background=colors[0],
                length=12
                ),
            widget.Spacer(
                background=colors[1],
                length=10
                ),
            widget.CurrentLayoutIcon(
                background=colors[0],
                padding=10,
                scale=0.5
                ),
            widget.Spacer(
                background=colors[1],
                length=6
                ),
            ]


def init_screens():
    return [
            Screen(
                wallpaper="~/.config/qtile/wallpaper.jpg",
                wallpaper_mode="fill",
                top=bar.Bar(widgets=set_widgets_screen(),
                            size=qtile_bar_size)),
            Screen(
                wallpaper="~/.config/qtile/wallpaper.jpg",
                wallpaper_mode="fill",
                top=bar.Bar(widgets=set_widgets_screen(),
                            size=qtile_bar_size)),
            Screen(
                wallpaper="~/.config/qtile/wallpaper.jpg",
                wallpaper_mode="fill",
                top=bar.Bar(widgets=set_widgets_screen(),
                            size=qtile_bar_size)),
            ]


screens = init_screens()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X
        # client.
        *layout.Floating.default_float_rules,
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

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
