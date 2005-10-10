# $Id$
# Authority: dag
# Upstream: <tim@bach.ece.jhu.edu>

%{?dist: %{expand: %%define %dist 1}}

%{?rh9:%define _without_tcltk_devel 1}
%{?rh8:%define _without_tcltk_devel 1}
%{?rh7:%define _without_tcltk_devel 1}
%{?el2:%define _without_tcltk_devel 1}

Summary: Electronic circuit schematic drawing program
Name: xcircuit
Version: 3.3.1
Release: 2
License: GPL
Group: Applications/Engineering
URL: http://xcircuit.ece.jhu.edu/

Source: http://xcircuit.ece.jhu.edu/archive/xcircuit-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libtool

%{!?_without_tcltk_devel:BuildRequires: tcl-devel >= 8.3, tk-devel}
%{?_without_tcltk_devel:BuildRequires: tcl >= 8.3, tk}

%description
Xcircuit is a general-purpose drawing program and also a specific-purpose
CAD program for circuit schematic drawing and schematic capture.

%prep
%setup

%build
%{__libtoolize} --force --copy
%{__aclocal}
%{__automake} --add-missing
%{__autoconf}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	datadir="%{buildroot}%{_libdir}"

%{__make} install-man \
	mandir="%{buildroot}%{_mandir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYRIGHT README* TODO examples/
%doc %{_mandir}/man1/xcircuit.1*
%{_bindir}/xcircuit
%{_libdir}/xcircuit-3.3/

%changelog
* Sat Dec 04 2004 Dag Wieers <dag@wieers.com> - 3.3.1-2
- Fixed problem with incorrect %%datadir. (Michael D. Setzer)

* Fri Dec 03 2004 Dag Wieers <dag@wieers.com> - 3.3.1-1
- Initial package. (using DAR)
