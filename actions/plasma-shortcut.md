# PlasmaShortcutAction
:::{list-table}
* - **Inherits**
  - [](/actions/index)

* - **Supported environments**
  - Plasma
:::

## Description
Invokes a Plasma global shortcut.

To view all shortcuts, open ``~/.config/kglobalshortcutsrc``. The text inside brackets is the component, and text before ``=`` is the shortcut.

For components such as ``[services][org.kde.dolphin.desktop]``, omit ``[services]``, replace ``.``, ``-`` and possibly some other characters with ``_``. The
component of that example would be ``org_kde_dolphin_desktop``.

You can also run ``qdbus6 org.kde.kglobalaccel | grep /component`` to list all components and
``qdbus6 org.kde.kglobalaccel /component/[replace this with the component] org.kde.kglobalaccel.Component.shortcutNames`` to list all shortcuts.

## Properties
:::{list-table}
:header-rows: 1

* - Property
  - Type
  - Description

* - **plasma_shortcut**
  - *string*
  - Format: ``component,shortcut``
:::

## Example
```yaml
plasma_shortcut: kwin,Window Close
```