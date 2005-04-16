# $Id$
# Authority: dries
# Upstream: Broc Seib <bseib$purdue,edu>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-Syslog

Summary: Tie a filehandle to Syslog
Name: perl-Tie-Syslog
Version: 1.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-Syslog/

Source: http://search.cpan.org/CPAN/authors/id/B/BR/BROCSEIB/Tie-Syslog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module allows you to tie a filehandle (output only) to
syslog. This becomes useful in general when you want to
capture any activity that happens on STDERR and see that it
is syslogged for later perusal. You can also create an arbitrary
filehandle, say LOG, and send stuff to syslog by printing to
this filehandle. This module depends on the Sys::Syslog module
to actually get info to syslog.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%{perl_vendorlib}/Tie/Syslog.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Initial package.
