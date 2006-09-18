# $Id$
# Authority: matthias

%{?dist: %{expand: %%define %dist 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{!?dist:%define _with_modxorg 1}
%{?fc6:  %define _with_modxorg 1}
%{?fc5:  %define _with_modxorg 1}

Summary: Raw VBI, Teletext and Closed Caption decoding library
Name: zvbi
Version: 0.2.21
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://zapping.sourceforge.net/
Source: http://dl.sf.net/zapping/zvbi-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libpng-devel, gcc-c++, doxygen, gettext
%{?_with_modxorg:BuildRequires: libXt-devel}
%{!?_with_modxorg:BuildRequires: XFree86-devel}
Obsoletes: libzvbi <= 0.2.4

%description
This library provides routines to access raw vbi sampling devices
(currently the V4L and V4L2 API are supported), a versatile raw vbi
bit slicer, decoders for various data services and basic search,
render and export functions for text pages. The library is the
vbi decoding backbone of the Zapping Gnome TV viewer and Zapzilla
Teletext browser. Documentation included.


%package devel
Summary: Static libraries and header files for zvbi development
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig
Obsoletes: libzvbi-devel <= 0.2.4

%description devel
The static libraries and header files needed for building programs that use
the zvbi library.


%prep
%setup


%build
%configure \
    --disable-gtk-doc
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO doc/html
%{_bindir}/zvbi-chains
%{_bindir}/zvbi-ntsc-cc
%{_sbindir}/zvbid
%{_libdir}/*.so.*
%{_mandir}/man1/zvbi-chains.1*
%{_mandir}/man1/zvbi-ntsc-cc.1*
%{_mandir}/man1/zvbid.1*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libzvbi.h
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu May 11 2006 Dag Wieers <dag@wieers.com> - 0.2.21-1
- Updated to release 0.2.21.

* Wed Mar 22 2006 Matthias Saou <http://freshrpms.net/> 0.2.19-2
- Add missing modular X build requirement.
- Try to disable static library, but the build fails, so exclude in %%files.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.2.19-1
- Update to 0.2.19.

* Sun Feb 12 2006 Dag Wieers <dag@wieers.com> - 0.2.18-1
- Updated to release 0.2.18.

* Fri Jan 13 2006 Matthias Saou <http://freshrpms.net/> 0.2.17-1
- Update to 0.2.17.
- Add now zvbi-ntsc-cc binary and man page.
- Add modular xorg build conditional.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 0.2.15-1
- Updated to release 0.2.15.

* Sun Feb 20 2005 Matthias Saou <http://freshrpms.net/> 0.2.13-1
- Update to 0.2.13.
- Added X and libpng build requirements.

* Wed Jan 19 2005 Dag Wieers <dag@wieers.com> - 0.2.12-1
- Updated to release 0.2.12.

* Thu Nov 11 2004 Matthias Saou <http://freshrpms.net/> 0.2.9-1
- Update to 0.2.9.
- Include new binaries, man pages and pkgconfig file.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.2.8-1
- Update to 0.2.8.
- Rebuilt for Fedora Core 2.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.2.5-1
- Update to 0.2.5.
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar 20 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.4.
- Exclude .la file.

* Wed Oct  9 2002 Michael H. Schimek <mschimek@users.sourceforge.net>
- Update to 0.2.2.

* Tue Aug  6 2002 Michael H. Schimek <mschimek@users.sourceforge.net>
- Added %%find_lang for locale support.
- Split with a devel package.
- Disabled gtk-doc since detection works but not build if not in /usr/local.

* Tue Jun  4 2002 Michael H. Schimek <mschimek@users.sourceforge.net>
- Removed libunicode requirement
- Made package relocatable

* Sat Jan 26 2002 Michael H. Schimek <mschimek@users.sourceforge.net>
- Created

