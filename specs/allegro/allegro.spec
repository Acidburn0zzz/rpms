# $Id$
# Authority: dries
# Upstream: Shawn Hargreaves <shawn$talula,demon,co,uk>

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: Game library
Name: allegro
Version: 4.2.0
Release: 1
License: Distributable
Group: Development/Libraries
URL: http://alleg.sourceforge.net/

Source: http://dl.sf.net/alleg/allegro-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes: allegro-tools

BuildRequires: gcc-c++, esound-devel, arts-devel, pkgconfig, texinfo
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
Allegro is a multi-platform game library for C/C++ developers that provides
many functions for graphics, sounds, player input (keyboard, mouse, and
joystick), and timers. It also provides fixed and floating point mathematical
functions, 3D functions, file management functions, compressed datafile, and
a GUI.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} docs-dvi

%install
%{__rm} -rf %{buildroot}
%makeinstall install-gzipped-man install-gzipped-info
%{__rm} -f %{buildroot}%{_datadir}/info/dir

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS THANKS
%doc %{_mandir}/man3/*
%{_datadir}/info/allegro*
%{_bindir}/allegro-config
%{_bindir}/colormap
%{_bindir}/dat
%{_bindir}/dat2c
%{_bindir}/dat2s
%{_bindir}/exedat
%{_bindir}/grabber
%{_bindir}/pack
%{_bindir}/pat2dat
%{_bindir}/rgbmap
%{_bindir}/textconv
%{_libdir}/liballeg*.so.*
%{_libdir}/allegro/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/allegro.h
%{_includedir}/linalleg.h
%{_includedir}/xalleg.h
%{_includedir}/allegro/
%{_libdir}/liballeg_unsharable.a
%{_libdir}/liballeg*.so
%{_datadir}/aclocal/allegro.m4

%changelog
* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org> - 4.2.0-1
- Initial package.
