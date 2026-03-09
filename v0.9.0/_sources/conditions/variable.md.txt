# VariableCondition
:::{list-table}
* - **Inherits**
  - [](/conditions/index)
:::

Compares the value of a [variable](/variables) against another value using a specific operator.

## Configuration
Format: ``$variable operator value``

An exclamation mark placed before ``$`` will negate the condition.

``value`` may be one of the following:
- a value of the same type as the variable (automatically converted to lists when necessary, no need to put single values in ``[]``),
- a list of values of the same types as ``variable``, may be empty (``[]``).
- a reference to another variable of the same type as the first one,

For variables of type ``bool``, ``operator`` and ``value`` may be omitted. ``$variable`` and ``!$variable`` conditions are equivalent to ``$variable == true``
and ``$variable == false`` respectively.

### Operators
*T2* must be the same as *T1* unless stated otherwise.

:::{list-table}
:header-rows: 1

* - Operator
  - Variable type (T1)
  - Value type (T2)
  - Description

* - ==
  - all
  -
  - Equal to.

* - !=
  - all
  -
  - Not equal to.

* - one_of
  - all
  - *list(T1)*
  - Whether the variable's value is present in the specified list.

* - \>
  - *number*, *point*
  -
  - Greater than.

* - <
  - *number*, *point*
  -
  - Less than.

* - \>=
  - *number*, *point*
  -
  - Greater than or equal to.

* - <=
  - *number*, *point*
  -
  - Less than or equal to.

* - between
  - *number*, *point*
  -
  - Whether the value fits within the specified range (inclusive).

    Format: ``a;b``

* - contains
  - *flags*, *string*
  -
  - Whether the string value contains the specified string or the flags value contains all of the specified flags.

* - matches
  - *string*
  - *regex*
  - Whether the value matches the specified regular expression.
:::

### Examples
```yaml
$fingers between 3;4 # 3 or 4
```
```yaml
$keyboard_modifiers == [] # no modifiers pressed
```
```yaml
!$keyboard_modifiers contains meta # meta not pressed
```
```yaml
$keyboard_modifiers contains [ ctrl, alt ] # ctrl, alt, and possibly other modifiers pressed
```
```yaml
$window_id == $window_under_pointer_id # pointer is over active window
```
```yaml
$cursor_shape one_of [ default, text ]
```