# $Id$
# Authority: dries
# Upstream: Richard Clamp <richardc$unixbeard,net>
# Upstream: Michael Stevens <mstevens$etla,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-Coverage

Summary: Checks if the documentation of a module is comprehensive
Name: perl-Pod-Coverage
Version: 0.19
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-Coverage/

Source: http://www.cpan.org/modules/by-module/Pod/Pod-Coverage-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)

%description
Checks if the documentation of a module is comprehensive.

This package contains the following Perl module:

    Pod::Coverage

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
%doc %{_mandir}/man3/Pod::Coverage.3pm*
%doc %{_mandir}/man3/Pod::Coverage::*.3pm*
%{_bindir}/pod_cover
%dir %{perl_vendorlib}/Pod/
%{perl_vendorlib}/Pod/Coverage/
%{perl_vendorlib}/Pod/Coverage.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.19-1
- Updated to release 0.19.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Updated to release 0.18.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Updated to release 0.17.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Initial package.
