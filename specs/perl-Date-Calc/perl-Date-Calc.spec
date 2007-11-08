# $Id$
# Authority: dag
# Upstream: Steffen Beyer <sb$engelschall,com>

# ExclusiveDist: el3

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Calc

Summary: Gregorian calendar date calculations
Name: perl-Date-Calc
Version: 5.4
Release: 1
License: Artistic/GPL/LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Calc/

Source: http://www.cpan.org/modules/by-module/Date/Date-Calc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Gregorian calendar date calculations

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Artistic.txt CHANGES.txt CREDITS.txt EXAMPLES.txt GNU_GPL.txt GNU_LGPL.txt INSTALL.txt MANIFEST README.txt TOOLS.txt examples/
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/Date/
%{perl_vendorarch}/auto/Date/

%changelog
* Tue Sep 13 2005 Dag Wieers <dag@wieers.com> - 5.4-1
- Initial package. (using DAR)
