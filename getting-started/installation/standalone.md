# Standalone
Works in any environment.

For package maintainers: this is the main version and should be called ``inputactions`` without any ``standalone`` in the name.

## CMake builds flags
- ``INPUTACTIONS_BUILD_STANDALONE`` - build the standalone implementation (default: OFF)
- ``INPUTACTIONS_SYSTEMD`` - enable systemd support, currently only installs the daemon service (default: ON)

## Packages
<details>
  <summary>NixOS (flakes)</summary>

``flake.nix``:
  ```nix
  {
    inputs = {
      nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

      inputactions = {
        url = "github:taj-ny/InputActions";
        inputs.nixpkgs.follows = "nixpkgs";
      };
    };
  }
  ```

  ```nix
  { inputs, pkgs, ... }:

  {
    environment.systemPackages = [
      inputs.inputactions.packages.${pkgs.system}.inputactions
    ];
  }
  ```
</details>


## Manual
### Dependencies
<details>
  <summary>Arch Linux</summary>

  ```
  sudo pacman -S --needed --noconfirm base-devel git extra-cmake-modules qt6-tools yaml-cpp libevdev
  ```
</details>
<details>
  <summary>Debian-based (KDE Neon, Kubuntu, Ubuntu)</summary>

  ```
  sudo apt install git cmake g++ extra-cmake-modules qt6-tools-dev gettext libyaml-cpp-dev libxkbcommon-dev pkg-config libevdev-dev libudev-dev libinput-dev libwayland-dev systemd-dev
  ```
</details>
<details>
  <summary>Fedora</summary>

  ```
  sudo dnf install git cmake extra-cmake-modules gcc-g++ qt6-qtbase-devel qt6-qtbase yaml-cpp yaml-cpp-devel libevdev libevdev-devel libinput-devel libudev-devel wayland-devel
  ```
</details>
<details>
  <summary>openSUSE</summary>

  ```
  sudo zypper in git cmake-full gcc-c++ kf6-extra-cmake-modules "cmake(Qt6Core)" "cmake(Qt6DBus)" "cmake(Qt6Network)" yaml-cpp-devel libevdev-devel libudev-devel libinput-devel wayland-devel libxkbcommon-devel "pkgconfig(systemd)"
  ```
</details>

### Installation
```sh
git clone https://github.com/taj-ny/InputActions
cd InputActions
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DINPUTACTIONS_BUILD_STANDALONE=ON
make -j$(nproc)
sudo make install
```

## Post-installation
1. Enable the daemon (``/usr/bin/inputactionsd``):
   ```
   sudo systemctl enable --now inputactionsd
   ```
2. Add ``/usr/bin/inputactions-client`` to autostart. The client must be started after the session, by the user who owns the session, in an environment where
   it can use KWin's DBus interface (Plasma only) and can connect to the Wayland server (non-GNOME environments). A running client is required in every virtual
   terminal InputActions will be used in.

### GNOME
Enable the ``InputActions`` helper extension (installed automatically after starting the client).

### Plasma
The helper script is loaded and unloaded automatically by the client.

## InputActions setup
By default, devices are not grabbed but their events are processed. Grabbing is required for event filtering. Both properties can be configured using
[device rules](<project:/devices/index.md#devicerule>).

```yaml
device_rules:
  - conditions: 
      all:
        - any: # remove some conditions if you don't use triggers for a specific device type
          - $types contains keyboard # keyboards must be grabbed for Trigger.clear_modifiers to work
          - $types contains mouse # ungrabbed mice are currently very buggy
          - $types contains touchpad # touchpad event filtering is experimental and may cause issues
        - not: # blacklist
          - $name == Yubico YubiKey OTP+FIDO+CCID
    grab: true
    ignore: false

  - conditions: $types != keyboard
    ignore: true # ignore all devices other than keyboards (required to get modifiers) by default
```

## Virtual devices
Two devices, named ``InputActions Virtual Keyboard`` and ``InputActions Virtual Mouse`` are created for the purpose of generating input events using the
input action.

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
   
5. Restart the daemon
   ```
   sudo systemctl restart inputactionsd
   ```