# $Id$
# Authority: dag
# Upstream: Jordan Ritter <jpr5$darkridge,com>

%{?dist: %{expand: %%define %dist 1}}

Summary: Realtime network grep tool
Name: ngrep
Version: 1.43
Release: 1
License: GPL
Group: Applications/Internet
URL: http://ngrep.sourceforge.net/

Source: http://dl.sf.net/ngrep/ngrep-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap

%description
ngrep is grep command that works on realtime network data.

ngrep strives to provide most of GNU grep's common features, applying
them to the network layer. ngrep is a pcap-aware tool that will allow
you to specify extended regular or hexadecimal expressions to match
against data payloads of packets. It currently recognizes TCP, UDP
and ICMP across Ethernet, PPP, SLIP, FDDI, Token Ring and null
interfaces, and understands bpf filter logic in the same fashion as
more common packet sniffing tools, such as tcpdump and snoop.

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
%doc *.txt doc/*.txt scripts/
%doc %{_mandir}/man8/ngrep.8*
%{_bindir}/ngrep

%changelog
* Wed Feb 23 2005 Dag Wieers <dag@wieers.com> - 1.43-1
- Updated to release 1.43.

* Mon Mar 29 2004 Dag Wieers <dag@wieers.com> - 1.42-1
- Updated to release 1.42.

* Mon Aug 11 2003 Dag Wieers <dag@wieers.com> - 1.41-0
- Updated to release 1.41.

* Thu Jul 17 2003 Dag Wieers <dag@wieers.com> - 1.40.1-0
- Initial package. (using DAR)
