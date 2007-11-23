# $Id$
# Authority: dag
# Upstream: Yves Orton (demerphq)

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

Summary: Accurately serialize a data structure as Perl code
Name: perl-Data-Dump-Streamer
Version: 2.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Dump-Streamer/

Source: http://www.cpan.org/modules/by-module/Data/Data-Dump-Streamer-%{version}-36.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Accurately serialize a data structure as Perl code.

%prep
%setup -n Data-Dump-Streamer-%{version}-36

%build
echo "no" | CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes INSTALL.SKIP MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Data::Dump::Streamer.3pm*
%dir %{perl_vendorarch}/auto/Data/
%dir %{perl_vendorarch}/auto/Data/Dump/
%{perl_vendorarch}/auto/Data/Dump/Streamer/
%dir %{perl_vendorarch}/Data/
%dir %{perl_vendorarch}/Data/Dump/
%{perl_vendorarch}/Data/Dump/Streamer/
%{perl_vendorarch}/Data/Dump/Streamer.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 2.05-1
- Initial package. (using DAR)
