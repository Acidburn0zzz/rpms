# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name SQL-Abstract

Name: perl-SQL-Abstract
Summary: Generate SQL from Perl data structures
Version: 1.20
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SQL-Abstract/

Source: http://www.cpan.org/modules/by-module/SQL/SQL-Abstract-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

%description
This module was inspired by the excellent L<DBIx::Abstract>.
However, in using that module I found that what I really wanted
to do was generate SQL, but still retain complete control over my
statement handles and use the DBI interface. So, I set out to
create an abstract SQL generation module.

While based on the concepts used by L<DBIx::Abstract>, there are
several important differences, especially when it comes to WHERE
clauses. I have modified the concepts used to make the SQL easier
to generate from Perl data structures and, IMO, more intuitive.
The underlying idea is for this module to do what you mean, based
on the data structures you provide it. The big advantage is that
you don't have to modify your code every time your data changes,
as this module figures it out.

%prep
%setup -n %{real_name}-%{version}
#chmod -R u+w %{_builddir}/%{pkgname}-%{version}

%build
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_mandir}/man3/*
%dir %{perl_vendorlib}/SQL/
%{perl_vendorlib}/SQL/Abstract.pm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 1.18-1
- Initial package. (using DAR)
