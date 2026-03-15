# ReplaceTextAction
:::{list-table}
* - **Inherits**
  - [](/actions/index)
:::

Replaces text in the currently focused text field.

:::{note}
This action is currently only supported in the compositor plugin implementations and  will only work in programs that support the Text Input Wayland protocol.
:::

## Configuration
### Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type

* - **replace_text**
  - *[](#textsubstitutionrule)*
:::

### TextSubstitutionRule
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - **regex**
  - *regex*
  - Regular expression executed on text **before the cursor, on the same line**.

    On a successful match, the ``match_0``, ``match_1``, ..., ``match_4`` variables are set to groups captured by the expression, where group ``0`` is the
    entire text, and the text is replaced with the value specified in the ``replace`` property.

* - **replace**
  - *string*
  - Text to replace the match with. Accepts dynamic values, evaluated asynchronously.
:::

### Examples
```yaml
replace_text:
  # :calc{2+2} -> 4
  - regex: :calc{(.*)}
    replace:
      command: printf "$(qalc -t "$match_1")"

   # :email -> example@example.com
  - regex: :email
    replace: example@example.com
```

## Description
Set a [can replace text condition](/conditions/can-replace-text.md) on the trigger to ensure it can only be activated if there is something to replace.

```yaml
keyboard:
  gestures:
    - type: shortcut
      shortcut: [ leftctrl, space ]

      conditions:
        - can_replace_text: &text_substitution_rules
            - regex: :calc{(.*)}
              replace:
                command: printf "$(qalc -t "$match_1")"

            - regex: :email
              replace: example@example.com

      actions:
        - replace_text: *text_substitution_rules
```
