# $Id$
# Authority: matthias

%define desktop_vendor rpmforge
%define cvs -cvs

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_alsa 1}
%{?el3:%define _without_alsa 1}
%{?rh9:%define _without_alsa 1}
%{?rh8:%define _without_alsa 1}
%{?rh7:%define _without_alsa 1}
%{?el2:%define _without_alsa 1}
%{?rh6:%define _without_alsa 1}
%{?yd3:%define _without_alsa 1}

%ifarch x86_64
%define _without_mmx 1
%endif

Summary: DVD player that supports DVD menus
Name: ogle
Version: 0.9.2
Release: 4
License: GPL
Group: Applications/Multimedia
URL: http://www.dtek.chalmers.se/groups/dvd/
Source0: http://www.dtek.chalmers.se/groups/dvd/dist/ogle-%{version}%{?cvs}.tar.gz
Source1: bluecurve-xine.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: XFree86-devel
BuildRequires: libdvdread-devel >= 0.9.4, libjpeg-devel, a52dec-devel >= 0.7.3
BuildRequires: libxml2-devel >= 2.4.19, libmad-devel, gcc-c++
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_alsa:BuildRequires: alsa-lib-devel}

%description
Ogle is a DVD player. It's features are: Supports DVD menus and navigation,
reads encrypted and unencrypted DVDs using libdvdread/libdvdcss, normal X11
and XFree86 Xvideo display support with subpicture overlay, audio and
subpicture selection, advanced subpicture commands such as fade/scroll and
wipe, detects and uses correct aspect for movie and menus, playing AC3 via
S/PDIF with an external command, fullscreen mode, screenshots with and
without subpicture overlay...

Available rpmbuild rebuild options :
--without : alsa freedesktop altivec


%package devel
Summary: Header files and static libraries from the Ogle DVD player
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: libdvdread-devel >= 0.9.4, libxml2-devel >= 2.4.19

%description devel
These are the header files and static libraries from Ogle that are needed
to build programs that use it (like GUIs).


%prep
%setup -n %{name}-%{version}%{?cvs}
### Workaround the hardcoded "lib" path for dvdread (vs. lib64)... doesn't work
%{__perl} -pi.orig -e '
		s|/lib\b|/%{_lib}|g;
		s|-ldvdread\b|-ldl -ldvdread|g;
	' configure*


%build
%configure \
    %{?_without_altivec:--disable-altivec} \
    %{?_without_mmx:--disable-mmx}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
# Needed for library dependencies (still current in 0.9.2)
export LIBRARY_PATH=%{buildroot}/usr/lib/ogle
%{__make} DESTDIR=%{buildroot} install
%{__install} -Dp -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/ogle.png

# Change the ALSA default to OSS if we have --without alsa
%{?_without_alsa:%{__perl} -pi -e 's|<driver>alsa</driver>|<driver>oss</driver>|g' %{buildroot}%{_datadir}/ogle/oglerc}

%{__cat} > ogle.desktop << EOF
[Desktop Entry]
Name=DVD Player
Comment=Play video DVDs with full menu support
Exec=ogle
Icon=ogle.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=X-Red-Hat-Base;Application;AudioVideo;
EOF

%if %{!?_without_freedesktop:1}0
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    ogle.desktop
%else
%{__install} -Dp -m 0644 ogle.desktop \
    %{buildroot}/etc/X11/applnk/Multimedia/ogle.desktop
%endif


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig
# If the /dev/dvd link doesn't exist, create a default one
test -e /dev/dvd || test -L /dev/dvd || ln -s cdrom /dev/dvd || :

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README
%{_bindir}/*
%dir %{_libdir}/ogle/
%{_libdir}/ogle/*.so.*
%{_libdir}/ogle/ogle_*
%{_mandir}/man?/*
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-ogle.desktop}
%dir %{_datadir}/ogle/
%config %{_datadir}/ogle/oglerc
%{_datadir}/ogle/ogle_conf.dtd
%{_datadir}/pixmaps/ogle.png
%{?_without_freedesktop:/etc/X11/applnk/Multimedia/ogle.desktop}

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ogle/
%dir %{_libdir}/ogle/
%{_libdir}/ogle/*.so
%exclude %{_libdir}/ogle/*.la
%{_libdir}/ogle/*.a


%changelog
* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 0.9.2-4
- Updated to latest available CVS snapshot to fix FC3 build failure.

* Mon Aug  3 2004 Matthias Saou <http://freshrpms.net/> 0.9.2-3
- Added patch for proper ALSA detection.
- Cosmetic changes.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.9.2-2
- Rebuild for Fedora Core 2.
- Minor spec updates.

* Thu Nov  6 2003 Matthias Saou <http://freshrpms.net/> 0.9.2-1
- Update to 0.9.2.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 0.9.1-7
- Rebuild for Fedora Core 1.

* Fri Sep 19 2003 Matthias Saou <http://freshrpms.net/>
- Update to today's CVS snapshot that will become 0.9.2.
- Change build dep from libmad to libmad-devel.

* Wed May 14 2003 Matthias Saou <http://freshrpms.net/>
- Added --without altivec build option for ppc < G4 users.

* Mon Apr 14 2003 Matthias Saou <http://freshrpms.net/>
- Added libdvdread and libxml devel deps.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Sat Mar 15 2003 Matthias Saou <http://freshrpms.net/>
- Add freedesktop build option.

* Tue Mar 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.1.

* Tue Feb 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0.

* Sun Feb 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to CVS version, "release imminent" :-)

* Fri Oct  4 2002 Matthias Saou <http://freshrpms.net/>
- Moved the /dev/dvd link creation to the %%post script.
- Enabled ALSA by default in the build, but OSS as default in the config
  unless rebuilt with --with alsadefaultdriver.

* Fri Sep 27 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- Added the new desktop entry to this main ogle package, it makes more sense.
- Shameless ripoff of the cool BlueCurve Xine icon for the menu entry.
- Added default /dev/dvd -> cdrom symlink.

* Fri Aug 30 2002 Matthias Saou <http://freshrpms.net/>
- Now build with support for ALSA by default.
- Updated description and URLs.

* Tue Aug  6 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.5.

* Mon Jul  1 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.4.

* Wed Jun 12 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.3.
- Spec file cleanup and inclusion of the Ogle team changes (Bj�rn & Martin).

* Wed May 15 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 7.3 (added a workaround for libxml2).
- Added the %%{?_smp_mflags} expansion.

* Tue Mar 19 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.2 current CVS version.

* Sat Dec  8 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.2.

* Sun Nov  4 2001 Matthias Saou <http://freshrpms.net/>
- Added an ugly hack to prevent the need to build the package twice to
  have it work done correctly.

* Wed Oct 31 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup and fixes.

* Fri Oct 26 2001 Martin Norb�ck <d95mback@dtek.chalmers.se>
- Updated version to 0.8.1
* Thu Oct 11 2001 Martin Norb�ck <d95mback@dtek.chalmers.se>
- Updated version to 0.8.0
* Thu Sep 20 2001 Martin Norb�ck <d95mback@dtek.chalmers.se>
- Added missing .la files
* Thu Sep 20 2001 Martin Norb�ck <d95mback@dtek.chalmers.se>
- Updated version to 0.7.5
- Split into normal and devel package
* Thu Sep 6 2001 Martin Norb�ck <d95mback@dtek.chalmers.se>
- Updated version to 0.7.4
* Fri Aug 10 2001 Martin Norb�ck <d95mback@dtek.chalmers.se>
- Updated version to 0.7.2
* Sun Jul 22 2001 Martin Norb�ck <d95mback@dtek.chalmers.se>
- initial version
