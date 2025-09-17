# Press
:::{list-table}
* - **Inherits**
  - [](/trigger)

* - **Type**
  - Time-based trigger
:::

## Description
Performed by pressing a button.

Press trigger do not start immediately by default, allowing swipe triggers and normal clicks to be performed. If this behavior is not desired, *instant* should
be set to true. The property is set per-trigger, but affects all activated press triggers.

## Properties
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