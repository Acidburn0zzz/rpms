# $Id$
# Authority: dag

Summary: waits until specified network resource is available or event has occured
Name: waitfor
Version: 0.5
Release: 1
License: GPL 
Group: Applications/System
URL: http://www.hennessynet.com/waitfor/

Source: http://www.hennessynet.com/waitfor/waitfor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: python2

%description
The waitfor utility will wait until a url is available, until a port is being
listened to, until an amount of time has passed or until a shell command
succeeds. It's very useful when you want to coordinate the startup or
shutdown of services.

%prep
%setup

%build
%{__make} %{?_smp_mflags} waitfor.1

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 waitfor %{buildroot}%{_bindir}/waitfor
%{__install} -D -m0644 waitfor.1 %{buildroot}%{_mandir}/man1/waitfor.1

%clean
%{__rm} -rf %{buildroot}

%files
%doc COPYING INSTALL README
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/waitfor.1*
%{_bindir}/waitfor

%changelog
* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
