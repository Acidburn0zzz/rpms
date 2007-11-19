# $Id$
# Authority: dries
# Upstream: Audrey Tang <autrijus$autrijus,org>

##Tag: test

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Install

Summary: Installer for perl modules
Name: perl-Module-Install
Version: 0.68
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Install/

Source: http://www.cpan.org/modules/by-module/Module/Module-Install-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.004
BuildRequires: perl(Archive::Tar)
BuildRequires: perl(ExtUtils::Install) >= 0.3
BuildRequires: perl(ExtUtils::ParseXS)
BuildRequires: perl(File::Spec) >= 0.87
BuildRequires: perl(Module::Build)
BuildRequires: perl(Module::CoreList)
BuildRequires: perl(Module::ScanDeps) >= 0.28
BuildRequires: perl(PAR::Dist) >= 0.03
BuildRequires: perl(Test::Harness) >= 2.03
BuildRequires: perl(Test::More) >= 0.42
# needed for certain older versions of perl-Module-Build
BuildRequires: perl(YAML::Syck)
Requires: perl >= 0:5.004

%description
Module::Install is a standalone, extensible installer for Perl modules.  It is
designed to be a drop-in replacement for ExtUtils::MakeMaker, and is a
descendent of CPAN::MakeMaker.

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
%doc Changes LICENSE MANIFEST META.yml README ToDo
%doc %{_mandir}/man3/Module::AutoInstall.3pm.gz
%doc %{_mandir}/man3/Module::Install.3pm.gz
%doc %{_mandir}/man3/Module::Install::*.3pm.gz
%doc %{_mandir}/man3/inc::Module::Install.3pm*
%dir %{perl_vendorlib}/Module/
%{perl_vendorlib}/Module/AutoInstall.pm
%{perl_vendorlib}/Module/Install/
%{perl_vendorlib}/Module/Install.pm
%{perl_vendorlib}/Module/Install.pod
%dir %{perl_vendorlib}/inc/
%dir %{perl_vendorlib}/inc/Module/
%{perl_vendorlib}/inc/Module/Install.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.68-1
- Updated to release 0.68.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.67-1
- Updated to release 0.67.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.64-1
- Updated to release 0.64.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 0.62-1
- Updated to release 0.62.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.61-1
- Updated to release 0.61.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Updated to release 0.52.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.44-1
- Initial package.
