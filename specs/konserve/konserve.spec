# $Id$
# Authority: dries

# Screenshot: http://konserve.sourceforge.net/konserve-screenshot424.png
# ScreenshotURL: http://konserve.sourceforge.net/screens.html

# ExcludeDist: el3 fc1

Summary: Small backup application
Name: konserve
Version: 0.10.3
Release: 1
License: GPL
Group: Applications/Archiving
URL: http://konserve.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source: http://dl.sf.net/konserve/konserve-%{version}.tar.bz2
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++
BuildRequires: XFree86-devel, qt-devel
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}
Requires: kdelibs

%description
Konserve is a small backup application for the KDE 3.x environment. It lives
in the system tray and is able to create backups of several directories or
files periodically.

Konserve uses standard KDE network transparency to upload your backups to
wherever you want (for example a ftp server). It is also possible to restore
an incidently deleted file or directory from a backup file with just one
mouse click.

A wizard helps you with the first steps in using Konserve.

%prep
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README AUTHORS COPYING TODO
%{_bindir}/konserve
%{_datadir}/applnk/Applications/konserve.desktop
%{_datadir}/apps/konserve/tips
%{_datadir}/doc/HTML/en/konserve
%{_datadir}/icons/*/*/apps/konserve.png

%changelog
* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> 0.10.3
- update to 0.10.3 for fc2

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 0.9-1
- first packaging for Fedora Core 1
