# $Id$

# Authority: dag

# Upstream: Paul A. Balyoz <pab@domtools.com>

Summary: A DNS error checking utility.
Name: dlint
Version: 1.4.0
Release: 0
License: GPL
Group: Applications/Internet
URL: http://www.domtools.com/dns/dlint.shtml

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.domtools.com/pub/%{name}%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch

%description
This program analyzes any DNS zone you specify, and reports any
problems it finds by displaying errors and warnings.  Then it descends
recursively to examine all zones below the given one (this can be
disabled with a command-line option).

%prep
%setup -n %{name}%{version}

%{__perl} -pi.orig -e 's|(rrfilt=)"/usr/local/bin/digparse"|$1"%{_bindir}/digparse"|' dlint

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/
%makeinstall \
	BIN="%{buildroot}%{_bindir}" \
	MAN="%{buildroot}%{_mandir}/man1"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES COPYING COPYRIGHT README TESTCASES
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Wed Sep 03 2003 Dag Wieers <dag@wieers.com> - 1.4.0-0
- Initial package. (using DAR)
