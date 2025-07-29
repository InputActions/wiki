# Introduction

## Configuration
```{include} ../config.md
:start-after: "# Configuration"
:end-before: "## "
```

## First gesture
All configuration for specific device types is located in the ``keyboard``, ``mouse`` and ``touchpad`` root nodes. Gestures are defined in the ``gestures``
property of the those nodes.

This gesture will launch dolphin if you swipe three fingers to the right.
```yaml
touchpad:
  gestures:
    - type: swipe
      direction: right
      fingers: 3

      actions:
        - on: end
          command: dolphin
```

The ``on`` property of actions allows you to control at which point of the [gesture's lifecycle](<project:/gestures/index.md#lifecycle>) it should execute. The
default value is ``end``. Set it to ``begin`` if you want the gesture to trigger immediately.

To create a repeating action, set ``on`` to ``update`` and specify the repeat rate in the ``interval`` property.
```yaml
touchpad:
  gestures:
    - type: swipe
      direction: up
      fingers: 3

      actions:
        - on: update
          interval: 10
          input:
            - keyboard: [ volumeup ]
```

See [](/gestures/index), [](/actions/index) and everything else in the ``Core`` section of the sidebar for more information.

## Input event blocking
Input events are processed and blocked in the compositor. Programs that do not receive events from the compositor will still be able to process them.

## Complex gestures
Complex gestures will require multiple actions that execute at different points of the gesture's lifecycle. Here is an example three-finger window drag gesture.
```yaml
- type: swipe
  direction: any
  fingers: 3

  actions:
    - on: begin
      input:
        - keyboard: [ +leftmeta ]
        - mouse: [ +left ]

    - on: update
      input:
        - mouse: [ move_by_delta ]

    - on: end_cancel
      input:
        - keyboard: [ -leftmeta ]
        - mouse: [ -left ]
```

## Conditions
Conditions allow you to make a gesture activate only if certain criteria are met - finger count, window class, cursor shape and [much more](/variables).

It is also possible to set conditions on actions, though they will not have an effect on whether events are blocked.

```yaml
touchpad:
  gestures:
    - type: swipe
      direction: right
      fingers: 3

      conditions:
        - $window_class == firefox

      actions:
        - input:
            - mouse: [ forward ]
```

See [](/conditions/index).

## Bidirectional gestures
Changing the direction does not cause gesture activation. The following configuration will not allow for changing direction without lifting fingers.
```yaml
- type: rotate
  direction: clockwise

  # ...

- type: rotate
  direction: counterclockwise

  # ...
```

To create gestures with two repeating actions depending on the direction, set ``direction`` to a value that allows multiple directions (explicitly stated in
the property's description).
```yaml
- type: rotate
  direction: any

  actions:
    - on: update
      interval: -10
      input:
        - keyboard: [ volumedown ]

    - on: update
      interval: 10
      input:
        - keyboard: [ volumeup ]
```

## Conflicting gestures
At some point you may run into a situation where you want a global gesture that does x, and a local one for program y that does z. The first solution that may 
come to your mind is this:
```yaml
# Global
- type: ...
  conditions:
    - $window_class != program

  # ...

# Local
- type: ...
  conditions:
    - $window_class == program

  # ...
```

This will very quickly become a big mess. Instead, you should rely on the behavior that the first gesture to execute an action will cancel all other gestures,
and gestures are updated from top to bottom. This is a simplification, see <project:/gestures/index.md#conflict-resolution> for a detailed explanation.

The proper solution is:
```yaml
# Local
- type: ...
  conditions:
    - $window_class == program

  # ...

# Global
- type: ...
  # No window_class condition
```

## Chaining gestures
The ``last_trigger_id`` variable contains the ID of the last gesture. You can use it to have a gesture activate only if another specific gesture had been
performed immediately prior.

```yaml
- type: press
  fingers: 2
  id: hold_2

- type: swipe
  direction: right
  fingers: 3

  conditions:
    - $last_trigger_id == hold_2

  actions:
    # ...
```

If you want to be able to perform the swipe gesture multiple times without holding every time, you can set ``set_last_trigger: false`` on the swipe gesture and
it will not set the ``last_trigger_id`` variable anymore.

There is currently no convenient way to chain more than two gestures.