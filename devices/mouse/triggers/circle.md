# MouseCircleTrigger
:::{list-table}
* - **Inherits**
  - [](/devices/mouse/triggers/index)

* - **Action events**
  - ``begin``, ``cancel``, ``end``, ``tick``, ``update``

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
  - Default

* - **direction**
  - *enum(clockwise, counterclockwise, any)*
  - ``any`` allows multiple directions.
  -

* - lock_pointer
  - *bool*
  - Lock the pointer's position while the trigger is active.
  - ``false``
:::