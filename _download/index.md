---
title: Download
permalink: /download/
currentver: 0.1.019
---

{% assign currentver = page.currentver %}

# Current Release (v{{ currentver }}) - [Release Info](https://git.zrythm.org/zrythm/zrythm/releases)

#### Download package for...
[Ubuntu](#ubuntu) [Debian](#debian) [Arch](#arch) [Fedora](#fedora) [openSUSE](#opensuse)

## Ubuntu
```bash
# Ubuntu 18.10
wget https://download.opensuse.org/repositories/home:/alextee/xUbuntu_18.10/amd64/zrythm_{{ currentver }}-1_amd64.deb
sudo apt install ./zrythm_{{ currentver }}-1_amd64.deb
rm zrythm_{{ currentver }}-1_amd64.deb

# Ubuntu 18.04
wget https://download.opensuse.org/repositories/home:/alextee/xUbuntu_18.04/amd64/zrythm_{{ currentver }}-1_amd64.deb
sudo apt install ./zrythm_{{ currentver }}-1_amd64.deb
rm zrythm_{{ currentver }}-1_amd64.deb

# Note: does not work on older versions
```
#### Repositories
[Ubuntu 18.10](https://download.opensuse.org/repositories/home:/alextee/xUbuntu_18.10/)
[Ubuntu 18.04](https://download.opensuse.org/repositories/home:/alextee/xUbuntu_18.04/)

## Debian
```bash
# Debian 10 (buster)
wget https://download.opensuse.org/repositories/home:/alextee/Debian_Testing/amd64/zrythm_{{ currentver }}-1_amd64.deb
sudo apt install ./zrythm_{{ currentver }}-1_amd64.deb
rm zrythm_{{ currentver }}-1_amd64.deb

# Note: does not work on older versions
```
#### Repositories
[Debian 10](https://download.opensuse.org/repositories/home:/alextee/Debian_Testing/)

## Arch
```bash
# == Release version ==
wget https://download.opensuse.org/repositories/home:/alextee/Arch/x86_64/zrythm-{{ currentver }}-1-x86_64.pkg.tar.xz
sudo pacman -U zrythm-{{ currentver }}-1-x86_64.pkg.tar.xz
rm zrythm-{{ currentver }}-1-x86_64.pkg.tar.xz

# == AUR version ==
# for latest release ({{ currentver }})
yaourt -S zrythm # replace yaourt with your AUR-compatible equivalent

# for git version
yaourt -S zrythm-git
```
#### Repositories
[Arch](https://download.opensuse.org/repositories/home:/alextee/Arch/)

## Fedora
```bash
# Fedora 27
wget https://download.opensuse.org/repositories/home:/alextee/Fedora_27/x86_64/zrythm-{{ currentver }}-13.1.x86_64.rpm
sudo dnf install zrythm-{{ currentver }}-2.1.x86_64
rm zrythm-{{ currentver }}-13.1.x86_64

# Fedora 28
wget https://download.opensuse.org/repositories/home:/alextee/Fedora_28/x86_64/zrythm-{{ currentver }}-13.1.x86_64.rpm
sudo dnf install zrythm-{{ currentver }}-2.1.x86_64
rm zrythm-{{ currentver }}-13.1.x86_64

# Fedora 29
wget https://download.opensuse.org/repositories/home:/alextee/Fedora_29/x86_64/zrythm-{{ currentver }}-13.1.x86_64.rpm
sudo dnf install zrythm-{{ currentver }}-2.1.x86_64
rm zrythm-{{ currentver }}-13.1.x86_64

# Fedora Rawhide
wget https://download.opensuse.org/repositories/home:/alextee/Fedora_Rawhide/x86_64/zrythm-{{ currentver }}-13.1.x86_64.rpm
sudo dnf install zrythm-{{ currentver }}-2.1.x86_64
rm zrythm-{{ currentver }}-13.1.x86_64
```
#### Repositories
[Fedora 28](https://download.opensuse.org/repositories/home:/alextee/Fedora_28/)
[Fedora 29](https://download.opensuse.org/repositories/home:/alextee/Fedora_29/)
[Fedora Rawhide](https://download.opensuse.org/repositories/home:/alextee/Fedora_Rawhide/)

## openSUSE
Coming soon
