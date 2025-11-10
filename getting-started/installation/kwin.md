# KWin
:::{important}
It is necessary to restart KWin after updating the plugin, otherwise the newer version will not be loaded and the old one will be used instead.
:::

The minimum Plasma version is 6.3, for older versions use InputActions v0.8.0.

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
      inputs.inputactions.packages.${pkgs.system}.inputactions-kwin
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
  sudo pacman -S --needed base-devel git extra-cmake-modules qt6-tools kwin yaml-cpp libevdev
  ```
</details>
<details>
  <summary>Debian-based (KDE Neon, Kubuntu, Ubuntu)</summary>

  ```
  sudo apt install git cmake g++ extra-cmake-modules qt6-tools-dev kwin-wayland kwin-dev libkf6configwidgets-dev gettext libkf6kcmutils-dev libyaml-cpp-dev libxkbcommon-dev pkg-config libevdev-dev libdrm-dev
  ```
</details>
<details>
  <summary>Fedora 40 - 42</summary>

  ```
  sudo dnf install git cmake extra-cmake-modules gcc-g++ qt6-qtbase-devel kwin-devel kf6-ki18n-devel kf6-kguiaddons-devel kf6-kcmutils-devel kf6-kconfigwidgets-devel qt6-qtbase kf6-kguiaddons kf6-ki18n wayland-devel yaml-cpp yaml-cpp-devel libepoxy-devel libevdev libevdev-devel libdrm-devel
  ```
</details>
<details>
  <summary>openSUSE</summary>

  ```
  sudo zypper in git cmake-full gcc-c++ kf6-extra-cmake-modules kf6-kguiaddons-devel kf6-kconfigwidgets-devel kf6-ki18n-devel kf6-kcmutils-devel "cmake(KF6I18n)" "cmake(KF6KCMUtils)" "cmake(KF6WindowSystem)" "cmake(Qt6Core)" "cmake(Qt6DBus)" "cmake(Qt6Quick)" "cmake(Qt6Widgets)" libepoxy-devel kwin6-devel yaml-cpp-devel libxkbcommon-devel libevdev-devel
  ```
</details>

### Installation
```sh
git clone https://github.com/taj-ny/InputActions
cd InputActions
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DINPUTACTIONS_BUILD_KWIN=ON
make -j$(nproc)
sudo make install
```

### Installation (Fedora immutable)
Build the plugin in a container. The image's KWin version must be the same as the one on your real system.

```sh
# enter container
sudo dnf install git cmake extra-cmake-modules gcc-g++ qt6-qtbase-devel kwin-devel kf6-ki18n-devel kf6-kguiaddons-devel kf6-kcmutils-devel kf6-kconfigwidgets-devel qt6-qtbase kf6-kguiaddons kf6-ki18n wayland-devel yaml-cpp yaml-cpp-devel libepoxy-devel libevdev libevdev-devel libdrm-devel rpmbuild
git clone https://github.com/taj-ny/InputActions
cd InputActions
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DINPUTACTIONS_BUILD_KWIN=ON
make -j$(nproc)
cpack -V -G RPM
exit # exit container
sudo rpm-ostree install InputActions/build/inputactions.rpm
```

## After installation
To enable the plugin, run 
```sh
qdbus6 org.kde.KWin /Effects org.kde.kwin.Effects.loadEffect kwin_gestures
```
or open the ``Desktop Effects`` page in ``System Settings`` and enable ``InputActions`` in the ``Tools`` category.

To rebuild, run ``make clean`` in the project directory and then all command starting from ``cd build``.

## Additional setup (optional)
To enable [extra touchpad features](/devices/touchpad/index.md#libevdev-backend), create a file at ``/etc/udev/rules.d/71-touchpad.rules`` with the following content:
```
ENV{ID_INPUT_TOUCHPAD}=="1", TAG+="uaccess"
```

This will give all programs read and write access to all touchpads.