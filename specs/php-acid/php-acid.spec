# $Id$
# Authority: dag

%define real_name acid

Summary: Analysis Console for Intrusion Databases 
Name: php-acid
Version: 0.9.6b22
Release: 1
License: GPL
Group: Applications/Internet
URL: http://acidlab.sourceforge.net/

Source: http://dl.sf.net/acidlab/acid-%{version}.tar.gz
Source1: acid.conf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: webserver, php, php-adodb, php-jpgraph

Obsoletes: %{real_name}
Provides: %{real_name}

%description
The Analysis Console for Intrusion Databases (ACID) is a PHP-based analysis
engine to search and process a database of security events generated by
various IDSes, firewalls, and network monitoring tools including: Snort
alerts, tcpdump binary logs, ipchians, iptables, and ipfw.

%prep
%setup -n %{real_name}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/acid.conf

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/acid/
%{__install} -p acid_* %{buildroot}%{_localstatedir}/www/acid/
touch %{buildroot}%{_localstatedir}/www/acid-users

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG create_acid_tbls_*.sql CREDITS index.html README* TODO
%config %{_sysconfdir}/httpd/conf.d/acid.conf
%config(noreplace) %{_localstatedir}/www/acid/acid_conf.php
%{_localstatedir}/www/acid/acid_*
%defattr(0640, root, apache)
%{_localstatedir}/www/acid-users

%changelog
* Sun Feb 16 2003 Dag Wieers <dag@wieers.com> - 0.9.6b22-0
- Initial package. (using DAR)
