# $Id$
# Authority: dag
# Upstream: <libxmlplusplus-general$lists,sf,net>

Summary: C++ wrapper for working with XML files
Name: libxml++
Version: 2.19.1
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://libxmlplusplus.sourceforge.net/

#Source: http://dl.sf.net/libxmlplusplus/libxml++-%{version}.tar.bz2
Source: http://ftp.gnome.org/pub/GNOME/sources/libxml++/2.19/libxml++-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libxml2-devel >= 2.5.1

%description
libxml++ is a C++ interface for working with XML files, using libxml
(gnome-xml) to parse and write the actual XML files. It has a simple
but complete API.

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
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/libxml++-2.6.so.*

%files devel
%defattr(-, root, root, 0755)
%doc examples/
%doc %{_docdir}/libxml++-2.6/
%{_includedir}/libxml++-2.6/
%{_libdir}/libxml++-2.6.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libxml++-2.6/
%exclude %{_libdir}/libxml++-2.6.la

%changelog
* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 2.19.1-1
- Updated to release 2.19.1.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 1.0.5-1
- Updated to release 1.0.5.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 0.26.0-1
- Cosmetic cleanup.

* Mon Jan 05 2004 Dag Wieers <dag@wieers.com> - 0.26.0-0
- Updated to release 0.26.0.

* Thu Sep 11 2003 Dag Wieers <dag@wieers.com> - 0.25.0-0
- Initial package. (using DAR)
