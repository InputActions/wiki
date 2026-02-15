# Mouse
:::{list-table}
* - **Inherits**
  - [](/devices/index)
:::

Trackpoints are also considered mice.

## Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - motion_timeout
  - *time*
  - The time during which a motion trigger must be performed. If not, a press trigger will be started. If no press triggers are activated, all pressed mouse
    buttons will actually be pressed, after having been blocked previously.
  - ``200``

* - press_timeout
  - *time*
  - The time during which press triggers are not started in case the user presses more than one mouse button.

    Swipe and wheel trigger aren't affected by this option.
  - ``50``

* - unblock_buttons_on_timeout
  - *bool*
  - Whether blocked mouse buttons should be pressed immediately on timeout. If false, they will be pressed and instantly released on button release.
  - ``true``
:::

## Description
In the Hyprland implementation, the delta is based on the pointer's position and may be either unaccelerated or accelerated, depending on the device configuration.

## Buttons
- ``left``
- ``middle``
- ``right``
- ``back`` (equivalent to ``BTN_SIDE`` evdev scancode)
- ``forward`` (equivalent to ``BTN_EXTRA`` evdev scancode)
- ``task`` (equivalent to ``BTN_FORWARD`` evdev scancode)
- ``side`` (equivalent to ``BTN_BACK`` evdev scancode)
- ``extra`` (equivalent to ``BTN_TASK`` evdev scancode)
- ``extra1`` (alias for ``back``)
- ``extra2`` (alias for ``forward``)
- ``extra3`` (alias for ``task``)
- ``extra4`` (alias for ``side``)
- ``extra5`` (alias for ``extra``)
- ``extra6``
- ``extra7``
- ``extra8``
- ``extra9``
- ``extra10``
- ``extra11``
- ``extra12``
- ``extra13``

```{toctree}
:maxdepth: 1
:hidden:

Triggers <triggers/index>
```