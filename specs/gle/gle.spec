# $Id$
# Authority: dries
# Upstream: Vincent LaBella <vlabella$albany,edu>

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: Graphics Layout Engine
Name: gle
Version: 4.0.11
Release: 2.2
License: BSD
Group: Applications/Multimedia
URL: http://www.gle-graphics.org/

Source: http://dl.sf.net/glx/gle_%{version}_src.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libpng-devel, libtiff-devel
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
GLE (Graphics Layout Engine) is a high-quality graphics package for
scientists, combining a user-friendly scripting language with a full
range of facilities for producing publication-quality graphs, diagrams,
posters and slides. GLE provides LaTeX quality fonts together with a
flexible graphics module which allows the user to specify any feature of
a graph. Complex pictures can be drawn with user-defined subroutines and
simple looping structures. Current output formats include EPS, PS, PDF,
JPEG, and PNG.

%prep
%setup

%build
export GLE_TOP=%{builddir}/%{name}-%{version}/src/fonts
%{__make} %{?_smp_mflags} -f Makefile.gcc

%install
%{__rm} -rf %{buildroot}
%makeinstall -f Makefile.gcc GLE_RPM_ROOT=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc readme
%{_bindir}/gle
%{_datadir}/gle

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 4.0.11-2.2
- Rebuild for Fedora Core 5.

* Sat Dec 17 2005 Dries Verachtert <dries@ulyssis.org> - 4.0.11-1
- Updated to release 4.0.11.

* Sat Nov 19 2005 Jonas Frantz <jonas.frantz@welho.com> - 4.0.10-2
- Fix problem with making inittex.ini

* Mon Nov 08 2005 Dries Verachtert <dries@ulyssis.org> - 4.0.10-1
- Initial package.
