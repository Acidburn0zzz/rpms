# $Id$
# Authority: matthias

%define confdir %{_sysconfdir}/postfix

Summary: Postfix Greylisting Policy Server
Name: postgrey
Version: 1.30
Release: 2
License: GPL
Group: System Environment/Daemons
URL: http://postgrey.schweikert.ch/
#URL: http://isg.ee.ethz.ch/tools/postgrey/

Source0: http://postgrey.schweikert.ch/pub/postgrey-%{version}.tar.gz
#Source0: http://isg.ee.ethz.ch/tools/postgrey/pub/postgrey-%{version}.tar.gz
Source1: postgrey.init
Source2: README-rpm
Patch0: postgrey-1.30-group.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

# We require postfix for its directories and gid
Requires: postfix
# This module seems to be a weak dependency from Net::Server, so we need to
# explicitly require it or it won't get installed.
Requires: perl(IO::Multiplex)
Requires(pre): /usr/sbin/useradd
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service, /sbin/chkconfig
Requires(postun): /sbin/service

%description
Postgrey is a Postfix policy server implementing greylisting.  When a request
for delivery of a mail is received by Postfix via SMTP, the triplet CLIENT_IP /
SENDER / RECIPIENT is built.  If it is the first time that this triplet is
seen, or if the triplet was first seen less than 5 minutes, then the mail gets
rejected with a temporary error. Hopefully spammers or viruses will not try
again later, as it is however required per RFC.

%prep
%setup
%patch0 -p1 -b .group
%{__install} -p -m0644 %{SOURCE2} README-rpm

%build
# We only have perl scripts, so just "build" the man page
pod2man \
    --center="Postgrey Policy Server for Postfix" \
    --section="8" \
    postgrey > postgrey.8

%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m0644 postgrey_whitelist_clients %{buildroot}%{confdir}/postgrey_whitelist_clients
%{__install} -Dp -m0644 postgrey_whitelist_recipients %{buildroot}%{confdir}/postgrey_whitelist_recipients
%{__install} -Dp -m0755 postgrey %{buildroot}%{_sbindir}/postgrey
%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_initrddir}/postgrey
%{__install} -Dp -m0644 postgrey.8 %{buildroot}%{_mandir}/man8/postgrey.8
%{__install} -Dp -m0755 contrib/postgreyreport %{buildroot}%{_sbindir}/postgreyreport

%{__mkdir_p} %{buildroot}%{_var}/spool/postfix/postgrey
touch %{buildroot}%{confdir}/postgrey_whitelist_clients.local

%clean
%{__rm} -rf %{buildroot}

%pre
/usr/sbin/useradd -d %{_var}/spool/postfix/postgrey -s /sbin/nologin \
    -M -r postgrey &>/dev/null || :

%post
/sbin/chkconfig --add postgrey

%preun
if [ $1 -eq 0 ]; then
    /sbin/service postgrey stop &>/dev/null || :
    /sbin/chkconfig --del postgrey
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service postgrey condrestart &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc Changes COPYING README README-rpm
%doc %{_mandir}/man8/postgrey.8*
%config %{_initrddir}/postgrey
%config(noreplace) %{confdir}/postgrey_whitelist_clients
%config(noreplace) %{confdir}/postgrey_whitelist_recipients
%config(noreplace) %{confdir}/postgrey_whitelist_clients.local
%{_sbindir}/postgrey
%{_sbindir}/postgreyreport

%defattr(0751, postgrey, postfix, 0751)
%dir %{_var}/spool/postfix/postgrey/

%changelog
* Mon Aug 06 2007 Dag Wieers <dag@wieers.com> - 1.30-2
- Readded nogroup patch. (What was I thinking ?)

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 1.30-1
- Updated to release 1.30.

* Mon Dec  4 2006 Matthias Saou <http://freshrpms.net/> 1.27-3
- Add man page generation (Mike Wohlgemuth).

* Fri Dec  1 2006 Matthias Saou <http://freshrpms.net/> 1.27-2
- Include postgreyreport script.

* Mon Nov  6 2006 Matthias Saou <http://freshrpms.net/> 1.27-1
- Spec file cleanup.

* Wed Jan 18 2006 Levente Farkas <lfarkas@lfarkas.org> 1.24
- some minor changes thanks to Peter Bieringer <pb@bieringer.de>

* Mon Jan 16 2006 Levente Farkas <lfarkas@lfarkas.org> 1.24
- upgrade to 1.24

* Sun Nov 13 2005 Levente Farkas <lfarkas@lfarkas.org> 1.22
- upgrade to 1.22

* Mon Aug 22 2005 Levente Farkas <lfarkas@lfarkas.org> 1.21
- spec file update from Luigi Iotti <luigi@iotti.biz>

* Thu Apr 28 2005 Levente Farkas <lfarkas@lfarkas.org> 1.21
- update to 1.21

* Tue Mar  8 2005 Levente Farkas <lfarkas@lfarkas.org> 1.18
- update to 1.18

* Tue Dec 14 2004 Levente Farkas <lfarkas@lfarkas.org> 1.17
- update to 1.17

* Wed Jul 14 2004 Levente Farkas <lfarkas@lfarkas.org> 1.14
- guard the pre and post scripts

* Wed Jul  7 2004 Levente Farkas <lfarkas@lfarkas.org> 1.13
- initial release 1.13
