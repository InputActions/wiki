# Circle
:::{list-table}
* - **Inherits**
  - [](/trigger)

* - **Action events**
  - ``begin``, ``cancel``, ``end``, ``tick``, ``update``

* - **Finger count range**
  - 1-5

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

* - **direction**
  - *enum(clockwise, counterclockwise, any)*
  - ``any`` allows multiple directions.
:::