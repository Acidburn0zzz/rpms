# $Id$
# Authority: dag

### Unresolved dependencies
##Tag: test

%{?dist: %{expand: %%define %dist 1}}

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-tools

Summary: Perl modules for parsing (and creating!) MIME entities
Name: perl-MIME-tools
Version: 5.418
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-tools/

Source: http://www.cpan.org/modules/by-module/MIME/MIME-tools-%{version}.tar.gz
Patch: http://www.roaringpenguin.com/mimedefang/mime-tools-patch.txt
Patch1: MIME-Tools.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(IO::Stringy) >= 1.211, perl-MailTools
Requires: perl(IO::Stringy) >= 1.211, perl-MailTools >= 1.15
%{?rh7:BuildRequires: perl(MIME::Base64) >= 2.04}
%{?el2:BuildRequires: perl-MIME-Base64 >= 2.04}

%description
MIME-tools - modules for parsing (and creating!) MIME entities Modules in this
toolkit : Abstract message holder (file, scalar, etc.), OO interface for
decoding MIME messages, an extracted and decoded MIME entity, Mail::Field
subclasses for parsing fields, a parsed MIME header (Mail::Header subclass),
parser and tool for building your own MIME parser, and utilities.

%prep
%setup -n %{real_name}-%{version}
#patch -p1
#patch1 -p1

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" 
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"
#{__make} test

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
%doc COPYING INSTALLING MANIFEST README* examples/
%doc %{_mandir}/man?/*
%{perl_vendorlib}/MIME/
#%{perl_vendorlib}/set-version.pl

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 5.418-1
- Updated to release 5.418.

* Thu Mar 10 2005 Dag Wieers <dag@wieers.com> - 5.417-1
- Updated to release 5.417.

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 5.415-1
- Updated to release 5.415.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
