# $Id$
# Authority: matthias
# Upstream: <vlc-devel@videolan.org>

%define desktop_vendor freshrpms
%define ffmpeg_date    20040520

Summary: The VideoLAN client, also a very good standalone video player
Name: videolan-client
Version: 0.7.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.videolan.org/
Source0: http://download.videolan.org/pub/videolan/vlc/%{version}/vlc-%{version}.tar.bz2
Source1: http://download.videolan.org/pub/videolan/vlc/%{version}/contrib/ffmpeg-%{ffmpeg_date}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, XFree86-devel, libpng-devel, desktop-file-utils
BuildRequires: fribidi-devel
%{!?_without_dvd:BuildRequires: libdvdcss-devel}
%{!?_without_dvdread:BuildRequires: libdvdread-devel}
%{!?_without_dvdplay:BuildRequires: libdvdplay-devel}
%{!?_without_dvbpsi:BuildRequires: libdvbpsi-devel}
%{!?_without_ogg:BuildRequires: libogg-devel}
%{!?_without_mad:BuildRequires: libmad-devel}
#{!?_without_ffmpeg:BuildRequires: lame-devel, faac-devel}
%{!?_without_xvid:BuildRequires: xvidcore-devel}
%{!?_without_a52:BuildRequires: a52dec-devel}
%{?_with_dv:BuildRequires: libdv-devel}
%{!?_without_flac:BuildRequires: flac-devel}
%{!?_without_vorbis:BuildRequires: libvorbis-devel}
%{!?_without_speex:BuildRequires: speex-devel}
%{!?_without_sdl:BuildRequires: SDL-devel}
%{!?_without_aa:BuildRequires: aalib-devel}
%{!?_without_esd:BuildRequires: esound-devel}
%{!?_without_arts:BuildRequires: arts-devel}
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_gtk:BuildRequires: gtk+-devel}
%{!?_without_gnome:BuildRequires: gnome-libs-devel}
%{!?_without_wxwin:BuildRequires: wxGTK-devel}
%{?_with_qt:BuildRequires: qt-devel}
%{?_with_kde:BuildRequires: kdelibs-devel}
%{?_with_ncurses:BuildRequires: ncurses-devel}
%{!?_without_xosd:BuildRequires: xosd-devel}
%{!?_without_lirc:BuildRequires: lirc}
%{?_with_mozilla:BuildRequires: mozilla-devel}
%{!?_without_id3tag:BuildRequires: libid3tag-devel}
%{!?_without_mpeg2dec:BuildRequires: mpeg2dec-devel >= 0.3.2}
%{!?_without_faad:BuildRequires: faad2-devel}
%{!?_without_theora:BuildRequires: libtheora-devel}
Conflicts: vlc

%description
VideoLAN Client (VLC) is a highly portable multimedia player for various
audio and video formats (MPEG-1, MPEG-2, MPEG-4, DivX, mp3, ogg, ...) as
well as DVDs, VCDs, and various streaming protocols.

Available rpmbuild rebuild options :
--with dv mga qt kde ncurses
--without dvd dvdread dvdplay dvbpsi v4l avi asf aac ogg rawdv mad ffmpeg xvid
          mp4 a52 vorbis mpeg2dec flac aa esd arts alsa gtk gnome wxwin xosd
          lsp lirc pth id3tag faad theora

Options that would need not yet existing add-on packages :
--with tremor tarkin svgalib ggi glide wxwindows


%package devel
Summary: Header files and static library from the Videolan Client
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
VideoLAN Client (VLC) is a highly portable multimedia player for various
audio and video formats (MPEG-1, MPEG-2, MPEG-4, DivX, mp3, ogg, ...) as
well as DVDs, VCDs, and various streaming protocols.

Install this package if you need to build Videolan Client plugins or intend
to link statically to it.


%prep
%setup -n vlc-%{version} -a 1


%build
# Build bundeled ffmpeg first
pushd ffmpeg-%{ffmpeg_date}
    %configure \
        --disable-shared \
        %ifarch %{ix86}
            --disable-mmx \
        %endif
        --enable-gpl \
        --enable-pp
#       --enable-mp3lame \
#       --enable-faac
    make
popd

