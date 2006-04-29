# $Id$
# Authority: dries
# Upstream: T.Fischer <fischer$unix,ag,uni-kl,de>

Summary: BibTex editor
Name: kbibtex
Version: 0.1.4
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://www.unix-ag.uni-kl.de/~fischer/kbibtex/

Source: http://www.unix-ag.uni-kl.de/~fischer/kbibtex/download/kbibtex-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gcc-c++, gettext

%description
KBibTeX is a BibTeX editor for KDE. It supports network transparent access
to .bib files, and export to both .pdf and .ps thru (pdf)latex.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/kbibtex*
%{_bindir}/kbibtex
%{_libdir}/kde3/libkbibtexpart.*
%{_datadir}/applnk/Office/kbibtex.desktop
%{_datadir}/apps/kbibtex/
%{_datadir}/apps/kbibtexpart/
%{_datadir}/doc/HTML/*/kbibtex/
%{_datadir}/icons/crystalsvg/*/apps/kbibtex.png
%{_datadir}/services/kbibtex_part.desktop

%changelog
* Sat Apr 29 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.4-1
- Updated to release 0.1.4.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.3-1.2
- Rebuild for Fedora Core 5.

* Sat Dec 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.3-1
- Initial package.
