# $Id$
# Authority: dag
# Upstream: Alain Tauch <ra$maisondubonheur,com>

%define pyver %(python2 -c 'import sys; print sys.version[:3]')

Summary: Graphical interface for RPM analyze
Name: rpm-analyzer
Version: 1.0
Release: 0.1.r19
License: GPL
Group: Applications/System
URL: http://www.maisondubonheur.com/rpm-analyzer/

Source: http://www.maisondubonheur.com/rpm-analyzer/dl/rpm-analyzer-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: pygtk2, python2, rpm-python, rhpl, libxml2-python
Requires: pygtk2, python2, rpm-python, rhpl, libxml2-python

%description
rpm-analyzer provides a graphical interface that allows the user to view
RPM dependencies according to the local rpm configuration or the
user-defined rpm configuration. This tool is hdlist based and may require
a comps.xml file for some features so please consider installing comps.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m0755 src/rpm-analyzer.py %{buildroot}%{_datadir}/rpm-analyzer/rpm-analyzer.py

%{__install} -dp -m0755 %{buildroot}%{_datadir}/rpm-analyzer/package_mgr/
%{__install} -p -m0644 src/*.py %{buildroot}%{_datadir}/rpm-analyzer/
%{__install} -p -m0644 src/package_mgr/*.py %{buildroot}%{_datadir}/rpm-analyzer/package_mgr/

%{__install} -Dp -m0644 man/rpm-analyzer.1 %{buildroot}%{_mandir}/man1/rpm-analyzer.1

%{__install} -dp -m0755 %{buildroot}%{_bindir}
%{__ln_s} -f %{_datadir}/rpm-analyzer/rpm-analyzer.py %{buildroot}%{_bindir}/rpm-analyzer


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING
%doc %{_mandir}/man1/rpm-analyzer.1*
%{_bindir}/rpm-analyzer
%{_datadir}/rpm-analyzer/

%changelog
* Mon Jun 12 2006 Dag Wieers <dag@wieers.com> - 1.0-0.1.r19
- Use the actual 1.0r19 tarball (was missed because unversioned).

* Fri Jun 09 2006 Dag Wieers <dag@wieers.com> - 1.0-0.r19
- Updated to release 1.0-19.

* Wed Feb 22 2006 Dag Wieers <dag@wieers.com> - 1.0-0.r17
- Updated to release 1.0-17.

* Fri Feb 17 2006 Dag Wieers <dag@wieers.com> - 1.0-0.r15
- Updated to release 1.0-15.

* Wed Aug 20 2003 Dag Wieers <dag@wieers.com> - 1.0-0.r10
- Updated to release 1.0-10.

* Wed Aug 20 2003 Dag Wieers <dag@wieers.com> - 1.0-0.r8
- Initial package. (using DAR)
