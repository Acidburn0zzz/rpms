# $Id$
# Authority: dag
# Upstream: <cairo$cairographics,org>

### EL5 ships with version 1.2.4-1.fc6
# ExclusiveDist: el2 rh7 rh9 el3 el4

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_modxorg 1}
%{?fc7:  %define _with_modxorg 1}
%{?el5:  %define _with_modxorg 1}
%{?fc6:  %define _with_modxorg 1}
%{?fc5:  %define _with_modxorg 1}

%{?rh9:%define _without_directfb 1}
%{?rh7:%define _without_directfb 1}
%{?el2:%define _without_directfb 1}

%{?rh7:%define _without_fontconfig 1}
%{?el2:%define _without_fontconfig 1}

%{?rh7:%define _without_pkgconfig 1}

Summary: Anti-aliased vector-based rendering for X
Name: cairo
Version: 1.2.4
Release: 1
License: MIT
Group: System Environment/Libraries
URL: http://cairo.freedesktop.org/

Source: http://cairo.freedesktop.org/snapshots/cairo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, freetype-devel, libpixman-devel
BuildRequires: libpng-devel, gcc-c++
%{!?_without_directfb:BuildRequires: directfb-devel >= 0.9.24}
%{!?_without_fontconfig:BuildRequires: fontconfig-devel}
#BuildRequires: glitz-devel, libxcb-devel
%{?_with_modxorg:BuildRequires: libX11-devel}
%{!?_with_modxorg:BuildRequires: XFree86-devel}

%description
Cairo provides anti-aliased vector-based rendering for X. Paths consist
of line segments and cubic splines and can be rendered at any width with
various join and cap styles. All colors may be specified with optional
translucence (opacity/alpha) and combined using the extended Porter/Duff
compositing algebra as found in the X Render Extension.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libpixman-devel, XFree86-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%{?_without_pkgconfig:export png_CFLAGS="$(libpng-config --cflags)"}
%{?_without_pkgconfig:export png_LIBS="$(libpng-config --libs)"}
%{?_without_pkgconfig:export png_REQUIRES=" "}

%configure \
%{!?_without_directfb:--enable-directfb}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libcairo.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/cairo/
%{_includedir}/cairo/
%{_libdir}/libcairo.a
%exclude %{_libdir}/libcairo.la
%{_libdir}/libcairo.so
%{_libdir}/pkgconfig/cairo.pc
%{_libdir}/pkgconfig/cairo-*.pc

%changelog
* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 0.2.0-1
- Updated to release 0.2.0.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.1.23-1
- Updated to release 0.1.23.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.1.18-0
- Initial package. (using DAR)
