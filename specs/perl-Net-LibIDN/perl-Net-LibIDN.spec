# $Id$
# Authority: dag
# Upstream: Thomas Jacob <jacob$internet24,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-LibIDN

Summary: Perl module with bindings for GNU Libidn
Name: perl-Net-LibIDN
Version: 0.09
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-LibIDN/

Source: http://www.cpan.org/modules/by-module/Net/Net-LibIDN-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)
Requires: perl

%description
Net-LibIDN is a Perl module with bindings for GNU Libidn.

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
%doc Artistic Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Net::LibIDN.3pm*
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/LibIDN.pm
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/LibIDN/

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
