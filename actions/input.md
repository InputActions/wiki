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
  - Delay between each item in the sequence.
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
See [](/devices/keyboard/index).

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
  - Move the pointer by the current delta of a motion trigger. Multiplied by *<project:/devices/touchpad/index.md#touchpadeventhandler>.delta_multiplier*.

* - ``move_to [x] [y]``
  - Move the pointer to (*x*, *y*).

* - ``wheel [x] [y]``
  - Move the wheel by (*x*, *y*). Currently not supported on Hyprland.
:::

## Known issues
- Input methods may cause improper processing of keyboard events. Workaround: set ``delay``, ``1`` should be enough.
- Windows that have just been activated by an action may not process events properly. Workaround: add a [](/actions/sleep) after the action that caused the
  activation.
- Keyboard text is always processed before keys. Workaround: set ``delay`` or split into multiple actions and add a [](/actions/sleep).

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