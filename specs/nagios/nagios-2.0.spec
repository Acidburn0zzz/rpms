# $Id$
# Authority: dag
# Upstream: Ethan Galstad <nagios$nagios,org>

# Tag: test

### FIXME: TODO: Add sysv script based on template. (remove cmd-file on start-up)
%define logmsg logger -t %{name}/rpm

%define real_version 2.0b1

Summary: Open Source host, service and network monitoring program
Name: nagios
Version: 2.0
Release: 0.b1
License: GPL
Group: Applications/System
URL: http://www.nagios.org/

Source: http://dl.sf.net/nagios/nagios-%{real_version}.tar.gz
Source1: http://dl.sf.net/nagios/imagepak-base.tar.gz
Patch0: nagios-1.2-embedperl.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gd-devel, zlib-devel, libpng-devel, libjpeg-devel, traceroute
Obsoletes: %{name}-www

%description
Nagios is an application, system and network monitoring application.
It can escalate problems by email, pager or any other medium. It is
also useful for incident or SLA reporting.

Nagios is written in C and is designed as a background process,
intermittently running checks on various services that you specify.

The actual service checks are performed by separate "plugin" programs
which return the status of the checks to Nagios. The plugins are
located in the nagios-plugins package.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{real_version}
#patch0

%{__perl} -pi.orig -e '
		s|^(command_file)=\@localstatedir\@/rw/nagios.cmd|$1=%{_localstatedir}/log/nagios/rw/nagios.cmd|;
		s|^(resource_file)=\@sysconfdir\@/resource.cfg|$1=\@sysconfdir\@/private/resource.cfg|;
	' sample-config/nagios.cfg.in

%{__perl} -pi -e '
		s|/usr/local/nagios/var/rw|%{_localstatedir}/log/nagios/rw|;
		s|/usr/local/nagios/libexec/eventhandlers|%{_libdir}/nagios/plugins/eventhandlers|;
		s|/usr/local/nagios/test/var|%{_localstatedir}/log/nagios|;
	' contrib/eventhandlers/* contrib/eventhandlers/*/*
%build
### FIXME: Disabled embedded perl on RH80 and RH9 to fix segfaults
%configure \
	--datadir="%{_datadir}/nagios" \
	--libexecdir="%{_libdir}/nagios/plugins" \
	--localstatedir="%{_localstatedir}/log/nagios" \
	--sbindir="%{_libdir}/nagios/cgi" \
	--sysconfdir="%{_sysconfdir}/nagios" \
	--with-cgiurl="/nagios/cgi-bin" \
	--with-command-user="apache" \
	--with-command-group="apache" \
	--with-gd-lib="%{_libdir}" \
	--with-gd-inc="%{_includedir}" \
	--with-init-dir="%{_initrddir}" \
	--with-htmurl="/nagios" \
	--with-lockfile="%{_localstatedir}/run/nagios.pid" \
	--with-mail="/bin/mail" \
	--with-nagios-user="nagios" \
	--with-nagios-group="nagios" \
	--enable-embedded-perl \
	--enable-event-broker \
	--enable-embedded-perl \
	--with-perlcache
%{__make} %{?_smp_mflags} all
%{__make} %{?_smp_mflags} -C contrib

%install
%{__rm} -rf %{buildroot}
%{__make} install install-init install-commandmode contrib \
	DESTDIR="%{buildroot}" \
	INSTALL_OPTS="" \
	COMMAND_OPTS="" \
	INIT_OPTS=""

