# $Id$
# Authority: dag
# Upstream: <gtk-perl-list$gnome,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Glib

Summary: Perl wrappers for the GLib utility and object libraries
Name: perl-Glib
Version: 1.101
Release: 1
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Glib/

Source: http://www.cpan.org/modules/by-module/Glib/Glib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.8.0, glib2-devel, perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::PkgConfig)
Requires: perl >= 0:5.8.0, glib2 >= 2.0.6

%description
perl-Glib provides perl access to GLib and GLib's GObject libraries.  GLib is
a portability and utility library; GObject provides a generic type system with
inheritance and a powerful signal system.  Together these libraries are used as
the foundation for many of the libraries that make up the Gnome environment,
and are used in many unrelated projects.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog LICENSE MANIFEST NEWS README* TODO
%doc %{_mandir}/man?/*
%{perl_vendorarch}/Glib/
%{perl_vendorarch}/Glib.pm
%{perl_vendorarch}/auto/Glib/

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.101-1
- Updated to release 1.101.

* Tue Mar 08 2005 Dag Wieers <dag@wieers.com> - 1.080-1
- Updated to release 1.080.

* Sun Feb 13 2005 Dag Wieers <dag@wieers.com> - 1.062-1 - $Rev$
- Updated to release 1.062.

* Fri Mar 26 2004 Dag Wieers <dag@wieers.com> - 1.040-1
- Updated to release 1.040.

* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 1.022-1
- Updated to release 1.022.

* Sat Oct 11 2003 Dag Wieers <dag@wieers.com> - 1.00-0
- Updated to release 1.00.

* Sun Sep 07 2003 Dag Wieers <dag@wieers.com> - 0.97-0
- Updated to release 0.97.

* Sat Aug 30 2003 Dag Wieers <dag@wieers.com> - 0.96-0
- Updated to release 0.96.

* Fri Aug 22 2003 Dag Wieers <dag@wieers.com> - 0.95-0
- Updated to release 0.95.

* Sat Aug 16 2003 Dag Wieers <dag@wieers.com> - 0.94-0
- Updated to release 0.94.

* Sat Aug 02 2003 Dag Wieers <dag@wieers.com> - 0.92-0
- Updated to release 0.92.

* Sun Jul 27 2003 Dag Wieers <dag@wieers.com> - 0.91-0
- Updated to release 0.91.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 0.90-0
- Initial package. (using DAR)
