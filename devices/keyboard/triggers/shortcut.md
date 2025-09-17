# Shortcut
:::{list-table}
* - **Inherits**
  - [](/trigger)

* - **Type**
  - Time-based trigger
:::

## Description
Shortcuts must consist of 0 or more modifier keys and 0 or 1 non-modifier key. Modifier keys are not blocked (even if the shortcut is a single modifier), all
other keys are.

## Properties
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