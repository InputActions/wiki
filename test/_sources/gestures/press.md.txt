# PressGesture
:::{list-table}
* - **Inherits**
  - [](/gestures/index)

* - **Supported devices**
  - [](/devices/mouse), [](/devices/touchpad)

* - **Type**
  - Time-based gesture
:::

## Description
### Mouse
Performed by pressing a button.

Press gestures do not start immediately by default, allowing swipe gestures and normal clicks to be performed. If this behavior is not desired, *instant* should
be set to true. The property is set per-gesture, but affects all activated press gestures.

### Touchpad
Performed by placing fingers on the touchpad.

Single- and two-finger press gestures begin almost immediately. Three- and four-finger gestures have a significant delay added by libinput.

## Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - instant
  - *bool*
  - Whether the gesture should begin immediately. By default, there is a delay to prevent conflicts with normal clicks and stroke/swipe gestures.

    Only applies to mouse gestures.
  - ``false``
:::