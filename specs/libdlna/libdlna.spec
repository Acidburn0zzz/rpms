# $Id$
# Authority: dag
# Upstream: Benjamin Zores <ben$geexbox,org>

Summary: Implementation of Digital Living Network Alliance (DLNA) standards
Name: libdlna
Version: 0.2.2
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://libdlna.geexbox.org/

Source: http://libdlna.geexbox.org/releases/libdlna-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
libdlna aims at being the reference open-source implementation of DLNA
(Digital Living Network Alliance) standards. Its primary goal is to
provide DLNA support to uShare, an embedded DLNA & UPnP A/V Media Server,
but it will be used to build both DLNA servers and players in the long term.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' config.mak

%build
./configure \
    --disable-static \
    --libdir="%{_libdir}" \
    --prefix="%{_prefix}"
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
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libdlna.so.*

%files devel
%{_includedir}/dlna.h
%{_libdir}/libdlna.so
%{_libdir}/pkgconfig/libdlna.pc

%changelog
* Sun Nov 25 2007 Dag Wieers <dag@wieers.com> - 0.2.2-1
- Updated to release 0.2.2.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.2.1-1
- Initial package. (using DAR)
