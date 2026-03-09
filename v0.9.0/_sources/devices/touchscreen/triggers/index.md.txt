# TouchscreenTrigger
:::{list-table}
* - **Inherits**
  - [](/trigger)

* - **Inherited by**
  - [](circle), [](hold), [](pinch), [](rotate), [](stroke), [](swipe), [](tap)
:::

Base of all touchscreen triggers.

## Configuration
### Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - fingers
  - *uint*
  - How many fingers must be present on the input device.

    Equivalent to a ``$fingers == [value]`` condition.
:::

```{toctree}
:maxdepth: 1
:hidden:

Circle <circle>
Hold <hold>
Pinch <pinch>
Rotate <rotate>
Stroke <stroke>
Swipe <swipe>
Tap <tap>
```