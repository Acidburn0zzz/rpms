# $Id$
# Authority: dries
# Upstream: Elizabeth Mattijsen <liz$dijkmat,nl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-RunAlways

Summary: Make sure always one invocation of a script is active
Name: perl-Sys-RunAlways
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-RunAlways/

Source: http://search.cpan.org//CPAN/authors/id/E/EL/ELIZABETH/Sys-RunAlways-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Make sure always one invocation of a script is active.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG README
%doc %{_mandir}/man3/Sys::RunAlways*
%{perl_vendorlib}/Sys/RunAlways.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
