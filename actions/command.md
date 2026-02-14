# CommandAction
:::{list-table}
* - **Inherits**
  - [](/actions/index)
:::

Executes a command in a shell.

## Configuration
### Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - **command**
  - *string*
  - The command to execute. Referenced InputActions variables will be provided as [environment variables](<project:/variables.md#commands>).
  -

* - wait
  - *bool*
  - Whether to wait up to 30 seconds for the shell process to exit.
  - ``false``
:::

### Examples
```yaml
command: kill -9 $window_pid
```