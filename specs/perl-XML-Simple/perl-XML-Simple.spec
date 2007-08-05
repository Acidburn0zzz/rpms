# $Id$
# Authority: dries
# Upstream: Grant McLean <grantm$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Simple

Summary: Easy API to XML files
Name: perl-XML-Simple
Version: 2.17
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Simple/

Source: http://www.cpan.org/modules/by-module/XML/XML-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module contains an easy API to XML files.

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
%doc %{_mandir}/man3/XML::Simple.3pm*
%doc %{_mandir}/man3/XML::Simple::FAQ.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Simple/
%{perl_vendorlib}/XML/Simple.pm

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 2.17-1
- Updated to release 2.17.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 2.16-1
- Updated to release 2.16.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 2.14-1
- Updated to release 2.14.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 2.13-2
- Fixed the license tag (Thanks to David Necas !)

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 2.13-1
- Updated to release 2.13.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 2.12-1
- Initial package.
