# $Id$
# Authority: dag
# Upstream: Matthew Lawrence <matt,lawrence$virgin,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-BOM

Summary: Perl module to implement utilities for handling Byte Order Marks
Name: perl-File-BOM
Version: 0.14
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-BOM/

Source: http://www.cpan.org/modules/by-module/File/File-BOM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)(Module::Build)
Requires: perl

%description
File-BOM is a Perl module to implement utilities for handling Byte Order Marks.

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
%doc Changes MANIFEST META.yml README TODO t/data/broken_bom.txt
%doc %{_mandir}/man3/File::BOM.3pm*
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/BOM.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Initial package. (using DAR)
