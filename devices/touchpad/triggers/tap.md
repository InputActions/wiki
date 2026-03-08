# TouchpadTapTrigger
:::{list-table}
* - **Inherits**
  - [](/devices/touchpad/triggers/index)

* - **Action events**
  - ``begin``, ``cancel``, ``end``, ``tick``, ``update``

* - **Finger count range**
  - 1-5

* - **Type**
  - Time-based trigger
:::

Performed by quickly putting down fingers and lifting all of them.

:::{note}
This trigger requires the [evdev input backend](<project:/devices/touchpad/index.md#evdev-backend>) to be enabled.
:::

## Description
Tap-to-click must be enabled in order for 1-3 finger tapping to work.