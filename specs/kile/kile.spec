# $Id$
# Authority: dries

# Screenshot: http://kile.sourceforge.net/images/screenshots/kile_screen.png
# ScreenshotURL: http://kile.sourceforge.net/screenshots.php

# ExcludeDist: el3 fc1

%{?dist: %{expand: %%define %dist 1}}

Summary: User friendly TeX/LaTeX editor
Name: kile
Version: 1.9.1
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://kile.sourceforge.net/

Source: http://dl.sf.net/kile/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, kdelibs-devel, gcc, make, gcc-c++
%{?el4:BuildRequires: libselinux-devel}
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}
Requires: kdelibs

%description
Kile is a user friendly TeX/LaTeX editor. The main features are:
* Compile, convert and view your document with one click.
* Templates and wizards makes starting a new document very little work.
* Easy insertion of many standard tags and symbols and the option
to define (an arbitrary number of) user defined tags
* Inverse and forward search: click in the DVI viewer and jump to the
corresponding LaTeX line in the editor, or jump from the editor to the
corresponding page in the viewer.
* Finding chapter or sections is very easy, Kile constructs a list of all
the chapter etc. in your document. You can use the list to jump to the
corresponding section.

%description -l nl
Kile is een gebruiksvriendelijke TeX/LaTeX editor met ondersteuning voor:
* Het compileren, transformeren en bekijken van uw document met 1 klik.
* Een nieuw document starten is eenvoudig met templates en wizards.
* U kan eenvoudig vele standaard tags en symbolen toevoegen en ook uw eigen
tags toevoegen.
* Zoeken: klikken in de DVI viewer opent de overeenkomstige LaTeX lijn in
de editor en andersom.
* Het vinden van hoofdstukken en secties is eenvoudig: Kile maakt een lijst
van alle hoofdstukken en dergelijke.

%prep
%setup

%build
. /etc/profile.d/qt.sh
%configure LDFLAGS=-L$QTDIR/lib
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%{__make} install DESTDIR=%{buildroot}
echo "Encoding=UTF-8" >> %{buildroot}%{_datadir}/applications/kde/kile.desktop
sed -i "s/KDE Desktop Entry/Desktop Entry/g;" %{buildroot}%{_datadir}/applications/kde/kile.desktop
sed -i "s/Categories=.*/Categories=Qt;KDE;Application;Office;/g;" %{buildroot}%{_datadir}/applications/kde/kile.desktop
%{__mv} %{buildroot}%{_datadir}/applications/kde/kile.desktop %{buildroot}%{_datadir}/applications/kile.desktop
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%{_datadir}/doc/HTML/*/kile/
%{_datadir}/apps/kile/
# conflicts with kdelibs-3.2.2-8.FC2
%exclude %{_datadir}/apps/katepart/syntax/bibtex.xml
%exclude %{_datadir}/apps/katepart/syntax/latex.xml
%{_datadir}/apps/kconf_update/kile.upd
%{_datadir}/apps/kconf_update/kile*_upd.pl
%{_datadir}/config.kcfg/kile.kcfg
%{_datadir}/icons/*/*/apps/kile.*
%{_datadir}/applications/kile.desktop
%{_datadir}/mimelnk/text/x-kilepr.desktop
%{_bindir}/kile


%changelog
* Sat Jul 29 2006 Dries Verachtert <dries@ulyssis.org> - 1.9.1-1
- Updated to release 1.9.1.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.8-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> 1.8-1
- Update to release 1.8.

* Fri Oct 22 2004 Dries Verachtert <dries@ulyssis.org> 1.7.1-1
- Update to release 1.7.1.

* Mon Oct 18 2004 Dries Verachtert <dries@ulyssis.org> 1.7-1
- Update to 1.7.
- %%find_lang removed.. it doesn't seem to work with version 1.7.
- syntax files excluded.. conflict with kdelibs

* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net> 1.6.3-1
- Partial spec file cleanup, added %%find_lang.

* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> 1.6.3-1
- update to 1.6.3

* Sun Apr 18 2004 Dries Verachtert <dries@ulyssis.org> 1.6.2-1
- update to 1.6.2

* Sun Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 1.6.1-1
- update to 1.6.1

* Sat Dec 13 2003 Dries Verachtert <dries@ulyssis.org> 1.6-4
- make install changed to make install-strip

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 1.6-3
- added some BuildRequires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 1.6-2
- cleanup and completion of spec file

* Sat Nov 29 2003 Dries Verachtert <dries@ulyssis.org> 1.6-1
- first packaging for Fedora Core 1
