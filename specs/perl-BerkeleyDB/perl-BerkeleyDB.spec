# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name BerkeleyDB

Summary: Perl extension for Berkeley DB version 2, 3 or 4
Name: perl-BerkeleyDB
Version: 0.32
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/BerkeleyDB/

Source: http://www.cpan.org/modules/by-module/BerkeleyDB/BerkeleyDB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503
%{!?dtag:BuildRequires: db4-devel}
%{?el5:BuildRequires: db4-devel}
%{?fc6:BuildRequires: db4-devel}
%{?fc5:BuildRequires: db4-devel}
%{?fc4:BuildRequires: db4-devel}
%{?el4:BuildRequires: db4-devel}
%{?fc3:BuildRequires: db4-devel}
%{?fc2:BuildRequires: db4-devel}

%description
Perl extension for Berkeley DB version 2, 3 or 4.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README Todo
%doc %{_mandir}/man3/BerkeleyDB.3pm*
%{perl_vendorarch}/BerkeleyDB/
%{perl_vendorarch}/BerkeleyDB.pm
%{perl_vendorarch}/BerkeleyDB.pod
%{perl_vendorarch}/auto/BerkeleyDB/

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.32-1
- Updated to release 0.32.

* Mon Nov  6 2006 Matthias Saou <http://freshrpms.net/> 0.31-1
- Update to 0.31.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Updated to release 0.30.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.27-1
- Updated to release 0.27.

* Tue Mar 29 2005 Dag Wieers <dag@wieers.com> - 0.26-2
- Cosmetic changes.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> 0.26-0
- Update to release 0.26.

* Tue Mar 02 2004 Dag Wieers <dag@wieers.com> - 0.25-0
- Initial package. (using DAR)
