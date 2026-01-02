# Stroke
:::{list-table}
* - **Inherits**
  - [](/trigger)

* - **Action events**
  - ``end``

* - **Finger count range**
  - 1-4

* - **Incompatible with**
  - [](circle), [](swipe)

* - **Type**
  - Motion trigger (delta based on distance)
:::

## Description
Draw any shape. At the end of the trigger, the performed stroke is compared against all active triggers' strokes and the trigger with the highest stroke match
(must be at least 70%) is ended, while all others are cancelled. **Only ``on: end`` actions are supported, making this trigger not suitable for certain use
cases.**

Strokes can be recorded using the stroke recorder at *System Settings* -> *Desktop Effects* -> *Input Actions (configure)* or the control tool:
``inputactions record-stroke``.

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
