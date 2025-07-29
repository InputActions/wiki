# WheelGesture
:::{list-table}
* - **Inherits**
  - [](/gestures/index)

* - **Supported devices**
  - [](/devices/mouse)

* - **Type**
  - Motion gesture (delta based on distance)
:::

## Description
Performed by using a scroll wheel.

Wheel gestures can have two different lifecycles - if the gesture has an ``on: update`` action and a mouse button or keyboard modifier is present, the gesture
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