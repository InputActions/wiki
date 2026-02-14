# Condition
:::{list-table}
* - **Inherited by**
  - [](/conditions/group), [](/conditions/variable)
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

Variable <variable>
Group <group>
```