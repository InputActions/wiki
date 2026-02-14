# ConditionGroup
:::{list-table}
* - **Inherits**
  - [](/conditions/index)
:::

Evaluates a set of conditions in a specific way.

## Configuration
### Properties
The group type is determined by the presence of one of the following properties, all of which are mutually exclusive with each other.

:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - all
  - *list([](/conditions/index))*
  - All conditions must be satisfied.

* - any
  - *list([](/conditions/index))*
  - At least one condition must be satisfied.

* - none
  - *list([](/conditions/index))*
  - No conditions must be satisfied.
:::

### Examples
```yaml
conditions:
  - $window_class == firefox
  - any:
      - $fingers == 3
      - $fingers == 4
```
```yaml
conditions:
  any:
    - $finger_1_initial_position_percentage_y <= 0.05
    - $finger_2_initial_position_percentage_y <= 0.05
```
