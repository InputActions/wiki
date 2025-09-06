# Configuration
There is no configuration UI. The file is located at ``~/.config/inputactions/config.yaml``. On debug builds ``~/.config/inputactions/config-debug.yaml`` takes priority over the previous path.

:::{warning}
InputActions can run commands and simulate keyboard and mouse events. You may want to restrict write access to the configuration file.
:::

Configuration will be reloaded automatically when the file is modified. You can run ``qdbus6 org.inputactions / reloadConfig`` to reload it manually, this will
also print any errors. Another way to get the errors is to run ``journalctl --boot=0 -g "inputactions:" -n 5``.

Configuration uses the YAML format, JSON will work as well if you really want to use it.

:::{important}
Breaking changes may be introduced at any time, they will be announced in pull requests and in the release changelog.
:::

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

* - keyboard
  - *[](#eventhandler)*
  - 
  - 

* - mouse
  - *<project:/devices/mouse.md#mouseeventhandler>*
  - 
  - 

* - touchpad
  - *<project:/devices/touchpad.md#touchpadeventhandler>*
  - 
  - 
:::

### EventHandler
Inherited by <project:/devices/mouse.md#mouseeventhandler> and <project:/devices/touchpad.md#touchpadeventhandler>.

:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - **gestures**
  - *list([](/gestures/index))*
  - 

* - speed
  - *[](#speed)*
  - Settings for how gesture speed is determined.
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
  - How many input events to sample in order to determine the speed at which the gesture is performed. The average of each event's delta is compared against the thresholds below. If the threshold is reached, the gesture is considered to have been performed fast, otherwise slow.

    **Note**: No gestures will be triggered until all events have been sampled.
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