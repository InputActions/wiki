# TouchpadHoldTrigger
:::{list-table}
* - **Inherits**
  - [](/devices/touchpad/triggers/index)

* - **Action events**
  - ``begin``, ``cancel``, ``end``, ``tick``, ``update``

* - **Finger count range**
  - 1-4

* - **Type**
  - Time-based trigger
:::

Performed by placing fingers on the touchpad and not moving them.

## Description
Single- and two-finger hold triggers begin almost immediately. Three- and four-finger triggers have a significant delay added by libinput.