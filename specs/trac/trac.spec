# $Id$
# Authority: dag
# Upstream: <trac$lists,edgewall,com>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Name: trac
Summary: Integrated SCM and project management tool
Version: 0.10.4
Release: 1
License: GPL
Group: Development/Tools
URL: http://projects.edgewall.com/trac/

Source: http://ftp.edgewall.com/pub/trac/trac-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.3
Requires: python >= 2.3, python-sqlite >= 0.4.3, subversion >= 1.0.0
Requires: python-clearsilver >= 0.9.3, webserver
#Requires: subversion-python >= 1.0.0

%description
Trac is a minimalistic web-based software project management and
bug/issue tracking system. It provides an interface to revision
control systems (Subversion), an integrated Wiki and convenient
report facilities.

Trac allows wiki markup in issue descriptions and commit messages,
to create links and seamless references between bugs, tasks,
changesets, files and wiki pages. A timeline shows all project
events in order, making getting an overview of the project and
tracking progress very easy.

%prep
%setup

%{__perl} -pi.orig -e 's|/usr/lib/|%{_libdir}|g' setup.py

%{__cat} <<EOF >trac.httpd
Alias /trac/ "%{_datadir}/trac/htdocs/"

### Trac need to know where the database is located
<Location "/cgi-bin/trac.cgi">
	SetEnv TRAC_ENV "%{_datadir}/trac/myproject.db"
</Location>

### You need this to allow users to authenticate
<Location "/cgi-bin/trac.cgi/login">
	AuthType Basic
	AuthName "trac"
	AuthUserFile %{_datadir}/trac/trac.htpasswd
	Require valid-user
</location>
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}"

%{__install} -Dp -m0644 trac.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/trac.conf
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/trac/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README THANKS UPGRADE
%doc %{_mandir}/man1/trac*.1*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/trac.conf
%{_bindir}/trac*
%{_datadir}/trac/
%{python_sitelib}/trac/
%{_localstatedir}/lib/trac/

%changelog
* Fri Apr 27 2007 Dag Wieers <dag@wieers.com> - 0.10.4-1
- Updated to release 0.10.4.

* Sat Mar 10 2007 Dag Wieers <dag@wieers.com> - 0.10.3.1-1
- Updated to release 0.10.3.1.

* Wed Dec 13 2006 Dag Wieers <dag@wieers.com> - 0.10.3-1
- Updated to release 0.10.3.

* Wed Nov 15 2006 Dag Wieers <dag@wieers.com> - 0.10.2-1
- Updated to release 0.10.2.

* Thu Nov 09 2006 Dag Wieers <dag@wieers.com> - 0.10.1-1
- Updated to release 0.10.1.

* Sat Sep 30 2006 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Sun Jul 09 2006 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release 0.9.6.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1
- Updated to release 0.9.5.

* Sat Feb 18 2006 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Wed Jan 11 2006 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Tue Dec 06 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.2-1
- Updated to release 0.9.2.

* Tue Nov 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Tue Jul 19 2005 Dag Wieers <dag@wieers.com> - 0.8.4-1
- Updated to release 0.8.4.

* Mon Jul 11 2005 Matt Whiteley <mattw@cat.pdx.edu> - 0.8.3-1
- Updated to release 0.8.3.

* Wed Jun 01 2005 Matt Whiteley <mattw@cat.pdx.edu> - 0.8.2-1
- Updated to release 0.8.2.
- Fixed env in apache conf.d file.

* Fri Mar 04 2005 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.

* Wed Jan 19 2005 Dag Wieers <dag@wieers.com> - 0.8-4
- Fixed typo causing missing trac.conf. (Simon Perreault)

* Mon Nov 29 2004 Dag Wieers <dag@wieers.com> - 0.8-3
- Fixed buildroot in %%install phase. (Dimiter Manevski)

* Mon Nov 29 2004 Dag Wieers <dag@wieers.com> - 0.8-2
- Remove the deprecated subversion-python requirement. (Dimiter Manevski)

* Sun Nov 21 2004 Dag Wieers <dag@wieers.com> - 0.8-1
- Updated to release 0.8.

* Fri Jun 04 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Sun May 30 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Initial package. (using DAR)
