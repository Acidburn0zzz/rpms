# $Id$
# Authority: dries

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name MLDBM-Sync

Summary: Safe concurrent access to MLDBM databases
Name: perl-MLDBM-Sync
Version: 0.30
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MLDBM-Sync/

Source: http://www.cpan.org/modules/by-module/MLDBM/MLDBM-Sync-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(MLDBM)
Requires: perl-MLDBM

%description
This module wraps around the MLDBM interface, by handling concurrent
access to MLDBM databases with file locking, and flushes i/o explicity
per lock/unlock. The new [Read]Lock()/UnLock() API can be used to
serialize requests logically and improve performance for bundled reads &
writes.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc CHANGES README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/MLDBM/
%{perl_vendorlib}/MLDBM/Sync/
%{perl_vendorlib}/MLDBM/Sync.pm

%changelog
* Sun Jul 11 2004 Dag Wieers <dag@wieers.com> - 0.30-1
- Cosmetic changes.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Initial package.
