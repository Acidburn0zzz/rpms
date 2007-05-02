# $Id$
# Authority: dag
# Upstream: Kevin C. Krinke <kckrinke$opendoorsoftware,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk2-Ex-Utils

Summary: Perl module that implements extra Gtk2 Utilities for working with Gnome2/Gtk2
Name: perl-Gtk2-Ex-Utils
Version: 0.09
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk2-Ex-Utils/

Source: http://www.cpan.org/modules/by-module/Gtk2/Gtk2-Ex-Utils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Gtk2-Ex-Utils is a Perl module that implements extra Gtk2 Utilities
for working with Gnome2/Gtk2.

%prep
%setup -n %{real_name}-%{version}

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
%doc COPYRIGHT Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Gtk2::Ex::Constants.3pm*
%doc %{_mandir}/man3/Gtk2::Ex::Utils.3pm*
%dir %{perl_vendorlib}/Gtk2/
%dir %{perl_vendorlib}/Gtk2/Ex/
%{perl_vendorlib}/Gtk2/Ex/Constants.pm
%{perl_vendorlib}/Gtk2/Ex/Utils.pm

%changelog
* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
