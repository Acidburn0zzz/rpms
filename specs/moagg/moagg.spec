# $Id$
# Authority: dries
# Upstream: <moagg-devel$lists,sourceforge,net>

# Screenshot: http://moagg.sourceforge.net/screenshots/blackhole.png
# ScreenshotURL: http://moagg.sourceforge.net/screenshots.php

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: Mother of all Gravity Games
Name: moagg
Version: 0.13
Release: 1
License: GPL
Group: Amusements/Games
URL: http://moagg.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/moagg/moagg-%{version}-src.tar.bz2
Source1: http://dl.sf.net/moagg/moagg-%{version}-data.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: expat-devel, SDL-devel, SDL_gfx-devel, SDL_mixer-devel 
BuildRequires: paragui-devel, freetype-devel, gcc-c++, SDL_image-devel
BuildRequires: desktop-file-utils, zlib-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: SDL, SDL_gfx, SDL_mixer, paragui, freetype, SDL_image, zlib

%description
Moagg combines several game types of other genres like races, search and
rescue, seek and destroy et cetera into a 2D gravity game. You are pilot of a
small space ship and have to navigate that ship through different levels.
But beside the gravity that drags you down there are other obstacles like
laser ports, magnets, black holes, cannons, rockets and grinders you have to
master.

%prep
%setup -D -b 1

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Moagg
Comment=Mother of all gravity games
Exec=moagg
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Game;X-Red-Hat-Extra;
EOF

%build
%configure \
	--disable-paraguitest
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -Rf %{buildroot}%{_datadir}/doc/moagg

%if %{?_without_freedesktop:1}0
        %{__install} -D -m0644 %{name}.desktop %{buildroot}%{_datadir}/applnk/Games/%{name}.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO doc moagg.dxy 
%{_bindir}/moagg
%{_datadir}/moagg
%{!?_without_freedesktop:%{_datadir}/applications/*.desktop}
%{?_without_freedesktop:%{_datadir}/applnk/Games/*.desktop}
%{_mandir}/man6/moagg*

%changelog
* Wed Jul 28 2004 Dries Verachtert <dries@ulyssis.org> 0.13-1
* Update to version 0.13.

* Mon Jul 12 2004 Dries Verachtert <dries@ulyssis.org> 0.12-1
* Update to version 0.12.

* Fri Jun 25 2004 Dries Verachtert <dries@ulyssis.org> 0.11-1
- Update to version 0.11.

* Fri Jun 4 2004 Dries Verachtert <dries@ulyssis.org> 0.10-1
- Update to version 0.10.

* Mon Apr 26 2004 Dries Verachtert <dries@ulyssis.org> 0.8-1
- Initial package.
