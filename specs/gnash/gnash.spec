# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?el5:%define _with_modxorg 1}
%{?fc6:%define _with_modxorg 1}
%{?fc5:%define _with_modxorg 1}

%{?fc1:%define _without_kde32 1}
%{?el3:%define _without_kde32 1}
%{?rh9:%define _without_kde32 1}
%{?rh7:%define _without_kde32 1}
%{?el2:%define _without_kde32 1}

#ifarch x86_64
#define _without_kde32 1
#endif

Summary: Flash player
Name: gnash
Version: 0.8.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.gnu.org/software/gnash/

Source: http://ftp.gnu.org/gnu/gnash/%{version}/gnash-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires: SDL-devel, libxml2-devel, SDL_mixer-devel, boost-devel
BuildRequires: libpng-devel, libmad-devel, libogg-devel, gcc-c++
BuildRequires: atk-devel, autotrace, agg-devel
%{!?_without_kde32:BuildRequires: kdebase-devel >= 3.2}
%{?_with_modxorg:BuildRequires: libGLU-devel, libXmu-devel, libXi-devel}
%{!?_with_modxorg:BuildRequires: XFree86-devel}

%description
Gnash is an open-source flash player.

%package -n konqueror-gnash
Summary: Konqueror plugin for playing Flash movies
Group: Applications/Multimedia
Requires: gnash = %{version}-%{release}
Requires: kdebase-core

%description -n konqueror-gnash
Konqueror plugin for playing Flash movies

%package -n mozilla-gnash
Summary: Mozilla plugin for playing Flash movies
Group: Applications/Multimedia
Requires: gnash = %{version}-%{release}

%description -n mozilla-gnash
Firefox plugin for playing Flash movies

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g;' configure

%build
#./autogen.sh
source %{_sysconfdir}/profile.d/qt.sh
%configure \
	--disable-ghelp \
	--disable-docbook \
	--disable-rpath \
	--disable-static \
	--enable-dom \
	--enable-glext \
	--enable-http \
	--enable-jpeg \
%{!?_without_kde32:--enable-klash} \
%{?_without_kde32:--disable-klash} \
	--enable-mp3 \
	--enable-net-conn \
	--enable-ogg \
	--enable-plugin \
	--enable-pthreads \
	--enable-png \
	--enable-xmlreader \
	--with-plugindir="%{_libdir}/mozilla/plugins"
#	--with-qtdir="$QTDIR"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source %{_sysconfdir}/profile.d/qt.sh
%{__install} -d -m0755 %{buildroot}%{_libdir}/mozilla/plugins/
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS TODO
%doc %{_mandir}/man1/gnash.1*
%{_bindir}/gnash
%{_bindir}/gtk-gnash
%{_bindir}/kde-gnash
%{_bindir}/gparser
%{_bindir}/gprocessor
%{_datadir}/gnash/
%{_libdir}/gnash/libgnashamf*.so*
%{_libdir}/gnash/libgnashbackend*.so*
%{_libdir}/gnash/libgnashbase*.so*
%{_libdir}/gnash/libgnashgeo*.so*
%{_libdir}/gnash/libgnashserver*.so*
%exclude %{_libdir}/gnash/libgnashamf.la
%exclude %{_libdir}/gnash/libgnashbackend.la
%exclude %{_libdir}/gnash/libgnashbase.la
%exclude %{_libdir}/gnash/libgnashgeo.la
%exclude %{_libdir}/gnash/libgnashserver.la

%if %{!?_without_kde32:1}0
%files -n konqueror-gnash
%defattr(-, root, root, 0755)
#%config %{_datadir}/config/klashrc
#%{_bindir}/klash
%{_datadir}/apps/klash
%{_datadir}/services/klash_part.desktop
%{_libdir}/kde3/libklashpart.la
%{_libdir}/kde3/libklashpart.so
%endif

%files -n mozilla-gnash
%defattr(-, root, root, 0755)
#%{_libdir}/libmozsdk.so*
%dir %{_libdir}/mozilla/
%{_libdir}/mozilla/plugins/

%changelog
* Mon Sep 24 2007 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.

* Sun Jun 10 2007 Dag Wieers <dag@wieers.com> - 0.8.0-1
- Updated to release 0.8.0.

* Mon Jan 15 2007 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Updated to release 0.7.2.

* Thu May 11 2006 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Initial package (using DAR)
