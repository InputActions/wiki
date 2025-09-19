# YAML Anchors
Anchors can be used to reduce duplication.

``&name`` - Define (can be done anywhere) <br>
``*name`` - Reference (must be defined first above the reference)

The merge operator ``<<`` is not supported.

## Example

```yaml
_anchors: # Call this whatever you want but prefix it with _ so it does not conflict with anything in the future
  - &touchpad_interval_p 75
  - &touchpad_interval_n -75
  
touchpad:
  gestures:
    - type: swipe
      direction: up
      threshold: &touchpad_swipe_threshold 100 # This will work too

      actions:
        - on: update
          interval: *touchpad_interval_n
          # ...
          
        - on: update
          interval: *touchpad_interval_p
          # ...
```