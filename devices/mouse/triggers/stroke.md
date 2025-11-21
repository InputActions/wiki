# Stroke
:::{list-table}
* - **Inherits**
  - [](/trigger)

* - **Type**
  - Motion trigger (delta based on distance)
:::

## Description
At the end, the performed stroke is compared against all active triggers' strokes and the trigger with the highest stroke match (must be at least 70%) is ended,
while all others are cancelled. Only ``on: end`` actions are supported.

Strokes can be recorded using the stroke recorder at *System Settings* -> *Desktop Effects* -> *Input Actions (configure)* or DBus: ``inputactions record-stroke``.

If ``on: begin`` or ``on: update`` actions are required, use [](swipe) instead. Stroke triggers are not compatible with swipe triggers, only one type may be
active at a time.

## Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - **strokes**
  - *string* or *list(string)*
  - Base64-encoded string(s) containing the processed stroke(s).
  -

* - lock_pointer
  - *bool*
  - Lock the pointer's position while the trigger is active.
  - ``false``
:::
