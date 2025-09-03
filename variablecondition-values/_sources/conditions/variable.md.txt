# VariableCondition
:::{list-table}
* - **Inherits**
  - [](/conditions/index)
:::

Variable conditions compare the value of a [variable](/variables) against another value using a specific operator.

Format:
```
[!]$(variable_name) (operator) (value)
```

An exclamation mark placed before ``$`` will negate the condition.

The value can be:
- a value of the same type as ``variable_name`` (automatically converted to lists when necessary, no need to put single values in ``[]``),
- a variable of the same type as ``variable_name``,
- a list of values of the same types as ``variable_name``, may be empty (``[]``).

## Operators
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