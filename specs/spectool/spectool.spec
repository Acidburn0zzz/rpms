# $Id$
# Authority: dag
# Upstream: Nils Philippsen <nphilipp$redhat,com>

Summary: Display expanded Source/Patch macros from SPEC files
Name: spectool
Version: 1.0.3
Release: 1
License: GPL
Group: System Environment/Base
URL: http://people.redhat.com/nphilipp/spectool/

Source: http://people.redhat.com/nphilipp/spectool/spectool-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
spectool is a tool to display expanded Source/Patch macros from a SPEC file.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 spectool %{buildroot}%{_bindir}/spectool

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/spectool

%changelog
* Wed Mar 16 2004 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Updated to release 1.0.3.

* Fri Mar 12 2004 Dag Wieers <dag@wieers.com> - 1.0.2-2
- Changed BuildArch to noarch. (Bert de Bruijn)
- Added fix to make spectool work better. (Bert de Bruijn)

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Wed Mar 03 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
