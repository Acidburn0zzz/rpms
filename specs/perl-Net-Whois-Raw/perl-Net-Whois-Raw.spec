# $Id$
# Authority: dries
# Upstream: Walery Studennikov <despairr$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Whois-Raw

Summary: Get Whois information for domains
Name: perl-Net-Whois-Raw
Version: 1.36
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Whois-Raw/

Source: http://www.cpan.org/modules/by-module/Net/Net-Whois-Raw-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Get Whois information for domains.

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
%doc COPYRIGHT Changes MANIFEST META.yml README
%doc %{_mandir}/man1/pwhois.1*
%doc %{_mandir}/man3/Net::Whois::Raw.3pm*
%{_bindir}/pwhois
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Whois/
%{perl_vendorlib}/Net/Whois/Raw/
%{perl_vendorlib}/Net/Whois/Raw.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.36-1
- Updated to release 1.36.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.34-1
- Updated to release 1.34.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Initial package.
