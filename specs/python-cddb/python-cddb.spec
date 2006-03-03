# $Id$
# Authority: dries

%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name CDDB

Summary: Fetch information about audio cd's
Name: python-cddb
Version: 1.4
Release: 1
License: GPL
Group: Applications/Internet
URL: http://cddb-py.sourceforge.net/

Source: http://dl.sf.net/cddb-py/CDDB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel

%description
This is a set of three modules to access the CDDB and FreeDB online 
databases of audio CD track titles and information.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%{python_sitearch}/CDDB.py*
%{python_sitearch}/DiscID.py*
%{python_sitearch}/cdrom.so

%changelog
* Fri Mar 03 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
