# $Id$
# Authority: dries

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

%define desktop_vendor rpmforge

%define real_version 2.37

Summary: 3D modeling, animation, rendering and post-production
Name: blender
Version: 2.37
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.blender.org/

Source: http://download.blender.org/source/blender-%{real_version}.tar.gz
Source1: blender.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, libjpeg-devel, libpng-devel, glut, python-devel
BuildRequires: openssl-devel, SDL-devel, libvorbis-devel
BuildRequires: libogg-devel, esound-devel, openal-devel, libtool, gettext
BuildRequires: scons, gcc-c++
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
Blender is the essential software solution you need for 3D, from modeling,
animation, rendering and post-production to interactive creation and
playback.

Professionals and novices can easily and inexpensively publish stand-alone,
secure, multi-platform content to the web, CD-ROMs, and other media, whether
they are users of Windows, Linux, Irix, Sun Solaris, FreeBSD or OSX.

%prep
%setup -n %{name}

%{__cat} <<EOF >blender.desktop
[Desktop Entry]
Name=Blender 3D Animations
Comment=Model, animate, render and post-produce 3D animations
Exec=blender -w
Icon=blender.png
Terminal=false
Type=Application
Categories=Application;Graphics;
Encoding=UTF-8
EOF

%build
# blender now works with a new build system, named Scons
sed -i "s/use_openal =.*/use_openal = 'true'/g;" SConstruct
scons clean
scons

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 blender %{buildroot}%{_bindir}/blender
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/blender.png
%{__install} -d %{buildroot}%{_libdir}/blender %{buildroot}%{_libdir}/blender/bpydata/config %{buildroot}%{_libdir}/blender/bpymodules
%{__install} -p -m0644 release/scripts/*.* %{buildroot}%{_libdir}/blender/
%{__install} -p -m0644 release/scripts/bpydata/*.* %{buildroot}%{_libdir}/blender/bpydata/
%{__install} -p -m0644 release/scripts/bpydata/config/*.* %{buildroot}%{_libdir}/blender/bpydata/config/
%{__install} -p -m0644 release/scripts/bpymodules/* %{buildroot}%{_libdir}/blender/bpymodules/



%if %{?_without_freedesktop:1}0
        %{__install} -Dp -m0644 blender.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/blender.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		blender.desktop
%endif

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README doc/* release/text/blender.html release/text/copyright.txt
%doc release/text/Python-license.txt release/text/release_*.txt
%{_bindir}/blender
%{_libdir}/blender
%{_datadir}/pixmaps/blender.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/blender.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-blender.desktop}

%changelog
* Fri Jul 22 2005 Dries Verachtert <dries@ulyssis.org> - 2.37-1
- Updated to release 2.37.

* Thu Dec 23 2004 David Cornette <rpms@davidcornette.com> - 2.36-1
- Updated to release 2.36.
- Also install the python scripts

* Tue Dec 14 2004 Dries Verachtert <dries@ulyssis.org> - 2.35-1
- Updated to release 2.35.

* Fri Sep 03 2004 Dries Verachtert <dries@ulyssis.org> - 2.34-1
- Updated to release 2.34.

* Tue May 25 2004 Dries Verachtert <dries@ulyssis.org> - 2.33-1.a
- use Scons for building

* Sat May 15 2004 Dag Wieers <dag@wieers.com> - 2.33-0.a
- Updated to release 2.30.

* Wed Nov 05 2003 Dag Wieers <dag@wieers.com> - 2.30-0
- Updated to release 2.30.

* Mon Jul 28 2003 Dag Wieers <dag@wieers.com> - 2.28-0
- Updated to release 2.28.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 2.26-0
- Initial package. (using DAR)
