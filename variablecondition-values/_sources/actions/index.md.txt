# Action
:::{list-table}
* - **Inherited by**
  - [](/actions/groups/index), [](/actions/command), [](/actions/input), [](/actions/sleep), [](/actions/plasma-shortcut)
:::

## Description
Executed at a specific point of a gesture's [lifecycle](<project:/gestures/index.md#lifecycle>).

Action type is determined by the presence of required properties.

## Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - on
  - *enum(begin, end, cancel, update, end_cancel)*
  - At which point of the gesture's lifecycle the action should be executed.
  - ``end``

* - conditions
  - *[](/conditions/index)* or *list([](/conditions/index))*
  - Same as *[](/gestures/index).conditions*, but only for this action.
  -

* - interval
  - *float* or *string*
  - How often should an ``on: update`` action execute. Can be negative for bi-directional gestures.

    ``0`` - Execute exactly once per event

    ``'+'`` - Execute exactly once per event with positive delta

    ``'-'`` - Execute exactly once per event with negative delta

    ``number`` - Execute when total delta is positive and is equal to or larger than ``number``

    ``-number`` - Execute when total delta is negative and is equal to or smaller than ``number``
  - ``0``

* - limit
  - *uint*
  - How many times the action can be executed during a gesture.

    ``0`` - no limit
  - ``0``

* - threshold
  - *float* (min) or *range(float)* (min and max)
  - Same as *[](/gestures/index).threshold*, but only for this action.

    **``on: begin`` actions cannot have this property.**
  -
:::

```{toctree}
:hidden:

Command <command>
Input <input>
Plasma shortcut <plasma-shortcut>
Sleep <sleep>
Groups <groups/index>
```