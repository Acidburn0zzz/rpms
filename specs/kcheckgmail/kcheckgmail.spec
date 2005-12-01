# $Id$
# Authority: dries

Summary: System tray application with information about your gmail account
Name: kcheckgmail
Version: 0.5.5
Release: 1
License: GPL
Group: Applications/Internet
URL: http://kcheckgmail.sf.net/

Source: http://dl.sf.net/kcheckgmail/kcheckgmail-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gcc-c++, gettext, autoconf, automake

%description
KCheckGmail is a system tray application to notify you about how many email 
messages you have in your Gmail account.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/kcheckgmail
%{_datadir}/icons/crystalsvg/*/apps/kcheckgmail.png
%{_datadir}/applications/kde/kcheckgmail.desktop
%{_datadir}/apps/kcheckgmail/
%{_datadir}/doc/HTML/*/kcheckgmail/

%changelog
* Tue Nov 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.5-1
- Initial package.
