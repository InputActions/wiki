# SwipeGesture
:::{list-table}
* - **Inherits**
  - [](/gestures/index)

* - **Supported devices**
  - [](/devices/mouse), [](/devices/touchpad)

* - **Type**
  - Motion gesture (delta based on distance)
:::

## Description
The direction is determined in the first few input events, making it possible to use ``on: begin`` and ``on: update`` actions.

If complex shapes or diagonal gestures are required, use [](/gestures/stroke) instead. Swipe gestures are not compatible with stroke gestures, only one type may
be active at a time. 

## Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - **direction**
  - *enum(left, right, up, down, left_right, up_down, any)*
  - ``any``, ``left_right`` and ``up_down`` allow multiple directions. ``any`` will not work well with action intervals, as they only accept a single value, not two (x and y).
:::