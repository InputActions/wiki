# Example triggers
:::{important}
Read [](/getting-started/introduction) first before complaining that these do not work.
:::

## Mouse
<details>
  <summary>Right + Draw circle clockwise - Close window</summary>

  ```yaml
  - type: stroke
    strokes: [ 'OAMAAUkEBRZZEgwkYCARMmA6GUBSViRPQGMrYyNkNLAOVT3DAzhH0AUdUOkYC1j2OQBkAA==' ]
    mouse_buttons: [ right ]

    actions:
      - plasma_shortcut: kwin,Window Close
  ```
</details>
<details>
  <summary>Meta + Wheel - Volume control</summary>

  ```yaml
  - type: wheel
    direction: up_down

    conditions:
      - $keyboard_modifiers == meta

    actions:
      - on: update
        interval: '+'
        input:
          - keyboard: [ volumedown ]

      - on: update
        interval: '-'
        input:
          - keyboard: [ volumeup ]
  ```
</details>
<details>
  <summary>Extra7/Extra8 - Volume control (repeats if held)</summary>

  ```yaml
  _anchors:
    - &repeat_delay 250
    - &repeat_interval 50

  mouse:
    gestures:
      - type: press
        mouse_buttons: [ extra8 ]
        instant: true

        actions:
          - on: begin
            input:
              - keyboard: [ volumedown ]

          - on: update
            threshold: *repeat_delay
            interval: *repeat_interval
            input:
              - keyboard: [ volumedown ]

      - type: press
        mouse_buttons: [ extra7 ]
        instant: true

        actions:
          - on: begin
            input:
              - keyboard: [ volumeup ]

          - on: update
            threshold: *repeat_delay
            interval: *repeat_interval
            input:
              - keyboard: [ volumeup ]
  ```
</details>
<details>
  <summary>Meta + Left/Right - Go back/forward</summary>

  ```yaml
  - type: press
    mouse_buttons: [ left ]
    instant: true

    conditions:
      - $keyboard_modifiers == meta

    actions:
      - on: begin
        input:
          - mouse: [ back ]

  - type: press
    mouse_buttons: [ right ]
    instant: true

    conditions:
      - $keyboard_modifiers == meta

    actions:
      - on: begin
        input:
          - mouse: [ forward ]

  ```
</details>
<details>
  <summary>Meta + Left + Swipe up/down - Home/End</summary>

  ```yaml
  - type: swipe
    direction: up
    mouse_buttons: [ left ]
    
    conditions:
      - $keyboard_modifiers == meta

    actions:
      - on: begin
        input:
          - keyboard: [ leftctrl+home ]

  - type: swipe
    direction: down
    mouse_buttons: [ left ]
    
    conditions:
      - $keyboard_modifiers == meta

    actions:
      - on: begin
        input:
          - keyboard: [ leftctrl+end ]
  ```
</details>
<details>
  <summary>Left click top left corner - Open dolphin</summary>

  ```yaml
  - type: press
    mouse_buttons: [ left ]
    instant: true

    conditions:
      - $pointer_position_screen_percentage <= 0.01,0.01

    actions:
      - on: begin
        command: dolphin
  ```
</details>
<details>
  <summary>Middle click top edge - Maximize window</summary>

  ```yaml
  - type: press
    mouse_buttons: [ middle ]
    instant: true
    
    conditions:
      - $pointer_position_screen_percentage_y <= 0.01

    actions:
      - on: begin
        plasma_shortcut: kwin,Window Maximize
  ```
</details>
<details>
  <summary>Right + Swipe down - Minimize window under cursor</summary>

  ```yaml
   - type: swipe
     direction: down
     mouse_buttons: [ right ]

     actions:
       - command: kdotool windowminimize $window_under_id
  ```
</details>

## Touchpad
<details>
  <summary>Swipe 3 - Window drag</summary>

Set *<project:/devices/touchpad/index.md#touchpadeventhandler>.delta_multiplier* to make the trigger faster or slower.

  ```yaml
  - type: swipe
    fingers: 3
    direction: any
    resume_timeout: 500 # Optional: allow lifting fingers for 500 ms, perform any other action (for example tap) to cancel the trigger immediately
    accelerated: true # May not work, see the Touchpad page

    actions:
      - on: begin
        input:
          - keyboard: [ +leftmeta ]
          - mouse: [ +left ]

      - on: update
        input:
          - mouse: [ move_by_delta ]

      - on: end_cancel
        input:
          - keyboard: [ -leftmeta ]
          - mouse: [ -left ]
```
</details>
<details>
  <summary>Swipe 3 left/right - Go back/forward</summary>

  ```yaml
  - type: swipe
    fingers: 3
    direction: left

    actions:
      - on: begin
        input:
          - mouse: [ back ]

  - type: swipe
    fingers: 3
    direction: right

    actions:
      - on: begin
        input:
          - mouse: [ forward ]
  ```

