# $Id$
# Authority: dag

### FIXME: Add sysv script and default configuration.

Summary: Virtual private network daemon
Name: tinc
Version: 1.0.8
Release: 1
License: GPL
Group: Applications/Internet
URL: http://tinc.nl.linux.org/

Source: http://tinc.nl.linux.org/packages/tinc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl >= 0.9.7, openssl-devel, lzo-devel

%description
tinc is a Virtual Private Network (VPN) daemon that uses tunnelling
and encryption to create a secure private network between hosts on
the Internet. Because the tunnel appears to the IP level network
code as a normal network device, there is no need to adapt any
existing software. This tunnelling allows VPN sites to share
information with each other over the Internet without exposing any
information to others.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/tincd %{buildroot}%{_sbindir}/tincd
%{__install} -Dp -m0644 doc/tincd.8 %{buildroot}%{_mandir}/man8/tincd.8
%{__install} -Dp -m0644 doc/tinc.conf.5 %{buildroot}%{_mandir}/man5/tinc.conf.5

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README THANKS
%doc doc/sample-config* doc/tinc.info* doc/tinc.texi
%doc %{_mandir}/man5/tinc.conf.5*
%doc %{_mandir}/man8/tincd.8*
%{_sbindir}/tincd

%changelog
* Wed May 16 2007 Dag Wieers <dag@wieers.com> - 1.0.8-1
- Updated to release 1.0.8.

* Wed Jan 10 2007 Dag Wieers <dag@wieers.com> - 1.0.7-1
- Updated to release 1.0.7.

* Tue Dec 19 2006 Dag Wieers <dag@wieers.com> - 1.0.6-1
- Updated to release 1.0.6.

* Wed Nov 05 2006 Dag Wieers <dag@wieers.com> - 1.0.5-1
- Updated to release 1.0.5.

* Wed May 04 2005 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Updated to release 1.0.4.

* Fri Nov 12 2004 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Updated to release 1.0.3.

* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 1.0.2-0
- Updated to release 1.0.2.

* Sat Aug 16 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Initial package. (using DAR)
