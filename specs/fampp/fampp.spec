# $Id$
# Authority: dries

Summary: C++ wrapper for fam, the file alteration monitor
Name: fampp
Version: 3.5.2
Release: 1
License: GPL
Group: System Environment/Daemons
URL: http://fampp.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/fampp/fampp2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, stlport-devel, pkgconfig, gamin-devel

%description
Fam++ is a C++ wrapper for fam from sgi. Fam uses imon to inform it when 
inodes change, the net effect being that applications can register interest 
in a file and be informed when that file changes.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n fampp2-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Wed Nov 03 2004 Dries Verachtert <dries@ulyssis.org> 3.5.2-1
- Update to release 3.5.2.

* Tue Apr 27 2004 Dries Verachtert <dries@ulyssis.org> 3.5.1-1
- Initial package

