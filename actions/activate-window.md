# ActivateWindow
:::{list-table}
* - **Inherits**
  - [](/actions/index)
:::

Activates a window and sets the ``previous_window_id`` variable to the ID of the previously active window. Certain actions, such as [](/actions/input) may not
function properly without a short delay after window activation.

:::{note}
This action is currently only supported in the compositor plugin implementations.
:::

## Configuration
### Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - **activate_window**
  - *string*
  - ID of the window to activate. Accepts dynamic values, evaluated synchronously.
:::

### Examples
```yaml
activate_window: $window_under_pointer_id
```
```yaml
actions: # actions of a trigger
  - activate_window: $window_under_pointer_id
  # ...
  # perform some actions on the window
  # ...
  - activate_window: $previous_window_id # Restore the previous window
```

## See also
- [](/common-patterns)