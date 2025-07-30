# InputAction
:::{list-table}
* - **Inherits**
  - [](/actions/index)
:::


## Description
Generates input events at compositor level. Only programs that receive input from the compositor will be able to process them.

The syntax of this action will change at some point in the future.

:::{warning}
Forgetting to release a keyboard key or mouse button can make your session unusable. Using a physical input device will not help.

Release actions should be performed in ``on: end_cancel`` actions instead of ``on: end`` ones.
:::

## Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - **input**
  - *list([](#deviceactions))*
  - Input actions to perform.
  - 

* - delay
  - *time*
  - Delay between each item in the sequence. Some programs (including input methods such as fcitx5) may not handle input events as expected if they are generated without delays.
  - ``0``
:::

### DeviceActions
Only one property per item allowed.

:::{list-table}
:header-rows: 1

* - Property
  - Type

* - keyboard
  - *list([KeyboardAction](#keyboardaction))*

* - mouse
  - *list([MouseAction](#mouseaction))*
:::

#### KeyboardAction
See [](/misc/keyboard-scancodes) for list of keys.

:::{list-table}
:header-rows: 1

* - Action
  - Description

* - ``+key``
  - Press ``key``.

* - ``-key``
  - Release ``key``.

* - ``key1+key2+...``
  - One or more keys separated by ``+``. Pressed in the order as specified and released in reverse order.

    ``key1+key2`` is equivalent to ``[ +key1, +key2, -key2, -key1 ]``

* - ``text: [text]``
  - Writes ``text`` into the application. Unlike other actions, this one is actually a map and accepts dynamic values (evaluated asynchronously).
:::

#### MouseAction
Button list: ``left``, ``middle``, ``right``, ``back``, ``forward``, ``task``, ``side``, ``extra``, ``extra6``, ``extra7``, ``extra8``, ``extra9``, ``extra10``,
``extra11``, ``extra12`` ``extra13``.

:::{list-table}
:header-rows: 1

* - Action
  - Description

* - ``+button``
  - Same as in [](#keyboardaction).

* - ``-button``
  - Same as in [](#keyboardaction).

* - ``button1+button2+...``
  - Same as in [](#keyboardaction).

* - ``move_by [x] [y]``
  - Move the pointer by (*x*, *y*).

* - ``move_by_delta``
  - Move the pointer by the current delta of a motion gesture. Multiplied by *<project:/devices/touchpad.md#touchpadeventhandler>.delta_multiplier*.

* - ``move_to [x] [y]``
  - Move the pointer to (*x*, *y*).
:::

## Example
```yaml
input:
  - keyboard: [ leftctrl+n ]
  - mouse: [ left, move_by 10 10 ]
  - keyboard: [ text: aaaaaa ]
  - keyboard:
      - text:
          command: date
```