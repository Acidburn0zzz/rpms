# $Id$
# Authority: dries
# Upstream: Lincoln D. Stein <lstein$cshl,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Shellwords

Summary: Wrapper around shellwords.pl
Name: perl-Text-Shellwords
Version: 1.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Shellwords/

Source: http://search.cpan.org/CPAN/authors/id/L/LD/LDS/Text-Shellwords-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a thin wrapper around the shellwords.pl package, which comes
preinstalled with Perl.  This module imports a single subroutine,
shellwords().  The shellwords() routine parses lines of text and
returns a set of tokens using the same rules that the Unix shell does
for its command-line arguments.  Tokens are separated by whitespace,
and can be delimited by single or double quotes.  The module also
respects backslash escapes.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/Shellwords.pm

%changelog
* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Initial package.
