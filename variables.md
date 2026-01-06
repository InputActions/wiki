# Variables
Variables are currently only used in conditions and cannot be created by users.

:::{list-table}
:header-rows: 1

* - **Name**
  - Type
  - Description

* - cursor_shape
  - *enum(alias, all_scroll, col_resize, copy, crosshair, default, e_resize, ew_resize, grab, grabbing, help, move, n_resize, ne_resize, nesw_resize, not_allowed, ns_resize, nw_resize, nwse_resize, pointer, progress, row_resize, s_resize, se_resize, sw_resize, text, up_arrow, w_resize, wait)*
  - Requires the application to use the cursor shape protocol. Will work in Qt 6 applications, may work in GTK applications, will not work in Qt 5 applications.

    See table at <https://developer.mozilla.org/en-US/docs/Web/CSS/cursor#syntax> for preview.

* - finger_{1..5}_initial_position_percentage
  - *point*
  - The initial position of the finger. This variable should be preferred over ``finger_{1..5}_position_percentage`` for swipe from edge triggers.

* - finger_{1..5}_position_percentage
  - *point*
  - Absolute current position of the finger as a percentage. Ranges from ``0.0`` to ``1.0``.

* - finger_{1..5}_pressure
  - *number*
  - 

* - fingers
  - *number*
  - Amount of fingers currently on the input device.

    Does not change thorough the trigger.

* - keyboard_modifiers
  - *flags(alt, ctrl, meta, shift)*
  - Currently pressed keyboard modifiers.

    Does not change thorough the trigger.

* - last_trigger_id
  - *string*
  - ID (*[](/trigger).id*) of the last trigger that was updated or ended.

* - plasma_overview_active
  - *bool*
  - Whether Plasma's overview is active.

* - pointer_position_screen_percentage
  - *point*
  - Pointer position relative to the top-left corner of the screen it is currently on as a percentage.

* - pointer_position_window_percentage
  - *point*
  - Pointer position relative to the top-left corner of the window it is currently hovering over as a percentage.

* - screen_name
  - *string*
  - Name of the currently active screen.

* - thumb_present
  - *bool*
  - Whether a thumb is currently present on the input device.

* - thumb_initial_position_percentage
  - *point*
  - See ``finger_{1..5}_initial_position_percentage``.

* - thumb_position_percentage
  - *point*
  - See ``finger_{1..5}_position_percentage``.

* - time_since_last_trigger
  - *time*
  - Time in milliseconds since ``last_trigger_id`` was set.

* - window_class<br>
    window_under_fingers_class<br>
    window_under_pointer_class
  - *string*
  - The window's resource class.

* - window_fullscreen<br>
    window_under_fingers_fullscreen<br>
    window_under_pointer_fullscreen
  - *bool*
  - Whether the window is fullscreen.

* - window_id<br>
    window_under_fingers_id<br>
    window_under_pointer_id
  - *string*
  - The window's identifier.

* - window_maximized<br>
    window_under_fingers_maximized<br>
    window_under_pointer_maximized
  - *bool*
  - Whether the window is maximized.

* - window_name<br>
    window_under_fingers_name<br>
    window_under_pointer_name
  - *string*
  - The window's resource name.

* - window_title<br>
    window_under_fingers_title<br>
    window_under_pointer_title
  - *string*
  - The window's title.
:::

All variables of the *point* type have variants with the ``_x`` and ``_y`` suffixes that return the X and Y values respectively.

``window_`` variables refer to the active window, ``window_under_pointer_`` - window under the cursor and ``window_under_fingers_`` - window under the finger
placed on a touchscreen (in case of multiple fingers, under the center).

## Commands
Variables can be referenced in commands (``$name``) and will be provided as environment variables if the value is not null. For boolean variables, the value
of the environment variable will be ``1`` if ``true``, and will not be set at all if ``false``.

## Listing variables
Some information that the user may need during configuration is exposed through variables. Run ``inputactions variables list`` to list all
variables and their current values, can be combined with ``watch -n [time] [command]`` to update automatically.
