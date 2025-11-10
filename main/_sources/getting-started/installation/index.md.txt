# Installation
The recommended InputActions implementation is [standalone](standalone), as it works in any environment. There are also two compositor plugins that have
slightly more features, but need to be rebuilt on every compositor update.

## Differences between implementations
This table only lists features that are not available in all implementations.

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

* - ``window{_under}_name``
  - ✅
  - ❌
  - ✅
  - ✅
  - [wlr foreign toplevel management](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1) required
  - ❌

* - other window variables
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