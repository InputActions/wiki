# Documentation
Make sure to select the right version above the file list or *main* if using the main branch. 

[Configuration](configuration.md)<br>
[Example gestures](example_gestures.md)<br>
[Variables](variables.md)

# Listing variables
Some information that the user may need during configuration is exposed through variables. Run ``watch -n .1 qdbus org.inputactions / variables`` to list all
variables and their current values (updates every 100 ms).

# Gestures
## Lifecycle
- activate - If a gesture's activation conditions are satisfied, it is added to the list of active gestures and can receive update events. If one of the activated gestures has set speed, all of them will only receive events after it is determined (*Speed.events*)
- begin - A gesture usually begins on the first update event, but that can be delayed or prevented entirely by thresholds.
- update - Before the gesture receives an update event, its update conditions (direction) are checked first. If not satisfied, the gesture is cancelled.
- end - The gesture has ended and end conditions have been satisfied.
- cancel - The gesture's update conditions were not satisfied, the finger count has changed (touchpad), or there is a gesture conflict (see section below). Cancel actions are only executed if the gesture had begun.

## Conflict resolution
All active gestures receive events. This can lead to them conflicting with each other. To prevent this, all other gestures are cancelled immediately when:
- a gesture is updated, and has any action that had been executed, or has an update action that can be executed but hasn't been yet (interval not reached)
- a gesture ends, and has an end action that can be executed
- a stroke gesture is active (in this case only swipe gestures are cancelled)

Gestures receive update events in order as specified in the configuration file.

In the following example, it is not necessary to set ``speed: slow`` on *Gesture 2* anymore, because when the action of *Gesture 1* is executed, *Gesture 2* will be cancelled immediately.
```yaml
# Gesture 1
- type: swipe
  direction: right
  speed: fast
  
  actions:
    - on: begin
      # ...

# Gesture 2
- type: swipe
  direction: right

  actions:
    - on: begin
      # ...
```

## Swipe gestures
Swipe gestures are limited to 4 directions. The direction is determined during the first few input events, which allows for executing actions at all points of the gesture's lifecycle.

Swipe gestures are currently not compatible with stroke gestures.

## Stroke gestures
Stroke gestures allow you to draw any shape. The performed stroke is compared against all gestures and the one with the highest match (must be ≥70%) is ended, while all others are cancelled. 

Strokes can be recorded using the stroke recorder at *System Settings* -> *Desktop Effects* -> *Input Actions (configure)* or DBus: ``qdbus org.inputactions / recordStroke``.

Only *end* actions are supported.

## Time-based gestures
Motionless gestures are based on time and update every *5 ms* with a delta of *5*.

# Input
Input events are generated and blocked at compositor level. Programs that read from /dev/input may not function as expected.

# Devices
## Mouse
Mouse gestures are only supported on Plasma 6.3

Supported gesture types: *press*, *stroke*, *swipe*, *wheel*

### Press gestures
Mouse press gestures do not start immediately by default, allowing swipe gestures or normal clicks to be performed. 

If this behavior is not desired, *PressGesture.instant* should be set to true. The property is set per-gesture, but affects all activated press gestures.

### Wheel gestures
Wheel gestures can have two different lifecycles - if the gesture has an ``on: update`` action and a mouse button or modifier is present, the gesture begins on
the first scroll event and ends when a modifier/button is released, otherwise it begins and ends on the same scroll event. 

### Distinguishing between normal clicks and press/swipe gestures
When a mouse button is pressed, the event is blocked and the plugin gives the user 200 ms to perform any mouse movement. After that period, a press gesture is started, however if none were activated, all previously blocked buttons are pressed.

## Touchpad
Supported gesture types: *click*, *pinch*, *press*, *rotate*, *stroke*, *swipe*

### Acceleration
KWin only provides unaccelerated deltas for both scroll and swipe events.

### libevdev backend
The libevdev backend enables click gestures, finger position variables, finger pressure variables and thumb variables.

[Setup instructions](https://github.com/taj-ny/InputActions#additional-setup-optional)

#### Click gestures
Available on buttonpads only (touchpads that do not have separate physical buttons below and instead act as one button).

#### Pressure
On most devices the pressure is the area covered by the finger. Few devices provide true pressure.

#### Thumb detection
Input Actions can detect whether a thumb is present on the touchpad based on the pressure range manually specified by the user.
See *[Device](configuration.md#device)*.

### Five-finger gestures
[Libinput does not support five-finger gestures](https://gitlab.freedesktop.org/libinput/libinput/-/issues/763), click gestures are an exception, as they are
managed by Input Actions.

### Pinch gesture recognition issues
Libinput is terrible at recognizing pinch gestures.

### Press (hold) gestures
Single- and two-finger press gestures begin almost immediately. Three- and four-finger gestures have a significant delay added by libinput that may make those
gestures annoying to use.

### Two-finger swipe/stroke gestures
Two-finger swipe gestures are achieved by treating scroll events as motion events. The thresholds for changing the scroll axis are quite large, which can cause 
problems with stroke gestures and ``direction: any`` swipe gestures utilizing the ``move_by_delta`` mouse input action. For two-finger stroke gestures it is 
recommended (but not required) to only use strokes that have been recorded using two fingers.

This feature will not work if scrolling on edges is enabled.