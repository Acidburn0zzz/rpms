# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc1:%define _without_alsa 1}
%{?el3:%define _without_alsa 1}
%{?rh9:%define _without_alsa 1}
%{?rh8:%define _without_alsa 1}
%{?yd3:%define _without_alsa 1}

#define prever         pre3
%define desktop_vendor rpmforge

Summary: Powerful audio editor
Name: audacity
Version: 1.2.4b
Release: %{?prever:0.%{prever}.}1
License: GPL
Group: Applications/Multimedia
URL: http://audacity.sourceforge.net/
Source: http://dl.sf.net/audacity/audacity-src-%{version}%{?prever:-%{prever}}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: wxGTK >= 2.4.0
BuildRequires: gcc-c++, zip, zlib-devel, gettext, desktop-file-utils
BuildRequires: wxGTK-devel >= 2.4.0, libogg-devel, libvorbis-devel
BuildRequires: libmad-devel, flac-devel, libsndfile-devel
BuildRequires: libsamplerate-devel, libid3tag-devel
BuildRequires: autoconf
%{!?_without_alsa:BuildRequires: alsa-lib-devel}

%description
Audacity is a free audio editor. You can record sounds, play sounds, import
and export WAV, AIFF, and MP3 files, and more. Use it to edit your sounds
using Cut, Copy and Paste (with unlimited Undo), mix tracks together, or
apply effects to your recordings. It also has a built-in amplitude envelope
editor, a customizable spectrogram mode and a frequency analysis window for
audio analysis applications. Built-in effects include Bass Boost, Wahwah,
and Noise Removal, and it also supports VST plug-in effects.


%prep
%setup -n %{name}-src-%{version}%{?prever:-%{prever}}


%build
# This is required or the configure in that directory will fail (1.2.1 & 1.2.2)
(cd lib-src/portaudio-v19/ && autoconf)
%configure \
    --with-libsndfile="system" \
    --with-portaudio="v18" \
    --without-portmixer
%{__perl} -pi.orig -e 's|^(CFLAGS) = -g |$1 = -fPIC |' \
    lib-src/portaudio-v19/Makefile
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

# Create a desktop entry
%{__cat} << EOF > %{name}.desktop
[Desktop Entry]
Name=Audacity Audio Editor
Comment=Audio editor to record, play sounds and import, export files
Icon=audacity.xpm
Exec=audacity
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF

# Complete the modifications
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications  \
    %{name}.desktop

# Install the image used in the desktop entry
%{__install} -Dp -m 644 images/AudacityLogo.xpm \
    %{buildroot}%{_datadir}/pixmaps/%{name}.xpm


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
# The help is actually in %{_docdir}/%{name} in order to be accessible directly
#doc LICENSE.txt README.txt help
%{_bindir}/audacity
%{_datadir}/applications/%{desktop_vendor}-audacity.desktop
%{_datadir}/audacity/
%{_docdir}/audacity/
%{_datadir}/pixmaps/audacity.xpm
%{_mandir}/man1/*


%changelog
* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.2.4b-1
- Update to 1.2.4b, but build untested since it's wxGTK 2.6 incompatible.

* Wed Nov 30 2005 Matthias Saou <http://freshrpms.net/> 1.2.4-1
- Update to 1.2.4.

* Thu Nov 25 2004 Matthias Saou <http://freshrpms.net/> 1.2.3-2
- Move back from postaudio v19 to v18 for now, as v19 has too many issues :-(
  (leave no longer relevant deps as-is, for later switching back to v19).

* Sat Nov 20 2004 Matthias Saou <http://freshrpms.net/> 1.2.3-1
- Update to 1.2.3.
- Added libid3tag and libsamplerate support.

* Thu Aug 26 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-1
- Update to 1.2.2.

* Tue Jun 01 2004 Matthias Saou <http://freshrpms.net/> 1.2.1-1
- Got 1.2.1 to build at last by running autoconf in the portaudio-v19 dir.

* Tue Mar  2 2004 Matthias Saou <http://freshrpms.net/> 1.2.0-2
- Recompile with ALSA support (should be near stable now).

* Tue Mar  2 2004 Matthias Saou <http://freshrpms.net/> 1.2.0-1
- Update to 1.2.0 final.

* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/> 1.2.0-0.pre3.2
- Rebuild against gtk+ wxGTK to fix crashes with the gtk2 version.

* Thu Nov 13 2003 Matthias Saou <http://freshrpms.net/> 1.2.0-0.pre3.1
- Update to 1.2.0pre3.
- Added find_lang macro.
- Updated the menu entry.
- Added libmad, flac and libsndfile support.
- Rebuild for Fedora Core 1.

* Thu Aug  1 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

