# $Id$
# Authority: dries
# Upstream: Edwin Pratomo <edwin$poskanzer,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-Permute

Summary: Fast permutation
Name: perl-Algorithm-Permute
Version: 0.06
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Permute/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-Permute-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Handy and fast permutation with object oriented interface.

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
%doc Changes
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Algorithm/
%{perl_vendorarch}/Algorithm/Permute.pm
%dir %{perl_vendorarch}/auto/Algorithm/
%{perl_vendorarch}/auto/Algorithm/Permute/

%changelog
* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
