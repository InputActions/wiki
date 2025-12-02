# Circle
:::{list-table}
* - **Inherits**
  - [](/trigger)

* - **Action events**
  - ``begin``, ``cancel``, ``end``, ``tick``, ``update``

* - **Incompatible with**
  - [](stroke), [](swipe)

* - **Type**
  - Motion trigger (delta based on angle)
:::

## Description
Continuous circular motion.

## Properties
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