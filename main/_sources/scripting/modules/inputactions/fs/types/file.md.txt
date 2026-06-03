# File
## Overview
### Static methods
:::{list-table}
* - *Promise(string)*
  - [readAllTextAsync](#sm-readAllTextAsync)(*string* path)

* - *Promise(void)*
  - [writeAllTextAsync](#sm-writeAllTextAsync)(*string* path, *string* text)
:::

## Details
### Static methods
(sm-readAllTextAsync)=
#### *Promise(string)* readAllTextAsync(*string* path)
<hr>

Returns: a promise that is fulfilled with the file's text contents on success, and rejected with an error on failure.

(sm-writeAllTextAsync)=
#### *Promise(void)* writeAllTextAsync(*string* path, *string* text)
<hr>

If the file does not exist, it is created. If it already exists, its contents are overwritten.

Returns: a promise that is fulfilled on success, and rejected with an error on failure.

## Example
```js
const { File } = require("inputactions/fs");

File.writeAllTextAsync("/tmp/test", "test")
    .then(() => console.log("success"))
    .catch(error => console.error(error));
```