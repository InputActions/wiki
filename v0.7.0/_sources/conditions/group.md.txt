# ConditionGroup
:::{list-table}
* - **Inherits**
  - [](/conditions/index)
:::


## Description
Contains one or more conditions.

## Properties
Group type is determined by the presence of one of the following properties, all of which are mutually exclusive with each other.

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
