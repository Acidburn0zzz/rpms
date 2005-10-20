# $Id$
# Authority: dag
# Upstream: R�diger Kuhlmann <info$ruediger-kuhlmann,de>
# Upstream: <micq-list$micq,org>

%{?dist: %{expand: %%define %dist 1}}

%{?rh9:%define _without_tcltk_devel 1}
%{?rh8:%define _without_tcltk_devel 1}
%{?rh7:%define _without_tcltk_devel 1}
%{?el2:%define _without_tcltk_devel 1}

Summary: Clone of the Mirabilis ICQ online messaging program
Name: micq
Version: 0.4.11
Release: 1
Group: Applications/Internet
License: GPL
URL: http://www.micq.org/

Source: http://www.micq.org/source/micq-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, tcl
%{!?dist:BuildRequires: libgcrypt-devel, gnutls-devel}
%{?el4:BuildRequires: libgcrypt-devel, gnutls-devel}
%{?fc3:BuildRequires: libgcrypt-devel, gnutls-devel}
%{?fc2:BuildRequires: libgcrypt-devel, gnutls-devel}
%{?fc1:BuildRequires: libgcrypt-devel, gnutls-devel}
#%{?el3:BuildRequires: libgcrypt-devel, gnutls-devel}
%{?el3:BuildRequires: libgcrypt-devel, gnutls-devel}
%{?rh9:BuildRequires: libgcrypt-devel, gnutls-devel}
%{?rh8:BuildRequires: libgcrypt-devel, gnutls-devel}
%{?rh7:BuildRequires: libgcrypt-devel}

%{!?_without_tcltk_devel:BuildRequires: tcl-devel >= 8.3}
%{?_without_tcltk_devel:BuildRequires: tcl >= 8.3}

%description
Micq is a clone of the Mirabilis ICQ online messaging/conferencing
program.

%prep
%setup

%build
%configure \
	--disable-dependency-tracking 
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* doc/*.txt doc/README* FAQ NEWS README TODO
%doc %{_mandir}/man?/micq*
%{_bindir}/micq
%{_datadir}/micq/

%changelog
* Wed Apr 07 2004 Dag Wieers <dag@wieers.com> - 0.4.11-1
- Initial package. (using DAR)
