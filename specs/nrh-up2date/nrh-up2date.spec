# Authority: dag
# Upstream: 

Summary: Open Source server for Redhat's up2date suite.
Name: nrh-up2date
Version: 1.3
Release: 0
License: GPL
Group: Applications/System
URL: http://www.nrh-up2date.org

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.nrh-up2date.org/download/nrh-up2date-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
Requires: perl, perl-Frontier-RPC, perl-XML-Parser, perl-BerkeleyDB, python, python-bsddb3
%{?rhfc1:Requires: httpd, rpm, rpm-python, db4}
%{?rhel3:Requires: httpd, rpm, rpm-python, db4}
%{?rh90:Requires: httpd, librpm404, rpm404-python, db4}
%{?rh80:Requires: httpd, librpm404, rpm404-python, db4}
%{?rh73:Requires: apache, python-xmlrpc, db3, perl-Digest-MD5}
%{?rhas21:Requires: apache, python-xmlrpc, db3, perl-Digest-MD5}
%{?rh62:Requires: apache, python-xmlrpc, db3, perl-Digest-MD5}

%description
NRH-up2date is a collection of utilities to use with RedHat's up2date 
client without relying on the RedHat network servers. NRH-up2date is 
implemented to provide an up2date server for a basic user, that wishes
to cache RHN content locally in his LAN (or central server), so each 
client in that site wouldn't have to connect to RedHat network for
updates, waisting your bandwidth. 

%prep 
%setup

%{__perl} -pi.orig -e '
		s|\$\(INSTALL_ROOT\)|\$(DESTDIR)|g;
		s|\$\(PREFIX\)/share|\$(datadir)|g;
		s|\$\(PREFIX\)/sbin|\$(sbindir)|g;
		s|/etc|\$(sysconfdir)|g;
		s|/var|\$(localstatedir)|g;
	' Makefile

%build

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	DOCS_DIR="./doc-rpm"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc-rpm/*
%config(noreplace) %{_sysconfdir}/nrh-up2date/
%{_sbindir}/*
%{_datadir}/nrh-up2date/
%{_localstatedir}/spool/nrh-up2date/

%changelog
* Tue Mar 02 2004 Dag Wieers <dag@wieers.com> - 1.3-0
- Initial package. (using DAR)