</details>
<details>
  <summary>Rotate 2 - Volume control</summary>

  ```yaml
  - type: rotate
    fingers: 2
    direction: any

    actions:
      - on: update
        interval: -10
        input:
          - keyboard: [ volumedown ]

      - on: update
        interval: 10
        input:
          - keyboard: [ volumeup ]
  ```
</details>
<details>
  <summary>Swipe 4 left/right - Switch window</summary>

Swipe slow - Switch window<br>
Swipe fast - Open alt+tab switcher

  ```yaml
  - type: swipe
    fingers: 4
    direction: left_right
    speed: fast
    
    actions:
      - on: begin
        input:
          - keyboard: [ +leftalt, tab ]

      - on: update
        interval: -75
        input:
          - keyboard: [ leftshift+tab ]

      - on: update
        interval: 75
        input:
          - keyboard: [ tab ]

      - on: end_cancel
        input:
          - keyboard: [ -leftalt ]

  # Quick window switching (left)
  - type: swipe
    fingers: 4
    direction: left
    speed: slow

    actions:
      - on: begin
        input:
          - keyboard: [ leftalt+leftshift+tab ]

  # Quick window switching (right)
  - type: swipe
    fingers: 4
    direction: right
    speed: slow

    actions:
      - on: begin
        input:
          - keyboard: [ leftalt+tab ]
  ```
</details>
<details>
  <summary>Swipe 4 down - Exit fullscreen/Unmaximize/Minimize</summary>

  ```yaml
  - type: swipe
    fingers: 4
    direction: down

    actions:
      - on: begin
        one:
          - plasma_shortcut: kwin,Window Fullscreen
            conditions:
              - $window_fullscreen == true

          - plasma_shortcut: kwin,Window Maximize
            conditions:
              - $window_maximized == true

          - plasma_shortcut: kwin,Window Minimize
  ```
</details>
<details>
  <summary>Swipe 1 - Move the pointer automatically if the finger is at an edge</summary>

  ```yaml
  - type: swipe
    fingers: 1
    direction: any
    block_events: false

    conditions: $finger_1_initial_position_percentage between 0.2,0.2;0.8,0.8 # prevent accidental activations

    actions:
      - on: tick
        conditions: $finger_1_position_percentage_x <= 0.05

        input:
          - mouse: [ move_by -1 0 ]

      - on: tick
        conditions: $finger_1_position_percentage_x >= 0.95

        input:
          - mouse: [ move_by 1 0 ]

      - on: tick
        conditions: $finger_1_position_percentage_y <= 0.05

        input:
          - mouse: [ move_by 0 -1 ]

      - on: tick
        conditions: $finger_1_position_percentage_y >= 0.95

        input:
          - mouse: [ move_by 0 1 ]
  ```
</details>
<details>
  <summary>Swipe 2 in circular motion - Circular scrolling</summary>

  Place two fingers, with at least one's initial position being the top or bottom edge, then start circling around any point.

  ```yaml
  - type: circle
    fingers: 2
    direction: any

    conditions:
      any:
        - $finger_1_initial_position_percentage_y <= 0.05
        - $finger_2_initial_position_percentage_y <= 0.05
        - $finger_1_initial_position_percentage_y >= 0.95
        - $finger_2_initial_position_percentage_y >= 0.95

    actions:
      - on: update
        interval: -0.5
        input:
          - mouse: [ wheel 0 -1 ]

      - on: update
        interval: 0.5
        input:
          - mouse: [ wheel 0 1 ]
  ```
</details>

From this point onwards triggers will only have placeholder actions.
<details>
  <summary>Tip tap</summary>
  Place one finger in the middle then another one on the left/right. The trigger will not activate if the second finger is removed too quickly.

  ```yaml
  - type: press
    fingers: 2

    conditions:
      - $finger_1_position_percentage_x between 0.4;0.6
      - $finger_2_position_percentage_x < 0.5

    actions:
      - on: begin
        input:
          - keyboard: [ a ]

  - type: press
    fingers: 2

    conditions:
      - $finger_1_position_percentage_x between 0.4;0.6
      - $finger_2_position_percentage_x > 0.5

    actions:
      - on: begin
        input:
          - keyboard: [ b ]
  ```
</details>
<details>
  <summary>Swipe up from bottom edge</summary>

  ```yaml
  - type: swipe
    fingers: 3
    direction: up

    conditions:
      - $finger_1_initial_position_percentage_y >= 0.8

    actions:
      - on: begin
        input:
          - keyboard: [ a ]
  ```
</details>
<details>
  <summary>Swipe 3 right then up (no lifting fingers)</summary>

  ```yaml
  - type: swipe
    fingers: 3
    direction: right
    id: swipe_3_right

  - type: swipe
    fingers: 3
    direction: up

    conditions:
      - $last_trigger_id == swipe_3_right

    actions:
      - on: begin
        input:
          - keyboard: [ a ]
  ```
</details>
