# $Id$
# Authority: dries

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Object shell
Name: osh
Version: 0.8.1
Release: 1
License: GPL
Group: System Environment/Shells
URL: http://geophile.com/osh/index.html

Source: http://geophile.com/osh/osh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python

%description
Object Shell (osh) is the interpreter for a Python-like language that 
supports the composition of commands through piping, similar to pipes 
in a Unix shell. However, the key difference is that objects are 
passed through the pipes in osh instead of streams of text. The objects 
passed between commands can be Python built-ins or complex objects such 
as dates and times, database rows, or OS resources. Objects can be 
automatically converted to strings for integration with the conventional 
Unix environment.

%prep
%setup
# it tries to install ../osh-%{version}.tar.gz in the datadir
%{__perl} -pi -e "s|, .\.\.\/osh-%{version}.tar.gz.||g;" setup.py

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
%{__mv} %{buildroot}%{_datadir}/doc/osh rpm-docs

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc rpm-docs/*
%{_bindir}/osh
%{_bindir}/oshtestssh
%{_bindir}/remoteosh
%{python_sitelib}/osh/
%{_datadir}/osh/

%changelog
* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.1-1
- Updated to release 0.8.1.

* Mon Jan 08 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.0-1
- Updated to release 0.8.0.

* Fri Apr 28 2006 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Updated to release 0.7.

* Fri Feb 17 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.3-1
- Updated to release 0.6.3.

* Fri Dec 16 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.2-1
- Initial package.
