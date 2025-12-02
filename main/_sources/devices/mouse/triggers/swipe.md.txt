# Swipe
:::{list-table}
* - **Inherits**
  - [](/trigger)

* - **Action events**
  - ``begin``, ``cancel``, ``end``, ``tick``, ``update``

* - **Incompatible with**
  - [](circle), [](stroke)

* - **Type**
  - Motion trigger (delta based on distance)
:::

## Description
Performed by moving the mouse left, right, up ur down.

The direction is determined in the first few input events, making it possible to use ``on: begin`` and ``on: update`` actions. Upon changing the swipe axis,
triggers of this type are cancelled and reactivated if there are no active triggers with ``any`` direction.

## Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - **direction**
  - *enum(left, right, up, down, left_right, up_down, any)*
  - ``any``, ``left_right`` and ``up_down`` allow multiple directions. ``any`` will not work well with action intervals, as they only accept a single value, not two (x and y).
  -

* - lock_pointer
  - *bool*
  - Lock the pointer's position while the trigger is active.
  - ``false``
:::