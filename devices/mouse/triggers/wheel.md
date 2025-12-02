# Wheel
:::{list-table}
* - **Inherits**
  - [](/trigger)

* - **Action events**
  - ``begin``, ``cancel``, ``end``, ``tick``, ``update``

* - **Type**
  - Motion trigger (delta based on distance)
:::

## Description
Performed by using a scroll wheel.

Wheel triggers can have two different lifecycles - if the trigger has an ``on: update`` action and a mouse button or keyboard modifier is present, the trigger
begins on the first scroll event and ends when a modifier/button is released, otherwise it begins and ends on the same scroll event.

## Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - **direction**
  - *enum(left, right, up, down, left_right, up_down)*
  - ``any``, ``left_right`` and ``up_down`` allow multiple directions.
:::