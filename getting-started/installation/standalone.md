# Standalone
:::{note}
A stable release of this implementation is currently not available.
:::

## Unsupported features
:::{important}
This implementation does not support certain features.
:::

- [](/actions/activate-window)
- [](/actions/replace-text)
- Keyboard text action of [](/actions/input)
- Get the window under fingers on the touchscreen
- Get the cursor shape
- Get the name of the current screen
- Reliable filtering of touchpad input events

Additionally, more features may be unsupported depending on the environment.
<details>
  <summary>GNOME, Plasma</summary>

  No additional features are unsupported in these environments.
</details>
<details>
  <summary>Other (Wayland)</summary>

  - If the compositor does not implement [wlr foreign toplevel management](https://wayland.app/protocols/wlr-foreign-toplevel-management-unstable-v1):
    - Get the active window
  - Get the window under the pointer
  - Get the PID of the active window
</details>
<details>
  <summary>Other (X11)</summary>

  - Get the active window
  - Get the window under the pointer
  - Get the position of the pointer
</details>

There are plans to make most of the aforementioned features implementable using custom scripts, which will be able to use DBus APIs, start proceses and more.

## CMake builds flags
- ``INPUTACTIONS_SYSTEMD`` - enable systemd support, currently only installs the daemon service (default: ON)

## Packages
<details>
  <summary>NixOS (flakes)</summary>

  ```{code-block} nix
  :caption: flake.nix
  {
    inputs = {
      inputactions-ctl = {
        url = "git+https://github.com/InputActions/ctl?submodules=1";
        inputs.nixpkgs.follows = "nixpkgs";
      };
      inputactions-standalone = {
        url = "git+https://github.com/InputActions/standalone?submodules=1";
        inputs.nixpkgs.follows = "nixpkgs";
      };
    };
  }
  ```

  ```{code-block} nix
  :caption: configuration.nix
  { inputs, pkgs, ... }:

  {
    environment.systemPackages = [
      inputs.inputactions-ctl.packages.${pkgs.system}.default
      inputs.inputactions-standalone.packages.${pkgs.system}.default
    ];
    users.groups.inputactions = {};
    security.wrappers.inputactions-client = {
      source = "${inputs.inputactions-standalone.packages.${pkgs.system}.default}/bin/inputactions-client";
      owner = "root";
      group = "inputactions";
      setgid = true;
    };
    systemd = {
      packages = [ inputs.inputactions-standalone.packages.${pkgs.system}.default ];
      services.inputactionsd.wantedBy = [ "multi-user.target" ];
    };
  }
  ```

  Optionally, add the official binary cache if compilation times are an issue:
  ```{code-block} nix
  :caption: configuration.nix
  {
    nix.settings = {
      extra-substituters = ["https://inputactions.cachix.org"];
      extra-trusted-public-keys = ["inputactions.cachix.org-1:yBGhAqTOv0V08lrOTBwMAkU7V/9a0i2UPvsvCu39CjE="];
    };
  }
  ```
</details>


## Manual
### Dependencies
<details>
  <summary>Arch Linux</summary>

  ```
  sudo pacman -S --needed --noconfirm base-devel git extra-cmake-modules qt6-declarative qt6-tools yaml-cpp libevdev cli11
  ```
</details>
<details>
  <summary>Debian-based (KDE Neon, Kubuntu, Ubuntu)</summary>

  ```
  sudo apt install git cmake g++ extra-cmake-modules qt6-declarative-dev qt6-tools-dev gettext libyaml-cpp-dev libxkbcommon-dev pkg-config libevdev-dev libudev-dev libinput-dev libwayland-dev systemd-dev libcli11-dev
  ```
</details>
<details>
  <summary>Fedora</summary>

  ```
  sudo dnf install git cmake extra-cmake-modules gcc-g++ qt6-qtbase-devel qt6-qtbase qt6-qtdeclarative-devel yaml-cpp yaml-cpp-devel libevdev libevdev-devel libinput-devel libudev-devel wayland-devel cli11-devel
  ```
</details>
<details>
  <summary>openSUSE</summary>

  ```
  sudo zypper in git cmake-full gcc-c++ kf6-extra-cmake-modules qt6-declarative-devel "cmake(Qt6Core)" "cmake(Qt6DBus)" "cmake(Qt6Network)" yaml-cpp-devel libevdev-devel libudev-devel libinput-devel wayland-devel libxkbcommon-devel "pkgconfig(systemd)" cli11-devel
  ```
</details>

### Installation
 the ``--standalone-no-systemd`` flag to ``./inputactions-installer.sh`` if not using systemd.

```sh
curl -o inputactions-installer.sh https://raw.githubusercontent.com/InputActions/installer/refs/heads/main/install.sh
chmod +x inputactions-installer.sh
./inputactions-installer.sh --ctl --standalone --latest
```

## Post-installation
:::{warning}
If you have previously installed the compositor plugin, make sure to disable it. There is currently no protection against running it and the standalone version
simultaneously.
:::

1. Enable the daemon (``/usr/bin/inputactionsd``):
   ```
   sudo systemctl enable --now inputactionsd
   ```
2. Add ``inputactions-client`` to autostart. A running client is required in every tty InputActions will be used in.

### GNOME
Enable the ``InputActions`` helper extension (installed automatically after starting the client).

## InputActions setup
By default, devices are not grabbed but their events are processed. Grabbing is required for event filtering. Both properties can be configured using
[device rules](/devices/rule).

```yaml
device_rules:
  - conditions:
      all:
        - any: # remove some conditions if you don't use triggers for a specific device type
          - $keyboard # keyboards must be grabbed for Trigger.clear_modifiers to work
          - $mouse # ungrabbed mice are currently very buggy
          - $touchpad # touchpad event filtering is experimental and may cause issues
          - $touchscreen
        - none: # blacklist
          - $name == Yubico YubiKey OTP+FIDO+CCID
    grab: true
    ignore: false

  - conditions: $types != keyboard
    ignore: true # ignore all devices other than keyboards (required to get modifiers) by default
```

## Virtual devices
Two devices, named ``InputActions Virtual Keyboard`` and ``InputActions Virtual Mouse`` are created for the purpose of generating input events using the
input action. Pointer acceleration should be disabled for ``InputActions Virtual Mouse``.

For each grabbed input device, a pair of virtual devices is created. The first one has the `` (InputActions internal)`` name suffix, is grabbed and only used
internally as a hack for injecting evdev events into libinput. The second one has the `` (InputActions output)`` suffix and is where real and simulated
events are written to.

The output device does not inherit settings from the real device, they must be copied manually.

## Udev rules
Libinput relies on udev environment variables for some features, such as pointer acceleration. These variables are not applied to virtual devices, which can
result in devices changing their behavior after starting InputActions. In that case, udev rules must be created to apply some missing variables.

1. Run ``sudo libinput list-devices`` to get the path of the input device
   ```
   Device:                  Logitech G502 X
   Kernel:                  /dev/input/event15
   ```

2. Run ``udevadm info [path]`` (where ``[path]`` is the value of ``Kernel:`` above). Look for lines that start with ``E:``. Known problematic variables include
   (but are not limited to) the following: ``MOUSE_DPI``.
   ```
   E: MOUSE_DPI=800@1000 1200@1000 *1600@1000 2400@1000 3200@1000
   ```

3. Add the rules to``/etc/udev/rules.d/99-inputactions.rules``. The rule for ``(InputActions internal)`` is optional but recommended.
   ```
   SUBSYSTEM=="input", ATTRS{name}=="Logitech G502 X (InputActions output)", ENV{MOUSE_DPI}="800@1000 1200@1000 *1600@1000 2400@1000 3200@1000"
   SUBSYSTEM=="input", ATTRS{name}=="Logitech G502 X (InputActions internal)", ENV{MOUSE_DPI}="800@1000 1200@1000 *1600@1000 2400@1000 3200@1000"
   ```

4. Reload rules
   ```
   sudo udevadm control --reload-rules
   sudo udevadm trigger
   ```

5. Reload the configuration
   ```
   inputactions config reload
   ```