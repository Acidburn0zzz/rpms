# $Id$
# Authority: dries
# Upstream: Gerald Richter <richter$ecos,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-Recordset

Summary: Extension for DBI recordsets
Name: perl-DBIx-Recordset
Version: 0.26
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-Recordset/

Source: http://search.cpan.org/CPAN/authors/id/G/GR/GRICHTER/DBIx-Recordset-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
DBIx::Recordset is a perl module for abstraction and simplification of
database access.

The goal is to make standard database access (select/insert/update/delete)
easier to handle and independend of the underlying DBMS. Special attention is
made on web applications to make it possible to handle the state-less access
and to process the posted data of formfields, but DBIx::Recordset is not
limited to web applications.

%prep
%setup -n %{real_name}-%{version}

%build
(echo . ; echo . ; echo . ; echo . ) | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DBIx/Recordset.pm
%{perl_vendorlib}/DBIx/Recordset
%{perl_vendorlib}/DBIx/Compat.pm
%{perl_vendorlib}/DBIx/Database.pm
%{perl_vendorlib}/DBIx/Intrors.pod

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Initial package.
