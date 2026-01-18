%global debug_package %{nil}
%global wxversion 3.2
%global wxincdir %{_includedir}/wx-%{wxversion}
%define major 0

%define libname %mklibname %{name}_ %{wxversion} %{major}
%define devname %mklibname %{name}_ %{wxversion} -d

Name:           wxsqlite3
Version:        4.11.2
Release:        1
Summary:        C++ wrapper around the SQLite 3.x database
Group:          System/Libraries
License:        wxWidgets
URL:            https://utelle.github.io/wxsqlite3
Source0:        https://github.com/utelle/wxsqlite3/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:  dos2unix
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  wxgtku%{wxversion}-devel

%description
wxSQLite3 is a C++ wrapper around the public domain SQLite 3.x database and
is specifically designed for use in programs based on the wxWidgets
%{wxversion} library.

wxSQLite3 does not try to hide the underlying database, in contrary almost
all special features of the recent SQLite3 versions are supported, like
for example the creation of user defined scalar or aggregate functions.

%package -n     %{libname}
Summary:        C++ wrapper around the SQLite 3.x database
Group:          System/Libraries

%description -n %{libname}
wxSQLite3 is a C++ wrapper around the public domain SQLite 3.x database and
is specifically designed for use in programs based on the wxWidgets
%{wxversion} library.

wxSQLite3 does not try to hide the underlying database, in contrary almost
all special features of the recent SQLite3 versions are supported, like
for example the creation of user defined scalar or aggregate functions.

%package -n     %{devname}
Summary:        Development files for %{name}
Group:          Development/C++
Requires:       %{libname} = %{version}-%{release}

%description -n %{devname}
This package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1

# delete bundled sqlite3 files
rm -rf sqlite3

dos2unix readme.md

%build
%configure
%make_build

%install
%make_install

# move headers from /usr/include/wx to /usr/include/wx-?.?/wx
install -d %{buildroot}%{wxincdir}
mv %{buildroot}%{_includedir}/wx %{buildroot}%{wxincdir}

# install multiple cipher support headers
install -m644 src/*.h %{buildroot}%{wxincdir}/wx

# install pkgconfig file
install -D -m644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%files -n       %{libname}
%doc LICENCE.txt readme.md
%{_libdir}/libwxcode_gtk3u_wxsqlite3-%{wxversion}.so.%{major}*

%files -n       %{devname}
%{wxincdir}/wx/%{name}*.h
%{wxincdir}/wx/sqlite3mc_amalgamation.h
%{wxincdir}/wx/sqlite3mc_config.h
%{_libdir}/libwxcode_gtk3u_wxsqlite3-%{wxversion}.so
%{_libdir}/pkgconfig/%{name}.pc
