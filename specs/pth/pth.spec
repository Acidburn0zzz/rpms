# $Id: _template.spec 201 2004-04-03 15:24:49Z dag $
# Authority: dag
# Upstream: Ralf S. Engelschall <rse$engelschall,com>

Summary: GNU Portable Threads.
Name: pth
Version: 2.0.1
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.ossp.org/pkg/lib/pth/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.ossp.org/pkg/lib/pth/pth-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Pth is a very portable POSIX/ANSI-C based library for Unix platforms
which provides non-preemptive priority-based scheduling for multiple
threads of execution ("multithreading") inside server applications.
All threads run in the same address space of the server application,
but each thread has it's own individual program-counter, run-time
stack, signal mask and errno variable.

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

%build
%configure
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCE AUTHORS ChangeLog COPYING HISTORY NEWS README SUPPORT
%doc TESTS THANKS USERS
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc HACKING PORTING
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4
%exclude %{_libdir}/*.la

%changelog
* Wed Jul 14 2004 Dag Wieers <dag@wieers.com> - 2.0.1-1
- Updated to release 2.0.1.

* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 2.0.0-1
- Initial package. (using DAR)
