# $Id$
# Authority: dag
# Upstream: SANO Taku (SAWATARI Mikage) and YAMASHINA Hio

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-Japanese

Summary: Japanese Character Encoding Handler
Name: perl-Unicode-Japanese
Version: 0.44
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-Japanese/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-Japanese-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Test)
BuildRequires: perl(Test::More)

%description
Japanese Character Encoding Handler.

This package contains the following Perl module:

    Unicode::Japanese

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
%doc Changes MANIFEST MANIFEST.en MANIFEST.noxs META.yml README SIGNATURE
%doc %{_mandir}/man1/ujconv.1*
%doc %{_mandir}/man1/ujguess.1*
%doc %{_mandir}/man3/Unicode::Japanese.3pm*
%doc %{_mandir}/man3/Unicode::Japanese::JA.3pm*
%{_bindir}/ujconv
%{_bindir}/ujguess
%dir %{perl_vendorarch}/Unicode/
%{perl_vendorarch}/Unicode/Japanese/
%{perl_vendorarch}/Unicode/Japanese.mlpod
%{perl_vendorarch}/Unicode/Japanese.pm
%dir %{perl_vendorarch}/auto/Unicode/
%{perl_vendorarch}/auto/Unicode/Japanese/

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.44-1
- Initial package. (using DAR)
