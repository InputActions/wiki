# TouchpadClickTrigger
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

Performed by clicking the touchpad itself, not the buttons below or above.

:::{note}
This trigger requires the [libevdev backend](<project:/devices/touchpad/index.md#libevdev-backend>) to be enabled.
:::