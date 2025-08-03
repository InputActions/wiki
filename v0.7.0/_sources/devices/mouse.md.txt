# Mouse
:::{list-table}
* - **Supported gestures**
  - [](/gestures/press), [](/gestures/stroke), [](/gestures/swipe), [](/gestures/wheel)
:::

Mouse gestures on Plasma require a version of 6.3 or higher.

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
  - The time during which a motion gesture must be performed. If not, a press gesture will be started. If no press gestures are activated, all pressed mouse buttons will actually be pressed, after having been blocked previously.
  - ``200``

* - press_timeout
  - *time*
  - The time during which press gestures are not started in case the user presses more than one mouse button.

    Swipe and wheel gesture aren't affected by this option.
  - ``50``

* - unblock_buttons_on_timeout
  - *bool*
  - Whether blocked mouse buttons should be pressed immediately on timeout. If false, they will be pressed and instantly released on button release.
  - ``true``
:::