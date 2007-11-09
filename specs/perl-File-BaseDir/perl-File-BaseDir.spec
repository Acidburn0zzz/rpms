# $Id$
# Authority: dag
# Upstream: Jaap Karssenberg <pardus$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-BaseDir

Summary: Perl module to use the freedesktop basedir spec
Name: perl-File-BaseDir
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-BaseDir/

Source: http://www.cpan.org/modules/by-module/File/File-BaseDir-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build) >= 0.24
BuildRequires: perl(Test::More)
Requires: perl

%description
File-BaseDir is a Perl module to use the freedesktop basedir spec.

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
%doc %{_mandir}/man3/File::BaseDir.3pm*
%dir %{perl_vendorlib}/File/
#%{perl_vendorlib}/File/BaseDir/
%{perl_vendorlib}/File/BaseDir.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Updated to release 0.03.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
