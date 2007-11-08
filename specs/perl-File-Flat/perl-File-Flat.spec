# $Id$
# Authority: dag
# Upstream: Adam Kennedy <cpan$ali,as>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Flat

Summary: Perl module that implements a flat filesystem
Name: perl-File-Flat
Version: 1.00
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Flat/

Source: http://www.cpan.org/modules/by-module/File/File-Flat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
File-Flat is a Perl module that implements a flat filesystem.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/File::Flat.3pm*
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/Flat.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
