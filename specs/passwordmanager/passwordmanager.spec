# $Id$
# Authority: dries
# Upstream: Michael Buesch <mbuesch$freenet,de>
# Screenshot: http://passwordmanager.sourceforge.net/1.png
# ScreenshotURL: http://passwordmanager.sourceforge.net/screenshots.html

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh8:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}
%{?rh6:%define _without_selinux 1}
%{?yd3:%define _without_selinux 1}

%{?fc1:%define _without_kwallet 1}
%{?el3:%define _without_kwallet 1}
%{?rh9:%define _without_kwallet 1}
%{?rh8:%define _without_kwallet 1}
%{?rh7:%define _without_kwallet 1}
%{?el2:%define _without_kwallet 1}
%{?rh6:%define _without_kwallet 1}
%{?yd3:%define _without_kwallet 1}


%define real_version 1.0
%define short_name pwmanager

Summary: Personal password manager
Name: passwordmanager
Version: 1.0.2
Release: 1
License: GPL
Group: Applications/Productivity
URL: http://passwordmanager.sourceforge.net/

Source: http://dl.sf.net/passwordmanager/%{short_name}-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, libart_lgpl-devel, arts-devel, gcc-c++,
BuildRequires: gettext, zlib-devel, qt-devel, 
BuildRequires: libjpeg-devel, kdelibs-devel, bzip2-devel, fam-devel
%{!?_without_selinux:BuildRequires: libselinux-devel}
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
PwManager saves your passwords blowfish-encrypted in one file, so you have
to remember only one master-password instead of all. Instead of the
master-password you can use a chipcard, so you don't have to remember a
password to access the list.

%prep
%setup -n %{short_name}-%{real_version}

%build
source %{_sysconfdir}/profile.d/qt.sh
%configure \
	--x-libraries="%{_prefix}/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source %{_sysconfdir}/profile.d/qt.sh
%makeinstall
%find_lang %{short_name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{short_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/*
%{!?_without_kwallet:%{_datadir}/services/kded/pwmanager_kwalletemu.desktop}
%{_datadir}/applnk/Applications/pwmanager.desktop
%{_datadir}/icons/*/*/apps/pw*.png
%{_datadir}/apps/pwmanager
%{!?_without_kwallet:%{_libdir}/kde3/kded_pwmanager_kwalletemu.*}

%changelog
* Mon Oct 25 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.2-1
- Update to version 1.0.2.

* Mon Sep 01 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Update to version 1.0.1.

* Fri Jul 30 2004 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Update to version 1.0.

* Sun Jul 11 2004 Dag Wieers <dag@wieers.com> - 1.0-0.rc1
- Update to release 1.0rc1.

* Sun Jun 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.0-pre1.1
- Update to version 1.0-pre1.

* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 0.8.1-1
- Update to version 0.8.1.

* Tue Jun 1 2004 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.
