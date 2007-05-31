# $Id$
# Authority: dag
# Upstream: Dan Dennedy <ddennedy$users,sf,net>

%{?dist: %{expand: %%define %dist 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{!?dist:%define _with_modxorg 1}
%{?el5:  %define _with_modxorg 1}
%{?fc7:  %define _with_modxorg 1}
%{?fc6:  %define _with_modxorg 1}
%{?fc5:  %define _with_modxorg 1}

%{?el4: %define _without_libiec61883 1}
%{?el3: %define _without_libiec61883 1}
%{?rh9: %define _without_libiec61883 1}
%{?rh7: %define _without_libiec61883 1}
%{?el2: %define _without_libiec61883 1}

Summary: Simple non-linear video editor
Name: kino
Version: 1.0.0
Release: 3
License: GPL
Group: Applications/Multimedia
URL: http://www.kinodv.org/
Source: http://downloads.sf.net/kino/kino-%{version}.tar.gz
Patch0: kino-1.0.0-install.patch
Patch1: kino-1.0.0-udev-rules.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gtk2 >= 2.6
Requires: mjpegtools
%{?_with_extffmpeg:Requires: ffmpeg}
BuildRequires: libdv-devel >= 0.102
BuildRequires: libavc1394-devel, libraw1394-devel
BuildRequires: libogg-devel, libvorbis-devel, a52dec-devel
BuildRequires: gtk2-devel >= 2.6, libglade2-devel >= 2.5, gettext
BuildRequires: libxml2-devel, libsamplerate-devel, intltool
%{?_with_modxorg:BuildRequires: libXt-devel, libXv-devel}
# libtool *sigh*
BuildRequires: gcc-c++
%{!?_without_libiec61883:BuildRequires: libiec61883-devel}
%{!?_without_quicktime:BuildRequires: libquicktime-devel}
%{?_with_extffmpeg:BuildRequires: ffmpeg-devel}
Obsoletes: kino-devel <= %{version}
Obsoletes: kino-dvtitler <= 0.2.0-2

%description
The new generation of digital camcorders use the Digital Video (DV) data
format. Kino allows you to record, create, edit, and play movies recorded
with DV camcorders. Unlike other editors, this program uses many keyboard
commands for fast navigating and editing inside the movie.


%prep
%setup
%patch0 -p1 -b .install
%patch1 -p1 -b .udev-rules


%build
%configure \
    --disable-static \
    %{!?_without_quicktime:--enable-quicktime} \
    %{?_without_libiec61883:--with-dv1394} \
    %{?_with_extffmpeg:--enable-local-ffmpeg="no"}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall 
%find_lang %{name}
# Move plugins back where they belong (new in 0.8.0)
%{__mkdir_p} %{buildroot}%{_libdir}/kino-gtk2/
%{__mv} %{buildroot}%{_libdir}/*.* %{buildroot}%{_libdir}/kino-gtk2/

### Clean up buildroot (conflicts with ffmpeg package)
%{__rm} -f %{buildroot}%{_mandir}/man1/ffmpeg.1*


%post
update-mime-database %{_datadir}/mime &>/dev/null || :

%postun
update-mime-database %{_datadir}/mime &>/dev/null || :


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README*
%config %{_sysconfdir}/udev/rules.d/kino.rules
%{_bindir}/*
%{_includedir}/kino/
%dir %{_libdir}/kino-gtk2/
%{_libdir}/kino-gtk2/*.so*
%exclude %{_libdir}/kino-gtk2/*.la
%{_datadir}/applications/Kino.desktop
%{_datadir}/kino/
%{_datadir}/mime/packages/kino.xml
%{_datadir}/pixmaps/kino.png
%{_mandir}/man1/*


%changelog
* Thu May 31 2007 Matthias Saou <http://freshrpms.net/> 1.0.0-3
- Include udev-rules patch to fix udev warnings on boot.

* Thu Mar 29 2007 Dag Wieers <dag@wieers.com> - 1.0.0-2
- Remove ffmpeg.1 manpage as it conflicts with ffmpeg package.

* Mon Mar 26 2007 Matthias Saou <http://freshrpms.net/> 1.0.0-1
- Update to 1.0.0.
- Use the internal ffmpeg snapshot, make _with_extffmpeg a build time option.
- Remove no longer shipped hotplug files, replace with new udev rules file.
- Include patch to fix absolute (DESTDIR + bindir) symlink.

* Tue Jan 16 2007 Matthias Saou <http://freshrpms.net/> 0.9.5-1
- Update to 0.9.5.

* Mon Dec 18 2006 Matthias Saou <http://freshrpms.net/> 0.9.3-2
- Rebuild against new ffmpeg snapshot (libavformat.so bump).

* Tue Nov 21 2006 Matthias Saou <http://freshrpms.net/> 0.9.3-1
- Update to 0.9.3.

* Tue Oct 24 2006 Matthias Saou <http://freshrpms.net/> 0.9.2-2
- Rebuild against new ffmpeg build (for new shared x264).
- Add explicit mjpegtools requirement, since it doesn't get pulled in and is
  required to export to mpeg.

* Mon Sep 18 2006 Matthias Saou <http://freshrpms.net/> 0.9.2-1
- Update to 0.9.2.

* Tue Aug 22 2006 Matthias Saou <http://freshrpms.net/> 0.9.1-1
- Update to 0.9.1.

* Tue Jun 27 2006 Matthias Saou <http://freshrpms.net/> 0.9.0-2
- Include patch to fix PPC build.

* Sun Jun 25 2006 Matthias Saou <http://freshrpms.net/> 0.9.0-1
- Update to 0.9.0.
- Add libiec61883-devel build requirement.
- Change --with-quicktime to --enable-quicktime for it to work...

* Wed Mar 22 2006 Matthias Saou <http://freshrpms.net/> 0.8.1-0.2.20060320
- Add missing modular X build requirement.

* Mon Mar 20 2006 Matthias Saou <http://freshrpms.net/> 0.8.1-0.1.20060320
- Update to today's CVS to fix rebuild against latest libquicktime.

* Fri Jan 13 2006 Matthias Saou <http://freshrpms.net/> 0.8.0-2
- Add modular xorg build conditional.

* Wed Dec  7 2005 Matthias Saou <http://freshrpms.net/> 0.8.0-1
- Update to 0.8.0.
- Change libgnomeui-devel dependency to new gtk2-devel only.
- Add explicit gtk2 >= 2.6 requirement.
- Include patch to change detection of libquicktime (HV was tested).
- Include new libdvtitler and libtimfx shared libraries.
- Obsolete kino-dvtitler <= 0.2.0-2.

* Mon Jun  6 2005 Matthias Saou <http://freshrpms.net/> 0.7.6-1
- Update to 0.7.6.
- Add update-mime-database calls.

* Fri Apr 29 2005 Matthias Saou <http://freshrpms.net/> 0.7.5-1
- Disable ffmpeg on FC4 for now.

* Mon Nov 22 2004 Matthias Saou <http://freshrpms.net/> 0.7.5-1
- Update to 0.7.5.

* Tue Oct 05 2004 Dag Wieers <dag@wieers.com> - 0.7.4-1
- Update to 0.7.4.

* Mon Aug 16 2004 Matthias Saou <http://freshrpms.net/> 0.7.3-1
- Update to 0.7.3.

* Mon Aug  2 2004 Matthias Saou <http://freshrpms.net/> 0.7.2-1.20040802
- Update to today's CVS tree to fix various bugs.

* Tue Jul 27 2004 Matthias Saou <http://freshrpms.net/> 0.7.2-1
- Update to 0.7.2.
- Spec file changes to match upstream build fixes.

* Tue Jul 20 2004 Dag Wieers <dag@wieers.com> - 0.7.1-3
- Rebuild for x86_64 with quicktime support.

* Mon Jun 14 2004 Matthias Saou <http://freshrpms.net/> 0.7.1-2
- Updated the desktop entry creation to the new current method.
- Fixed build requirements.
- Added custom icon for the menu entry (taken from the logo).

* Sun Apr 11 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Obsolete older kino-devel package. (Jeff Moe)

* Fri Dec 19 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated to 0.7.0.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.6.5-0
- Updated to 0.6.5.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.6.4-0
- Updated to 0.6.4.

* Wed Feb 12 2003 Dag Wieers <dag@wieers.com> - 0.6.3-0
- Initial package. (using DAR)
