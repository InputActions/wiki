# Mouse
## MouseEventHandler
Inherits <project:/config.md#eventhandler>.

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

```{toctree}
:maxdepth: 1
:hidden:

triggers/index
```