# $Id$
# Authority: dag
# Upstream: Chia-liang Kao (高嘉良) <clkao$clkao,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVK-Util
%define real_version 2.000001

Summary: Perl module that implements a Distributed Version Control System
Name: perl-SVK-Util
Version: 2.0.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVK-Util/

Source: http://www.cpan.org/authors/id/C/CL/CLKAO/SVK-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Algorithm::Annotate), perl(Algorithm::Diff) >= 1.1901
BuildRequires: perl(YAML::Syck) >= 0.60, perl(Data::Hierarchy) >= 0.30
BuildRequires: perl(PerlIO::via::dynamic) >= 0.11, perl(PerlIO::via::symlink) >= 0.02
BuildRequires: perl(IO::Digest), perl(SVN::Simple::Edit) >= 0.27
BuildRequires: perl(URI), perl(PerlIO::eol) >= 0.13, perl(Class:Autouse) >= 1.15
BuildRequires: perl(App::CLI), perl(List::MoreUtils), perl(Class::Accessor::Fast)
BuildRequires: perl(Class::Data::Inheritable), perl(Path::Class) >= 0.16
BuildRequires: perl(UNIVERSAL::require), perl(Term::ReadKey)
BuildRequires: perl(Time::HiRes), perl(File::Temp) >= 0.17, perl(Encode) >= 2.10
BuildRequires: perl(Getopt::Long) >= 2.35, perl(Pod::Escapes), perl(Pod::Simple)
BuildRequires: perl(File::Spec) >= 3.19

%description
perl-SVK-Util is a Perl module that implements a Distributed Version
Control System.

%prep
%setup -n SVK-v%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ARTISTIC CHANGES CHANGES-1.0 COPYING MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/SVK::Util.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/SVK/
#%{perl_vendorlib}/SVK/Util/
%{perl_vendorlib}/SVK/Util.pm

%changelog
* Sun May 27 2007 Dag Wieers <dag@wieers.com> - 2.0.1-1
- Initial package. (using DAR)
