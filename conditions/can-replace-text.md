# CanReplaceTextCondition
:::{list-table}
* - **Inherits**
  - [](/conditions/index)
:::

Checks whether a text subtitution rule can be applied at the time of evaluation. Intended to be used with [](/actions/replace-text) to ensure the trigger can
only be activated if there is something to replace.

## Configuration
### Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - can_replace_text
  - *list([](<project:/actions/replace-text.md#textsubstitutionrule>))*
  - It is recommended to define an anchor here and then reference it in the action.
:::

### Examples
```yaml
conditions:
  - can_replace_text: &text_substitution_rules
      - regex: :email
        replace: example@example.com
```
