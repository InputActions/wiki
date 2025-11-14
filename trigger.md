# Trigger
## Description
An action or set of actions performed using an input device, also referred to as *gesture*.

Each device has its own set of triggers, listed in the ``Triggers`` subpage of the device.

Thresholds and action intervals are based on the trigger's delta. Time-based triggers update every *5 ms* with a delta of *5*.

Triggers use the unaccelerated delta if available. The accelerated delta is only used for action intervals and ``move_by_delta`` input actions if
``accelerated`` is set to ``true``.

### Lifecycle
- ``begin`` - Can be delayed or prevented by thresholds.
- ``update`` - Before a trigger receives an update event, its update conditions (direction) are checked first. If not satisfied, the trigger is cancelled.
- ``tick`` - Uses the same interval and delta as time-based triggers. Intended for creation of time-based actions in non-time-based triggers. Ticking starts
  when the trigger begins.
- ``end`` - The user has finished performing the trigger and end conditions have been satisfied.
- ``cancel`` - The trigger's update conditions were not satisfied, the trigger has been overridden by another one as a result of conflict resolution, or the
  user has started performing a different trigger.

### Conflict resolution
Conflict resolution ensures that there are never multiple triggers executing actions simultaneously by immediately cancelling all other triggers when:
- a trigger is updated, and has any action that had been executed, or has an update action that can be executed but hasn't been yet (interval not reached),
- a trigger ends, and has an end action that can be executed,
- a stroke trigger is active (in this case only swipe triggers are cancelled).

Triggers are updated in the same order as specified in the configuration.

In the following example, it is not necessary to set ``speed: slow`` on *Trigger 2*, because when the action of *Trigger 1* is executed, *Trigger 2* will be
cancelled immediately. The same applies to all other properties - conditions, thresholds etc.
```yaml
# Trigger 1
- type: swipe
  direction: right
  speed: fast

  actions:
    - on: begin
      # ...

# Trigger 2
- type: swipe
  direction: right

  actions:
    - on: begin
      # ...
```

It is also possible for a trigger below to cancel the one above it if actions are executed at different points of the lifecycle.
```yaml
# Trigger 1
- type: swipe
  direction: right

  actions:
    - on: end
      # ...

# Trigger 2
- type: swipe
  direction: right

  actions:
    - on: begin
      # ...
```

## Properties
These properties can be set on all triggers. See the other tables below and the ``Triggers`` page of every device for properties that are only available in
specific cases.

:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - **type**
  - *enum(click, hover, pinch, press, rotate, shortcut, stroke, swipe, tap, wheel)*
  - Same as the trigger's name but lowercase.
  -

* - accelerated
  - *bool*
  - Use the accelerated delta (if available) for action intervals and the ``move_by_delta`` input action.
  - ``false``

* - actions
  - *list([](/actions/index))*
  -
  -

* - block_events
  - *bool*
  - Whether this trigger should block all input events required to perform it while active. Only one active trigger needs this property set to ``true`` in order
    for events to be blocked.
  - ``true``

* - clear_modifiers
  - bool
  - Whether keyboard modifiers should be cleared when this trigger begins. They will not be restored after the trigger ends.
  - ``true`` if an [](/actions/input) is present, ``false`` otherwise

* - conditions
  - *[](/conditions/index)* or *list([](/conditions/index))*
  - Must be satisfied in order for this trigger to be activated.

    If the value is a list, the behavior is the same as an ``all`` [](/conditions/group).
  - 

* - end_conditions
  - *[](/conditions/index)* or *list([](/conditions/index))*
  - If satisfied, the trigger will end, otherwise it will be cancelled.

    If the value is a list, the behavior is the same as an ``all`` [](/conditions/group).
  -

* - id
  - *string*
  - Must be unique.
  -

* - resume_timeout
  - *time*
  - The amount of time after a trigger ends, during which the trigger can be performed again as if it never actually ended. Performing any action that does not
    activate this trigger causes it to be cancelled immediately.

    Can be used for a drag touchpad trigger that allows lifting fingers.

    Not compatible with stroke triggers.
  - ``0``

* - set_last_trigger
  - *bool*
  - Whether to set ``last_trigger`` variables.
  - ``true``

* - threshold
  - *float* (min) or *range(float)* (min and max)
  - How far this trigger needs to progress in order to begin.

    **Triggers with ``on: begin`` or ``on: update`` actions cannot have maximum thresholds.**
  -

* - ~~keyboard_modifiers~~
  -
  - **Deprecated.** Use the ``keyboard_modifiers`` variable in a condition instead.
  -
:::

### Motion triggers
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - speed
  - *enum(fast, slow)*
  - The speed at which the trigger must be performed. Will be available as a variable in the future.
:::