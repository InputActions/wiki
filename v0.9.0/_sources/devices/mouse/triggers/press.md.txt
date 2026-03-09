# MousePressTrigger
:::{list-table}
* - **Inherits**
  - [](/devices/mouse/triggers/index)

* - **Action events**
  - ``begin``, ``cancel``, ``end``, ``update``

* - **Type**
  - Time-based trigger
:::

Button press.

## Configuration
### Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - instant
  - *bool*
  - Whether the trigger should begin immediately. By default, there is a delay to prevent conflicts with normal clicks and stroke/swipe triggers.
  - ``false``
:::

## Description
Press trigger do not start immediately by default, allowing swipe triggers and normal clicks to be performed. If this behavior is not desired, *instant* should
be set to true. The property is set per-trigger, but affects all activated press triggers.