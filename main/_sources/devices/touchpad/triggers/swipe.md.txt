# TouchpadSwipeTrigger
:::{list-table}
* - **Inherits**
  - [](/devices/touchpad/triggers/index)

* - **Action events**
  - ``begin``, ``cancel``, ``end``, ``tick``, ``update``

* - **Finger count range**
  - 1-4

* - **Incompatible with**
  - [](circle), [](stroke)

* - **Type**
  - Motion trigger (delta based on distance)
:::

Straight motion of all fingers in one of four directions: left, right, up or down.

## Configuration
### Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - **direction**
  - *enum(left, right, up, down, left_right, up_down, any)*
  - ``any``, ``left_right`` and ``up_down`` allow multiple directions. ``any`` will not work well with action intervals, as they only accept a single value, not two (x and y).
:::

## Description
The direction is determined in the first few input events, making it possible to use ``on: begin`` and ``on: update`` actions. Upon changing the swipe axis,
triggers of this type are cancelled and reactivated if there are no active triggers with ``any`` direction.