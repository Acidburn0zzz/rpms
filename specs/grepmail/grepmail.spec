# $Id$
# Authority: dag
# Upstream: David Coppit <david$coppit,org>

Summary: Search for emails in a mailbox using regular expressions
Name: grepmail
Version: 5.3030
Release: 1
License: GPL
Group: Applications/System
URL: http://grepmail.sourceforge.net/

Source: http://dl.sf.net/grepmail/grepmail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
Requires: perl

%description
grepmail is a tool to search for emails in a normal or compressed mailbox
using a regular expression or date constraint.

%prep
%setup

%build
%{_bindir}/pod2man grepmail >grepmail.1

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 grepmail %{buildroot}%{_bindir}/grepmail
%{__install} -D -m0644 grepmail.1 %{buildroot}%{_mandir}/man1/grepmail.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE README
%doc %{_mandir}/man1/grepmail.1*
%{_bindir}/grepmail

%changelog
* Mon Feb 21 2005 Dag Wieers <dag@wieers.com> - 5.3030-1
- Initial package. (using DAR)
