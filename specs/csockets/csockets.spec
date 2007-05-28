# $Id$
# Authority: dries

Summary: C++ wrapper for sockets
Name: csockets
Version: 2.1.5
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.alhem.net/Sockets/index.html

Source: http://www.alhem.net/Sockets/Sockets-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, openssl-devel

%description
C++ Sockets is a C++ wrapper for BSD-style sockets. Its features include
transparent SOCKS4 client support and asynchronous DNS. It implements the TCP,
UDP, ICMP, HTTP (GET, PUT, and POST), and HTTPS (using OpenSSL) protocols.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n Sockets-%{version}

### Work-around for kerberos/openssl on RH9 and EL3
%{__perl} -pi.orig -e 's|^(INCLUDE\s*=\s*)|$1 -I/usr/kerberos/include |' Makefile
%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' Makefile

%build
%{__make} %{?_smp_mflags} PREFIX=%{_prefix}

%install
%{__rm} -rf %{buildroot}
%makeinstall PREFIX=%{buildroot}%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/Sockets-config

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/Sockets/
%{_libdir}/libSockets.a
#%{_libdir}/libSocketsEx.a

%changelog
* Mon May 28 2007 Dries Verachtert <dries@ulyssis.org> - 2.1.5-1
- Updated to release 2.1.5.

* Fri May 11 2007 Dries Verachtert <dries@ulyssis.org> - 2.1.4-1
- Updated to release 2.1.4.

* Wed May 09 2007 Dries Verachtert <dries@ulyssis.org> - 2.1.3-1
- Updated to release 2.1.3.

* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 2.1.1-1
- Updated to release 2.1.1.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Updated to release 2.1.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.9-1
- Updated to release 2.0.9.

* Mon Jul 31 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.5-1
- Updated to release 2.0.5.

* Fri Apr 21 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.4-1
- Updated to release 2.0.4.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.9.9-1.2
- Rebuild for Fedora Core 5.

* Thu Nov 17 2005 Dries Verachtert <dries@ulyssis.org> - 1.9.9-1
- Updated to release 1.9.9.

* Mon Oct 03 2005 Dries Verachtert <dries@ulyssis.org> - 1.9.8-1
- Updated to release 1.9.8.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 1.9.7-1
- Update to release 1.9.7.

* Tue Sep 06 2005 Dries Verachtert <dries@ulyssis.org> - 1.9.6-1
- Update to release 1.9.6.

* Wed Aug 31 2005 Dries Verachtert <dries@ulyssis.org> - 1.9.5-1
- Update to release 1.9.5.

* Fri Aug 26 2005 Dries Verachtert <dries@ulyssis.org> - 1.8.7-1
- Initial package.
