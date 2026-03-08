# Hyprland

## Packages
<details>
  <summary>NixOS (flakes, home-manager)</summary>

  ``flake.nix``:
  ```nix
  {
    inputs = {
      inputactions-ctl = {
        url = "git+https://github.com/InputActions/ctl?submodules=1";
        inputs.nixpkgs.follows = "nixpkgs";
      };
      inputactions-hyprland = {
        url = "git+https://github.com/InputActions/hyprland?submodules=1";
        inputs.nixpkgs.follows = "nixpkgs";
      };
    };
  }
  ```

  ```nix
  {
    home.packages = [
      inputs.inputactions-ctl.packages.${pkgs.system}.default
    ];
    wayland.windowManager.hyprland.plugins = [
      inputs.inputactions-hyprland.packages.${pkgs.system}.default
    ];
  }
  ```
</details>

## Manual (hyprpm)
### Dependencies
<details>
  <summary>Arch Linux</summary>

  ```
  sudo pacman -S --needed base-devel git extra-cmake-modules qt6-tools yaml-cpp libevdev cli11
  ```
</details>

### Installation
First, build the control tool:
```sh
git clone --recursive https://github.com/InputActions/ctl
cd ctl
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
make -j$(nproc)
sudo make install
```

Then, build the Hyprland plugin. Read <https://wiki.hypr.land/Plugins/Using-Plugins> first.

```
hyprpm add https://github.com/InputActions/hyprland
```

## Additional setup (optional)
To enable [extra touchpad features](/devices/touchpad/index.md#evdev-backend), create a file at ``/etc/udev/rules.d/71-touchpad.rules`` with the following content:
```
ENV{ID_INPUT_TOUCHPAD}=="1", TAG+="uaccess"
```

This will give all programs read and write access to all touchpads.