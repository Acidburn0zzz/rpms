# $Id$
# Authority: dag

Summary: This is the ASN.1 library used in GNUTLS
Name: libtasn1
Version: 0.2.18
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://www.gnu.org/software/gnutls/download.html

Source: ftp://ftp.gnutls.org/pub/gnutls/libtasn1/libtasn1-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison, gcc-c++

%description
This is the ASN.1 library used in GNUTLS.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{_infodir}/dir

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README THANKS
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.ps doc/TODO
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_bindir}/libtasn1-config
%{_libdir}/pkgconfig/libtasn1.pc
%{_datadir}/aclocal/libtasn1.m4
%{_infodir}/libtasn1*
%{_mandir}/man3/*asn1*

%changelog
* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.18-1
- Updated to release 0.2.18.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.17-1
- Updated to release 0.2.17.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 0.2.9-1
- Updated to release 0.2.9.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.2.5-0
- Initial package. (using DAR)
