# $Id$
# Authority: dag

# ExcludeDist: el4

Summary: Library for tracking application startup
Name: startup-notification
Version: 0.5
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://www.freedesktop.org/software/startup-notification/

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
This package contains libstartup-notification which implements a
startup notification protocol. Using this protocol a desktop
environment can track the launch of an application and provide
feedback such as a busy cursor, among other features.

%package devel
Summary: Libraries and include files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel	
Development files for %{name}

%prep
%setup

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
%doc AUTHORS ChangeLog NEWS README doc/startup-notification.txt
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/startup-notification-1.0/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%exclude %{_libdir}/*.la

%changelog
* Tue Feb 11 2003 Dag Wieers <dag@wieers.com> - 0.5-0
- Initial package. (using DAR)
