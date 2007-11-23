# $Id$
# Authority: dag
# Upstream: Masatoshi Mizuno E<lt>lusheE<64>cpan,orgE<gt>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Egg-Release
%define real_version 2.02

Summary: Version of Egg WEB Application Framework
Name: perl-Egg-Release
Version: 2.26
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Egg-Release/

Source: http://www.cpan.org/modules/by-module/Egg/Egg-Release-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Version of Egg WEB Application Framework.

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
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README eg/
%doc %{_mandir}/man3/Egg.3pm*
%doc %{_mandir}/man3/Egg::*.3pm*
%{perl_vendorlib}/Egg/
%{perl_vendorlib}/Egg.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 2.26-1
- Initial package. (using DAR)
