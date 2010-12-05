Name:           argus-clients
Version:        3.0.2
Release:        %mkrel 3
Epoch:          0
Summary:        Client tools for argus network audit
License:        GPLv2+
Group:          Networking/Other
URL:            http://qosient.com/argus/
Source0:        http://qosient.com/argus/src/%{name}-%{version}.tar.gz
Patch0:		argus-clients-3.0.2-fix-str-fmt.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  ncurses-devel
BuildRequires:  libsasl-devel
BuildRequires:	mysql-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Clients to the argus probe which process and display information.

%prep
%setup -q -n %name-%version
%patch0 -p0

%build
%configure2_5x
make

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

rm -rf %{buildroot}%_docdir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ChangeLog COPYING CREDITS INSTALL MANIFEST README VERSION doc support
%attr(0755,root,root) %{_bindir}/*
%attr(0755,root,root) %{_sbindir}/*
%{_prefix}/argus
%{_mandir}/man?/*
