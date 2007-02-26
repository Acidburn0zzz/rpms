# $Id: nttlscan.spec 4899 2006-11-18 23:37:30Z dag $
# Authority: dag
# Upstream:

%{?dist: %{expand: %%define %dist 1}}

%{!?dist:%define _with_libpcapdevel 1}
%{?fc7:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Quick network topology scanner
Name: nttlscan
Version: 0.1
Release: 2
License: GPL
Group: Applications/Internet
URL: http://www.honeyd.org/tools.php

Source: http://www.honeyd.org/data/nttlscan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap, libdnet-devel, libevent-devel
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Nttlscan is a quick network topology scanner and functions as a highly
parallel traceroute. It randomly picks destination IP addresses and
sends TCP or UDP probes. Returing ICMP messages are interpreted to
reconstruct the route that packets take to their respective destination.
Nttlscan can be used to construct virtual routing topologies for Honeyd.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/nttlscan.1*
%{_bindir}/nttlscan

%changelog
* Tue Feb 20 2007 Dag Wieers <dag@wieers.com> - 0.1-2
- Rebuild against libevent-1.3a.
- Added missing BuildRequires. (Robert Hardy)

* Sat Jul 10 2004 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
