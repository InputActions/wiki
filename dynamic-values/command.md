# Command dynamic value

## Description
Runs the specified command in a shell and returns its standard output once it finishes.

:::{warning}
In synchronous evaluation mode, launching programs that communicate with the compositor will result in a deadlock.
:::

[Variables can be used here.](/variables.md)

## Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type

* - **command**
  - *string*
:::