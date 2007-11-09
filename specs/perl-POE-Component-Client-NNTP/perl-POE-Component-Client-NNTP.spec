# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-NNTP

Summary: POE component that provides access to NNTP
Name: perl-POE-Component-Client-NNTP
Version: 2.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-NNTP/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Client-NNTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A component that provides access to NNTP.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Client/
%{perl_vendorlib}/POE/Component/Client/NNTP.pm
%{perl_vendorlib}/POE/Component/Client/NNTP/

%changelog
* Thu Jul 5 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.02-1
- Updated to latest upstream version { old source not available }

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 2.01-1
- Updated to release 2.01.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
