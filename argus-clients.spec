Name:           argus-clients
Version:        3.0.7.11
Release:        1
Epoch:          0
Summary:        Client tools for argus network audit
License:        GPLv2+
Group:          Networking/Other
URL:            http://qosient.com/argus/
Source0:        http://qosient.com/argus/dev/%{name}-%{version}.tar.gz
Patch0:		argus-clients-3.0.2-fix-str-fmt.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  ncurses-devel
BuildRequires:  libsasl-devel
BuildRequires:	mysql-devel

%description
Clients to the argus probe which process and display information.


%package	devel
Summary:        Static library and header files for the %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:       %{name} = %{version}-%{release}

%description	devel
Static library and header files for the %{name}

%prep
%setup -q -n %name-%version

%build
%configure2_5x
make

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

rm -rf %{buildroot}%_docdir

%files
%defattr(0644,root,root,0755)
#%doc ChangeLog COPYING CREDITS INSTALL MANIFEST README VERSION doc support
%attr(0755,root,root) %{_bindir}/*
%{_prefix}/argus
%{_mandir}/man?/*

%files devel
%{_includedir}/argus/*
%{_libdir}/*.a
%{_libdir}/pkgconfig/%{name}.pc


