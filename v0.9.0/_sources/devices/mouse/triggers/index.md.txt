# MouseTrigger
:::{list-table}
* - **Inherits**
  - [](/trigger)

* - **Inherited by**
  - [](circle), [](press), [](stroke), [](swipe), [](wheel)
:::

Base of all mouse triggers.

## Configuration
### Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description
  - Default

* - mouse_buttons
  - *flags([MouseButton](<project:/devices/mouse/index.md#buttons>))*
  - Mouse buttons that must be pressed in order for the trigger to be activated.
  -

* - mouse_buttons_exact_order
  - *bool*
  - Whether mouse buttons must be pressed in the same order as specified in ``mouse_buttons``.
  - ``false``
:::

```{toctree}
:maxdepth: 1
:hidden:

Circle <circle>
Press <press>
Stroke <stroke>
Swipe <swipe>
Wheel <wheel>
```