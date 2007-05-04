# $Id$
# Authority: dag
# Upstream: Chia-liang Kao <clkao@clkao.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PerlIO-via-symlink

Summary: PerlIO layer for symlinks
Name: perl-PerlIO-via-symlink
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PerlIO-via-symlink/

Source: http://www.cpan.org/modules/by-module/PerlIO/PerlIO-via-symlink-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
PerlIO layer for symlinks.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/PerlIO::via::symlink.3pm*
%dir %{perl_vendorlib}/PerlIO/
%dir %{perl_vendorlib}/PerlIO/via/
%{perl_vendorlib}/PerlIO/via/symlink.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
