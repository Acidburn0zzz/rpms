# $Id$

# Authority: dag
# Upstream: MIMEDefang mailinglist <mimedefang@lists.roaringpenguin.com>

Summary: Email filtering application using sendmail's milter interface
Name: mimedefang
Version: 2.42
Release: 1
License: GPL
Group: System Environment/Daemons
URL: http://www.roaringpenguin.com/mimedefang/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.mimedefang.org/static/mimedefang-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: sendmail-devel > 8.12.0, perl-Mail-SpamAssassin
BuildRequires: perl-Digest-SHA1, perl-MIME-tools, perl-IO-stringy, perl-MailTools
Requires: sendmail >= 8.12.0

%description
MIMEDefang is an e-mail filter program which works with Sendmail 8.11
and later.  MIMEDefang filters all e-mail messages sent via SMTP.
MIMEDefang splits multi-part MIME messages into their components and
potentially deletes or modifies the various parts.  It then
reassembles the parts back into an e-mail message and sends it on its
way.

There are some caveats you should be aware of before using MIMEDefang.
MIMEDefang potentially alters e-mail messages.  This breaks a "gentleman's
agreement" that mail transfer agents do not modify message bodies.  This
could cause problems, for example, with encrypted or signed messages.

Deleting attachments could cause a loss of information.  Recipients must
be aware of this possibility, and must be willing to explain to senders
exactly why they cannot mail certain types of files.  You must have the
willingness of your e-mail users to commit to security, or they will
complain loudly about MIMEDefang.

%prep
%setup

%build
%configure \
	--with-spooldir="%{_localstatedir}/spool/MIMEDefang" \
	--with-quarantinedir="%{_localstatedir}/spool/MD-Quarantine"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/mimedefang/
%{__make} install-redhat \
	RPM_INSTALL_ROOT="%{buildroot}"


%pre
### Old packages may have these...
if [ -d %{_localstatedir}/spool/mimedefang -a ! -d %{_localstatedir}/spool/MIMEDefang ]; then
	%{__mv} -f %{_localstatedir}/spool/mimedefang %{_localstatedir}/spool/MIMEDefang
fi

if [ -d %{_localstatedir}/spool/quarantine -a ! -d %{_localstatedir}/spool/MD-Quarantine ]; then
	%{__mv} -f %{_localstatedir}/spool/quarantine %{_localstatedir}/spool/MD-Quarantine
fi

useradd -M -r -d %{_localstatedir}/spool/MIMEDefang -s /bin/false -c "MIMEDefang User" defang &>/dev/null || :

%post
#%{__cat} << EOF
#
#In order to complete the installation of mimedefang, you will need to add the 
#following line to your sendmail mc file:
#
#   INPUT_MAIL_FILTER(\`mimedefang', \`S=unix:/var/spool/MIMEDefang/mimedefang.sock, F=T, T=S:1m;R:1m;E:5m')
#
#Use the sendmail-cf package to rebuild your /etc/mail/sendmail.cf file and 
#restart your sendmail daemon.
#
#EOF
/sbin/chkconfig --add mimedefang

%preun
if [ $1 -eq 0 ] ; then
	/sbin/service mimedefang stop &>/dev/null || :
	/sbin/chkconfig --del mimedefang
fi

%postun
if [ $1 -ne 0 ]; then
    /sbin/service mimedefang condrestart &>/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING README* examples/ contrib/ SpamAssassin/
%doc %{_mandir}/man?/*
%dir %{_sysconfdir}/mail/spamassassin
%config(noreplace) %{_sysconfdir}/mail/mimedefang-filter
%config(noreplace) %{_sysconfdir}/mail/spamassassin/sa-mimedefang.cf
%config(noreplace) %{_sysconfdir}/sysconfig/*
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%config %{_initrddir}/*
%{_bindir}/*
%defattr(-, defang, defang, 0755)
%dir %{_localstatedir}/log/mimedefang/
%defattr(-, defang, defang, 0700)
%dir %{_localstatedir}/spool/MIMEDefang
%dir %{_localstatedir}/spool/MD-Quarantine

%changelog
* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 2.42-1
- Updated to release 2.42.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 2.40-1
- Updated to release 2.40.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 2.38-0
- Updated to release 2.38.

* Fri Sep 05 2003 Dag Wieers <dag@wieers.com> - 2.37-0
- Updated to release 2.37.

* Wed Aug 27 2003 Dag Wieers <dag@wieers.com> - 2.35-3
- Require perl-IO-Stringy.

* Tue Jul 22 2003 Dag Wieers <dag@wieers.com> - 2.35-2
- Changed user mimedefang to defang.

* Wed Jul 16 2003 Dag Wieers <dag@wieers.com> - 2.35-0
- Initial package. (using DAR)
