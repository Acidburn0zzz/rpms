# $Id$
# Authority: dries
# Screenshot: http://widelands.sourceforge.net/images/screens/build-6/00.jpg
# ScreenshotURL: http://widelands.sourceforge.net/screenshots.html

Summary: Game like Settlers II
Name: widelands
Version: b9
Release: 1
License: GPL
Group: Amusements/Games
URL: http://widelands.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source: http://dl.sf.net/widelands/widelands-%{version}-source.tar.bz2
Source1: http://dl.sf.net/widelands/widelands-%{version}-linux.tar.bz2
BuildRequires: SDL-devel, make, gcc-c++, SDL_image-devel, SDL_ttf-devel
Requires: SDL

%description
In Widelands, you are the regent of a small tribe. You start out with
nothing but your headquarters, a kind of castle in which all your resources
are stored. Every member of your tribe will do his or her part to produce
more resources - wood, food, iron, gold and more - to further this growth.
But you are not alone in the world, and you will meet other tribes sooner or
later. Some of them may be friendly and trade with you. However, if you want
to rule the world, you will have to train soldiers and fight.
 
%prep
%setup -b 1 -n widelands

%build
%{__rm} -f widelands
%{__make} %{?_smp_mflags}
%{__mv} widelands widelands.orig
(echo "#!/bin/bash";echo "cd /usr/share/widelands";echo "./widelands") > widelands
%{__chmod} +x widelands

cat > widelands.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Encoding=UTF-8
Name=Widelands
Exec=/usr/bin/widelands
Categories=Application;Game;ArcadeGame
EOF

%install
%{__rm} -rf %{buildroot}
export DESTDIR=%{buildroot}
%{__install} -d %{buildroot}%{_datadir}/widelands
%{__install} -d %{buildroot}%{_bindir}
%{__install} -d %{buildroot}%{_datadir}/applications

%{__install} -s -m 755 widelands.orig %{buildroot}%{_datadir}/widelands/widelands
%{__install} -m 755 widelands %{buildroot}%{_bindir}/widelands
%{__cp} -r fonts maps pics tribes worlds %{buildroot}%{_datadir}/widelands/
%{__cp} widelands.desktop %{buildroot}%{_datadir}/applications/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README COPYING AUTHORS
%{_bindir}/widelands
%{_datadir}/widelands
%{_datadir}/applications/widelands.desktop

%changelog
* Tue Jan 11 2005 Dries Verachtert <dries@ulyssis.org> b9-1
- Updated to release b9.

* Fri Nov 26 2004 Dries Verachtert <dries@ulyssis.org> b8-1
- Update to release b8.

* Fri Jan 02 2004 Dries Verachtert <dries@ulyssis.org> b6-2
- added a desktop icon

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> b6-1
- first packaging for Fedora Core 1
