# Condition
:::{list-table}
* - **Inherited by**
  - [](/conditions/group), [](/conditions/variable)
:::

:::{important}
Legacy conditions from versions below v0.6.0 are deprecated and will be removed in v0.9.0.
:::

## Example
```yaml
conditions:
  - any:
    - $fingers between 3;4
    - $keyboard_modifiers == [] # No modifiers must be pressed
  - !$keyboard_modifiers contains meta # Any modifiers are allowed as long as meta isn't one of them
  - !$window_class one_of [ Terraria.bin.x86_64, some, other, blacklisted, games ]
  - $pointer_position_window_percentage_x < 0.5 # Left side
  - $pointer_position_screen_percentage >= 0.99;0.99 # Bottom-right corner
  - $pointer_position_window_percentage between 0.4,0.4;0.6,0.6 # Middle
  - $cursor_shape != text
```

```{toctree}
:hidden:

Variable <variable>
Group <group>
```