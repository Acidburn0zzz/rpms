# $Id$
# Authority: dag
# Upstream: Leon Brocard <leon$astray,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Page

Summary: Perl module that helps when paging through sets of results.
Name: perl-Data-Page
Version: 2.00
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Page/

Source: http://www.cpan.org/modules/by-module/Data/Data-Page-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
Data-Page is a Perl module that helps when paging through sets of results.

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
%doc MANIFEST META.yml README
%doc %{_mandir}/man3/Data::Page.3pm*
%dir %{perl_vendorlib}/Data/
%{perl_vendorlib}/Data/Page.pm

%changelog
* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 2.00-1
- Initial package. (using DAR)
