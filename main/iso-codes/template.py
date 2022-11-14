pkgname = "iso-codes"
pkgver = "4.12.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["gettext-tiny", "python", "pkgconf"]
pkgdesc = "List of country, language and currency names"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = f"https://salsa.debian.org/iso-codes-team/iso-codes"
source = f"$(DEBIAN_SITE)/main/i/{pkgname}/{pkgname}_{pkgver}.orig.tar.xz"
sha256 = "650f050c3553adbf727e5ac74bd52a04ddc6b9f1bac79f1c041c02e581e209ad"
