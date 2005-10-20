# $Id$
# Authority: dag
# Upstream: Gerd Knorr <kraxel$bytesex,org>

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Television application for video4linux compliant devices
Name: xawtv
Version: 3.94
Release: 2
License: GPL
Group: Applications/Multimedia
URL: http://bytesex.org/xawtv/

Source: http://dl.bytesex.org/releases/xawtv/xawtv-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: XFree86-devel, ncurses-devel, Xaw3d-devel, libjpeg-devel
BuildRequires: zvbi-devel
%{!?rh62:BuildRequires: openmotif-devel}
%{?rh62:BuildRequires: Mesa-devel}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
#BuildRequires: libdv-devel, libquicktime-devel

%description
Xawtv is a simple xaw-based TV program which uses the bttv driver or
video4linux. Xawtv contains various command-line utilities for
grabbing images and .avi movies, for tuning in to TV stations, etc.
Xawtv also includes a grabber driver for vic.

%prep
%setup

%{__perl} -pi.orig -e 's| -o root||' Makefile.in

%{__cat} <<EOF >xawtv.desktop
[Desktop Entry]
Name=Xawtv Television Viewer
Comment=Watch television on your computer
Icon=gnome-multimedia.png
Exec=xawtv
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF

%build
### FIXME: Work-around for buildproblems with rpm configure macro (can't find the problem) Not related to optflags, _target_platform, CFLAGS (Builds fine on rh62 though)
%configure
#./configure --prefix="%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
### On RH62 it fails because %{buildroot}%{_bindir} does not exist. (Fix upstream please)
%{__install} -d -m0755 %{buildroot}%{_bindir}
%makeinstall \
	DESTDIR="%{buildroot}" \
	libdir="%{buildroot}%{_libdir}/xawtv" \
	datadir="%{buildroot}%{_datadir}/xawtv"

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 xawtv.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/xawtv.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		xawtv.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes contrib/frequencies* COPYING README* TODO
%doc %{_mandir}/man?/*
%doc %{_mandir}/*/man?/*
%{_bindir}/*
%{_libdir}/xawtv/
%{_datadir}/xawtv/
%{_prefix}/X11R6/lib/X11/app-defaults/*
%{!?rh62:%{_prefix}/X11R6/lib/X11/*/app-defaults/*}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/xawtv.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-xawtv.desktop}

%changelog
* Wed Feb 09 2005 Dag Wieers <dag@wieers.com> - 3.94-2
- Added zvbi-devel build requirement. (Klaus-Peter Schrage)
- Rebuild with zvbi-support.

* Sun Aug 29 2004 Dag Wieers <dag@wieers.com> - 3.94-1
- Updated to release 3.94.

* Mon Apr 26 2004 Dag Wieers <dag@wieers.com> - 3.92-1
- Updated to release 3.92.

* Sat Apr 11 2004 Dag Wieers <dag@wieers.com> - 3.91-1
- Rebuild against libdv 0.102.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 3.91-0
- Updated to release 3.91.

* Thu Dec 04 2003 Dag Wieers <dag@wieers.com> - 3.90-1
- Added desktop file. (Alfredo Milani-Comparetti)

* Tue Oct 21 2003 Dag Wieers <dag@wieers.com> - 3.90-0
- Updated to release 3.90.

* Thu May 01 2003 Dag Wieers <dag@wieers.com> - 3.88-0
- Updated to release 3.88.

* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 3.86-0
- Updated to release 3.86.

* Sun Jan 05 2003 Dag Wieers <dag@wieers.com> - 3.82-0
- Initial package. (using DAR)
