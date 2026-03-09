# KWin
:::{important}
It is necessary to restart KWin after updating the plugin, otherwise the newer version will not be loaded and the old one will be used instead.
:::

The minimum Plasma version is 6.3, for older versions use InputActions v0.8.0. If a new feature requires additional changes to work on older versions, it will
likely be made available only on the latest one.

## Packages
<details>
  <summary>Arch Linux (AUR)*</summary>

  :::{important}
  Choose ``cleanBuild`` when reinstalling the package.
  :::

  <https://aur.archlinux.org/packages/inputactions-kwin>
  ```
  yay -S inputactions-kwin
  ```
</details>
<details>
  <summary>NixOS (flakes)</summary>

  ``flake.nix``:
  ```nix
  {
    inputs = {
      inputactions-ctl = {
        url = "git+https://github.com/InputActions/ctl?submodules=1";
        inputs.nixpkgs.follows = "nixpkgs";
      };
      inputactions-kwin = {
        url = "git+https://github.com/InputActions/kwin?submodules=1";
        inputs.nixpkgs.follows = "nixpkgs";
      };
    };
  }
  ```

  ```nix
  { inputs, pkgs, ... }:

  {
    environment.systemPackages = [
      inputs.inputactions-ctl.packages.${pkgs.system}.default
      inputs.inputactions-kwin.packages.${pkgs.system}.default
    ];
  }
  ```
</details>

**\* Unofficial package, use at your own risk.**

## Manual
### Dependencies
<details>
  <summary>Arch Linux</summary>

  ```
  sudo pacman -S --needed base-devel git extra-cmake-modules qt6-tools kwin yaml-cpp libevdev cli11
  ```
</details>
<details>
  <summary>Debian-based (KDE Neon, Kubuntu, Ubuntu)</summary>

  ```
  sudo apt install git cmake g++ extra-cmake-modules qt6-tools-dev kwin-wayland kwin-dev libkf6configwidgets-dev gettext libkf6kcmutils-dev libyaml-cpp-dev libxkbcommon-dev pkg-config libevdev-dev libdrm-dev libcli11-dev
  ```
</details>
<details>
  <summary>Fedora</summary>

  ```
  sudo dnf install git cmake extra-cmake-modules gcc-g++ qt6-qtbase-devel kwin-devel kf6-ki18n-devel kf6-kguiaddons-devel kf6-kcmutils-devel kf6-kconfigwidgets-devel qt6-qtbase kf6-kguiaddons kf6-ki18n wayland-devel yaml-cpp yaml-cpp-devel libepoxy-devel libevdev libevdev-devel libdrm-devel cli11-devel
  ```
</details>
<details>
  <summary>openSUSE</summary>

  ```
  sudo zypper in git cmake-full gcc-c++ kf6-extra-cmake-modules kf6-kguiaddons-devel kf6-kconfigwidgets-devel kf6-ki18n-devel kf6-kcmutils-devel "cmake(KF6I18n)" "cmake(KF6KCMUtils)" "cmake(KF6WindowSystem)" "cmake(Qt6Core)" "cmake(Qt6DBus)" "cmake(Qt6Quick)" "cmake(Qt6Widgets)" libepoxy-devel kwin6-devel yaml-cpp-devel libxkbcommon-devel libevdev-devel cli11-devel
  ```
</details>

### Installation
```sh
curl -o inputactions-installer.sh https://raw.githubusercontent.com/taj-ny/InputActions/refs/heads/main/install.sh
chmod +x inputactions-installer.sh
./inputactions-installer.sh --ctl --kwin --latest
```

### Installation (Fedora immutable)
Build the plugin in a container. The image's KWin version must be the same as the one on your real system.

```sh
# enter container
sudo dnf install git cmake extra-cmake-modules gcc-g++ qt6-qtbase-devel kwin-devel kf6-ki18n-devel kf6-kguiaddons-devel kf6-kcmutils-devel kf6-kconfigwidgets-devel qt6-qtbase kf6-kguiaddons kf6-ki18n wayland-devel yaml-cpp yaml-cpp-devel libepoxy-devel libevdev libevdev-devel libdrm-devel cli11-devel rpmbuild
curl -o inputactions-installer.sh https://raw.githubusercontent.com/taj-ny/InputActions/refs/heads/main/install.sh
chmod +x inputactions-installer.sh
./inputactions-installer.sh --ctl --kwin -p RPM --latest
exit # exit container

installer_dir="${XDG_DATA_HOME:-$HOME/.local/share}/inputactions-installer"
sudo rpm-ostree install "$installer_dir/inputactions-ctl.rpm" "$installer_dir/inputactions-kwin.rpm"
```

## After installation
To enable the plugin, run
```sh
qdbus6 org.kde.KWin /Effects org.kde.kwin.Effects.loadEffect kwin_gestures
```
or open the ``Desktop Effects`` page in ``System Settings`` and enable ``InputActions`` in the ``Tools`` category.

If the plugin ever causes the compositor to crash repeatedly, making it impossible to disable it, remove ``kwin_gesturesEnabled=true`` from
``~/.config/kwinrc``.

## Additional setup (optional)
To enable [extra touchpad features](/devices/touchpad/index.md#evdev-backend), create a file at ``/etc/udev/rules.d/71-touchpad.rules`` with the following content:
```
ENV{ID_INPUT_TOUCHPAD}=="1", TAG+="uaccess"
```

This will give all programs read and write access to all touchpads.