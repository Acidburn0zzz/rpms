# $Id$
# Authority: dries
# Upstream: <herrekberg$users,sourceforge,net>

Summary: Comic book viewer
Name: comix
Version: 3.0
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://comix.sourceforge.net/

Source: http://dl.sf.net/comix/comix-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: python
Requires: python, python-imaging

%description
Comix is a comic book viewer. It reads zip, rar, tar, tar.gz, and tar.bz2
archives (often called .cbz, .cbr and .cbt) as well as normal image files.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_prefix}
%{__python} install.py install --installdir %{buildroot}%{_prefix}
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%doc %{_mandir}/man1/comicthumb.1*
%doc %{_mandir}/man1/comix.1*
%{_bindir}/comicthumb
%{_bindir}/comix
%{_datadir}/applications/*comix.desktop
%{_datadir}/icons/hicolor/48x48/apps/comix.png
%{_datadir}/pixmaps/comix.png
%{_datadir}/pixmaps/comix/

%changelog
* Mon Apr 03 2006 Dries Verachtert <dries@ulyssis.org> - 3.0-1
- Updated to release 3.0.

* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 2.9-1
- Updated to release 2.9.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 2.8-1
- Updated to release 2.8.

* Mon Jan 30 2006 Dries Verachtert <dries@ulyssis.org> - 2.7-1
- Updated to release 2.7.

* Tue Jan 17 2006 Dag Wieers <dag@wieers.com> - 2.6-1
- Updated to release 2.6.

* Wed Jan 11 2006 Dries Verachtert <dries@ulyssis.org> - 2.5-1
- Updated to release 2.5.
- Added the python-imaging requirement, thanks to Gergely Gabor!

* Sun Jan 01 2006 Dries Verachtert <dries@ulyssis.org> - 2.4-1
- Updated to release 2.4.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 2.3-1
- Updated to release 2.3.

* Sat Dec 10 2005 Dries Verachtert <dries@ulyssis.org> - 2.2-1
- Updated to release 2.2.

* Sat Nov 26 2005 Dag Wieers <dag@wieers.com> - 2.1-1
- Updated to release 2.1.

* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org> - 2.0-1
- Updated to release 2.0.

* Mon Nov 07 2005 Dries Verachtert <dries@ulyssis.org> - 1.6-1
- Initial package.
