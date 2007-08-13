# $Id$
# Authority: dag
# Upstream: Torsten Schönfeld <kaffeetisch$gmx,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Cairo

Summary: Perl interface to the cairo library  
Name: perl-Cairo
Version: 1.041
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Cairo/

#Source: http://www.cpan.org/modules/by-module/GStreamer/TSCH/Cairo-%{version}.tar.gz
Source: http://www.cpan.org/authors/id/T/TS/TSCH/Cairo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(Glib) >= 1.0.0
BuildRequires: cairo-devel, perl(ExtUtils::Depends)
Requires: perl >= 2:5.8.0

%description
Perl interface to the cairo library.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE MANIFEST MANIFEST.SKIP META.yml NEWS README TODO examples/
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/Cairo/
%{perl_vendorarch}/Cairo.pm
%{perl_vendorarch}/auto/Cairo/

%changelog
* Wed Aug 08 2007 Dag Wieers <dag@wieers.com> - 1.041-1
- Updated to release 1.041.

* Thu Mar 29 2007 Dag Wieers <dag@wieers.com> - 1.023-1
- Initial package. (using DAR)
