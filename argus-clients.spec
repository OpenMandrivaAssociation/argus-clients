%define raprelude_version 0.3.1

Name:           argus-clients
Version:        2.0.6.fixes.1
Release:        %mkrel 6
Epoch:          0
Summary:        Client tools for argus network audit
License:        GPLv2+
Group:          Networking/Other
URL:            http://qosient.com/argus/
Source0:        http://qosient.com/argus/src/argus-clients-2.0.6.tar.gz
Source1:        http://qosient.com/argus/src/argus-clients-2.0.6.tar.gz.asc
Source2:        http://qosient.com/argus/src/argus-clients-2.0.6.tar.gz.md5
Source3:        http://www.intrusion-lab.net/downloads/raprelude-%{raprelude_version}.tar.bz2
Patch0:         argus-clients-2.0.6.fixes.1-makefile.patch
Patch1:         argus-clients-2.0.6.fixes.1-build.patch
Patch2:         argus-clients-2.0.6.fixes.1-print.patch
Patch3:         argus-clients-2.0.6.fixes.1-raprelude-Makefile.in.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  ncurses-devel
BuildRequires:  prelude-devel
BuildRequires:  libsasl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Clients to the argus probe which process and display information.

This version contains raprelude %{raprelude_version} from
<http://www.intrusion-lab.net/raprelude/>.

raprelude is a client to log network events to a prelude manager. For
this task you would use argus to log all information of network
connections in your network. Then you can make use of any argus client
to select the network traffic you are interested in. For example you
use the ra client to select just the connections to a certain server
you are examining. raprelude uses a configuration file with rules to
determine which alerts to log and with wich class name. That way ICMP
traffic can be classified as ICMP traffic, some other traffic records
can be dropped and again other records might be logged with more
detailed information than others. This way raprelude enables you to log
selected traffic information to prelude so you can visualize it
together with the other hostile network events that are detected by
other prelude sensors. Prelude uses IDMEF format to log the events.

%prep
%setup -q -n argus-clients-2.0.6
%patch0 -p1
%patch1 -p1
%patch2 -p1
%setup -q -n argus-clients-2.0.6 -T -D -a 3
pushd raprelude-%{raprelude_version}
%patch3 -p1
./apply.sh << EOF
foobar
..
%{_libdir}
%{_libdir}
EOF
popd

%build
export CPPFLAGS="-I%{_includedir}/sasl"
%{configure2_5x} --with-sasl
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} -r %{buildroot}%{_libdir}

pushd raprelude-%{raprelude_version}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/prelude/profile/raprelude
%{__cp} -a class.conf %{buildroot}%{_sysconfdir}/prelude/profile/raprelude/class.conf
popd

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ChangeLog COPYING CREDITS INSTALL MANIFEST README VERSION doc support
%doc raprelude-%{raprelude_version}/README.TXT
%attr(0755,root,root) %{_bindir}/ra
%attr(0755,root,root) %{_bindir}/racount
%attr(0755,root,root) %{_bindir}/ragator
%attr(0755,root,root) %{_bindir}/ragraph
%attr(0755,root,root) %{_bindir}/ragrep
%attr(0755,root,root) %{_bindir}/rahistogram
%attr(0755,root,root) %{_bindir}/rahosts
%attr(0755,root,root) %{_bindir}/ramon
%attr(0755,root,root) %{_bindir}/ranonymize
%attr(0755,root,root) %{_bindir}/rapath
%attr(0755,root,root) %{_bindir}/rapolicy
%attr(0755,root,root) %{_bindir}/rarpwatch
%attr(0755,root,root) %{_bindir}/raseq
%attr(0755,root,root) %{_bindir}/rasort
%attr(0755,root,root) %{_bindir}/rasrvstats
%attr(0755,root,root) %{_bindir}/rastrip
%attr(0755,root,root) %{_bindir}/ratop
%attr(0755,root,root) %{_bindir}/raxml
%{_mandir}/man1/ra.1*
%{_mandir}/man1/racount.1*
%{_mandir}/man1/ragator.1*
%{_mandir}/man1/rahosts.1*
%{_mandir}/man1/ramon.1*
%{_mandir}/man1/ranonymize.1*
%{_mandir}/man1/rapolicy.1*
%{_mandir}/man1/rasort.1*
%{_mandir}/man1/rastrip.1*
%{_mandir}/man1/raxml.1*
%{_mandir}/man5/rarc.5*
%attr(0755,root,root) %{_bindir}/raprelude
%{_mandir}/man1/raprelude.1*
%config(noreplace) %{_sysconfdir}/prelude/profile/raprelude/class.conf
