# $Id$
# Authority: dag
# Upstream: <squidguard$squidguard,org>

%{?dist: %{expand: %%define %dist 1}}

%define real_name squidGuard
%define dbhomedir %{_localstatedir}/lib/squidguard

Summary: Combined filter, redirector and access controller plugin for squid
Name: squidguard
Version: 1.2.0
Release: 2
License: GPL
Group: System Environment/Daemons
URL: http://www.squidguard.org/

Source: http://ftp.teledanmark.no/pub/www/proxy/squidGuard/squidGuard-%{version}.tar.gz
Patch0: squidguard-1.2.0-db4.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison, flex, perl
%{?fc4:BuildRequires: db4-devel}
%{?fc3:BuildRequires: db4-devel}
%{?fc2:BuildRequires: db4-devel}
%{?fc1:BuildRequires: db4-devel}
%{?el3:BuildRequires: db4-devel}
%{?rh9:BuildRequires: db4-devel}
%{?rh8:BuildRequires: db4-devel}
%{?rh7:BuildRequires: db3-devel}
%{?el2:BuildRequires: db3-devel}
Requires: squid
Obsoletes: squidGuard
Provides: squidGuard

%description
squidGuard is a combined filter, redirector and access controller
plugin for squid. squidGuard can be used to limit or block access
users to a list of webservers, based on keywords.

%prep
%setup -n %{real_name}-%{version}
%patch0
#{?fc3:%patch0}
#{?fc2:%patch0}
#{?fc1:%patch0}
#{?el3:%patch0}

%{__perl} -pi.orig -e '
		s|^(dbhome) .+$|$1 \@sg_dbhome\@|;
		s|^(logdir) .+$|$1 \@sg_logdir\@|;
	' samples/sample.conf.in

%{__perl} -pi.orig -e '
		s|\$\(logdir\)|\$(localstatedir)/log/squidguard|;
		s|\$\(cfgdir\)|\$(sysconfdir)/squid|;
	' src/Makefile.in

%{__cat} <<EOF >%{name}.logrotate
%{_localstatedir}/log/squid/squidguard.log {
	missingok
	copytruncate
	notifempty
}
EOF

%build
%configure \
	--with-sg-config="%{_sysconfdir}/squid/squidguard.conf" \
	--with-sg-logdir="%{_localstatedir}/log/squidguard" \
	--with-sg-dbhome="%{dbhomedir}"
%{__make} %{?_smp_mflags} \
	LIBS="-ldb -lpthread"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0644 squidguard.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/squidguard
%{__install} -Dp -m0644 samples/sample.conf %{buildroot}%{_sysconfdir}/squid/squidguard.conf
%{__ln_s} -f squidGuard %{buildroot}%{_bindir}/squidguard

%{__install} -d -m0755 \
	%{buildroot}%{dbhomedir} \
	%{buildroot}%{_localstatedir}/log/squidguard/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc samples/sample.conf samples/squidGuard-simple.cgi samples/squidGuard.cgi
%doc doc/*.txt doc/*.html doc/*.gif
%config(noreplace) %{_sysconfdir}/squid/
%config %{_sysconfdir}/logrotate.d/*
%{_bindir}/*
%{dbhomedir}
%{_localstatedir}/log/squidguard/

%changelog
* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 1.2.0-2
- Added patch for db4 (RHEL3 and RHFC1). (Tom Gordon)

* Sat Apr 12 2003 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Removed the default blacklists.

* Thu Jan 09 2003 Dag Wieers <dag@wieers.com> - 1.2.0-0
- Initial package. (using DAR)
