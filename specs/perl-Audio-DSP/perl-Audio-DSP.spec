# $Id$
# Authority: dries
# Upstream: Seth David Johnson <seth$pdamusic,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Audio-DSP

Summary: Interface to *NIX digital audio device
Name: perl-Audio-DSP
Version: 0.02
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Audio-DSP/

Source: http://search.cpan.org/CPAN/authors/id/S/SE/SETHJ/Audio-DSP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Audio::DSP is built around the OSS (Open Sound System) API and allows
perl to interface with a digital audio device. The Audio::DSP object
stores I/O parameters and also supplies temporary storage for raw
audio data.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Audio/
%{perl_vendorarch}/Audio/DSP.pm
%dir %{perl_vendorarch}/auto/Audio/
%{perl_vendorarch}/auto/Audio/DSP/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
