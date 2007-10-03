# $Id$
# Authority: dries
# Upstream: Matt Mackall <mpm$selenic,com>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Fast lightweight source control management system
Name: mercurial
Version: 0.9.4
Release: 2
License: GPL
Group: Development/Tools
URL: http://www.selenic.com/mercurial/wiki/

Source: http://www.selenic.com/mercurial/release/mercurial-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.3

%description
Mercurial is a fast, lightweight Source Control Management system designed 
for the efficient handling of very large distributed projects. 

%package hgk
Summary: hgk GUI for mercurial
Group: Development/Tools
Requires: %{name} = %{version}-%{release}

%description hgk
With hgk you can browse a repository graphically.

Add the following to ~/.hgrc and use 'hg view':
[extensions]
hgk=

%prep
%setup

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
%{__make} install-doc PREFIX="%{buildroot}%{_prefix}" MANDIR="%{buildroot}%{_mandir}"
%{__install} contrib/hgk %{buildroot}%{_bindir}/hgk
# TODO: also install other contribs, maybe in subpackage

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CONTRIBUTORS COPYING README contrib/
%doc %{_mandir}/man1/hg.1*
%doc %{_mandir}/man1/hgmerge.1*
%doc %{_mandir}/man5/hgignore.5*
%doc %{_mandir}/man5/hgrc.5*
%{_bindir}/hg
%{_bindir}/hgmerge
%{python_sitearch}/hgext/
%{python_sitearch}/mercurial/

%files hgk
%defattr(-, root, root, 0755)
%{_bindir}/hgk

%changelog
* Wed Oct  3 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.4-2
- Added hgk as a subpackage, based on the PLD spec file started by arekm.

* Fri Jun 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.4-1
- Updated to release 0.9.4.

* Fri Jun 15 2007 Dag Wieers <dag@wieers.com> - 0.9.3-2
- Use %%{python_sitearch} to build for x86_64. (Tong Ho)
- Added contrib/.

* Tue Jun 05 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.3-1
- Initial package.
