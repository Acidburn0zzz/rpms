# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Graphical desktop publishing (DTP) application
Name: scribus
Version: 1.3.3.9
Release: 1
License: GPL
Group: Applications/Productivity
URL: http://web2.altmuehlnet.de/fschmid/

Source: http://dl.sf.net/scribus/scribus-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, python-devel >= 2.3, python >= 2.3
BuildRequires: zlib-devel, libjpeg-devel, libpng-devel, libtiff-devel
BuildRequires: libart_lgpl-devel, gettext, kdelibs-devel
BuildRequires: cups-devel, lcms-devel >= 1.12, libtool, libxml2-devel
BuildRequires: freetype-devel >= 2.1.7, ghostscript >= 7.07, tkinter
%{?!_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Scribus is a GUI desktop publishing (DTP) application for GNU/Linux.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Scribus Desktop Publishing
Comment=%{summary}
Exec=scribus
Icon=scribus.png
Type=Application
Terminal=false
Categories=Application;Office;
Encoding=UTF-8
EOF

%build
source "%{_sysconfdir}/profile.d/qt.sh"
%configure \
	--disable-dependency-tracking \
	--with-xinerama \
	--with-extra-libs=%{_libdir}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0644 scribus/icons/scribusicon.png %{buildroot}%{_datadir}/pixmaps/scribus.png

%if %{?_without_freedesktop:1}0
        %{__install} -Dp -m0644 scribus.desktop %{buildroot}%{_datadir}/gnome/apps/Applications/scribus.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

### Clean up buildroot
# %{__rm} -f %{buildroot}%{_libdir}/scribus/{libs,plugins}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%{_mandir}/man1/scribus*
%{_mandir}/pl/man1/scribus*
%{_bindir}/*
%{_libdir}/scribus/
%{_includedir}/scribus/
%{_datadir}/scribus
%{_datadir}/mime/packages/scribus.xml
%{_datadir}/pixmaps/*
%{?_without_freedesktop:%{_datadir}/gnome/apps/Applications/*.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/*.desktop}

%changelog
* Wed May 09 2007 Dries Verachtert <dries@ulyssis.org> - 1.3.3.9-1
- Updated to release 1.3.3.9.

* Fri Mar 02 2007 Dries Verachtert <dries@ulyssis.org> - 1.3.3.8-1
- Updated to release 1.3.3.8.

* Sat Jan 13 2007 Dries Verachtert <dries@ulyssis.org> - 1.3.3.7-1
- Updated to release 1.3.3.7.

* Sun Jan 07 2007 Dries Verachtert <dries@ulyssis.org> - 1.3.3.6-2
- Also build th python scripts on amd64, thanks to Rohan Walsh.

* Tue Dec 05 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.3.6-1
- Updated to release 1.3.3.6.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.3.5-1
- Updated to release 1.3.3.5.

* Mon Aug 09 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.3.3-1
- Updated to release 1.3.3.3.

* Sun Jan 29 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.2-1
- Updated to release 1.3.2.

* Wed Dec 28 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.1-2
- Fixes in the buildrequirements, thanks to Peter Linell.

* Wed Oct 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.1-1
- Updated to release 1.3.1.

* Wed Sep 14 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.3-1
- Updated to release 1.2.3.

* Wed Jul 06 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.2.1-1
- Updated to release 1.2.2.1.

* Mon Jul 04 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.2-1
- Updated to release 1.2.2.

* Sun Jan 09 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.1-1
- Updated to release 1.2.1.

* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Updated to release 1.2.

* Tue Aug 12 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Updated to release 1.0.1.

* Wed Jul 16 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
