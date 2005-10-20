# $Id$
# Authority: dag
# Upstream: Eric S. Raymond <esr$thyrsus,com>

%{?dist: %{expand: %%define %dist 1}}

%define _requires_exceptions perl

Summary: Fast anti-spam filtering by Bayesian statistical analysis
Name: bogofilter
Version: 0.92.4
Release: 1
License: GPL
Group: Applications/Internet
URL: http://bogofilter.sourceforge.net/

Source: http://dl.sf.net/bogofilter/bogofilter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex
%{!?_without_tdb:BuildRequires: tdb-devel}
Conflicts: bogofilter-static

%description
Bogofilter is a Bayesian spam filter.  In its normal mode of
operation, it takes an email message or other text on standard input,
does a statistical check against lists of "good" and "bad" words, and
returns a status code indicating whether or not the message is spam.
Bogofilter is designed with fast algorithms (including Berkeley DB system),
coded directly in C, and tuned for speed, so it can be used for production
by sites that process a lot of mail.

Available rpmbuild rebuild options :
--without : tdb

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}" \
%{!?_without_tdb:--with-tdb} \
	--with-included-gsl
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__mv} -f %{buildroot}%{_sysconfdir}/bogofilter.cf.example %{buildroot}%{_sysconfdir}/bogofilter.cf

%{__install} -d -m0755 rpm-doc/xml/ rpm-doc/html/
%{__install} -m644 doc/*.xml rpm-doc/xml/
%{__install} -m644 doc/*.html rpm-doc/html/

for dir in contrib; do
	for file in $(find "$dir" -maxdepth 1 -type f -print); do
		case $file in
			*.c|*.o|*.obj|*/Makefile*) continue ;;
			*.1) %{__install} -Dp -m0644 $file %{buildroot}%{_mandir}/man1/$file;;
			*) %{__install} -Dp -m0644 $file %{buildroot}%{_datadir}/bogofilter/$dir/$file;;
		esac
	done
done

for README in randomtrain; do
	%{__ln_s} -f ../contrib/README.$README doc/README.$README
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGES* COPYING METHODS NEWS README* RELEASE.NOTES* TODO bogofilter.cf.example
%doc doc/bogofilter-SA-2002-01 doc/bogofilter-tuning.HOWTO doc/integrating* doc/programmer/
%doc rpm-doc/html/ rpm-doc/xml/
%doc %{_mandir}/man1/bogo*.1*
%config(noreplace) %{_sysconfdir}/bogofilter.cf
%{_bindir}/bogo*
%{_datadir}/bogofilter/

%changelog
* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 0.92.4-1
- Updated to release 0.92.4.

* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 0.17.5-1
- Updated to release 0.17.5.

* Mon Jan 26 2004 Dag Wieers <dag@wieers.com> - 0.16.4-0
- Initial package. (using DAR)
