# $id$
# Authority: dag
# Upstream: Rick Jones <netperf-feedback$netperf,org>

Summary: Performance testing tool for TCP/UDP
Name: netperf
Version: 2.4.2
Release: 1
License: BSD
Group: Applications/Internet
URL: http://www.netperf.org/netperf/NetperfPage.html 

Source: ftp://ftp.netperf.org/netperf/netperf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Netperf is a tool to measure TCP/UDP performance.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/install-info %{_infodir}/${infofile} %{_infodir}/dir 2>/dev/null || :

%preun
/sbin/install-info --delete %{_infodir}/${infofile} %{_infodir}/dir 2>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc COPYING README Release_Notes
%doc %{_mandir}/man1/netperf.1*
%doc %{_mandir}/man1/netserver.1*
%doc %{_infodir}/netperf.*
%{_bindir}/netperf
%{_bindir}/netserver

%changelog
* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 2.4.2-1
- Initial package. (using DAR)
