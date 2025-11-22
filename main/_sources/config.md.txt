# Configuration
There is no configuration UI.

Configuration path candidates:
- ``~/.config/inputactions/config-debug.yaml`` (debug builds only)
- ``/etc/inputactions/config.yaml``
- ``~/.config/inputactions/config.yaml`` (created if does not exist)

Candidates are checked from top to bottom. The configuration path is only chosen once, a restart is required if you wish to use a different file.

:::{warning}
InputActions can execute commands. In the future, it will also be capable of running commands on key press/release events without blocking them. If you do not
want normal users to have the ability to create such configurations, use the ``/etc/inputactions/config.yaml`` file.
:::

Configuration will be reloaded automatically when the file is modified, any errors will be shown in notifications. You can run
``inputactions config reload`` to reload it manually, this will also print errors.

Configuration uses the YAML format, JSON will work as well if you really want to use it.

:::{important}
Breaking changes may be introduced at any time, they will be announced in pull requests and in the release changelog.
:::

If a specific configuration renders the session unusable, the emergency key combination (backspace+space+enter in any order) can be held for 2 seconds to
suspend InputActions until the next config reload. A notification will be sent when triggered.

## Subproperties
``a.b`` in the ``Property`` column means that ``b`` is a property of ``a``:
```yaml
a:
  b: value
```

## Inheritance
Child objects inherit all properties from their parent, add new ones and can be used in properties where an object of the parents' type is required.

## Types
:::{list-table}
:header-rows: 1
:widths: 10 20 15

* - Type
  - Description
  - Examples

* - bool
  - ``true`` or ``false``
  -

* - float
  - Floating point number.
  -

* - int
  - Signed integer, can be negative.
  -

* - keyboard_key
  - See [](misc/keyboard-scancodes.md).
  -

* - regex
  - Regular expression.
  -

* - string
  - Text, can be wrapped in ``"`` or ``'``, but usually does not have to be.
  -

* - time
  - Duration in milliseconds, cannot be negative.
  -

* - uint
  - Unsigned integer, cannot be negative.
  -

* - enum(value1, value2, ...)
  - One value from the list of values in brackets.
  - ``value2``

* - flags(value1, value2, ...)
  - List of one or more values from the list of values in brackets.
  - ```yaml
    [ value1, value2 ]
    ```

* - list(type)
  - List of elements of type ``type``.
  - ```yaml
    [ 1, 2, 3 ]
    ```

    ```yaml
    - 1
    - 2
    - 3
    ```

* - map(key_type, value_type)
  - A map (``key: value``) where all keys are of type ``key_type`` and values of type ``value_type``.
  - ```yaml
    key1: value1
    key2: value2
    ```

* - point(type)
  - Two numeric values (x and y) of type ``type``. Format: ``x,y``
  - ``point(int)`` - ``4,0``<br>
    ``point(float)`` - ``1.1,2.2``

* - range(type)
  - Range of numbers of type ``type``. Format: ``min-max``, ``-`` may be surrounded by exactly one space on each side.
  - ``range(int)`` - ``1 - 2``<br>
    ``range(point)`` - ``0;0 - 0.5;0.5``
:::

## Structure
**Bold** properties are required, ~~struck through~~ properties are deprecated and will be removed in the future.

### Root
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - autoreload
  - *bool*
  - Whether the configuration should be automatically reloaded on file change.
  - ``true``

* - device_rules
  - *list(<project:/devices/index.md#devicerule>)*
  - Evaluated from bottom to top, each rule applies properties to all devices that satisfy the rule's conditions.
  -

* - notifications.config_error
  - *bool*
  - Send a notification when the configuration fails to load.
  - ``true``

* - keyboard
  - *[](#eventhandler)*
  - 
  - 

* - mouse
  - *<project:/devices/mouse/index.md#mouseeventhandler>*
  - 
  - 

* - pointer
  - *[](#eventhandler)*
  - 
  - 

* - touchpad
  - *<project:/devices/touchpad/index.md#touchpadeventhandler>*
  - 
  - 
:::

### EventHandler
Inherited by <project:/devices/mouse/index.md#mouseeventhandler> and <project:/devices/touchpad/index.md#touchpadeventhandler>.

:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - **gestures**
  - *list([](/trigger))*
  - 

* - speed
  - *[](#speed)*
  - Settings for how motion trigger speed is determined.
:::

### Speed
The defaults may not work for everyone, as they depend on the device's sensitivity and size.

:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - events
  - *uint*
  - How many input events to sample in order to determine the speed at which the trigger is performed. The average of each event's delta is compared against the thresholds below. If the threshold is reached, the trigger is considered to have been performed fast, otherwise slow.

    **Note**: No triggers will begin until all events have been sampled.
  - ``3``

* - swipe_threshold
  - *float*
  - 
  - ``20``

* - pinch_in_threshold
  - *float*
  - 
  - ``0.04``

* - pinch_out_threshold
  - *float*
  - 
  - ``0.08``

* - rotate_threshold
  - *float*
  - 
  - ``5``
:::

## Example
```yaml
mouse:
  click_timeout: 50
  
  gestures:
    # ...

touchpad:
  devices:
    Synaptics TM3276-022:
      pressure_ranges:
        thumb: 75
        palm: 140

  speed:
    swipe_threshold: 15

  gestures:
    - type: pinch
      fingers: 2
      direction: in

      actions:
        - plasma_shortcut: kwin,Window Close
```