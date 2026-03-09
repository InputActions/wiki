# TouchscreenRotateTrigger
:::{list-table}
* - **Inherits**
  - [](/devices/touchscreen/triggers/index)

* - **Action events**
  - ``begin``, ``cancel``, ``end``, ``tick``, ``update``

* - **Finger count range**
  - 2-5

* - **Type**
  - Motion trigger (delta based on angle)
:::

## Configuration
### Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - **direction**
  - *enum(clockwise, counterclockwise, any)*
  - ``any`` allows multiple directions.
:::