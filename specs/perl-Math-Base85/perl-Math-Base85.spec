# $Id$
# Authority: dries
# Upstream: Tony Monroe <tmonroe+cpan$nog,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Base85

Summary: Base 85 numbers, as referenced by RFC 1924
Name: perl-Math-Base85
Version: 0.2
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Base85/

Source: http://www.cpan.org/modules/by-module/Math/Math-Base85-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module handles numbers in base 85, via strings and Math::BigInt.
For more information, read the module or rfc1924.txt.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Base85.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-1.2
- Rebuild for Fedora Core 5.

* Mon Apr 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
