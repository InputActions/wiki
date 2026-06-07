# Dynamic values
Certain properties accept dynamic values if explicitly stated in its description. Those are evaluated every time the value is accessed.

Dynamic values are evaluated either synchronously or asynchronously. Synchronous evaluation is used when the value must be known immediately and may freeze
the main process if it takes too long. Asynchronous evaluation will never freeze the main process but can delay actions.

To assign an [InputActions variable](/variables) to a property, set it to ``$variable_name``.

## Example
```yaml
property1: value # static value
property2:
  command: echo -n value # dynamic command value
property3: $window_id # variable
```

```{toctree}
:hidden:

Command <command>
```