%configure \
    --enable-release \
    %{?_without_dvd:--disable-dvd} \
    %{!?_without_dvdread:--enable-dvdread} \
    %{!?_without_dvdplay:--enable-dvdplay} \
    %{!?_without_dvbpsi:--enable-dvbpsi} \
    %{!?_without_v4l:--enable-v4l} \
    --enable-vcd \
    %{?_without_avi:--disable-avi} \
    %{?_without_asf:--disable-asf} \
    %{?_without_aac:--disable-aac} \
    %{?_without_ogg:--disable-ogg} \
    %{?_without_rawdv:--disable-rawdv} \
    %{!?_without_mad:--enable-mad} \
    %{!?_without_ffmpeg:--enable-ffmpeg} \
    %{!?_without_ffmpeg:--with-ffmpeg-tree=ffmpeg-%{ffmpeg_date}} \
    %{!?_without_faad:--enable-faad} \
    %{!?_without_xvid:--enable-xvid} \
    %{?_without_mp4:--disable-mp4} \
    %{?_without_a52:--disable-a52} \
    %{?_without_cinepak:--disable-cinepak} \
    %{?_with_dv:--enable-dv} \
    %{!?_without_flac:--enable-flac} \
    %{?_without_mpeg2dec:--disable-libmpeg2} \
    %{?_without_vorbis:--disable-vorbis} \
    %{?_with_tremor:--enable-tremor} \
    %{?_with_tarkin:--enable-tarkin} \
    %{!?_without_theora:--enable-theora} \
    --enable-x11 \
    --enable-xvideo \
    %{?_without_sdl:--disable-sdl} \
    --disable-qte \
    --disable-directx \
    --enable-fb \
    %{?_with_mga:--enable-mga} \
    %{?_with_svgalib:--enable-svgalib} \
    %{?_with_ggi:--enable-ggi} \
    %{?_with_glide:--enable-glide} \
    %{!?_without_aa:--enable-aa} \
    --without-wingdi \
    --enable-oss \
    %{!?_without_esd:--enable-esd} \
    %{!?_without_arts:--enable-arts} \
    %{!?_without_alsa:--enable-alsa} \
    --disable-waveout \
    %{!?_without_gtk:--enable-gtk} \
    --disable-familiar \
    %{!?_without_gnome:--enable-gnome} \
    %{!?_without_wxwindows:--enable-wxwindows} \
    %{?_with_qt:--enable-qt} \
    %{?_with_kde:--enable-kde} \
    --disable-opie \
    --disable-macosx \
    --disable-qnx \
    --disable-intfwin \
    %{?_with_ncurses:--enable-ncurses} \
    %{!?_without_xosd:--enable-xosd} \
    %{?_without_slp:--disable-slp} \
    %{!?_without_lirc:--enable-lirc} \
    %{!?_without_pth:--enable-pth} \
    --disable-st \
    %{?_with_mozilla:--enable-mozilla} \
    --disable-testsuite \
    --enable-plugins
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
find  %{buildroot}%{_libdir}/vlc -name "*.so" | xargs strip
%find_lang vlc
# Include the docs below, our way
%{__rm} -rf installed-docs
%{__mv} %{buildroot}%{_docdir}/vlc installed-docs
# So that the icon gets themable
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
%{__cp} -a %{buildroot}%{_datadir}/vlc/vlc48x48.png \
    %{buildroot}%{_datadir}/pixmaps/vlc.png

%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=VideoLAN Client
Comment=Play DVDs, other various video formats and network streamed videos
Icon=vlc.png
Exec=vlc
Terminal=false
Type=Application
Encoding=UTF-8
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
  --dir %{buildroot}%{_datadir}/applications    \
  --add-category Application                    \
  --add-category AudioVideo                     \
  %{name}.desktop


%clean
%{__rm} -rf %{buildroot}


