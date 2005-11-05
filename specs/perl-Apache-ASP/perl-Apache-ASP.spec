# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-ASP

Summary: Active Server Pages for Apache with mod_perl
Name: perl-Apache-ASP
Version: 2.59
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-ASP/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-ASP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503, perl(Digest::MD5), perl(MLDBM), perl(MLDBM::Sync)
Requires: perl >= 0:5.00503, perl(Digest::MD5), perl(MLDBM), perl(MLDBM::Sync)
#Requires: mod_perl

### FIXME: Provide perl(Apache::ASP::Share::CORE) as it seems to be missing
Provides: perl(Apache::ASP::Share::CORE)

%description
Apache::ASP provides an Active Server Pages port to the Apache Web
Server with Perl scripting only, and enables developing of dynamic
web applications with session management and embedded Perl code.
There are also many powerful extensions, including XML taglibs, XSLT
rendering, and new events not originally part of the ASP API!

%prep
%setup -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor" \
	--ssl
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
%doc CHANGES LICENSE MANIFEST README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/ASP/
%{perl_vendorlib}/Apache/ASP.pm
%dir %{perl_vendorlib}/Bundle/
%dir %{perl_vendorlib}/Bundle/Apache/
%{perl_vendorlib}/Bundle/Apache/ASP/
%{perl_vendorlib}/Bundle/Apache/ASP.pm
%{_bindir}/asp-perl

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.59-1
- Updated to release 2.59.

* Fri Aug 06 2004 Dag Wieers <dag@wieers.com> - 2.57-2
- Added explicit perl(Apache::ASP::Share::CORE) provides. (Johnathan Kupferer)

* Sun Jul 11 2004 Dag Wieers <dag@wieers.com> - 2.57-1
- Cosmetic changes.

* Fri Jul  9 2004 Johnathan Kupferer <kupferer@redhat.com> 2.57-1
- Initial build.
