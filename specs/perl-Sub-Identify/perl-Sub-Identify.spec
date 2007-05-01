# $Id$
# Authority: dag
# Upstream: Rafa�l Garcia-Suarez <rgarciasuarez$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sub-Identify

Summary: Perl module to retrieve names of code references
Name: perl-Sub-Identify
Version: 0.02
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sub-Identify/

Source: http://www.cpan.org/modules/by-module/Sub/Sub-Identify-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
Sub-Identify is a Perl module to retrieve names of code references.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Sub::Identify.3pm*
%dir %{perl_vendorlib}/Sub/
%{perl_vendorlib}/Sub/Identify.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
