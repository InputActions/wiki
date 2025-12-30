# Introduction

## Configuration
```{include} ../config.md
:start-after: "# Configuration"
:end-before: "## "
```

## First trigger
All configuration for specific device types is located in the ``keyboard``, ``mouse``, ``pointer`` and ``touchpad`` root nodes. Triggers are defined in the
``gestures``property of the those nodes.

This trigger will launch dolphin if you swipe three fingers to the right.
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

The ``on`` property of actions allows you to control at which point of the [trigger's lifecycle](<project:/trigger.md#lifecycle>) it should execute. The default
value is ``end``. Set it to ``begin`` if you want to execute an actions as soon as the trigger begins.

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

See [](/trigger), [](/actions/index) and everything else in the ``Core`` section of the sidebar for more information. The list of triggers for a particular
device can be found at ``Devices`` -> ``[device]`` -> ``Triggers``.

![](/_static/images/touchpad_triggers.png)

## Complex triggers
Complex triggers will require multiple actions that execute at different points of the trigger's lifecycle. Here is an example three-finger window drag trigger.
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
Conditions allow you to make a trigger activate only if certain criteria are met - finger count, window class, cursor shape and [much more](/variables).

It is also possible to set conditions on actions, though events will be blocked even if no action can be executed.

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

## Bidirectional triggers
Changing the direction does not cause trigger activation. The following configuration will not allow for changing direction without lifting fingers.
```yaml
- type: rotate
  direction: clockwise

  # ...

- type: rotate
  direction: counterclockwise

  # ...
```

To create triggers with two repeating actions depending on the direction, set ``direction`` to a value that allows multiple directions (explicitly stated in
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

## Conflicting triggers
At some point you may run into a situation where you want a global trigger that does x, and a local one for program y that does z. The first solution that may
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

This will very quickly become a big mess. Instead, you should rely on the behavior that the first trigger to execute an action will cancel all other triggers,
and triggers are updated from top to bottom. This is a simplification, see <project:/trigger.md#conflict-resolution> for a detailed explanation.

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

## YAML anchors
[YAML anchors](/advanced/yaml-anchors.md) can be used to define values (mouse trigger button, strokes etc.) once and reuse them thorough the configuration.

- ``&name`` - Define (can be done anywhere)
- ``*name`` - Reference (must be defined first above the reference)

```yaml
_anchors: # Prefixed with _ to prevent potential conflicts with future properties, may be renamed to anything
  - &mouse_stroke_button [ back ]
  - &stroke_up [ 'MGQA0DMnPMwwAGQA' ]
  - &stroke_left [ 'ZDIAnQAxZAA=' ]
  - &stroke_down [ 'MAAAMTNkZAA=' ]
  - &stroke_circle_clockwise [ 'PgwAAE8LBRldGgwpZDEUN19LHUhTWSNgMl0uphJTObUERj/JAChJ2gUaT/AaDVf7QAZkAA=='  ]
  - &stroke_circle_counterclockwise [ 'UQsAojwHBl0mDA1UFBYTSgcjGT8AMx8yAEEjIgpWKhEXXi8CKl81+UBaPO9YS0XiZDtLzGInUbtZGVayRAhfpTUEZAA=' ]

mouse:
  gestures:
    - type: stroke
      strokes: *stroke_up
      mouse_buttons: *mouse_stroke_button
      # ...
```

## Trigger groups
[Trigger groups](/advanced/trigger-groups.md) apply a set of properties to all triggers specified in the ``gestures`` property of the group and can be nested.

Conditions are merged into an ``all:`` condition group consisting of the group's and the trigger's condition.

```yaml
_anchors:
  - &mouse_stroke_button [ back ]
  - &stroke_up [ 'MGQA0DMnPMwwAGQA' ]
  - &stroke_down [ 'MAAAMTNkZAA=' ]

mouse:
  gestures:
    - conditions:
        - $window_class == firefox
      gestures:
        # Firefox triggers
        - type: stroke
          mouse_buttons: *mouse_stroke_button

          gestures:
            # Stroke triggers
            - strokes: *stroke_up
              actions:
                - input:
                    - keyboard: [ leftctrl+t ]

            - strokes: *stroke_down
              actions:
                - input:
                    - keyboard: [ leftctrl+n ]

        # Other Firefox triggers
        - type: press
          mouse_buttons: [ extra7 ]

          actions:
            - input:
                - mouse: [ back ]

    - conditions:
        - $window_class == VSCodium
      gestures:
        # VSCodium triggers
        - type: stroke
          mouse_buttons: *mouse_stroke_button

          gestures:
            # Stroke triggers
            - strokes: *stroke_up
              actions:
                - input:
                    - keyboard: [ leftctrl+pageup ]

            - strokes: *stroke_down
              actions:
                - input:
                    - keyboard: [ leftctrl+pagedown ]
```

## Chaining triggers
The ``last_trigger_id`` variable contains the ID of the last trigger. You can use it to have a trigger activate only if another specific trigger had been
performed immediately prior.

```yaml
- type: hold
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

If you want to be able to perform the swipe trigger multiple times without holding every time, you can set ``set_last_trigger: false`` on the swipe trigger and
it will not set the ``last_trigger_id`` variable anymore.

There is currently no convenient way to chain more than two triggers.