# $Id$
# Authority: dries

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name psycopg2

Summary: PostgreSQL database adapter for Python
Name: python-psycopg2
Version: 2.0.4
Release: 1
License: GPL/ZPL
Group: Development/Libraries
URL: http://initd.org/tracker/psycopg

Source: http://initd.org/pub/software/psycopg/psycopg2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python >= 2.2, python-devel, postgresql-devel, mx

%description
psycopg is a PostgreSQL database adapter for the Python programming
language. Its main advantages are that it supports the full Python
DBAPI 2.0 and it is thread safe at level 2. It was designed for heavily
multi-threaded applications that create and destroy lots of cursors and
make a conspicuous number of concurrent INSERTs or UPDATEs. The psycopg
distribution includes ZPsycopgDA, a Zope Database Adapter.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL README  doc/*
%{python_sitearch}/psycopg*

%changelog
* Sun Aug 13 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.4-2
- Renamed to python-psycopg2.

* Thu Aug 03 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.4-1
- Updated to release 2.0.4.

* Mon Jul 31 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.3-1
- Updated to release 2.0.3.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.21-1.2
- Rebuild for Fedora Core 5.

* Fri Jan 06 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.21-1
- Updated to release 1.1.21.

* Tue Sep 13 2005 Dries Verachtert <dries$ulyssis.org> - 1.1.20-1
- Initial package.
