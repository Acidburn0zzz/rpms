# $Id$
# Authority: dag
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-HTTP

Summary: Perl module that implements date conversion routines.
Name: perl-DateTime-Format-HTTP
Version: 0.37
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-HTTP/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-HTTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker), perl(Module::Build)
Requires: perl

%description
DateTime-Format-HTTP is a Perl module that implements date conversion routines.

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
%doc Artistic AUTHORS Changes COPYING CREDITS LICENCE MANIFEST META.yml README
%doc %{_mandir}/man3/DateTime::Format::HTTP.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Format/
%{perl_vendorlib}/DateTime/Format/HTTP.pm

%changelog
* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.37-1
- Initial package. (using DAR)
