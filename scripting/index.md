# Scripting
InputActions supports scripting in JavaScript for extending functionality and implementing logic that is difficult or impossible to express in YAML.

:::{note}
This feature is work in progress and only a very small subset of the scripting API is currently implemented.
:::

## Engine
The JavaScript engine currently in use is Qt's QJSEngine, which implements the ES6 standard, along with some features from later standards, such as the
exponentiation operator (``**``), [nullish coalescing](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing) (``??``)
, [optional chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining) (``?.``) and numeric separators
(``1_000_000``). The ``async`` and ``await`` keywords are not supported, however this issue can be worked around by using TypeScript.

[List of objects and functions provided by QJSEngine](https://doc.qt.io/qt-6/qtqml-javascript-functionlist.html).

## Built-in modules
The scripting API is contained in the following modules:

:::{list-table}
:header-rows: 1

* - Module
  - Description
  - Type definitions file

* - ``inputactions``
  - Various utility functions and classes
  - ``main.d.ts``

* - ``inputactions/core``
  - Core InputActions functionality - config, input, variables etc.
  - ``core.d.ts``

* - ``inputactions/desktop/generic``
  - Desktop environment integration (generic interface for any environment)
  - ``desktop/generic.d.ts``

* - ``inputactions/fs``
  - File system accesss
  - ``fs.d.ts``
:::

The documentation for those modules can be found in the [InputActions/scripting-types](https://github.com/InputActions/scripting-types/tree/main/src)
repository.

## Classic scripts
:::{note}
Prefer [module scripts](#module-scripts) over classic scripts unless the script is short.
:::

Classic scripts can be directly embedded in the configuration. Functions defined using the ``function`` keyword as well as variables defined with ``var`` will
be visible to all other classic scripts evaluated after the declaring script, including those in [](/actions/function) and [](/conditions/function). Scripts are always the first element of the configuration to be loaded, regardless of where the ``scripting`` node is located.

```yaml
scripting:
  scripts:
    - source: |
        var count = 0;
        function incrementCount() {
            count++;
        }

touchpad:
  gestures:
    - type: swipe
      fingers: 3
      direction: any

      actions:
        - on: update
          function: incrementCount

        - on: end
          function: () => console.log(count);
```

To import modules, use the ``require`` global function:
```js
const { Point } = require("inputactions");
new Point(1, 1);

const ia = require("inputactions");
new ia.Point(1, 1);
```

## Module scripts
Module scripts cannot be embedded in the configuration and must be [packaged](#package). In the future it will be possible to install those packages and
import scripts using their IDs.
```yaml
scripting:
  scripts:
    - package: /absolute/path/to/script/package
```

To import modules, use the ``import`` declaration:
```js
import { Point } from "inputactions";
new Point(1, 1);

import * as ia from "inputactions";
new ia.Point(1, 1);
```

If the main module exports a default function, it will be called as soon as the module is loaded with an instance of a ``ModuleScript`` object containing the directory of the script package.
```js
import { ModuleScript } from "inputactions";

export default function(script) {
    // script.packageDirectory
}
```

### Package
A module script package is a directory containing the main module in a ``.js`` file and a ``metadata.yaml`` file with the following properties:
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - **id**
  - *string*
  - Unique identifier of the script in reverse domain name notation.

* - **version**
  - *string*
  - Format: ``major.minor.patch``, for example ``1.0.0``

* - **main_module**
  - *string*
  - Path to the main module relative to the package directory. This is the module that will be imported by InputActions.
:::

Example metadata file:
```yaml
id: com.example.example-script
version: 1.0.0
main_module: main.js
```

## Errors
Uncaught errors thrown during configuration loading will prevent the configuration from being loaded, while errors thrown after the configuration is activated
(e.g. during the execution of a [](/actions/function)) will only result in warnings. Run ``inputactions config issues`` to view them.

## TypeScript
Using TypeScript is strongly recommended due to static typing in addition to the ``async`` and ``await`` keywords. Official TypeScript type declarations can be
found in the [InputActions/scripting-types](https://github.com/InputActions/scripting-types) repository, while the
[InputActions/script-template](https://github.com/InputActions/script-template) repository hosts a script template.

:::{important}
When importing ``.ts`` files from a module, it is required to use the ``.js`` extension, otherwise the import will fail at runtime.
```ts
import * as utils from "./utils.js";

// Incorrect:
import * as utils from "./utils";
import * as utils from "./utils.ts";
```
:::

## Configuration
Scripting is configured in the ``scripting`` [root](/config.md#root) node.

### Scripting
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - scripts
  - *list([](#classicscript) or [](#modulescript))*
  - Loaded in order as specified.
:::

### ClassicScript
See [](#classic-scripts).

:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - **source**
  - *string*
  - The script's source.
:::

### ModuleScript
See [](#module-scripts).

:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - **package**
  - *string*
  - The absolute path to the script [package](#package).
:::