# $Id$
# Authority: dries
# Upstream: John Peacock <jpeacock$rowman,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVN-Notify-Mirror
%define real_version 0.03603

Summary: Keep a mirrored working copy of a repository path
Name: perl-SVN-Notify-Mirror
Version: 0.36.3
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Notify-Mirror/

Source: http://www.cpan.org/modules/by-module/SVN/SVN-Notify-Mirror-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)

%description
Keep a mirrored working copy of a repository path.

%prep
%setup -n %{real_name}-%{real_version}

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
%doc Changes LICENSE MANIFEST MANIFEST.SKIP META.yml README SIGNATURE Todo
%doc %{_mandir}/man3/SVN::Notify::Mirror.3pm*
%doc %{_mandir}/man3/SVN::Notify::Mirror::*.3pm*
%dir %{perl_vendorlib}/SVN/
%dir %{perl_vendorlib}/SVN/Notify/
%{perl_vendorlib}/SVN/Notify/Mirror/
%{perl_vendorlib}/SVN/Notify/Mirror.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.36.3
- Updated to release 0.03603.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.036-1
- Initial package.
