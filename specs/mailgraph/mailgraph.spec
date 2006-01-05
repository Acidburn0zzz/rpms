# $Id$
# Authority: nac

Summary: RRDtool-based mail graphing tool
Name: mailgraph
Version: 1.11
Release: 1
License: GPL
Group: Applications/System
URL: http://people.ee.ethz.ch/~dws/software/mailgraph/

Source0: http://people.ee.ethz.ch/~dws/software/mailgraph/pub/mailgraph-%{version}.tar.gz
Source1: mailgraph.httpd-conf
Patch0: mailgraph.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: perl(File::Tail)

%description
Mailgraph is a very simple mail statistics RRDtool frontend for Postfix
and Sendmail that produces daily, weekly, monthly and yearly graphs of
received/sent and bounced/rejected mail.

%prep
%setup
%patch0

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp mailgraph.pl %{buildroot}%{_libdir}/mailgraph/mailgraph.pl
%{__install} -Dp mailgraph.cgi %{buildroot}%{_libdir}/mailgraph/cgi/mailgraph.cgi
%{__install} -Dp mailgraph-init %{buildroot}%{_initrddir}/mailgraph
%{__install} -Dp mailgraph.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/mailgraph
%{__install} -Dp %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/mailgraph.conf.example

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/mailgraph/{img,rrd}/

%clean
%{__rm} -rf %{buildroot}

%postun
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --del mailgraph
fi

%post
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add mailgraph
fi

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mailgraph.conf.example
%config(noreplace) %{_sysconfdir}/sysconfig/mailgraph
%config %{_initrddir/mailgraph
%{_libdir}/mailgraph/
%{_localstatedir}/lib/mailgraph/img/
%{_localstatedir}/lib/mailgraph/rrd/

%changelog
* Fri Jul 29 2005 Wil Cooley <wcooley@nakedape.cc> - 1.11-1
- Initial package creation
