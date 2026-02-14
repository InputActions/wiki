# KeyboardShortcutTrigger
:::{list-table}
* - **Inherits**
  - [](/trigger)

* - **Action events**
  - ``begin``, ``cancel``, ``end``, ``update``

* - **Type**
  - Time-based trigger
:::

## Configuration
### Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - **shortcut**
  - *list(keyboard_key)*
  - Must consist of 0 or more modifier keys and 0 or 1 non-modifier key.

    Example: ``shortcut: [ leftctrl, z ]``
:::

## Description
Shortcuts must consist of 0 or more modifier keys and 0 or 1 non-modifier key. Modifier keys are not blocked (even if the shortcut is a single modifier), all
other keys are.

