# Touchpad
:::{list-table}
* - **Supported gestures**
  - [](/gestures/click), [](/gestures/pinch), [](/gestures/press), [](/gestures/rotate), [](/gestures/stroke), [](/gestures/swipe)
:::

## Description
### Acceleration
Touchpad gestures are unaccelerated, this also applies to the ``move_by_delta`` mouse input action.

### libevdev backend
The libevdev input backend supplies the following touchpad data, which libinput does not:
- absolute position of each finger,
- pressure of each finger (usually the surface area but some devices provide true pressure),
- clicked state (only on touchpads that can be clicked).

This enables the following features:
- ``finger_`` and ``thumb_`` [variables](/variables) (thumb detection requires the pressure range to be set, see *[](#touchpadproperties)*),
- click gestures.

Additional [setup instructions](<project:/getting-started/installation/index.md#additional-setup-optional>) are required to enable those features.

### Five-finger gestures
[Libinput does not support five-finger gestures](https://gitlab.freedesktop.org/libinput/libinput/-/issues/763), click gestures are an exception, as they are managed by InputActions.

### Two-finger swipe/stroke gestures
Two-finger swipe gestures are achieved by treating scroll events as motion events. The thresholds for changing the scroll axis are quite large, which can cause
unexpected behavior with stroke gestures and ``direction: any`` swipe gestures utilizing the ``move_by_delta`` mouse input action. For two-finger stroke
gestures it is  recommended (but not required) to only use strokes that have been recorded using two fingers.

This feature will not work if scrolling on edges is enabled.

## TouchpadEventHandler
Inherits <project:/config.md#eventhandler>.

:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - devices
  - *map(string, [](#touchpadproperties))*
  - Device properties where the key is the device name, which can be obtained from variables.

    Some properties are detected automatically, but due to device or driver bugs, the value may be incorrect, in which case the user must override it manually.
  - 

* - click_timeout
  - *time*
  - The time during which a click gesture must be performed. If not, a press gesture will be started.
  - ``200``

* - delta_multiplier
  - *float*
  - Delta multiplier used for *move_by_delta* mouse input actions.
  - ``1.0``
:::

## TouchpadProperties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - buttonpad
  - *bool*
  - Whether the touchpad is a buttonpad (no physical buttons below, the entire device is a button). Detected automatically.

* - pressure_ranges.thumb
  - *range(uint)*
  - Pressure range for thumb detection. Current pressures can be obtained from variables.
:::