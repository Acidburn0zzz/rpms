# $Id$
# Authority: dag
# Upstream: Michael G Schwern <schwern$pobox,com>

# ExclusiveDist: el2 rh7 rh9 el3

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-MakeMaker

Summary: Create a module Makefile
Name: perl-ExtUtils-MakeMaker
Version: 6.36
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-MakeMaker/

Source: http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-MakeMaker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a CPAN distribution of the venerable MakeMaker module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml NOTES README SIGNATURE TODO
%doc %{_mandir}/man1/instmodsh.1*
%doc %{_mandir}/man3/ExtUtils::*.3pm*
%{_bindir}/instmodsh
%{perl_vendorlib}/ExtUtils/

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 6.36-1
- Updated to release 6.36.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 6.30-1
- Updated to release 6.30.

* Sat Apr 02 2005 Dag Wieers <dag@wieers.com> - 6.17-1
- Initial package. (using DAR)
