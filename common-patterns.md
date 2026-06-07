# Common patterns
Various patterns that may not immediately be obvious to users reading the wiki.

:::{note}
Examples may contain features exclusive to specific implementations or desktop environments.
:::

## Performing actions on inactive windows
Retrieve the window id from one of the [variables](/variables), activate the window using a [](/actions/activate-window), perform the action(s) and optionally
restore the previously active window, whose ID is saved to the ``previous_window_id`` variable. Certain actions, such as [](/actions/input) may not function
properly without a short delay after window activation.

```yaml
actions: # actions of a trigger
  - activate_window: $window_under_pointer_id
  - sleep: 1
  - input:
      - keyboard: [ home ]
  - activate_window: $previous_window_id # Restore the previous window
```
```yaml
actions: # actions of a trigger
  - activate_window: $window_under_pointer_id
  - input:
      - keyboard: [ leftmeta+pagedown ] # Minimize window shortcut, this one is handled by the compositor, so a delay is not required
```
```yaml
actions: # actions of a trigger
  - activate_window: $window_under_pointer_id
  - plasma_shortcut: kwin,Window Close # Also handled by the compositor
```

## Performing actions on a window the pointer is over at the beginning of a stroke gesture, but not at the end of it
The ``window_id``, ``window_under_fingers_id`` and ``window_under_pointer_id`` may change during a gesture, making it impossible to access the original values
at the end of the gesture. To solve this problem, the values of the aforementioned variables are copied to the ``initial_window_id``,
``initial_window_under_fingers_id`` and ``initial_window_under_pointer_id`` variables after triggers are activated.

```
mouse:
  gestures:
    - type: stroke
      strokes: [ 'MQAAMTJkZAA=' ] # down
      mouse_buttons: [ right ]

      actions:
        - activate_window: $initial_window_under_pointer_id
        - plasma_shortcut: kwin,Window Close
```

See the [](#performing-actions-on-inactive-windows) section for more information.