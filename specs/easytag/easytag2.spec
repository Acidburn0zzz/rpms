# $Id$
# Authority: matthias

Summary: Tag editor for mp3, ogg, flac and other music files
Name: easytag
Version: 1.99.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://easytag.sourceforge.net/
Source: http://dl.sf.net/easytag/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel >= 2.4.0, id3lib-devel >= 3.7.12
BuildRequires: libvorbis-devel >= 1.0, flac-devel, gettext

%description
EasyTAG is an utility for viewing, editing and writing tags of your
MP3, MP2, FLAC and OGG files. Its simple and nice GTK+ interface makes
tagging easier.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog README TODO THANKS USERS-GUIDE
%{_bindir}/easytag
%{_datadir}/applications/*easytag.desktop
%{_datadir}/easytag/
%{_datadir}/pixmaps/*
%{_mandir}/man?/*


%changelog
* Fri Oct 29 2004 Matthias Saou <http://freshrpms.net/> 1.0-1
- Fork off to "unstable" 1.99.1.

* Tue Jun  1 2004 Matthias Saou <http://freshrpms.net/> 0.31-1
- Update to stable 0.31.

* Fri Mar 26 2004 Matthias Saou <http://freshrpms.net/> 0.30.2-1
- Update to unstable 0.30.2.

* Wed Mar 24 2004 Matthias Saou <http://freshrpms.net/> 0.30.1-1
- Update to unstable 0.30.1.
- Remove desktop-file-install as it's now freedesktop style.

* Thu Feb 26 2004 Matthias Saou <http://freshrpms.net/> 0.30-4d
- Added patch for 0.30d.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.30-3c
- Rebuild for Fedora Core 1.

* Thu Oct 30 2003 Matthias Saou <http://freshrpms.net/> 0.30-2c
- Added patches to update to 0.30c.

* Tue Sep  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.30.

* Mon Sep  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.29.

* Tue Jul 15 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.28.1.

* Wed Jun  4 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.28.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar 20 2003 Matthias Saou <http://freshrpms.net/>
- Added patch to 0.27a.

* Fri Feb  7 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.27.

* Fri Jan  3 2003 Ville Skytt� <ville.skytta at iki.fi> 0.26-fr1
- Update to 0.26.

* Wed Dec 25 2002 Ville Skytt� <ville.skytta at iki.fi> 0.25b-fr1
- Update to 0.25b.
- Build with flac support.

* Thu Oct 10 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.
- Rebuild with flac support... nope, doesn't compile :-(

* Fri Sep 20 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.24.

* Fri Aug 30 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup for Red Hat Linux.
- A few %%files fixes and improvements.

* Thu Dec 18 2001 Jerome Couderc <j.couderc@ifrance.com>
- Updated for (Build)Requires entries

* Thu Sep 22 2001 Jerome Couderc <j.couderc@ifrance.com>
- Updated for /etc/X11/applnk/Multimedia/easytag.desktop

* Thu Sep 20 2001 G�tz Waschk <waschk@linux-mandrake.com> 0.15.1-1
- Updated for autoconf

* Fri Jun 2 2000 Jerome Couderc <j.couderc@ifrance.com>
- Updated to include po files into the rpm package

* Fri May 5 2000 Jerome Couderc <j.couderc@ifrance.com>
- Initial spec file.