### Install config files
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/nagios/private/ \
%{__install} -m0664 sample-config/{cgi,nagios}.cfg %{buildroot}%{_sysconfdir}/nagios/
%{__install} -m0640 sample-config/resource.cfg %{buildroot}%{_sysconfdir}/nagios/private/
%{__install} -m0664 sample-config/template-object/*.cfg %{buildroot}%{_sysconfdir}/nagios/
#%{__ln_s} -f private/resource.cfg %{buildroot}%{_sysconfdir}/nagios/resource.cfg

#%{__cp} -afpv contrib/eventhandlers/* %{buildroot}%{_libdir}/nagios/plugins/eventhandlers/

### Install logos
tar -xvz -C %{buildroot}%{_datadir}/nagios/images/logos -f %{SOURCE1}

exit 0

%{__install} -d -m0775 %{buildroot}%{_localstatedir}/log/nagios/rw/
%{__install} -d -m0755 %{buildroot}%{_includedir}/nagios/ \
			%{buildroot}%{_libdir}/nagios/cgi/ \
			%{buildroot}%{_sysconfdir}/logrotate.d/ \
			%{buildroot}%{_sysconfdir}/httpd/conf.d/ \
			%{buildroot}%{_sysconfdir}/nagios/private/ \
			%{buildroot}%{_libdir}/nagios/plugins/eventhandlers/
%{__make} install DESTDIR="%{buildroot}" INSTALL_OPTS="" COMMAND_OPTS=""
%{__make} install-daemoninit DESTDIR="%{buildroot}" INSTALL_OPTS="" COMMAND_OPTS="" INIT_OPTS=""

%{__install} -m0644 common/locations.h %{buildroot}%{_includedir}/nagios/
#%{__install} -m0644 common/common.h common/config.h common/locations.h ./cgi/cgiutils.h cgi/popen.h %{buildroot}%{_includedir}/nagios/

### FIXME: Add default .htpasswd file in /etc/nagios/ (in nagios.conf) (Please fix upstream)
%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|' contrib/htaccess.sample
%{__install} -m0644 contrib/htaccess.sample %{buildroot}%{_sysconfdir}/httpd/conf.d/nagios.conf

%pre
if ! /usr/bin/id nagios &>/dev/null; then
	/usr/sbin/useradd -r -d %{_localstatedir}/log/nagios -s /bin/sh -c "nagios" nagios || \
		%logmsg "Unexpected error adding user \"nagios\". Aborting installation."
fi

%post
/sbin/chkconfig --add nagios

if /usr/bin/id apache &>/dev/null; then
	if ! /usr/bin/id -Gn apache 2>/dev/null | grep -q nagios ; then 
		/usr/sbin/usermod -G nagios apache &>/dev/null
	fi
else
	%logmsg "User \"apache\" does not exist and is not added to group \"nagios\". Sending commands to Nagios from the command CGI is not possible."
fi

if [ -f %{_sysconfdir}/httpd/conf/httpd.conf ]; then
	if ! grep -q "Include .*/nagios.conf" %{_sysconfdir}/httpd/conf/httpd.conf; then
		echo -e "\n# Include %{_sysconfdir}/httpd/conf.d/nagios.conf" >> %{_sysconfdir}/httpd/conf/httpd.conf
#		/sbin/service httpd restart
	fi
fi

%preun
if [ $1 -eq 0 ]; then
	/sbin/service nagios stop &>/dev/null || :
	/sbin/chkconfig --del nagios
fi

%postun
if [ $1 -eq 0 ]; then
	/usr/sbin/userdel nagios || %logmsg "User \"nagios\" could not be deleted."
	/usr/sbin/groupdel nagios || %logmsg "Group \"nagios\" could not be deleted."
fi
/sbin/service nagios condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog INSTALLING LICENSE README UPGRADING
%dir %{_sysconfdir}/nagios/
%config(noreplace) %{_sysconfdir}/nagios/*.cfg
%config(noreplace) %{_sysconfdir}/httpd/conf.d/nagios.conf
%config %{_initrddir}/nagios
%{_bindir}/*
%{_libdir}/nagios/
%{_datadir}/nagios/

%defattr(-, root, nagios, 0755)
%config(noreplace) %{_sysconfdir}/nagios/private/

%defattr(-, nagios, nagios, 0755)
%{_localstatedir}/log/nagios/

%defattr(-, nagios, apache, 2755)
%dir %{_localstatedir}/log/nagios/rw/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/nagios/

%changelog
* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 2.0-0.b1
* Updated to release 2.0b1.

* Fri Nov 26 2004 Dag Wieers <dag@wieers.com> - 1.2-1
* Fixed %%{_libdir} in httpd nagios.conf. (Thomas Zehetbauer)

* Wed Feb 11 2004 Dag Wieers <dag@wieers.com> - 1.2-0
- Added embedded perl patch for perl > 5.8. (Stanley Hopcroft)
- Updated to release 1.2.

* Wed Jan 28 2004 Dag Wieers <dag@wieers.com> - 1.1-6
- Fixed the longstanding nagios.cmd problem. (Magnus Stenman)

* Wed Oct 29 2003 Dag Wieers <dag@wieers.com> - 1.1-5
- Fixed resource.cfg location from nagios.cfg. (Ragnar Wisloff)
- Cleaned up perl one-liners.

* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 1.1-4
- Removed --with-file-perfdata, use default. (Erik De Cock)

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 1.1-3
- Fixed the missing @MAIL_PROG@ problem in misccommands.cfg.

* Mon Aug 18 2003 Dag Wieers <dag@wieers.com> - 1.1-2
- Let %pre silently check for user nagios.
- Added base imagepak.

* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 1.1-1
- Disabled embedded perl.

* Wed Jun 04 2003 Dag Wieers <dag@wieers.com> - 1.1-0
- Updated to release 1.1.

* Tue Jun 03 2003 Dag Wieers <dag@wieers.com> - 1.0-1
- Don't restart webserver.

* Sun Feb 16 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
