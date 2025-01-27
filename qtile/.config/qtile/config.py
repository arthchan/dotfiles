# Import libraries
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
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


bat_discharge_icon = ['󱃍', '󰁺', '󰁻', '󰁼', '󰁽', '󰁾', '󰁿', '󰂀', '󰂁', '󰂂', '󰁹']
bat_charge_icon = ['󰢟', '󰢜', '󰂆', '󰂇', '󰂈', '󰢝', '󰂉', '󰢞', '󰂊', '󰂋', '󰂅']
bat_empty_icon = '󱟩'
bat_full_icon = '󰂄'
bat_not_charging_icon = '󰂃'
bat_unknown_icon = '󰂑'


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
            i = round(int(bat_p), -1)//10
            return "{} {:>3.0f}%".format(bat_discharge_icon[i], int(bat_p))

        elif bat_s == "charging":
            i = round(int(bat_p), -1)//10
            return "{} {:>3.0f}%".format(bat_charge_icon[i], int(bat_p))

        elif bat_s == "empty":
            return "{}   0%".format(bat_empty_icon)

        elif bat_s == "fully-charged":
            return "{} {:>3.0f}%".format(bat_full_icon, int(bat_p))

        elif bat_s == "pending-charge" or bat_s == "pending-discharge":
            if bat_p[0] == '0':
                bat_p = '0'
            return "{} {:>3.0f}%".format(bat_not_charging_icon, int(bat_p))

        else:
            return "{}   ?%".format(bat_unknown_icon)

    except BaseException:
        return "{}   ?%".format(bat_unknown_icon)


def get_network():
    try:
        out = os.popen(
                "nmcli -t -f NAME,DEVICE,STATE con show --active"
                ).read().split('\n')
        out = [x.split(':') for x in out if x != '']

        if "enp" in out[0][1]:
            return ''

        elif "wlan0" in out[0][1]:
            quality = int(os.popen(
                "nmcli -t -f IN-USE,SIGNAL device wifi | " +
                "grep '*' | grep -o '[0-9]\\+'").read().split('\n')[0])

            if quality >= 60:
                return '󰤨'

            elif quality >= 40:
                return '󰤥'

            elif quality >= 20:
                return '󰤢'

            else:
                return '󰤟'

        else:
            return '󰤮'

    except BaseException:
        return '󱐅'


def check_vpn():
    if int(os.popen("nmcli con show --active | grep wireguard | wc -l")
           .read()) >= 1:
        return ''

    else:
        return ''


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
    Key([mod], "a",
        lazy.spawn(file_manager),
        desc="Open the file manager"
        ),
    Key([mod], "b",
        lazy.spawn(bluetooth_manager),
        desc="Open the bluetooth manager"
        ),
    Key([mod], "d",
        lazy.spawn("rofi -show run"),
        desc="Run Rofi"
        ),
    Key([mod], "f",
        lazy.spawn("flameshot gui"),
        desc="Run flameshot"
        ),
    Key([mod], "i",
        lazy.spawn(
            terminal + " -e " +
            network_manager),
        desc="Open the network manager"
        ),
    Key([mod], "m",
        lazy.spawn(
            terminal + " --title=" + system_monitor + " -e " +
            system_monitor),
        desc="Open the system monitor"
        ),
    Key([mod], "n",
        lazy.spawn(
            terminal + " -e " +
            text_editor),
        desc="Open the text editor"
        ),
    Key([mod], "o",
        lazy.spawn(pdf_editor),
        desc="Open the PDF editor"
        ),
    Key([mod], "s",
        lazy.spawn(music_player),
        desc="Open the music player"
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
    font="FiraCode Nerd Font",
    fontsize=20,
    background=colors[1],
)


def set_widgets_screen():
    return [
            widget.Sep(
                foreground=colors[1],
                padding=3
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
            widget.Sep(
                linewidth=10,
                foreground=colors[1]
                ),
            widget.GenPollText(
                update_interval=0.1,
                func=get_volume,
                background=colors[0],
                padding=15
                ),
            widget.Sep(
                foreground=colors[1],
                padding=10
                ),
            widget.CPU(
                format="{load_percent:>3.0f}%",
                fmt=" {}",
                background=colors[0],
                padding=15
                ),
            widget.Sep(
                foreground=colors[1],
                padding=10
                ),
            widget.Memory(
                format="{MemPercent:>3.0f}%",
                fmt=" {}",
                background=colors[0],
                padding=15
                ),
            widget.Sep(
                foreground=colors[1],
                padding=10
                ),
            widget.GenPollText(
                update_interval=1,
                func=get_network,
                background=colors[0],
                ),
            widget.Sep(
                linewidth=6,
                foreground=colors[0],
                background=colors[0]
                ),
            widget.Sep(
                foreground=colors[1],
                padding=10
                ),
            widget.GenPollText(
                update_interval=5,
                func=check_vpn,
                background=colors[0],
                ),
            widget.Sep(
                linewidth=6,
                foreground=colors[0],
                background=colors[0]
                ),
            widget.Sep(
                foreground=colors[1],
                padding=10
                ),
            widget.GenPollText(
                update_interval=1,
                func=get_battery,
                background=colors[0],
                padding=15
                ),
            widget.Sep(
                foreground=colors[1],
                padding=10
                ),
            widget.Clock(
                format="%H:%M",
                background=colors[0],
                padding=15
                ),
            widget.Sep(
                foreground=colors[1],
                padding=10
                ),
            widget.Clock(
                format="%d/%m/%Y",
                background=colors[0],
                padding=15
                ),
            widget.Sep(
                foreground=colors[1],
                padding=10
                ),
            widget.CurrentLayoutIcon(
                background=colors[0],
                foreground=colors[2],
                scale=0.5,
                padding=10
                ),
            widget.Sep(
                foreground=colors[1],
                padding=6
                ),
            ]


def init_screens():
    return [
            Screen(
                wallpaper="~/.config/qtile/wallpaper.png",
                wallpaper_mode="fill",
                top=bar.Bar(widgets=set_widgets_screen(), size=36)),
            Screen(
                wallpaper="~/.config/qtile/wallpaper.png",
                wallpaper_mode="fill",
                top=bar.Bar(widgets=set_widgets_screen(), size=36)),
            Screen(
                wallpaper="~/.config/qtile/wallpaper.png",
                wallpaper_mode="fill",
                top=bar.Bar(widgets=set_widgets_screen(), size=36)),
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
