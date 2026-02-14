# OneActionGroup
:::{list-table}
* - **Inherits**
  - [](/actions/groups/index)
:::

Executes only the first action that can be executed.

## Configuration
### Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type

* - **one**
  - *list([](/actions/index))*
:::

### Examples
Exit fullscreen if fullscreen, unmaximize if maximized and minimize otherwise.
```yaml
one:
  - plasma_shortcut: kwin,Window Fullscreen
    conditions: $window_fullscreen

  - plasma_shortcut: kwin,Window Maximize
    conditions: $window_maximized

  - plasma_shortcut: kwin,Window Minimize
```