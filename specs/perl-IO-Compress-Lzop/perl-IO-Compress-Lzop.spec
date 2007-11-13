# $Id$
# Authority: dries
# Upstream: Paul Marquess <pmqs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Compress-Lzop

Summary: Write and read Lzop files of buffers
Name: perl-IO-Compress-Lzop
Version: 2.008
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Compress-Lzop/

Source: http://www.cpan.org/modules/by-module/IO/IO-Compress-Lzop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Write and read Lzop files of buffers.

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
%doc %{_mandir}/man3/IO::Compress::Lzop.3pm*
%doc %{_mandir}/man3/IO::Uncompress::UnLzop.3pm*
%dir %{perl_vendorlib}/IO/
%{perl_vendorlib}/IO/Compress/
%{perl_vendorlib}/IO/Uncompress/

%changelog
* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 2.008-1
- Updated to release 2.008.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 2.003-1
- Initial package.
