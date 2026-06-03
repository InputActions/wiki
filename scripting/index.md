# Scripting
InputActions supports scripting in JavaScript for extending functionality and implementing logic that is difficult or impossible to express in YAML.

:::{note}
Scripting is an experimental feature and breaking changes may be introduced to the API at any time. It is currently not available in the standalone
implementation until [issue 457](https://github.com/taj-ny/InputActions/issues/457) is resolved.
:::

:::{warning}
Scripts are executed on the main thread (in the case of compositor plugin implementations, the compositor's main thread) and as such resource intensive tasks
may result in performance issues like increased input latency and frame rate issues (the latter only applying to compositor plugin implementations).
:::

The JavaScript engine in use is Qt's QJSEngine, which provides the following [objects and functions](https://doc.qt.io/qt-6/qtqml-javascript-functionlist.html).

It is assumed you already know the basics of JavaScript.

## Built-in modules
The InputActions scripting API is divided into modules, which can be imported using the ``require`` global function.

:::{list-table}
:header-rows: 1

* - Module
  - Description

* - [inputactions/core](modules/inputactions/core/index)
  - Core InputActions functionality - input, variables etc.

* - [inputactions/fs](modules/inputactions/fs/index)
  - File system accesss
:::

```js
// import specific elements
const { variableRegistry, Point } = require("inputactions/core");
new Point(1, 1);

// import everything into 'ia'
const ia = require("inputactions/core");
new ia.Point(1, 1);
```

## Main scripts
The main scripts are specified in the ``scripting.scripts`` node. To make variables accessible in actions and conditions, declare them using ``var``.

```yaml
scripting:
  scripts:
    - source: |
        var ia = { variableRegistry, Point } = require("inputactions/core");
```

## Errors
Uncaught errors that occur during initial script evaluation will prevent the configuration from being loaded, while errors that occur after (e.g. during a [](/actions/function)'s function call) will only result in warnings and no notifications. Both may be viewed by running ``inputactions config issues``.

## Object cloning
Custom objects provided by InputActions are not cloned when assigned to variables or passed to functions:
```js
const { Point } = require("inputactions/core");

let p1 = new Point(0, 0);
let p2 = p1;
p1.x = 1;

// p1 and p2 refer to the same object, therefore p2.x == 1 as well
```

For all objects constructible from JavaScript, a ``clone`` method is provided that returns a copy of the object:
```js
const { Point } = require("inputactions/core");

let p1 = new Point(0, 0);
let p2 = p1.clone();
p1.x = 1;

// p2.x is 0
```

Certain objects, such as Point, are always cloned when crossing the C++/JavaScript boundary. As the entirety of the API is implemented in C++, there is no
need to manually clone objects passed to or received from the InputActions API. However, properties of non-primitive types reuse object instances instead of
constructing new ones each time its value is changed:
```js
const { variableRegistry } = require("inputactions/core");

let variable = variableRegistry.variable("finger_1_position_percentage"); // Point
let value1 = variable.value;
// variable value changes here
let value2 = variable.value;

// value1 and value2 refer to the same object, therefore both are the same
```

When storing the values of such properties for later use, it is necessary to clone them:
```js
const { variableRegistry } = require("inputactions/core");

let variable = variableRegistry.variable("finger_1_position_percentage"); // Point
let value1 = variable.value.clone();
// variable value changes here
let value2 = variable.value;

// value1 and value2 do not refer to the same object
```

