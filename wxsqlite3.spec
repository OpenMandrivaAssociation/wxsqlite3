%global wxversion 3.0
%global wxincdir %{_includedir}/wx-%{wxversion}
%define major 0

%define libname %mklibname %{name}_ %{wxversion} %{major}
%define devname %mklibname %{name}_ %{wxversion} -d

Name:           wxsqlite3
Version:        3.4.1
Release:        1
Summary:        C++ wrapper around the SQLite 3.x database
Group:          System/Libraries
License:        wxWidgets
URL:            http://utelle.github.io/wxsqlite3
Source0:        https://github.com/utelle/wxsqlite3/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         wxsqlite3-3.3.0-mga-fix-soname.patch

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
%setup -q
%autopatch -p1

# activate correct build folder
mv build30 build

# set correct permission
chmod a+x configure

# delete bundled sqlite3 files
rm -rf sqlite3

dos2unix readme.md

%build
%configure2_5x
%make

%install
%makeinstall_std

# move headers from /usr/include/wx to /usr/include/wx-?.?/wx
install -d %{buildroot}%{wxincdir}
mv %{buildroot}%{_includedir}/wx %{buildroot}%{wxincdir}

# install pkgconfig file
install -D -m644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%files -n       %{libname}
%doc LICENCE.txt readme.md
%{_libdir}/libwx_gtk?u_%{name}-%{wxversion}.so.%{major}
%{_libdir}/libwx_gtk?u_%{name}-%{wxversion}.so.%{major}.*

%files -n       %{devname}
%{wxincdir}/wx/%{name}*.h
%{_libdir}/libwx_gtk?u_%{name}-%{wxversion}.so
%{_libdir}/pkgconfig/%{name}.pc
