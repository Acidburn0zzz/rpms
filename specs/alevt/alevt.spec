# $Id$
# Authority: dag
# Upstream: Edgar Toernig <froese$gmx,de>

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Teletext/videotext decoder and browser for the bttv driver and X
Name: alevt
Version: 1.6.1
Release: 1.2
License: GPL
Group: Applications/Multimedia
URL: http://www.goron.de/~froese/

Source: http://www.goron.de/~froese/alevt/alevt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
AleVT is a teletext/videotext decoder and browser for the bttv driver
(/dev/vbi) and the X Window System. AleVT features include multiple
windows, a page cache, regexp searching, a built-in manual, and a program
(alevt-date) to get the time from teletext.

%prep
%setup

### FIXME: Make work on 64bit archs. (Please fix upstream)
%ifarch x86_64
%{__perl} -pi.orig -e 's|/usr/X11R6/lib|%{_prefix}/X11R6/%{_lib}|g' Makefile
%endif

%{__cat} <<EOF >alevt.desktop
[Desktop Entry]
Name=AleVT Teletext Decoder
Comment=View Teletext/Videotext information
Icon=alevt.xpm
Exec=alevt
Terminal=false
Type=Application
Categories=GNOME;Application;AudioVideo;
EOF

%build
%{__make} %{?_smp_mflags} \
	OPT="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 alevt %{buildroot}%{_bindir}/alevt
%{__install} -Dp -m0755 alevt-date %{buildroot}%{_bindir}/alevt-date
%{__install} -Dp -m0755 alevt-cap %{buildroot}%{_bindir}/alevt-cap
%{__install} -Dp -m0644 alevt.1x %{buildroot}%{_mandir}/man1/alevt.1x
%{__install} -Dp -m0644 alevt-date.1 %{buildroot}%{_mandir}/man1/alevt-date.1
%{__install} -Dp -m0644 alevt-cap.1 %{buildroot}%{_mandir}/man1/alevt-cap.1
%{__install} -Dp -m0644 contrib/mini-alevt.xpm %{buildroot}%{_datadir}/pixmaps/alevt.xpm

%if %{?_without_freedesktop:1}0
        %{__install} -Dp -m0644 alevt.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/alevt.desktop
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor %{desktop_vendor}    \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                alevt.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYRIGHT README alevt.lsm.in
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_datadir}/pixmaps/alevt.xpm
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/alevt.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-alevt.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.1-1.2
- Rebuild for Fedora Core 5.

* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 1.6.1-1
- Initial package. (using DAR)
