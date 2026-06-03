# Condition
:::{list-table}
* - **Inherited by**
  - [](/conditions/function), [](/conditions/group), [](/conditions/variable)
:::

## Configuration
A property of the condition type may either be a single value or a list (equivalent to an ``all`` [condition group](/conditions/group)).

### Examples
```yaml
conditions: $fingers == 3
```
```yaml
conditions:
  - $fingers == 3
```

```{toctree}
:hidden:

Function <function>
Group <group>
Variable <variable>
```