# StrokeGesture
:::{list-table}
* - **Inherits**
  - [](/gestures/index)

* - **Supported devices**
  - [](/devices/mouse), [](/devices/touchpad)

* - **Type**
  - Motion gesture (delta based on distance)
:::

## Description
At the end, the performed stroke is compared against all active gestures' strokes and the gesture with the highest stroke match (must be at least 70%) is ended,
while all others are cancelled. Only ``on: end`` actions are supported.

Strokes can be recorded using the stroke recorder at *System Settings* -> *Desktop Effects* -> *Input Actions (configure)* or DBus: ``qdbus org.inputactions / recordStroke``.

If ``on: begin`` or ``on: update`` actions are required, use [](/gestures/swipe) instead. Stroke gestures are not compatible with swipe gestures, only one type 
may be active at a time.

## Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - **strokes**
  - *string* or *list(string)*
  - Base64-encoded string(s) containing the processed stroke(s).
:::
