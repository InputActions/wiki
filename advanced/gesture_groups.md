# Gesture groups
Gesture groups apply all properties except *gestures* to the gestures specified in the *gestures* property. This can also be used to reduce duplication.

## Example
```yaml
touchpad:
  gestures:
    # Firefox gestures
    - conditions:
        - $window_class == firefox

      gestures:
        # Firefox swipe gestures with meta modifier
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

        # Firefox swipe gestures with alt modifier
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