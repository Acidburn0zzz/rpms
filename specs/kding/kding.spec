# $Id$
# Authority: dries
# Upstream: Michael Rex <me$rexi,org>

Summary: Frontend for ding, a dictionary lookup program
Name: kding
Version: 0.3
Release: 1.2
License: GPL
Group: Applications/Internet
URL: http://www.rexi.org/software/kding/

Source: http://www.rexi.org/downloads/kding/kding-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gcc-c++, gettext
Requires: ding

%description
KDing is a KDE frontend for Ding, a dictionary lookup program. It sits
in KDE's system tray and can translate the current clipboard content.
Users can also enter single words or phrases for translation. It is
intended to be used for translating between German and English, but
can be used with every language for which a word list is available for
Ding.

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/kding
%{_datadir}/applnk/Utilities/kding.desktop
%{_datadir}/apps/kding/
%{_datadir}/doc/HTML/*/kding/
%{_datadir}/icons/*/*/apps/kding.png

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1.2
- Rebuild for Fedora Core 5.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
