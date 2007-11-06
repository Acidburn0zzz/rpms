# $Id$
# Authority: dries
# Upstream: Richard Soderberg <perl$crystalflame,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Remove

Summary: Remove files and directories
Name: perl-File-Remove
Version: 0.38
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Remove/

Source: http://www.cpan.org/modules/by-module/File/File-Remove-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Remove files and directories.

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
%doc %{_mandir}/man3/File::Remove.3pm*
%dir %{perl_vendorlib}/File/
#%{perl_vendorlib}/File/Remove/
%{perl_vendorlib}/File/Remove.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.38-1
- Updated to release 0.38.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.34-1
- Updated to release 0.34.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Updated to release 0.31.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Updated to release 0.30.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.29-1
- Initial package.
