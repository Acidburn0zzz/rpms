# $Id$
# Authority: dag
# Upstream: Ian Brayshaw <ian$onemore,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-Damn

Summary: Perl module to 'Unbless' Perl objects
Name: perl-Acme-Damn
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-Damn/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-Damn-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Acme-Damn is a Perl module to 'Unbless' Perl objects.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Acme::Damn.3pm*
%dir %{perl_vendorarch}/Acme/
%{perl_vendorarch}/Acme/Damn.pm
%dir %{perl_vendorarch}/auto/Acme/
%{perl_vendorarch}/auto/Acme/Damn/

%changelog
* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
