# $Id$
# Authority: dag
# Upstream: <bluez-devel$lists,sourceforge,net>

# ExclusiveDist: rh6 el2 rh7 rh8 rh9 el3 fc1

Summary: Bluetooth libraries
Name: bluez-libs
Version: 2.9
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.bluez.org/

Source: http://bluez.sf.net/download/bluez-libs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExcludeArch: s390 s390x
BuildRequires: glib-devel >= 1.2

%description
Libraries for use in Bluetooth applications.

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., U.S.A.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: bluez-sdp-devel

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
%makeinstall \
	includedir="%{buildroot}%{_includedir}/bluetooth"

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/libbluetooth.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/bluetooth/*
%{_libdir}/libbluetooth*.a
%exclude %{_libdir}/libbluetooth.la
%{_libdir}/libbluetooth.so
%{_libdir}/pkgconfig/bluez.pc

%changelog
* Sat Aug 07 2004 Dag Wieers <dag@wieers.com> - 2.9-1
- Updated to release 2.9.

* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 2.5-0
- Initial package. (using DAR)
