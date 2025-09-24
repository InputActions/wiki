# Installation
Follow the instructions for your environment:
- [Hyprland](hyprland)
- [KWin (KDE Plasma)](kwin)

:::{important}
All implementations are compositor plugins for better integration with the environment than Wayland protocols allow for. As such, they must be rebuilt manually
when the compositor is updated.
:::

## Additional setup (optional)
To enable [extra touchpad features](/devices/touchpad/index.md#libevdev-backend), create a file at ``/etc/udev/rules.d/71-touchpad.rules`` with the following content:
```
ENV{ID_INPUT_TOUCHPAD}=="1", TAG+="uaccess"
```

This will give all programs read and write access to all touchpads.


```{toctree}
:maxdepth: 1
:hidden:

Hyprland <hyprland>
KWin <kwin>
```