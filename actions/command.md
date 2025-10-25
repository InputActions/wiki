# CommandAction
:::{list-table}
* - **Inherits**
  - [](/actions/index)
:::

## Description
Runs a command in a shell.

[Variables can be used here.](<project:/variables.md#commands>)

## Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - **command**
  - *string*
  - 
  -

* - wait
  - *bool*
  - Whether to wait (up to 30 seconds) for the shell process to exit, no actions will be executed until then.
  - ``false``
:::
