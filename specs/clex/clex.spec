# $Id$
# Authority: dries
# Upstream: Vlado Potisk <clex$clex,sk>

Summary: File manager with an ncurses interface
Name: clex
Version: 3.14
Release: 1.2
License: GPL
Group: System Environment/Shells
URL: http://www.clex.sk/

Source: http://www.clex.sk/download/clex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
CLEX is a file manager with a full-screen user interface written in C with
the curses library. It displays directory contents (including file status
details) and provides features like command history, filename insertion, or
name completion in order to help the user to construct commands to be
executed by the shell (there are no built-in commands). CLEX is easily
configurable and all its features are explained in the on-line help.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/clex*
%{_bindir}/clex


%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.14-1.2
- Rebuild for Fedora Core 5.

* Fri Nov 04 2005 Dries Verachtert <dries@ulyssis.org> - 3.14-1
- Updated to release 3.14.

* Thu Sep 22 2005 Dries Verachtert <dries@ulyssis.org> - 3.13-1
- Initial package.
