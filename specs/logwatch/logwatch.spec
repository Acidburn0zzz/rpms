# $Id$
# Authority: dag
# Upstream: Kirk Bauer <kirk@kaybee.org>

Summary: Log file analysis program
Name: logwatch
Version: 5.1
Release: 3
License: MIT
Group: Applications/System
URL: http://www.logwatch.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.kaybee.org/pub/linux/logwatch-%{version}.tar.gz
Patch: logwatch-4.3.2-nounicode.patch
Patch1: logwatch-4.3.2-nosegfault.patch
Patch3: logwatch-5.1-catchlocal.patch
Patch9: logwatch-5.1-RejectedAtt.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: perl, textutils, sh-utils, grep, mailx

%description
Logwatch is a customizable, pluggable log-monitoring system. LogWatch parses
through your system's logs for a given period of time and creates a report
analyzing areas that you specify, in as much detail as you require.

%prep
%setup
%patch -p1
%patch1 -p1
%patch3 -p1
%patch9 -p1

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 scripts/logwatch.pl %{buildroot}%{_sysconfdir}/log.d/scripts/logwatch.pl

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/log.d/scripts/services/
%{__install} -m0755 scripts/services/* %{buildroot}%{_sysconfdir}/log.d/scripts/services/

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/log.d/scripts/shared/
%{__install} -m0755 scripts/shared/* %{buildroot}%{_sysconfdir}/log.d/scripts/shared/

for file in scripts/logfiles/* ; do
	if [ $(ls $file | wc -l) -ne 0 ] ; then
		%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/log.d/$file
		%{__install} -m0755 $file/* %{buildroot}%{_sysconfdir}/log.d/$file
	fi
done

%{__install} -D -m0644 conf/logwatch.conf %{buildroot}%{_sysconfdir}/log.d/conf/logwatch.conf
%{__install} -D -m0644 logwatch.8 %{buildroot}%{_mandir}/man8/logwatch.8
%{__install} -D -m0644 lib/Logwatch.pm %{buildroot}%{_sysconfdir}/log.d/lib/Logwatch.pm

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/log.d/conf/logfiles/
%{__install} -m0644 conf/logfiles/* %{buildroot}%{_sysconfdir}/log.d/conf/logfiles/

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/log.d/conf/services/
%{__install} -m0644 conf/services/* %{buildroot}%{_sysconfdir}/log.d/conf/services/

%{__ln_s} -f scripts/logwatch.pl %{buildroot}%{_sysconfdir}/log.d/logwatch
%{__ln_s} -f conf/logwatch.conf %{buildroot}%{_sysconfdir}/log.d/

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/cron.daily/
%{__ln_s} -f ../log.d/scripts/logwatch.pl %{buildroot}%{_sysconfdir}/cron.daily/00-logwatch

%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__ln_s} -f ../..%{_sysconfdir}/log.d/scripts/logwatch.pl %{buildroot}%{_sbindir}/logwatch

#%{__rm} -f %{buildroot}%{_sysconfdir}/log.d/logwatch \
#   %{buildroot}%{_sysconfdir}/log.d/logwatch.conf \
#   %{buildroot}%{_sysconfdir}/cron.daily/logwatch \
#   %{buildroot}%{_sbindir}/logwatch

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc License project/CHANGES project/TODO
%doc README HOWTO-Make-Filter
%doc %{_mandir}/man8/*
%config %{_sysconfdir}/log.d/
%config %{_sysconfdir}/cron.daily/00-logwatch
%{_sbindir}/*

%changelog
* Wed May 12 2004 Dag Wieers <dag@wieers.com> - 5.1-3
- Moved the logwatch manpage to the correct location. (Matthew Lenz)

* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 5.1-2
- Fixed the perl(Logwatch) problem.
- Updated to release 5.1.

* Thu Mar 27 2003 Dag Wieers <dag@wieers.com> - 4.3.2-0
- Initial package. (using DAR)
