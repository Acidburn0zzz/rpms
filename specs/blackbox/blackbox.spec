# $Id$
# Authority: matthias

Summary: Very small and fast Window Manager
Name: blackbox
Version: 0.65.0
Release: 9
License: GPL
Group: User Interface/Desktops
URL: http://blackboxwm.sourceforge.net/
Source0: http://dl.sf.net/blackboxwm/blackbox-%{version}.tar.gz
Source1: blackbox.desktop
Patch0: blackbox-0.65.0-assert.patch
Patch1: blackbox-0.65.0-gcc34.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: XFree86-devel, gcc-c++

%description
Blackbox is a window manager for the X Window environment, which is
almost completely compliant with ICCCM specified operation policies.
It features nice and fast interface with multiple workspaces and
simple menus. Fast built-in graphics code that can render solids,
gradients and bevels is used to draw window decorations. Remaining
small in size, blackbox preserves memory and CPU.


%prep
%setup
%patch0 -p0 -b .assert
%patch1 -p1 -b .gcc34


%build
# Work around NLS problem
export LANG="en_US" LC_ALL="en_US"
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

# Install GDM session filee
%{__mkdir_p} %{buildroot}/etc/X11/gdm/Sessions
%{__cat} > %{buildroot}/etc/X11/gdm/Sessions/Blackbox << EOF
#!/bin/sh
exec /etc/X11/xdm/Xsession %{name}
EOF

# Install the desktop entry
%{__install} -Dp -m644 %{SOURCE1} \
    %{buildroot}%{_datadir}/xsessions/%{name}.desktop


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog* LICENSE README*
%attr(755, root, root) /etc/X11/gdm/Sessions/Blackbox
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/*


%changelog
* Mon Nov 15 2004 Mattthias Saou <http://freshrpms.net/> 0.65.0-9
- Added gcc 3.4 patch from Arch Linux.

* Thu May  6 2004 Mattthias Saou <http://freshrpms.net/> 0.65.0-8
- Removed switchdesk file, it doesn't work because of hardcoded stuff.

* Wed Mar 24 2004 Mattthias Saou <http://freshrpms.net/> 0.65.0-8
- Removed explicit XFree86 dependency.

* Mon Feb 23 2004 Mattthias Saou <http://freshrpms.net/> 0.65.0-7
- Added blackbox.desktop file for xsessions based on the GNOME one.

* Tue Feb 10 2004 Scott R. Godin <nospam@webdragon.net> 0.65.0-6
- Patch for #include <cassert> in Window.cc
- Fixed nls problem, left in --disable just in case. Smile, Matthias. :-) 

* Fri Nov 14 2003 Mattthias Saou <http://freshrpms.net/> 0.65.0-5
- Rebuild for Fedora Core 1.

* Wed May 14 2003 Matthias Saou <http://freshrpms.net/>
- Added --without nls to enable rebuilding on Red Hat Linux 9 :-(

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Oct  6 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Fri Sep 20 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.65.0 final.

* Mon Aug 12 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

