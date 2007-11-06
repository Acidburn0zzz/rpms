# $Id$
# Authority: dag
# Upstream: Marcel Grënauer <marcel$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Compile

Summary: check whether Perl module files compile correctly
Name: perl-Test-Compile
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Compile/

Source: http://www.cpan.org/modules/by-module/Test/Test-Compile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0 
BuildRequires: perl(Test::More) >= 0.7
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)

%description
check whether Perl module files compile correctly.

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
%doc %{_mandir}/man3/Test::Compile.3pm*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/Compile/
%{perl_vendorlib}/Test/Compile.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
