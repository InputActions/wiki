# TouchscreenSwipeTrigger
:::{list-table}
* - **Inherits**
  - [](/devices/touchscreen/triggers/index)

* - **Action events**
  - ``begin``, ``cancel``, ``end``, ``tick``, ``update``

* - **Finger count range**
  - 1-5

* - **Incompatible with**
  - [](circle), [](stroke)

* - **Type**
  - Motion trigger (delta based on distance)
:::

Straight motion of all fingers at a particular angle.

## Configuration
### Properties
Either ``angle`` or ``direction`` must be set.

:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - **angle**
  - *range(float)*
  - Custom angle range. See the [](#angle-ranges) section below.

    Format: ``a-b``, where each angle ranges from ``0`` to ``360``.

    **Mutually exclusive with ``direction``.**
  -

* - **direction**
  - *enum(left, right, up, down, left_right, up_down, left_up, left_down, right_up, right_down, left_up_right_down, left_down_right_up, any)*
  - Predefined direction.

    ``left_right``, ``up_down`` - bidirectional
    ``left_up``, ``left_down``, ``right_up``, ``right_down`` - diagonal
    ``left_up_right_down``, ``left_down_right_up`` - bidirectional diagonal

    For bidirectional values, the first direction in the enum will always have a negative delta, while the second one will have a positive one.

    The ``left``, ``right``, ``up``, ``down``, ``left_right`` and ``up_down`` directions have an angle tolerance equivalent to the value of the
    ``swipe.angle_tolerance`` device property (20° by default). The remaining space is used for diagonal directions.

    **Mutually exclusive with ``angle``.**
  -

* - bidirectional
  - *bool*
  - Allow motion in the angle range opposite to the one specified in the ``angle`` property. Such motion will have a negative delta.

    This property has no effect if a predefined direction is used.
  - ``false``
:::

## Description
The direction is determined when the motion threshold is reached, allowing for ``on: begin`` and ``on: update`` actions. In case of issues regarding direction detection, create a [device rule](/devices/rule) that sets the device's motion threshold property.

:::{note}
The device's size ratio has no effect on the angle.
:::

If swipe triggers are active and the motion angle changes, but none of the active triggers acccept it, they are cancelled and all swipe triggers are activated
again, allowing for chaining multiple triggers together.

## Angle ranges
0° - right, 90° - up, 180° - left, 270° - down

```{image} /_static/images/swipe-trigger/angle1.png
:width: 400px
```

If ``a < b``, the range includes values where ``x >= a`` **and** ``x <= b``. Example for ``30-330``:
```{image} /_static/images/swipe-trigger/angle2.png
:width: 400px
```

If ``a > b``, the range includes values where ``x >= a`` **or** ``x <= b``. Example for ``330-30``:
```{image} /_static/images/swipe-trigger/angle3.png
:width: 400px
```

For ``330-30``, the opposite angle range (red) is ``150-210``:
```{image} /_static/images/swipe-trigger/angle4.png
:width: 400px
```

In the case of overlapping angle ranges, the normal one takes priority over the opposite one.

## Restoring the pre-0.9 angle tolerances
Prior to v0.9, the ``left``, ``right``, ``up``, ``down``, ``left_right`` and ``up_down`` directions had an angle tolerance of 45°, which was later changed to
20° in order to make space for diagonal directions. To restore the old behavior **and disable diagonal gestures**, set the ``swipe.angle_tolerance`` device
property to ``45`` using a [device rule](/devices/rule):
```yaml
device_rules:
  - conditions: $touchscreen
    swipe:
      angle_tolerance: 45
```