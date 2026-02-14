# Touchscreen
:::{list-table}
* - **Inherits**
  - [](/devices/index)
:::

:::{note}
Touchscreen support is experimental.
:::

## Event filtering
Touchscreen event filtering requires blocking all events by default until a gesture is recognized. Setting the ``gestures`` property on
``TouchscreenEventHandler`` changes the behavior of the following actions:
- hold - latency increased by 50 ms
- motion - threshold for each finger increased by 4 mm
- tap - latency increased by 50 ms

## Window under fingers
Information about the window located under the center of all touch points is available in ``window_under_fingers_*`` variables.

## KWin and multiple touchscreens
The KWin plugin may currently not process touchscreen input correctly if multiple devices are present. In such situations, a device rule must be created to ignore all but one touchscreen.

```yaml
device_rules:
  - conditions:
      - $types contains touchscreen
      - $name != device_name # replace 'device_name' with the device's name
    ignore: true
```

```{toctree}
:maxdepth: 1
:hidden:

Triggers <triggers/index>
```