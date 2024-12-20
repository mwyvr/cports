pkgname = "picom"
pkgver = "12.4"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dunittest=true", "-Dwith_docs=true"]
hostmakedepends = ["asciidoctor", "meson", "pkgconf"]
makedepends = [
    "dbus-devel",
    "libconfig-devel",
    "libepoxy-devel",
    "libev-devel",
    "libx11-devel",
    "libxcb-devel",
    "mesa-devel",
    "pcre2-devel",
    "pixman-devel",
    "uthash",
    "xcb-util-devel",
    "xcb-util-image-devel",
    "xcb-util-renderutil-devel",
]
pkgdesc = "Standalone compositor for X11"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0 AND MIT"
url = "https://github.com/yshui/picom"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d890a5e484d55b2a4e9284161c71c36bcc5acc23bd74eec269d3253e69cb96fa"


def post_install(self):
    self.install_license("COPYING")
    self.install_license("LICENSES/MIT")


@subpackage("picom-devel")
def _(self):
    return self.default_devel()
