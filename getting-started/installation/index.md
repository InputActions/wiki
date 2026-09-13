# Installation
InputActions has multiple versions, referred to as *implementations* in the rest of the wiki.

The [Hyprland](/getting-started/installation/hyprland.md) and [KWin](/getting-started/installation/kwin.md) (for KDE Plasma) implementations run entirely in
the compositor as plugins, as such they are not restricted by Wayland protocols and can use the compositors' much more powerful APIs instead. Those need to be
recompiled every time the compositor is updated.

The [standalone](/getting-started/installation/standalone.md) implementation runs in its own process, as such it must filter input events at the evdev level
(which is less reliable than filtering libinput events in the compositor) and use the restrictive Wayland protocols to get information about the environment
(such as the active window). Many features are unsupported in this implementation. The list of unsupported features is available on the page of each implementation.

```{toctree}
:maxdepth: 1
:hidden:

Hyprland <hyprland>
KWin <kwin>
Standalone <standalone>
```
