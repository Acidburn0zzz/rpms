# $Id $

# Authority: dries

Summary: Free implementation of the logic programming language PROLOG
Name: gprolog
Version: 1.2.16
Release: 1
License: GPL
Group: Development/Languages
URL: http://gnu-prolog.inria.fr/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: ftp://ftp.inria.fr/INRIA/Projects/contraintes/gprolog/gprolog-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}

%description
GNU Prolog is a free implementation (under GPL) of the logic programming
language PROLOG. It can compile to native machine code which is extremely
fast in execution. Another feature is the included constraint solver.

%prep
%setup 

%build
cd src
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd src
%makeinstall \
	INSTALL_DIR=%{buildroot}/usr \
	LINKS_DIR=%{buildroot}/links \
	DOC_DIR=%{buildroot}/usr/share/gprolog/doc \
	HTML_DIR=%{buildroot}/usr/share/gprolog/doc/html \
	EXAMPLES_DIR=%{buildroot}/usr/share/gprolog/examples
%{__rm} -f %{buildroot}/usr/COPYING \
	%{buildroot}/usr/ChangeLog \
	%{buildroot}/usr/NEWS \
	%{buildroot}/usr/VERSION

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%package doc
Summary: Documentation of gprolog.
Group: Development/Languages
Requires: gprolog = %{version}-%{release}

%description doc
This package contains the documentation of gprolog.

%package examples
Summary: Examples of gprolog.
Group: Development/Languages
Requires: gprolog = %{version}-%{release}

%description examples
This package contains the examples of gprolog.


%files
%defattr(-,root,root, 0755)
%doc COPYING ChangeLog NEWS VERSION
%{_bindir}/fd2c
%{_bindir}/gplc
%{_bindir}/gprolog
%{_bindir}/hexgplc
%{_bindir}/ma2asm
%{_bindir}/pl2wam
%{_bindir}/wam2ma
%{_includedir}/gprolog.h
%{_includedir}/fd_to_c.h
%{_libdir}/all_fd_bips.o
%{_libdir}/all_pl_bips.o
%{_libdir}/debugger.o
%{_libdir}/libbips_fd.a
%{_libdir}/libbips_pl.a
%{_libdir}/libengine_fd.a
%{_libdir}/libengine_pl.a
%{_libdir}/liblinedit.a
%{_libdir}/obj_begin.o
%{_libdir}/obj_end.o
%{_libdir}/top_level.o

%files doc
%defattr(-,root,root, 0755)
%{_datadir}/gprolog/doc

%files examples
%defattr(-,root,root, 0755)
%{_datadir}/gprolog/examples/ExamplesFD
%{_datadir}/gprolog/examples/ExamplesPl
%{_datadir}/gprolog/examples/ExamplesC

%changelog
* Sat Mar 20 2004 Dries Verachtert <dries@ulyssis.org> 1.2.16-1
- update to version 1.2.16

* Sun Jan 25 2004 Dries Verachtert <dries@ulyssis.org> 1.2.3-1
- first packaging for Fedora Core 1
