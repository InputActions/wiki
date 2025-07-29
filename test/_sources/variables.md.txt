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

* - finger_{1..5}_position_percentage
  - *point*
  - Absolute position of the finger as a percentage.

* - finger_{1..5}_pressure
  - *number*
  - 

* - fingers
  - *number*
  - Amount of fingers currently on the input device.

    Does not change thorough the gesture.

* - keyboard_modifiers
  - *flags(alt, ctrl, meta, shift)*
  - Currently pressed keyboard modifiers.

    Does not change thorough the gesture.

* - last_trigger_id
  - *string*
  - ID (*Gesture.id*) of the last trigger that was updated or ended.

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

* - thumb_position_percentage
  - *point*
  - Position of the thumb (if present) as a percentage.

* - window{_under}_class
  - *string*
  - The window's resource class.

* - window{_under}_fullscreen
  - *bool*
  - Whether the window is fullscreen.

* - window{_under}_id
  - *string*
  - The window's identifier.

* - window{_under}_maximized
  - *bool*
  - Whether the active window is maximized.

* - window{_under}_name
  - *string*
  - The window's resource name.

* - window{_under}_title
  - *string*
  - 
:::

All variables of the *point* type have variants with the ``_x`` and ``_y`` suffixes that return the X and Y values respectively.

``window_`` variables have ``window_under_`` variants that return information about the window the pointer is hovering over.

## Expansion
String, bool, number variables can be referenced (``$name``) in command actions and will be replaced. Expansion currently cannot be prevented.

## Listing variables
Some information that the user may need during configuration is exposed through variables. Run ``qdbus org.inputactions / variables`` to list all
variables and their current values, can be combined with ``watch -n [time] [command]`` to update automatically.
