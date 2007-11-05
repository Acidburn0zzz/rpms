# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Simple-Creator

Summary: Email::Simple constructor for starting anew
Name: perl-Email-Simple-Creator
Version: 1.422
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Simple-Creator/

Source: http://www.cpan.org/modules/by-module/Email/Email-Simple-Creator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Buildrequires: perl(ExtUtils::MakeMaker)

%description
Email::Simple constructor for starting anew.

This package contains the following Perl module:

    Email::Simple::Creator

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
%doc %{_mandir}/man3/Email::Simple::Creator.3pm*
%dir %{perl_vendorlib}/Email/
%dir %{perl_vendorlib}/Email/Simple/
#%{perl_vendorlib}/Email/Simple/Creator/
%{perl_vendorlib}/Email/Simple/Creator.pm

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 1.422-1
- Updated to release 1.422.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 1.41-1
- Initial package.
