# TouchpadPinchTrigger
:::{list-table}
* - **Inherits**
  - [](/devices/touchpad/triggers/index)

* - **Action events**
  - ``begin``, ``cancel``, ``end``, ``tick``, ``update``

* - **Finger count range**
  - 2-4

* - **Type**
  - Motion trigger (delta based on scale)
:::

## Configuration
### Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - **direction**
  - *enum(in, out, any)*
  - ``any`` allows multiple directions.
:::

## Description
Libinput may often incorrectly recognize pinch gestures as swipe gestures.