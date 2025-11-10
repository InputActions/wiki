# Hyprland

## Packages
<details>
  <summary>NixOS (flakes, home-manager)</summary>

``flake.nix``:
  ```nix
  {
    inputs = {
      inputactions = {
        url = "github:taj-ny/InputActions";
        inputs.nixpkgs.follows = "nixpkgs";
        inputs.hyprland.follows = "hyprland"; # Use if hyprland is in inputs too
      };
    };
  }
  ```

  ```nix
  {
    wayland.windowManager.hyprland.plugins = [
      inputs.inputactions.packages.${pkgs.system}.inputactions-hyprland
    ];
  }
  ```
</details>

## hyprpm
### Dependencies
<details>
  <summary>Arch Linux</summary>

  ```
  sudo pacman -S --needed base-devel git extra-cmake-modules qt6-tools yaml-cpp libevdev
  ```
</details>

### Installation
Read <https://wiki.hypr.land/Plugins/Using-Plugins> first.

```
hyprpm add https://github.com/taj-ny/InputActions
```

## Additional setup (optional)
To enable [extra touchpad features](/devices/touchpad/index.md#libevdev-backend), create a file at ``/etc/udev/rules.d/71-touchpad.rules`` with the following content:
```
ENV{ID_INPUT_TOUCHPAD}=="1", TAG+="uaccess"
```

This will give all programs read and write access to all touchpads.