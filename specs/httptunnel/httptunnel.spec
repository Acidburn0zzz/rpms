# $Id$
# Authority: dag
# Upstream: Lars Brinkhoff <bug-httptunnel$gnu,org>

Summary: Tunnels tcp/ip connections over http
Name: httptunnel
Version: 3.0.5
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.nocrew.org/software/httptunnel.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.nocrew.org/software/httptunnel/httptunnel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
httptunnel creates a bidirectional virtual data path tunnelled in HTTP
requests. The HTTP requests can be sent via an HTTP proxy if so desired.
This can be useful for users behind restrictive firewalls. If WWW access
is allowed through a HTTP proxy, it's possible to use httptunnel and,
say, telnet or PPP to connect to a computer outside the firewall.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog DISCLAIMER FAQ HACKING NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sun Mar 28 2004 Dag Wieers <dag@wieers.com> - 3.0.5-1
- Initial package. (using DAR)
