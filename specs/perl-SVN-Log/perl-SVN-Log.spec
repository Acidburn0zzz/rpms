# $Id$
# Authority: dries
# Upstream: Garrett Rooney <rooneg$electricjellyfish,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVN-Log

Summary: Extract change logs from a Subversion server
Name: perl-SVN-Log
Version: 0.02
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Log/

Source: http://search.cpan.org/CPAN/authors/id/R/RO/ROONEG/SVN-Log-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build, subversion-perl

%description
SVN::Log retrieves and parses the commit logs from Subversion
repositories.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/SVN/
%{perl_vendorlib}/SVN/Log.pm

%changelog
* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Updated to release 0.02.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
