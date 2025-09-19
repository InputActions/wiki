# Trigger groups
Trigger groups apply all properties except ``gestures`` to the triggers specified in the ``gestures`` property. This can be used to reduce duplication.

## Example
```yaml
touchpad:
  gestures:
    # Firefox triggers
    - conditions:
        - $window_class == firefox

      gestures:
        # Firefox swipe triggers with meta modifier
        - type: swipe
          conditions:
            - $keyboard_modifiers == meta
  
          gestures:
            - direction: right
              conditions:
                - $pointer_position_window_percentage_x < 0.5
              
            - direction: left
              conditions:
                - $pointer_position_window_percentage_x >= 0.5

        # Firefox swipe triggers with alt modifier
        - type: swipe
          conditions:
            - $keyboard_modifiers == alt

          gestures:
            - direction: right
              conditions:
                - $pointer_position_window_percentage_x < 0.5

            - direction: left
              conditions:
                - $pointer_position_window_percentage_x >= 0.5
```

A practical example with strokes:
```yaml
mouse:
  gestures:
    - type: stroke
      mouse_buttons: [ right ]

      conditions:
        - $keyboard_modifiers == meta

      gestures:
        - strokes: 'ADEAAGQyZAA='
          actions:
            - command: kwrite

        - strokes: 'HwkAB0QSDBBYHRMbYyoZMWQ3HUFaSCRMTFYqVztdMGITXj2vBlZCwABJR9EBNE3eDxpX5x0LXvQuBWQA'
          actions:
            - command: dolphin
```