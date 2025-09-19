# OneActionGroup
:::{list-table}
* - **Inherits**
  - [](/actions/groups/index)
:::

## Description
Executes only the first action that can be executed.

## Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type

* - **one**
  - *list([](/actions/groups/index))*
:::

## Example
Exit fullscreen if fullscreen, unmaximize if maximized and minimize otherwise.
```yaml
one:
  - plasma_shortcut: kwin,Window Fullscreen
    conditions:
      - $window_fullscreen == true

  - plasma_shortcut: kwin,Window Maximize
    conditions:
      - $window_maximized == true

  - plasma_shortcut: kwin,Window Minimize
```