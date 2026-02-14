# InputAction
:::{list-table}
* - **Inherits**
  - [](/actions/index)
:::

Simulates keyboard and mouse input.

## Configuration
### Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - **input**
  - *list([](#deviceaction))*
  - Input actions to perform.
  -

* - delay
  - *time*
  - Delay between each item in the sequence.
  - ``0``
:::

### DeviceAction
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

### KeyboardAction
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

### MouseAction
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

* - ``move_by_delta [multiplier]``
  - Move the pointer by the current delta of a motion trigger. Multiplier is optional and defaults to ``1``.

* - ``move_to [x] [y]``
  - Move the pointer to (*x*, *y*).

* - ``wheel [x] [y]``
  - Move the wheel by (*x*, *y*). Currently not supported on Hyprland.
:::

### Examples
```yaml
input:
  - keyboard: [ leftctrl+n ]
  - mouse: [ left, move_by 10 10 ]
  - mouse: [ move_by_delta, move_by_delta 0.5 ]
  - keyboard: [ text: aaaaaa ]
  - keyboard:
      - text:
          command: date
```

## Description
:::{important}
As triggers may be cancelled, release actions should be performed in ``on: end_cancel`` actions instead of ``on: end`` ones.
:::

The emergency key combination will release all pressed buttons and keys.

In the KWin and Hyprland implementations, input is simulated in the compositor, thus programs which read from ``/dev/input`` will not see them. In the standalone
implementation, uinput is used.

## Known issues
- Input methods may cause improper processing of keyboard events. Workaround: set ``delay``, ``1`` should be enough.
- Windows that have just been activated by an action may not process events properly. Workaround: add a [](/actions/sleep) after the action that caused the
  activation.
- Keyboard text is always processed before keys. Workaround: set ``delay`` or split into multiple actions and add a [](/actions/sleep).