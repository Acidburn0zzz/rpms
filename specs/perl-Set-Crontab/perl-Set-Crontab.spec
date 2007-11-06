# $Id$
# Authority: dries
# Upstream: Abhijit Menon-Sen <ams@wiw.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Set-Crontab

Summary: Expand crontab(5)-style integer lists
Name: perl-Set-Crontab
Version: 1.00
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Set-Crontab/

BuildArch: noarch
Source: http://www.cpan.org/modules/by-module/Set/Set-Crontab-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Set::Crontab parses crontab-style lists of integers and defines
some utility functions to make it easier to deal with them.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Set/
%{perl_vendorlib}/Set/Crontab.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.00-1.2
- Rebuild for Fedora Core 5.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
