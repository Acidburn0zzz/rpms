# $Id$

# Authority: dag

%define rname jpgraph

Summary: OO Graph Library for PHP
Name: php-jpgraph
Version: 1.14
Release: 1
License: QPL
Group: Development/Languages
URL: http://www.aditus.nu/jpgraph/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://jpgraph.techuk.com/jpgraph/downloads/jpgraph-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
Requires: webserver, php
Obsoletes: jpgraph
Provides: jpgraph

%description
JpGraph is an OO class library for PHP 4.1 (or higher). JpGraph makes it
easy to draw both "quick and dirty" graphs with a minimum of code and
complex professional graphs which requires a very fine grain control.

JpGraph is equally well suited for both scientific and business type of graphs.

An important feature of the library is that it assigns context sensitive
default values for most of the parameters which radically minimizes the
learning curve. The features are there when you need it - they don't get
in your way when you don't need them!

%package docs
Summary: Documentation for package %{name}
Group: Documentation

%description docs
JpGraph is an OO class library for PHP 4.1 (or higher). JpGraph makes it
easy to draw both "quick and dirty" graphs with a minimum of code and
complex professional graphs which requires a very fine grain control.

This package includes the documentation for %{name}.

%prep
%setup -n %{rname}-%{version}

### Change the default TTF_DIR to Red Hat's TTF_DIR.
%{__perl} -pi.orig -e 's|/usr/X11R6/lib/X11/fonts/truetype/|/usr/X11R6/lib/X11/fonts/TTF/|' src/jpgraph.php

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/%{rname}-%{version}
%{__install} -m0644 src/jpgraph*.php src/*.inc src/*.dat %{buildroot}%{_localstatedir}/www/%{rname}-%{version}/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc QPL.txt README src/Changelog
%{_localstatedir}/www/%{rname}-%{version}/

%files docs
%defattr(-, root, root, 0755)
%doc src/Examples/ docs/*

%changelog
* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> - 1.14-1
- Added missing dat files. (Matti Lindell)

* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 1.14-0
- Added missing inc files. (Matti Lindell)
- Updated to release 1.14.

* Tue Sep 16 2003 Dag Wieers <dag@wieers.com> - 1.13-0
- Updated to release 1.13.

* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 1.10-0
- Initial package. (using DAR)
