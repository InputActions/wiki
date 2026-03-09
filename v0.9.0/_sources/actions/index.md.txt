# Action
:::{list-table}
* - **Inherited by**
  - [](/actions/groups/index), [](/actions/command), [](/actions/input), [](/actions/sleep), [](/actions/plasma-shortcut)
:::

## Configuration
### Properties
Unlike triggers, action types are determined by the presence of required properties.

:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - conditions
  - *[](/conditions/index)*
  - Must be satisfied in order for the action to be executed.
  -

* - conflicting
  - *bool*
  - Whether this action can activate [trigger conflict resolution](<project:/trigger.md#conflict-resolution>).
  - ``true``

* - interval
  - *float* or *string*
  - How often should an ``on: update`` action execute. Can be negative for bidirectional motion triggers.

    ``0`` - Execute exactly once per event

    ``'+'`` - Execute exactly once per event with positive delta

    ``'-'`` - Execute exactly once per event with negative delta

    ``number`` - Execute when total delta is positive and is equal to or larger than ``number``

    ``-number`` - Execute when total delta is negative and is equal to or smaller than ``number``
  - ``0``

* - limit
  - *uint*
  - How many times the action can be executed during a trigger.

    ``0`` - no limit
  - ``0``

* - on
  - *enum(begin, cancel, end, end_cancel, tick, update)*
  - At which point of the trigger's [lifecycle](<project:/trigger.md#lifecycle>) the action should be executed.

    Valid values for a given trigger type are specified on its page in the ``Action events`` table row.
  - ``end``

* - threshold
  - *float* (min) or *range(float)* (min and max)
  - Same as *[](/trigger).threshold*, but only for this action.

    **``on: begin`` actions cannot have this property.**
  -
:::

### Examples
Update actions assigned to the ``actions`` property of a bidirectional trigger:
```yaml
- on: update
  interval: -10

  input:
    - keyboard: [ volumeup ]

- on: update
  interval: 10

  input:
    - keyboard: [ volumedown ]
```

```{toctree}
:hidden:

Command <command>
Input <input>
Plasma shortcut <plasma-shortcut>
Sleep <sleep>
Groups <groups/index>
```