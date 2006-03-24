# $Id$
# Authority: dries
# Upstream: Peter Billam <contact,html$pjb,com,au>

%define real_name Crypt-Tea
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: The Tiny Encryption Algorithm in Perl and JavaScript
Name: perl-Crypt-Tea
Version: 2.09
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Tea/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-Tea-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module implements TEA, the Tiny Encryption Algorithm, and some
Modes of Use based on CBC, compatibly in both Perl and JavaScript.
This enables CGI scripts to communicate with browsers.

Subroutines offer encryption, decryption & digest, and all cyphertext
is ascii-encoded to prevent munging. Another routine returns JavaScript
code with identical functions, and this can be used by GCIs to feed to
a browser. A wrapper executable 'tea' is included for command-line use.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man1/*
%doc %{_mandir}/man3/*
%{_bindir}/tea
%{perl_vendorlib}/Crypt/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.09-1.2
- Rebuild for Fedora Core 5.

* Mon Feb 21 2005 Dries Verachtert <dries@ulyssis.org> - 2.09-1
- Update to release 2.09.

* Mon Dec 27 2004 Dries Verachtert <dries@ulyssis.org> - 2.07-1
- Initial package.
