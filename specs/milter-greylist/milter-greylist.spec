# $Id$
# Authority: dries
# Upstream: http://groups.yahoo.com/group/milter-greylist/

Summary: Stand-alone milter written in C that implements greylist filtering
Name: milter-greylist
Version: 3.0
Release: 1
License: BSD
Group: System Environment/Daemons
URL: http://hcpnet.free.fr/milter-greylist/

Source: ftp://ftp.espci.fr/pub/milter-greylist/milter-greylist-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: sendmail-devel >= 8.11

%description
milter-greylist is a stand-alone milter written in C that implements the 
greylist filtering method, as proposed by Evan Harris. 

Grey listing works by assuming that, unlike legitimate MTA, spam engines 
will not retry sending their junk mail on a temporary error. The filter 
will always reject mail temporarily on a first attempt, then accept it 
after some time has elapsed.

If spammers ever try to resend rejected messages, we can assume they will 
not stay idle between the two sends (if they do, the spam problem would 
just be solved). Odds are good that the spammer will send a mail to a honey 
pot address and get blacklisted in several real-time distributed black lists 
before the second attempt.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -D milter-greylist.m4 %{buildroot}%{_datadir}/sendmail-cf/feature/milter-greylist.m4
%{__install} -D rc-redhat.sh %{buildroot}%{_initrddir}/milter-greylist

%post
/sbin/chkconfig --add milter-greylist

%preun
if [ $1 -eq 0 ]; then
	/sbin/service milter-greylist stop &>/dev/null || :
	/sbin/chkconfig --del milter-greylist
fi

%postun
/sbin/service milter-greylist condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man5/greylist.conf.5*
%doc %{_mandir}/man8/milter-greylist.8*
%config(noreplace) %{_sysconfdir}/mail/greylist.conf
%{_initrddir}/milter-greylist
%{_bindir}/milter-greylist
%dir %{_localstatedir}/milter-greylist/
%{_datadir}/sendmail-cf/feature/milter-greylist.m4

%changelog
* Mon Sep 24 2007 Dries Verachtert <dries@ulyssis.org> - 3.0-1
- Initial package, based on the spec file made by Ivan F. Martinez.
