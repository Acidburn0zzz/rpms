# $Id$
# Authority: dag
# Upstream: Marcin Wiacek <marcin$mwiacek,com>

%define desktop_vendor rpmforge

Summary: Mobile phone tools
Name: gammu
Version: 1.03.0
Release: 1
License: GPL
Group: Applications/Communications
URL: http://www.gammu.net/

Source: http://www.mwiacek.com/zips/gsm/gammu/stable/1_0x/gammu-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bluez-libs-devel

%description
Gammu can do such things with cellular phones as making data calls,
updating the address book, changing calendar and ToDo entries, sending and
receiving SMS messages, loading and getting ring tones and pictures (different
types of logos), synchronizing time, enabling NetMonitor, managing WAP
settings and bookmarks and much more. Functions depend on the phone model.

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

%{__perl} -pi.orig -e '
		s|^(port) =.*$|$1 = /dev/ttyS0|;
		s|^(connection) =.*$|$1 = dlr3|;
		s|||;
	' docs/examples/config/gammurc

%build
%configure \
	--enable-cb \
	--enable-7110incoming
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} installlib \
	DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 docs/examples/config/gammurc %{buildroot}%{_sysconfdir}/gammurc

%files
%defattr(-, root, root, 0755)
%doc changelog copying docs/docs/ docs/examples/ readme.txt
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/gammurc
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/gammu/

%files devel
%defattr(-, root, root, 0755)
%doc docs/develop/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/gammu/
%{_libdir}/pkgconfig/*.pc
%exclude %{_docdir}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%changelog
* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.03.0-1
- Updated to release 1.03.0.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 0.98.0-1
- Updated to release 0.98.0.

* Tue Jun 15 2004 Dag Wieers <dag@wieers.com> - 0.96.0-1
- Updated to release 0.96.0.

* Wed May 05 2004 Dag Wieers <dag@wieers.com> - 0.95.0-1
- Updated to release 0.95.0.

* Fri Mar 05 2004 Dag Wieers <dag@wieers.com> - 0.94.0-1
- Updated to release 0.94.0.

* Sat Feb 07 2004 Dag Wieers <dag@wieers.com> - 0.93.0-1
- Added BuildRequires for bluez-libs-devel. (So�s P�ter)

* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 0.93.0-0
- Initial package. (using DAR)
