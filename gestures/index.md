# Gesture
:::{list-table}
* - **Inherited by**
  - [](/gestures/click), [](/gestures/hover) [](/gestures/pinch), [](/gestures/press), [](/gestures/rotate), [](/gestures/shortcut), [](/gestures/stroke),
    [](/gestures/swipe), [](/gestures/tap), [](/gestures/wheel)
:::

## Description
Each gesture's page explicitly states the type, supported devices and source of the delta.

Thresholds and action intervals are based on the gesture's delta.  Time-based gestures update every *5 ms* with a delta of *5*.

### Lifecycle
- ``begin`` - Can be delayed or prevented by thresholds.
- ``update`` - Before a gesture receives an update event, its update conditions (direction) are checked first. If not satisfied, the gesture is cancelled.
- ``end`` - The user has finished performing the gesture and end conditions have been satisfied.
- ``cancel`` - The gesture's update conditions were not satisfied, the gesture has been overridden by another one as a result of conflict resolution, or the
  user has started performing a different gesture.

### Conflict resolution
Conflict resolution ensures that there are never multiple gestures executing actions simultaneously by immediately cancelling all other gestures when:
- a gesture is updated, and has any action that had been executed, or has an update action that can be executed but hasn't been yet (interval not reached),
- a gesture ends, and has an end action that can be executed,
- a stroke gesture is active (in this case only swipe gestures are cancelled).

Gestures are updated in the same order as specified in the configuration.

In the following example, it is not necessary to set ``speed: slow`` on *Gesture 2*, because when the action of *Gesture 1* is executed, *Gesture 2* will be
cancelled immediately. The same applies to all other properties - conditions, thresholds etc.
```yaml
# Gesture 1
- type: swipe
  direction: right
  speed: fast
  
  actions:
    - on: begin
      # ...

# Gesture 2
- type: swipe
  direction: right

  actions:
    - on: begin
      # ...
```

It is also possible for a gesture below to cancel the one above it if actions are executed at different points of the lifecycle.
```yaml
# Gesture 1
- type: swipe
  direction: right
  
  actions:
    - on: end
      # ...

# Gesture 2
- type: swipe
  direction: right

  actions:
    - on: begin
      # ...
```

## Properties
These properties can be set on all gestures. See the other tables below for properties that are only available in specific cases.

:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - **type**
  - *enum(click, hover, pinch, press, rotate, shortcut, stroke, swipe, tap, wheel)*
  -
  -

* - actions
  - *list([](/actions/index))*
  -
  -

* - clear_modifiers
  - bool
  - Whether keyboard modifiers should be cleared when this gesture begins. They will not be restored after the gesture ends.
  - ``true`` if an [](/actions/input) is present, ``false`` otherwise

* - conditions
  - *[](/conditions/index)* or *list([](/conditions/index))*
  - Must be satisfied in order for this gesture to be activated.
    
    If the value is a list, the behavior is the same as an ``all`` [](/conditions/group).
  - 

* - end_conditions
  - *[](/conditions/index)* or *list([](/conditions/index))*
  - If satisfied, the gesture will end, otherwise it will be cancelled.

    If the value is a list, the behavior is the same as an ``all`` [](/conditions/group).
  -

* - id
  - *string*
  - Must be unique.
  -

* - set_last_trigger
  - *bool* 
  - Whether to set ``last_trigger`` variables.
  - ``true``

* - threshold
  - *float* (min) or *range(float)* (min and max)
  - How far this gesture needs to progress in order to begin.
    
    **Gestures with ``on: begin`` or ``on: update`` actions cannot have maximum thresholds.**
  -

* - ~~keyboard_modifiers~~
  -
  - **Deprecated.** Use the ``keyboard_modifiers`` variable in a condition instead.
  -
:::

### Motion gestures
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - speed
  - *enum(fast, slow)*
  - The speed at which the gesture must be performed. Will be available as a variable in the future.
:::

### Mouse gestures
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - mouse_buttons
  - *flags(left, middle, right, back, forward, extra1, extra2, ..., extra13)*
  - Mouse buttons that must be pressed in order for the gesture to be activated.

    ``extra1`` and ``extra2`` are equal to ``back`` and ``forward`` respectively.
  -

* - mouse_buttons_exact_order
  - *bool*
  - Whether mouse buttons must be pressed in the same order as specified in ``mouse_buttons``.
  - ``false``
:::

### Touchpad gestures
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - fingers
  - *uint*
  - How many fingers must be present on the input device.

    Equivalent to a ``$fingers == [value]`` condition.
:::

```{toctree}
:hidden:

Click <click>
Hover <hover>
Pinch <pinch>
Press <press>
Rotate <rotate>
Shortcut <shortcut>
Stroke <stroke>
Swipe <swipe>
Tap <tap>
Wheel <wheel>
```