%files -f vlc.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog MAINTAINERS README THANKS
%doc installed-docs/*
%{_bindir}/*vlc
%{_libdir}/vlc
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/pixmaps/vlc.png
%{_datadir}/vlc

%files devel
%defattr(-, root, root, 0755)
%doc HACKING 
%{_bindir}/vlc-config
%{_includedir}/vlc
%{_libdir}/libvlc.a


%changelog
* Tue Jun  1 2004 Matthias Saou <http://freshrpms.net/> 0.7.2-1
- Update to 0.7.2.
- Added fribidi support.
- Added --enable-gpl to ffmpeg for the postprocessing code to stay enabled.

* Mon May 17 2004 Matthias Saou <http://freshrpms.net/> 0.7.1-1
- Fix the desktop entry's description, make the icon themable.
- Add theora and faad2 support, enabled by default.

* Sat May 15 2004 Dag Wieers <dag@wieers.com> - 0.7.1-0.1
- Updated to release 0.7.1.

* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 0.7.0-0.3
- Rebuild against new libfame.

* Sat Feb 21 2004 Matthias Saou <http://freshrpms.net/> 0.7.0-0.1
- Update to 0.7.0.
- Bundle ffmpeg to avoid all the hassles of using the shared lib.
- Move the (now installed) docs to the proper location.
- Added wxWindows interface, the currently most maintained.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.6.2-0.2
- Rebuild for Fedora Core 1.

* Thu Aug 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.2.

* Tue Jul  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.0.
- Added libid3tag support.
- Added mpeg2dec dependency, cvs version, same for ffmpeg.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Tue Mar 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.2.
- Fix the dv build dependency, thanks to Alan Hagge.
- Added flac support.
- Fixed the libdvbpsi requirements.

* Mon Feb 24 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt against the new xosd lib.

* Wed Feb 19 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.1.
- Major spec file update.

* Fri Nov 15 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.6.

* Tue Oct 22 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.5.
- Minor --with / --without adjustments.

* Sun Oct  6 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.
- Added all --without options and --with qt.

* Mon Aug 12 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.4.

* Fri Jul 26 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.3.

* Fri Jul 12 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.2.

* Wed Jun  5 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.1.

* Fri May 24 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.0.
- Disabled qt interface, it's hell to build with qt2/3!
- Use %%find_lang and %%{?_smp_mflags}.

* Fri Apr 19 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.1.

* Mon Apr  8 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.0.

* Sat Jan 12 2002 Matthias Saou <http://freshrpms.net/>
- Removed the dependency on libdvdcss package, use the built in one instead,
  because 1.x.x is not as good as 0.0.3.ogle3.

* Tue Jan  1 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.92.
- Build fails with libdvdcss < 1.0.1.

* Tue Nov 13 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.91 and now requires libdvdcss 1.0.0.

* Mon Oct 22 2001 Matthias Saou <http://freshrpms.net/>
- Split libdvdcss into a separate package since it's also needed by the
  xine menu plugin.

* Thu Oct 11 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.2.90.
- Removed ggi, svgalib and aalib since they aren't included in Red Hat 7.2.

* Mon Aug 27 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.2.83.

* Sat Aug 11 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.2.82.

* Mon Jul 30 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.2.81.
- Added all the new split libdvdcss.* files to the %%files section.

* Tue Jun  5 2001 Matthias Saou <http://freshrpms.net/>
- Updated to the latest release, 0.2.80.

* Wed May 30 2001 Matthias Saou <http://freshrpms.net/>
- Updated to today's CVS version, works great! :-)
- Fixed the desktop menu entry.

* Tue May 22 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup to make it look more like others do.
- Added the use of many macros.
- Disabled automatic requires and provides (the package always needed qt,
  gtk+, gnome etc. otherwise).
- Added a system desktop menu entry.

* Mon Apr 30 2001 Arnaud Gomes-do-Vale <arnaud@glou.org>
Added relocation support and compile fixes for Red Hat 7.x.

* Sat Apr 28 2001 Henri Fallon <henri@videolan.org>
New upstream release (0.2.73)

* Mon Apr 16 2001 Samuel Hocevar <sam@zoy.org>
New upstream release (0.2.72)

* Fri Apr 13 2001 Samuel Hocevar <sam@zoy.org>
New upstream release (0.2.71)

* Sun Apr 8 2001 Christophe Massiot <massiot@via.ecp.fr>
New upstream release (0.2.70)

* Fri Feb 16 2001 Samuel Hocevar <sam@via.ecp.fr>
New upstream release

* Tue Aug  8 2000 Samuel Hocevar <sam@via.ecp.fr>
Added framebuffer support

* Sun Jun 18 2000 Samuel Hocevar <sam@via.ecp.fr>
Took over the package

* Thu Jun 15 2000 Eric Doutreleau <Eric.Doutreleau@int-evry.fr>
Initial package

