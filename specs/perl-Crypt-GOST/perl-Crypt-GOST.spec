# $Id$
# Authority: dries
# Upstream: Abhijit Menon-Sen <ams$wiw,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-GOST

Summary: GOST Encryption Algorithm
Name: perl-Crypt-GOST
Version: 1.00
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-GOST/

Source: http://search.cpan.org/CPAN/authors/id/A/AM/AMS/Crypt-GOST-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
GOST 28147-89 is a 64-bit symmetric block cipher with a 256-bit
key developed in the former Soviet Union. Some information on it
is available at <URL:http://vipul.net/gost/>.

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
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Crypt/
%{perl_vendorarch}/Crypt/GOST.pm
%dir %{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/auto/Crypt/GOST

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
