# $Id$
# Authority: matthias

%define desktop_vendor freshrpms
#define beta 8

Summary: Breakout and Arkanoid style arcade game
Name: lbreakout2
Version: 2.5
Release: %{?beta:0.beta%{beta}.}1
License: GPL
Group: Amusements/Games
URL: http://www.lgames.org/
Source: http://dl.sf.net/lgames/lbreakout2-%{version}%{?beta:beta-%{beta}}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, SDL_mixer-devel, zlib-devel, libpng-devel
BuildRequires: ImageMagick
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
The successor to LBreakout offers you a new challenge in more than 50 levels
with loads of new bonuses (goldshower, joker, explosive balls, bonus magnet
...), maluses (chaos, darkness, weak balls, malus magnet ...) and special
bricks (growing bricks, explosive bricks, regenerative bricks ...). If you
are still hungry for more after that you can create your own levelsets with
the integrated level editor.


%prep
%setup -n %{name}-%{version}%{?beta:beta-%{beta}}


%build
%configure \
    --datadir="%{_datadir}/games" \
    --localstatedir="%{_localstatedir}/lib/games" \
    --with-docdir="/tmp"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot} _docs
%{__make} install DESTDIR=%{buildroot}

# Put the docs back into place
%{__mv} %{buildroot}/tmp _docs

# Install desktop entry icon, and change that gif to a nice png
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
convert lbreakout48.gif %{buildroot}%{_datadir}/pixmaps/lbreakout.png

# Create the system menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Linux Breakout 2
Comment=Breakout and Arkanoid style arcade game
Exec=lbreakout2
Icon=lbreakout.png
Terminal=false
Type=Application
Categories=Application;Game;
Encoding=UTF-8
EOF

%if %{!?_without_freedesktop:1}0
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop
%else
%{__install} -D -m 0644 %{name}.desktop \
    %{buildroot}%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
%endif


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog README TODO _docs/lbreakout2/
%attr(2551, root, games) %{_bindir}/lbreakout2
%{_bindir}/lbreakout2server
%{_datadir}/games/lbreakout2
%{_datadir}/pixmaps/lbreakout.png
%config(noreplace) %attr(664, games, games) %{_localstatedir}/lib/games/lbreakout2.hscr
%if %{!?_without_freedesktop:1}0
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%else
%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
%endif


%changelog
* Mon Aug  9 2004 Matthias Saou <http://freshrpms.net/> 2.5-1
- Update to 2.5 final.

* Mon Jun 21 2004 Matthias Saou <http://freshrpms.net/> 2.5-0.beta8.1
- Update to 2.5beta-8.

* Mon Jun 14 2004 Matthias Saou <http://freshrpms.net/> 2.5-0.beta6.1
- Update to 2.5beta-6.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 2.5-0.beta5.1
- Update to 2.5beta-5.
- Change the gif pixmap to png.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.5-0.beta3.1
- Update to 2.5beta-3.
- Added missing zlib and libpng dependencies.
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Mar  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.4.1.

* Fri Jan  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.4.

* Sat Oct 26 2002 Matthias Saou <http://freshrpms.net/>
- Fixed the menu entry, thanks to Erwin J. Prinz.

* Sat Sep 28 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry with icon.

* Mon Sep 23 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.3.5.

* Tue Sep 10 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.3.3.

* Tue Sep 10 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.3.3.

* Mon Aug 19 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.3.2.

* Wed Aug 14 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.3.1.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Sun Feb 24 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.2.

* Tue Feb  5 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.1.

* Mon Jan 28 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.

* Sun Jan  6 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.2.

* Tue Jan  1 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.1.

* Sat Dec  8 2001 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.1.

* Thu Nov 29 2001 Matthias Saou <http://freshrpms.net/>
- Update to 2.0-pre2.

* Thu Nov 22 2001 Matthias Saou <http://freshrpms.net/>
- Update to 2.0beta2.

* Tue Apr 10 2001 Matthias Saou <http://freshrpms.net/>
- Update to 010315.

* Mon Nov 27 2000 Matthias Saou <http://freshrpms.net/>
- Initial RPM release for RedHat 7.0

