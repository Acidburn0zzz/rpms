# $Id$
# Authority: dries
# Upstream: T.J. Mather <tjmather$maxmind,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-IP

Summary: Database which maps IP blocks on countries
Name: perl-Geo-IP
Version: 1.28
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-IP/

Source: http://www.cpan.org/modules/by-module/Geo/Geo-IP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: geoip-devel
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module a simple file-based database.  This database simply contains
IP blocks as keys, and countries as values.  The data contains all
public IP addresses and should be more
complete and accurate than reverse DNS lookups.

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
find example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL MANIFEST META.yml README example/
%doc %{_mandir}/man3/Geo::IP.3pm*
%doc %{_mandir}/man3/Geo::IP::Record.3pm*
%doc %{_mandir}/man3/Geo::Mirror.3pm*
%dir %{perl_vendorarch}/Geo/
%{perl_vendorarch}/Geo/IP/
%{perl_vendorarch}/Geo/IP.pm
%{perl_vendorarch}/Geo/Mirror.pm
%dir %{perl_vendorarch}/auto/Geo/
%{perl_vendorarch}/auto/Geo/IP/

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.28-1
- Updated to release 1.28.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.27-1
- Initial package.
