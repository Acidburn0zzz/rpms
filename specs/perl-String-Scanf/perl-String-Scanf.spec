# $Id$
# Authority: dries
# Upstream: Jarkko Hietaniemi <jhi$iki,fi>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-Scanf

Summary: Emulate sscanf() of the C library
Name: perl-String-Scanf
Version: 2.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-Scanf/

Source: http://search.cpan.org/CPAN/authors/id/J/JH/JHI/String-Scanf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The 2.0 release of String::Scanf introduces an object-oriented interface
(works only for Perl release 5.005 and up) that should speed up repetitive
sscanf() operations.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" "PREFIX=%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/String/Scanf.pm

%changelog
* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Initial package.
