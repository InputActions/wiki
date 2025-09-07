# Dynamic values
Some properties accept dynamic values if explicitly stated in the description. They are useful if you need the value to be evaluated every time.

The property will also state whether the value will be evaluated synchronously or asynchronously. Synchronous evaluation is used when the value must be known
immediately and may freeze the compositor if it takes too long. Asynchronous evaluation will never freeze the compositor but can delay actions.

## Example
```yaml
property1: value # static value
property2:
  command: echo -n value # dynamic value
```

```{toctree}
:hidden:

Command <command>
```