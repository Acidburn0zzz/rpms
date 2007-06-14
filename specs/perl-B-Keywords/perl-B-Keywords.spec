# $Id$
# Authority: dag
# Upstream: Joshua ben Jore <jjore$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name B-Keywords

Summary: Perl module with lists of reserved barewords and symbol names
Name: perl-B-Keywords
Version: 1.06
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/B-Keywords/

Source: http://www.cpan.org/modules/by-module/B/B-Keywords-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)
Requires: perl

%description
B-Keywords is a perl module with lists of reserved barewords and symbol names.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/B::Keywords.3pm*
%dir %{perl_vendorlib}/B/
%{perl_vendorlib}/B/Keywords.pm

%changelog
* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Initial package. (using DAR)
