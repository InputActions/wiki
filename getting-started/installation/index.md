# Installation
The recommended InputActions implementation is [standalone](standalone), as it works in any environment. There are also two compositor plugins that have
slightly more features, but need to be rebuilt on every compositor update.

## Feature comparison
This table only lists features that are not available in all implementations.

If the standalone implementation turns out to work well, the compositor plugins will be rewritten to work with the daemon, which will reduce the number of
differences.

:::{list-table}
:header-rows: 1

* -
  - GNOME
  - Hyprland
  - Plasma (Wayland)
  - Plasma (Wayland, X11)
  - Other (Wayland)
  - Other (X11)

* - InputActions implementation
  - [Standalone](/getting-started/installation/standalone.md) + extension
  - [Hyprland](/getting-started/installation/hyprland.md) (compositor plugin)
  - [KWin](/getting-started/installation/standalone.md) (compositor plugin)
  - [Standalone](/getting-started/installation/standalone.md) + script
  - [Standalone](/getting-started/installation/standalone.md)
  - [Standalone](/getting-started/installation/standalone.md)

* - &nbsp;
  -
  -
  -
  -
  -
  -

* - **General**
  -
  -
  -
  -
  -
  -

* - Multi-session support
  - ✅<sup>[1]</sup>
  - ✅
  - ✅
  - ✅<sup>[1]</sup>
  - ✅<sup>[1]</sup>
  - ✅<sup>[1]</sup>

* - Compatibility with other input tools
  - ?<sup>[2]</sup>
  - ✅<sup>[3]</sup>
  - ✅<sup>[3]</sup>
  - ?<sup>[2]</sup>
  - ?<sup>[2]</sup>
  - ?<sup>[2]</sup>

* - &nbsp;
  -
  -
  -
  -
  -
  -

* - **[InputAction](/actions/input.md)**
  -
  -
  -
  -
  -
  -

* - Keyboard text action
  - ❌
  - ✅
  - ✅
  - ❌
  - ❌
  - ❌

* - &nbsp;
  -
  -
  -
  -
  -
  -

* - **Touchpad**
  -
  -
  -
  -
  -
  -

* - Accelerated gestures
  - ✅
  - ❌
  - ❌
  - ✅
  - ✅
  - ✅

* - &nbsp;
  -
  -
  -
  -
  -
  -

* - **[Variables](/variables.md)**
  -
  -
  -
  -
  -
  -

* - ``cursor_shape``
  - ❌
  - ✅
  - ✅
  - ❌
  - ❌
  - ❌

* - ``plasma_overview_active``
  - ❌
  - ❌
  - ✅
  - ❌
  - ❌
  - ❌

* - pointer position variables
  - ✅
  - ✅
  - ✅
  - ✅
  - ❌
  - ❌

* - ``screen_name``
  - ❌
  - ✅
  - ✅
  - ❌
  - ❌
  - ❌

* - &nbsp;
  -
  -
  -
  -
  -
  -

* - **Windows**
  -
  -
  -
  -
  -
  -

* - Active window info
  - ✅
  - ✅
  - ✅
  - ✅
  - [wlr foreign toplevel management](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) required
  - ❌

* - Window under pointer info
  - ✅
  - ✅
  - ✅
  - ✅
  - ❌
  - ❌

* - Window resource class (``window{_under}_class`` variable)
  - ✅
  - ✅
  - ✅
  - ✅
  - [wlr foreign toplevel management](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) required
  - ❌

* - Window resource name (``window{_under}_name`` variable)
  - ✅
  - ❌
  - ✅
  - ✅
  - ❌
  - ❌

* - Window fullscreen state (``window{_under}_fullscreen`` variable)
  - ✅
  - ❌
  - ✅
  - ✅
  - [wlr foreign toplevel management](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) required
  - ❌

* - Window maximized state (``window{_under}_maximized`` variable)
  - ✅
  - ✅
  - ✅
  - ✅
  - [wlr foreign toplevel management](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) required
  - ❌

* - Window title (``window{_under}_title`` variable)
  - ✅
  - ✅
  - ✅
  - ✅
  - [wlr foreign toplevel management](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) required
  - ❌
:::

1. Each virtual terminal has its own InputActions session.

2. InputActions will conflict with any program that grabs input devices and creates virtual ones. Virtual input devices created by InputActions need to be
   blacklisted in such tools if possible. InputActions can be configured to ignore and not grab specific devices in order to let other tools process their
   events first.

3. InputActions blocks input events in the compositor. Event generation also occurs in the compositor and tools operating at evdev level do not receive such
   events.

```{toctree}
:maxdepth: 1
:hidden:

Hyprland <hyprland>
KWin <kwin>
Standalone <standalone>
```