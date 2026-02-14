# DeviceRule
Applies a set properties to all devices that satisfy the rule's conditions.

## Configuration
### Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - conditions
  - *[](/conditions/index)*
  - Must be satisfied in order for the rule to be applied.
:::

All properties of the rule other then the ones listed above are device properties that the rule will apply.

### Examples
```yaml
device_rules:
  - conditions:
      any:
        - $name == Synaptics TM3276-02
        - $name contains Logitech
    ignore: false # don't ignore this device, overrides the rule below

  - conditions: $types contains mouse
    press_timeout: 300
    unblock_buttons_on_timeout: false

  - ignore: true # ignore all devices by default
```

## Conditions
Device rule conditions use a separate set of variables that describe the device for which a rule is currently being evaluated. Global variables are not
accessible here.

:::{list-table}
:header-rows: 1

* - Name
  - Type
  - Description

* - name
  - *string*
  -

* - types
  - *flags(keyboard, mouse, touchpad)*
  - Certain devices may have multiple types (e.g. mouse and keyboard).
:::