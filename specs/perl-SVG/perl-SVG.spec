# $Id: perl-IP-Country.spec 171 2004-03-28 01:43:07Z dag $
# Authority: dag
# Upstream: Ronan Oger <ronan$roasp,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVG

Summary: Perl extension for generating Scalable Vector Graphics (SVG) documents
Name: perl-SVG
Version: 2.33
Release: 2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVG/

Source: http://www.cpan.org/modules/by-module/SVG/SVG-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Perl extension for generating Scalable Vector Graphics (SVG) documents.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/SVG/
%{perl_vendorlib}/SVG.pm

%changelog
* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 2.33-2
- Disabled auto-requires for examples/.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.33-1
- Updated to release 2.33.

* Tue Apr 13 2004 Dag Wieers <dag@wieers.com> - 2.28-1
- Initial package. (using DAR)
