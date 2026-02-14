# TouchscreenCircleTrigger
:::{list-table}
* - **Inherits**
  - [](/devices/touchscreen/triggers/index)

* - **Action events**
  - ``begin``, ``cancel``, ``end``, ``tick``, ``update``

* - **Finger count range**
  - 1-5

* - **Incompatible with**
  - [](stroke), [](swipe)

* - **Type**
  - Motion trigger (delta based on angle)
:::

Continuous circular motion.

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