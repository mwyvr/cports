pkgname = "plasma-activities-stats"
pkgver = "6.3.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "kconfig-devel",
    "plasma-activities-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Library to access KDE activity manager statistics data"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-activities-stats"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-activities-stats-{pkgver}.tar.xz"
sha256 = "c801901c62144f30ecd7e4f7b17bc8e05a45ab1cb3d808c8d0a1d569f012b5a6"
hardening = ["vis"]


@subpackage("plasma-activities-stats-devel")
def _(self):
    return self.default_devel()
