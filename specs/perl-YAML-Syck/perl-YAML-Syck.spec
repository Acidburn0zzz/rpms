# $Id$
# Authority: dries
# Upstream: Audrey Tang <cpan$audreyt,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAML-Syck

Summary: Fast YAML loader and dumper
Name: perl-YAML-Syck
Version: 0.99
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-Syck/

Source: http://www.cpan.org/modules/by-module/YAML/YAML-Syck-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.3.7
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.3.7

%description
perl-YAML-Syck contains a fast, lightweight YAML loader and dumper.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/JSON::Syck.3pm*
%doc %{_mandir}/man3/YAML::Syck.3pm*
%dir %{perl_vendorarch}/JSON/
%{perl_vendorarch}/JSON/Syck.pm
%dir %{perl_vendorarch}/YAML/
%dir %{perl_vendorarch}/YAML/Dumper/
%{perl_vendorarch}/YAML/Dumper/Syck.pm
%dir %{perl_vendorarch}/YAML/Loader/
%{perl_vendorarch}/YAML/Loader/Syck.pm
%{perl_vendorarch}/YAML/Syck.pm
%dir %{perl_vendorarch}/auto/YAML/
%{perl_vendorarch}/auto/YAML/Syck/

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.99-1
- Updated to release 0.99.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.72-1
- Updated to release 0.72.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.71-1
- Updated to release 0.71.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.67-1
- Updated to release 0.67.

* Tue May 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.45-1
- Initial package.
