# $Id$
# Authority: dag
# Upstream: Marc Girod <CENSORED>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ClearCase-Wrapper-MGi

Summary: Marc Girod's contributed cleartool wrapper functions
Name: perl-ClearCase-Wrapper-MGi
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ClearCase-Wrapper-MGi/

Source: http://www.cpan.org/modules/by-module/ClearCase/ClearCase-Wrapper-MGi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Marc Girod's contributed cleartool wrapper functions.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/ClearCase::Wrapper::MGi.3pm*
%dir %{perl_vendorlib}/auto/ClearCase/
%{perl_vendorlib}/auto/ClearCase/Wrapper/
%dir %{perl_vendorlib}/ClearCase/
%dir %{perl_vendorlib}/ClearCase/Wrapper/
#%{perl_vendorlib}/ClearCase/Wrapper/MGi/
%{perl_vendorlib}/ClearCase/Wrapper/MGi.pm

%changelog
* Mon Nov 26 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
